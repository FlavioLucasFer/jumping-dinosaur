from typing import Tuple, List
from uuid import UUID
import pygame

from object import Object

name: str
window: pygame.display
__is_initialized: bool = False
__is_running: bool = False
__clock = pygame.time.Clock()
__elapsed: float
__objects: List[Object] = []
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


def render_obj(object: Object) -> Object:
    global __objects

    __objects.append(object)
    return object


def unrender_obj(object: Object) -> Object:
    global __objects

    __objects.remove(object)
    return object


def unrender_obj(uuid: UUID) -> Object:
    global __objects

    for object in __objects:
        if object.uuid == uuid:
            __objects.remove(object)
            return object


def rendered_object() -> int:
    global __objects

    return len(__objects)


def __render_objects():
    for object in __objects:
        object.render()


def __handle_event() -> None:
    global __is_running

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            __is_running = False
        elif event.type == pygame.KEYDOWN:
            print('KEYDOWN')


def __framerate_counter() -> None:
    global __clock, __elapsed, framerate

    __elapsed = __clock.tick_busy_loop(framerate) / 1000.0
    fps = int(__clock.get_fps())
    print('FPS: ', fps)


def __reset_resulting_force() -> None:
    global __objects

    for object in __objects:
        object.resulting_force.reset()


def __process_objects_physics() -> None:
    global __objects

    for object in __objects:
        object.physics()


def elapsed() -> int:
    global __elapsed

    return __elapsed


def __loop() -> None:
    global __is_running, __elapsed

    while (__is_running):
        # reset objects' resulting force
        __reset_resulting_force()

        # handle time since the last tick and count fps
        __framerate_counter()

        # handle events: keyboard, mouse, etc...
        __handle_event()

        # process physics
        __process_objects_physics()

        # check collisions

        # clean up window
        window.fill((0, 0, 0))

        # re-render objects
        __render_objects()

        # update screen
        pygame.display.flip()

    pygame.quit()
