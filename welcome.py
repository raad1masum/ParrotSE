import os
import time

from ursina import *
from ursina .shaders import camera_vertical_blur_shader
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

e = Entity(model=Terrain('loddefjord_height_map', skip=8), texture='explosion', scale=500, scale_y=500)
Sky(rotation_y=125)

scene.fog_color = color.gray
scene.fog_density = .01

fpc = FirstPersonController(speed=50)

window.exit_button.visible = True
window.fps_counter.enabled = False
mouse.visible = False

camera.shader = camera_vertical_blur_shader
camera.set_shader_input('blur_size', .0)

camera.blur_amount = 0
def update():
    camera.set_shader_input("blur_size", camera.blur_amount)

t = Text('ParrotSE', enabled=False, scale=3, origin=(0,0), color=color.dark_text)

camera.animate('blur_amount', .6, duration=4)
invoke(t.appear, speed=.1, delay=4.2)

# def input(key):
#     if key == 'enter':
#         camera.animate('blur_amount', .6, duration=4)
#         invoke(t.appear, speed=.1, delay=4.2)

app.run()