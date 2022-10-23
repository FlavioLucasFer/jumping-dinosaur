from __future__ import annotations
from typing import Tuple
from enum import Enum

from pygame import Surface, init as init_pygame, quit as pygame_quit
from pygame.display import init as init_display, set_mode as display_set_mode
from pygame.font import init as init_font
from pygame.time import Clock as PyClock


__game: Game = None


class WindowRecomendedResolutions(Enum):
    P240 = (426, 240)
    P360 = (640, 360)
    P480 = (854, 480)
    HD = (1280, 720)
    FULL_HD = (1920, 1080)
    QUAD_HD = (2560, 1440)
    FOUR_K = (3840, 2160)
    EIGHT_K = (7680, 4320)


class Clock:
    __elapsed: float
    __clock = PyClock()

    def tick_busy_loop(self, framerate=0) -> int:
        tick = self.__clock.tick_busy_loop(framerate)
        self.__elapsed = tick / 1000.0
        return tick

    def tick(self, framerate=0) -> int:
        tick = self.__clock.tick(framerate)
        self.__elapsed = tick / 1000.0
        return tick

    @property
    def elased(self) -> float:
        return self.__elapsed

    @property
    def fps(self) -> float:
        return self.__clock.get_fps()


class Game:
    __is_initialized = False
    __window: Surface
    name: str

    def __new__(cls: Game) -> Game:
        global __game
        if not __game:
            __game = object.__new__(cls)
        return __game

    def __init__(self, name: str) -> None:
        self.name = name
        
    def init(self, 
            window_size: WindowRecomendedResolutions.FULL_HD.value) -> None:
        if self.__is_initialized:
            raise Exception('Game is already initialized')

        init_pygame()
        init_display()
        init_font()

        self.window = window_size
        self.__is_initialized = True

    def quit() -> None:
        global __game
        pygame_quit()
        __game = None

    @property
    def window(self) -> Surface:
        return self.__window

    @window.setter
    def window(self, size: Tuple[int, int]) -> None:
        self.__window = display_set_mode(size)
