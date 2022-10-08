from vector import Vector
from physics.calc import weight_calc
from physics.gravity import SolarSystemGravityAccelerations, g_to_mps2


def weight_force(
    gravity_acclr: SolarSystemGravityAccelerations, 
    mass: float) -> Vector:
    gravity_acclr_mps2: float = g_to_mps2(gravity_acclr.value)
    return Vector(0.0, weight_calc(gravity_acclr_mps2, mass), 0.0)
    
