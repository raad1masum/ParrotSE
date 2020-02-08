import os
import time

from ursina import *
from ursina .shaders import camera_vertical_blur_shader
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

f = open('scoreTMP.txt','r')

e = Entity(model=Terrain('height_map', skip=8), texture='explosion', scale=600, scale_y=600)
Sky(rotation_y=125)

b = Entity(model='cube', texture='white_cube', color=color.blue, highlight_color=color.lime, scale=100, scale_y=100,text='Score',)

r = Entity(model=Plane(subdivisions=(3,6)), texture='shore', color=color.blue, scale=100, scale_y=100, position=(0, 50.2), rotation_y=180)

score = f.read()

help_text = Text(text=f'Controls:\n\nw: Forward\ns: Back\na: Left\nd: Right\ne: Up\nq: Down\nScore: {score}', origin=(-.5,.5), position=window.top_left*.95, color=color.black)

scene.fog_color = color.light_gray
scene.fog_density = .005

fpc = FirstPersonController(speed=80)

# window.exit_button.visible = True
# window.fps_counter.enabled = True
# mouse.visible = False

# camera.shader = camera_vertical_blur_shader
# camera.set_shader_input('blur_size', .0)

# camera.blur_amount = 0
# def update():
#     camera.set_shader_input("blur_size", camera.blur_amount)

t = Text('ParrotSE', enabled=False, scale=3, origin=(0,-5.5), color=color.dark_text)
by = Text('Concieved and Developed by: Raadwan Masum', enabled=False, scale=1, origin=(0,-13.6), color=color.dark_text)

invoke(t.appear, speed=.23, delay=4)
invoke(by.appear, speed=.06, delay=6)

print('hello')

app.run()