from __future__ import annotations
import math


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
