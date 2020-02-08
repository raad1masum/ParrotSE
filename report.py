import os
import time

from ursina import *
from ursina .shaders import camera_vertical_blur_shader
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

f = open('score.txt','r')

e = Entity(model=Terrain('height_map', skip=8), texture='explosion', scale=500, scale_y=500)
Sky(rotation_y=125)

Entity(model='cube', texture='white_cube', color=color.blue, highlight_color=color.lime, scale=100, scale_y=100)

score = f.read()

help_text = Text(text=f'Controls:\n\nw: Forward\ns: Back\na: Left\nd: Right\ne: Up\nq: Down\nScore: {score}', origin=(-.5,.5), position=window.top_left*.95, color=color.black)

scene.fog_color = color.light_gray
scene.fog_density = .005

fpc = FirstPersonController(speed=80)

window.exit_button.visible = True
window.fps_counter.enabled = True
mouse.visible = False

camera.shader = camera_vertical_blur_shader
camera.set_shader_input('blur_size', .0)

camera.blur_amount = 0
def update():
    camera.set_shader_input("blur_size", camera.blur_amount)

t = Text('ParrotSE', enabled=False, scale=3, origin=(0,-5), color=color.dark_text)

invoke(t.appear, speed=.1, delay=3)

print('hello')

app.run()