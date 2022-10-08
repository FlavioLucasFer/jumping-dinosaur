from typing import NewType, Tuple
from uuid import UUID, uuid4
from pygame import draw, Color, Rect

import game

Vector = NewType('Vector', Tuple[float, float])


class Object:
    __uuid: UUID
    shape: draw
    hitbox: Rect
    size: Vector
    pos: Vector
    color: Color
    vel: Vector = (0.0, 0.0)
    mass: float = 0.0
    resulting_force: float

    def __init__(
        self,
        pos: Vector,
        size: Vector,
        color: Color,
        shape: draw = draw.rect
    ) -> None:
        self.__uuid = uuid4()
        self.hitbox = Rect(pos, size)
        self.position = pos
        self.size = size
        self.color = color
        self.shape = shape

    @property
    def uuid(self) -> UUID:
        return self.__uuid

    def render(self):
        self.shape(surface=game.window, rect=self.hitbox, color=self.color)
