from uuid import UUID, uuid4
from pygame import draw, Color, Rect

import game
from vector import Vector
from physics.calc import uniformly_variable_motion
from physics.force import weight_force


class ResultingForce():
	__f: Vector = Vector(0.0, 0.0, 0.0)

	@property
	def value(self) -> Vector:
		return self.__f

	def apply(self, force: Vector) -> None:
		self.__f.add(force)

	def reset(self) -> None:
		self.__f.set(0.0, 0.0, 0.0)


class Object:
	__uuid: UUID
	__gravity_accrl: float
	__free_fall_enabled: bool = False
	__accrl: Vector = Vector(0.0, 0.0, 0.0)
	__size: Vector = Vector(0.0, 0.0, 0.0)
	__pos: Vector = Vector(0.0, 0.0, 0.0)
	shape: draw
	hitbox: Rect
	vel: Vector = Vector(0.0, 0.0, 0.0)
	color: Color
	mass: float = 0.0
	resulting_force: ResultingForce = ResultingForce()

	def __init__(
			self,
			pos: Vector,
			size: Vector,
			color: Color,
			shape: draw = draw.rect
	) -> None:
		self.__uuid = uuid4()
		self.hitbox = Rect(pos.i, pos.j, size.i, size.j)
		self.pos = pos
		self.size = size
		self.color = color
		self.shape = shape

	def __free_fall(self) -> None:
		if not self.__free_fall_enabled:
			return
		f: Vector = weight_force(self.__gravity_accrl, self.mass)
		self.resulting_force.apply(f)

	def __update_acceleration(self) -> None:
		if self.mass == 0.0:
			return
		accrl_vector: Vector = self.resulting_force.value
		accrl_vector.divide(self.mass)
		self.__accrl.set(accrl_vector.i, accrl_vector.j, accrl_vector.k)

	def __update_position(self, ax: float, ay: float) -> None:		
		posx: float = uniformly_variable_motion(
			self.pos.i,
			self.vel.i,
			ax,
			game.elapsed()
		)
		posy:float = uniformly_variable_motion(
			self.pos.j,
			self.vel.j,
			ay,
			game.elapsed()
		)
		self.pos = Vector(posx, posy, 0.0)

	def __update_velocity(self, ax: float, ay: float) -> None:
		self.vel.i = self.vel.i + ax * game.elapsed()
		self.vel.j = self.vel.j + ay * game.elapsed()

	@property
	def uuid(self) -> UUID:
		return self.__uuid

	@property
	def pos(self) -> Vector:
		return self.__pos

	@pos.setter
	def pos(self, pos: Vector) -> None:
		self.__pos.copy(pos)
		self.hitbox.left = pos.i
		self.hitbox.top = pos.j

	@property
	def size(self) -> Vector:
		return self.__size

	@size.setter
	def size(self, size: Vector) -> None:
		self.__size.copy(size)
		self.hitbox.width = size.i
		self.hitbox.height = size.j

	def enable_free_fall(self, gravity_accrl: float) -> None:
		self.__free_fall_enabled = True
		self.__gravity_accrl = gravity_accrl

	def disable_free_fall(self) -> None:
		self.__free_fall_enabled = False
		self.__gravity_accrl = None

	def render(self) -> None:
		self.shape(surface=game.window, rect=self.hitbox, color=self.color)

	def physics(self) -> None:
		ax: float = self.__accrl.i
		ay: float = self.__accrl.j

		self.__free_fall()
		self.__update_acceleration()
		self.__update_position(ax, ay)
		self.__update_velocity(ax, ay)
	