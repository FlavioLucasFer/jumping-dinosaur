from __future__ import annotations
from enum import Enum
import math

class SolarSystemGravityAccelerations(Enum):
	EARTH = 1.0
	MOON = 0.165
	SUN = 28.02
	MERCURY = 0.377
	VENUS = 0.905
	MARS = 0.379
	JUPITER = 2.528
	SATURN = 1.065
	URANUS = 0.886
	NEPTUNE = 1.137
	PLUTO = 0.063


class Gravity:
	__g_standard_value = 9.0

	@property
	def G_STANDARD_VALUE() -> float:
		return Gravity.__g_standard_value

	def g_to_mps2(g: float) -> float:
		return Gravity.G_STANDARD_VALUE * g

	def mps2_tp_g(mps: float) -> float:
		return mps / Gravity.G_STANDARD_VALUE


class Vector:
	i: float
	j: float
	k: float

	def __init__(self, i=0.0, j=0.0, k=0.0) -> None:
		self.set(i, j, k)

	def __str__(self) -> str:
		return 'Vector(i: {i}, j: {j}, k: {k})'.format(i=self.i, j=self.j, k=self.k)

	def __eq__(self, object: object) -> bool:
		if isinstance(object, Vector):
			return self.i == object.i and self.j == object.j and self.k == object.k
		return False

	def __ne__(self, object: object) -> bool:
		return not self.__eq__(object)

	def __add__(self, vector: Vector) -> None:
		self.add(vector)

	def __sub__(self, vector: Vector) -> None:
		self.sub(vector)

	def __mul__(self, n: float) -> None:
		self.mult(n)

	def __truediv__(self, n: float) -> None:
		self.div(n)

	def copy(self, vector: Vector) -> None:
		self.i = vector.i
		self.j = vector.j
		self.k = vector.k

	def set(self, i: float, j: float, k: float) -> None:
		self.i = i
		self.j = j
		self.k = k

	def add(self, vector: Vector) -> None:
		self.i += vector.i
		self.j += vector.j
		self.k += vector.k

	def sub(self, vector: Vector) -> None:
		self.i -= vector.i
		self.j -= vector.j
		self.k -= vector.k

	def mult(self, n: float) -> None:
		self.i *= n
		self.j *= n
		self.k *= n

	def div(self, n: float) -> None:
		self.i /= n
		self.j /= n
		self.k /= n

	def prod_int(vector1: Vector, vector2: Vector) -> float:
		return (vector1.i * vector2.i) + (vector1.j * vector2.j) + (vector1.k * vector2.k)

	def module(self) -> float:
		return math.sqrt(Vector.prod_int(self, self))

	def set_module(mod: float) -> None:
		Vector.div(Vector.module())
		Vector.mult(mod)

	def prod_vec(self, vector1: Vector, vector2: Vector) -> None:
		self.i = (vector1.j * vector2.k) - (vector2.j * vector1.k)
		self.j = (vector2.i * vector1.k) - (vector1.i * vector2.k)
		self.k = (vector1.i * vector2.j) - (vector2.i * vector1.j)

	def proj_vec(self, vector1: Vector, vector2: Vector) -> None:
		p = Vector.prod_int(vector1, vector2)
		m = vector1.module()

		if (p < 0):
			p *= -1

		m *= m
		p /= m
		self.copy(vector1)
		self.mult(p)

	def cos_ang(vector1: Vector, vector2: Vector) -> float:
		p = Vector.prod_int(vector1, vector2)
		p /= vector1.module()
		p /= vector2.module()

		return p


def uniformly_variable_motion(
		S0: float,
		V0: float,
		a: float,
		t: float) -> float:
	"""
	Calculate uniformly variable motion
	
	S = S0 + V0.t + (a.t²) / 2
	Args:
		S0 (float): initial position
		V0 (float): initial velocity
		a (float): acceleration
		t (float): time
	Returns
		float: uniformly variable motion result
	"""
	# S = S0 + V0.t + (a.t²) / 2
	return S0 + V0 * t + (a * t ** 2) / 2.0


def weight_calc(a: float, m: float) -> float:
	return a * m


def weight_mass(
		f: float,
		a: float = SolarSystemGravityAccelerations.EARTH.value) -> float:
	return f / a


def weight_accrl(f: float, m: float) -> float:
	return f / m
