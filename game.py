from typing import Tuple
import pygame
from pygame import Rect

class Game:
	name: str
	display = pygame.display
	window: pygame.display
	running: bool = False

	def __init__(self, name: str, window_size: Tuple[int, int]) -> None:
		self.name = name
		self.window = pygame.display.set_mode(size=window_size)

	def run(self) -> None:
		pygame.init()
		pygame.font.init()
		self.display.init()

		print(self.name)

		self.running = True
		self.loop()

	def handle_event(self) -> None:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False

	def loop(self) -> None:
		rect = Rect((10.0, 10.0), (10.0, 10.0))
		pygame.draw.rect(surface=self.window, rect=rect, color=(255, 0, 255))

		while (self.running):
			# handle events: keyboard, mouse, etc...
			self.handle_event()

			# process physics

			# check collisions

			# re-render objects

			# update screen
			self.display.flip()
