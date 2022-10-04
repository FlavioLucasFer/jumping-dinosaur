
import math
from __future__ import annotations

class Vector:
    i: float
    j: float
    k: float

    def copy (self, vector: Vector) -> None:
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

    def subtract(self, vector: Vector) -> None:
        self.i -= vector.i
        self.j -= vector.j
        self.k -= vector.k

    def multiply(self, n: float) -> None:
        self.i *= n
        self.j *= n
        self.k *= n

    def divide(self, n: float) -> None:
        self.i /= n
        self.j /= n
        self.k /= n

    def prod_int(vector1: Vector, vector2: Vector) -> float:
        p: float = (vector1.i * vector2.i) + (vector1.j * vector2.j) + (vector1.k * vector2.k)
        return p

    def module(self) -> float:
        m: float = math.sqrt(Vector.prod_int(self, self))
        return m

    def set_module(mod: float) -> None:
        Vector.divide(Vector.module())
        Vector.multiply(mod)

    def prod_vec(self, vector1: Vector, vector2: Vector) -> None:
        self.i = (vector1.j * vector2.k) - (vector2.j * vector1.k)
        self.j = (vector2.i * vector1.k) - (vector1.i * vector2.k)
        self.k = (vector1.i * vector2.j) - (vector2.i * vector1.j)

    def proj_vec(self, vector1: Vector, vector2: Vector)-> None:
        p: float = Vector.prod_int(vector1, vector2)
        m: float = vector1.module()

        if (p < 0): p *= -1

        m *= m
        p /=m
        self.copy(vector1)
        self.multiply(p)

    def cos_ang(vector1: Vector, vector2: Vector) -> float:
        p: float = Vector.prod_int(vector1, vector2)
        p /= vector1.module()
        p /= vector2.module()

        return p
