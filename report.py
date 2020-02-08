from ursina import *
from ursina .shaders import camera_vertical_blur_shader
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.prefabs.dropdown_menu import DropdownMenuButton
from ursina.prefabs.dropdown_menu import DropdownMenu

app = Ursina()

f = open('scoreTMP.txt','r')

score = f.read()

e = Entity(
	model=Terrain('height_map', skip=8), 
	texture='explosion', 
	scale=2000, 
	scale_y=2000)

Sky(rotation_y=125)

c = Entity(
	model='cube_uv_top', 
	texture='white_cube', 
	color=color.blue, 
	highlight_color=color.violet, 
	scale=200, 
	scale_y=200,
	text='Score',)

r = Entity(
	model=Plane(subdivisions=(3,6)), 
	texture='parrot_3',
	scale=200, 
	scale_y=200, 
	position=(0, 100.2), 
	rotation_y=180,
	text='Score')

def input(key):
	if key == 'p':
		b = Button(
			text='hello world!', 
			color=color.blue,
			texture='shore', 
			origin=(0,0))

help_text = Text(
	text=f'Controls:\n\nw: Forward\ns: Back\na: Left\nd: Right\ne: Up\nq: Down\nScore Report: p\nEXIT: Shift+Q\nScore: {score}', 
	origin=(-.5,.5), 
	position=window.top_left*.95, 
	color=color.black)

scene.fog_color = color.light_gray
scene.fog_density = .003

fpc = FirstPersonController(speed=80)

window.exit_button.visible = True
window.fps_counter.enabled = True
mouse.visible = False

t = Text(
	'ParrotSE', 
	enabled=False, 
	scale=3, 
	origin=(0,-5.5), 
	color=color.dark_text)

by = Text(
	'Conceived and Developed by: Raadwan Masum', 
	enabled=False, 
	scale=1, 
	origin=(0,-13.6), 
	color=color.dark_text)

invoke(t.appear, 
	speed=.23, 
	delay=4)
invoke(by.appear, 
	speed=.06, 
	delay=6)

app.run()