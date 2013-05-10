import pyglet

pyglet.resource.path = ['C:/hatchling/resources', 
  					'C:/hatchling/resources/jump', 'C:/hatchling/resources/run']

pyglet.resource.path.append('../resources')
pyglet.resource.path.append('../resources/run')
pyglet.resource.path.append('../resources/jump')
pyglet.resource.reindex()
  
#Create jumping animation
h_jr_1 = pyglet.resource.image('hatchling_jump_right_1.png')
h_jr_2 = pyglet.resource.image('hatchling_jump_right_2.png')
h_jr_3 = pyglet.resource.image('hatchling_jump_right_3.png')
h_jr_4 = pyglet.resource.image('hatchling_jump_right_4.png')
h_jr_5 = pyglet.resource.image('hatchling_jump_right_5.png')
h_jr_6 = pyglet.resource.image('hatchling_jump_right_6.png')
h_jr_7 = pyglet.resource.image('hatchling_jump_right_7.png')
h_jr_8 = pyglet.resource.image('hatchling_jump_right_8.png')
h_jr_9 = pyglet.resource.image('hatchling_jump_right_9.png')
h_jr_10 = pyglet.resource.image('hatchling_jump_right_10.png')
h_jr_11 = pyglet.resource.image('hatchling_jump_right_11.png')
h_jr_12 = pyglet.resource.image('hatchling_jump_right_12.png')

h_jump_anim = pyglet.image.Animation.from_image_sequence([h_jr_1, h_jr_2, h_jr_3, h_jr_4, h_jr_5, h_jr_6, h_jr_7, h_jr_8, h_jr_9, h_jr_10, h_jr_11, h_jr_12], 0.1, False)
h_jump_sprite = pyglet.sprite.Sprite(h_jump_anim)

#Running

h_r_1 = pyglet.resource.image('run1.png')
h_r_2 = pyglet.resource.image('run2.png')
h_r_3 = pyglet.resource.image('run3.png')
h_r_4 = pyglet.resource.image('run4.png')
h_r_5 = pyglet.resource.image('run5.png')
h_r_6 = pyglet.resource.image('run6.png')
h_r_7 = pyglet.resource.image('run7.png')

h_run_anim = pyglet.image.Animation.from_image_sequence([h_r_1, h_r_2, h_r_3, h_r_4, h_r_5, h_r_6, h_r_7], 0.1, False)
h_run_sprite = pyglet.sprite.Sprite(h_run_anim)

hatchling_image = pyglet.resource.image('hatchling.png')

bunny_image = pyglet.resource.image('bunny.png')
