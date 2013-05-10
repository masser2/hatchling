import pyglet
from game import resources

#Draw window
W=1200
H=800
game_window = pyglet.window.Window(width=W,height=H)
main_batch = pyglet.graphics.Batch()

#Setup initial labels
score_label = pyglet.text.Label(text="Some Label: 0", x=W-200, y=H-22, batch=main_batch)
lvl_label = pyglet.text.Label('Hatchling', 
                          font_name='Times New Roman', 
                          font_size=36,
                          x=10, y=H-30,
                          batch=main_batch,
                          anchor_y='center')

game_objects = []

# We need to pop off as many event stack frames as we pushed on
# every time we reset the level.
event_stack_size = 0



class PhysicalObject(pyglet.sprite.Sprite):
    
    def __init__(self, *args, **kwargs):
        super(PhysicalObject, self).__init__(*args, **kwargs)
        
        # Velocity
        self.velocity_x, self.velocity_y = 0.0, 0.0
        
        # Flags to toggle collision
        self.collidable = True
        self.is_weapon = False
        
        # Flag to remove this object from the game_object list
        self.dead = False
        
        # List of new objects to go in the game_objects list
        self.new_objects = []
        
        # Tell the game handler about any event handlers
        # Only applies to things with keyboard/mouse input
        self.event_handlers = []
    
    def update(self, dt):
        """This method should be called every frame."""
        #Collision? We dont have it yet...
        
        # Update position according to velocity and time
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt


class Player(PhysicalObject):
    """Physical object that responds to user input"""
    
    def __init__(self, *args, **kwargs):
        super(Player, self).__init__(img=resources.hatchling_image, *args, **kwargs)
        
        # Create a child sprite to show when the ship is thrusting
        #self.engine_sprite = pyglet.sprite.Sprite(img=resources.engine_image, *args, **kwargs)
        #self.engine_sprite.visible = False
        
        # Set some easy-to-tweak constants
        self.thrust = 200.0
        #self.rotate_speed = 200.0
        #self.bullet_speed = 700.0
        
        # dunno
        self.is_weapon = False
        
        # Tell the game handler about any event handlers
        self.key_handler = pyglet.window.key.KeyStateHandler()
        self.event_handlers = [self, self.key_handler]
    
    def update(self, dt):
        #NOTE: mostly this function doesnt work!
        # Do all the normal physics stuff
        super(Player, self).update(dt)
        
        if self.key_handler[pyglet.window.key.LEFT]:
            self.x -= self.thrust * dt
        if self.key_handler[pyglet.window.key.RIGHT]:
            self.x += self.thrust * dt
        
        if self.key_handler[pyglet.window.key.UP]:
            pass
    
    def on_key_press(self, symbol, modifiers):
        if symbol == pyglet.window.key.SPACE:
            #self.fire()
            self.scale += 0.1
        if symbol == pyglet.window.key.RIGHT:
            self.x += self.thrust * (1/120.0)
        if symbol == pyglet.window.key.LEFT:
            self.x -= self.thrust * (1/120.0)

    def delete(self):
        # We have a child sprite which must be deleted when this object
        # is deleted from batches, etc.
        #self.engine_sprite.delete()
        super(Player, self).delete()

def init():
    #Global vars
    global score, event_stack_size
    score = 0
    
    #make a player sprite
    player_character = Player(x=100, y=30, batch=main_batch)
    
    #make a (static) enemy
    bunny = pyglet.sprite.Sprite(img=resources.bunny_image, x=600, y=30, batch=main_batch)
    
    game_objects = [player_character]
    
    # Add any specified event handlers to the event handler stack
    for obj in game_objects:
        for handler in obj.event_handlers:
            game_window.push_handlers(handler)
            event_stack_size += 1


#register draw function to receive game_window events
@game_window.event
def on_draw():
    game_window.clear()
    main_batch.draw()
    
#testing sprites
#    h_jump_sprite.draw()
#    h_run_sprite.draw()
#    resources.hatchling_img.blit(0+50,0)
#    resources.bunny_img.blit(0+600+50,0)

def update(dt):
    global score
    
    # To avoid handling collisions twice, we employ nested loops of ranges.
    # This method also avoids the problem of colliding an object with itself.

    # Let's not modify the list while traversing it
    to_add = []
    
    for obj in game_objects:
        obj.update(dt)
        
        to_add.extend(obj.new_objects)
        obj.new_objects = []


if __name__ == "__main__":
    #Run initialization code
    init()
    
    # Update the game 120 times per second
    pyglet.clock.schedule_interval(update, 1/120.0)
    
    # Tell pyglet to do its thing
    pyglet.app.run()
