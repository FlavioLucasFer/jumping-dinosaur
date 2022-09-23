from typing import Tuple
import pygame
from object import Object

from render import render_obj, render_objects

name: str
window: pygame.display
__is_initialized: bool = False
__is_running: bool = False
__clock = pygame.time.Clock()
__elapsed: float
framerate: int = 0

def init(game_name: str, window_size: Tuple[int, int]) -> None:
	global name, window, __is_initialized

	pygame.init()
	pygame.font.init()
	pygame.display.init()

	name = game_name
	window = pygame.display.set_mode(size=window_size)
	__is_initialized = True

def run() -> None:
	global name, __is_running, __is_initialized

	if not __is_initialized:
		raise Exception("Game should be initialized first. Call \"run\"!")

	print(name)

	__is_running = True
	__loop()

def __handle_event() -> None:
	global __is_running

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			__is_running = False
		elif event.type == pygame.KEYDOWN:
			render_obj(Object((10.0, 12.0), (25.0, 12.0), (255, 0, 255)))
		
def __framerate_counter() -> None:
	global __clock, __elapsed, framerate

	__elapsed = __clock.tick_busy_loop(framerate)
	fps = int(__clock.get_fps())
	print('FPS: ', fps)

@property
def elapsed() -> int:
	global __elapsed

	return __elapsed


def __loop() -> None:
	global __is_running

	while (__is_running):
		# handle time since the last tick and count fps
		__framerate_counter()

		# handle events: keyboard, mouse, etc...
		__handle_event()

		# process physics

		# check collisions

		#clean up window
		window.fill((0, 0, 0))

		# re-render objects
		render_objects()

		# update screen
		pygame.display.flip()
