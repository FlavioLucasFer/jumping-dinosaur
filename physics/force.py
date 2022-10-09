from vector import Vector
from physics.calc import weight_calc


def weight_force(
    gravity_acclr: float,
    mass: float
) -> Vector:
    return Vector(0.0, weight_calc(gravity_acclr, mass), 0.0)
