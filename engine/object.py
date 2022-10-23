from __future__ import annotations
from uuid import UUID, uuid4
from pygame import draw, Color, Rect, display

from physics import Vector

class Object(Rect):
	__uuid: UUID
	color: Color

	def __init__(
			self,
			pos: Vector,
			size: Vector,
			color: Color,
			mass=0.0,
			velocity=Vector(0.0, 0.0, 0.0)) -> None:
		self.__uuid = uuid4()
		self.__hash__ = self.uuid
		self.left, self.top = pos.i, pos.j
		self.width, self.height = size.i, size.j
		self.color = color
		self.mass = mass
		self.velocity = velocity

	def __str__(self) -> str:
		return "<Object({uuid})>".format(uuid=self.uuid)

	def __eq__(self, object: object) -> bool:
		if isinstance(object, Object):
			return self.uuid == object.uuid
		return False

	def __ne__(self, object: object) -> bool:
		return not self.__eq__(object)

	@property
	def uuid(self) -> UUID:
		return self.__uuid

	@property
	def pos(self) -> Vector:
		return Vector(self.left, self.top, 0.0)

	@pos.setter
	def pos(self, pos: Vector) -> None:
		self.left, self.top = pos.i, pos.j

	@property
	def size(self) -> Vector:
		return Vector(self.width, self.height, 0.0)

	@size.setter
	def size(self, size: Vector) -> None:
		self.width, self.height = size.i, size.j

	def draw(self) -> None:
		rect = ((self.left, self.top), (self.width, self.height))
		draw.rect(surface=display.get_surface(), rect=rect, color=self.color)
	