from pygame import display

from engine.game import Game as EngineGame, Clock


class Game:
	__engine_game = EngineGame('Jumping Dinosaur')
	__is_running = False
	__clock = Clock()
	__FRAMERATE = 0

	def run() -> None:
		Game.__is_running = True
		Game.__engine_game.init()
		Game.__loop()
		Game.__quit()

	def __loop() -> None:
		while Game.__is_running:
			Game.__framerate_manager()
			Game.__event_handler()
			Game.__render_objects()

	def __render_objects() -> None:
		Game.__engine_game.window.fill((0, 0, 0))
		
		# object rendering goes here
		
		display.flip()

	def __framerate_manager() -> None:
		Game.__clock.tick_busy_loop(Game.__FRAMERATE)

	def __event_handler() -> None:
		pass

	def __quit() -> None:
		Game.__is_running = False
		Game.__engine_game.quit()