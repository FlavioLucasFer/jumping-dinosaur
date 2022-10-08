from physics.gravity import SolarSystemGravityAccelerations


def weight_calc(a: float, m: float) -> float:
    return a * m


def weight_mass(
    f: float, 
    a: float = SolarSystemGravityAccelerations.EARTH.value) -> float:
    return f / a


def weight_accrl(f: float, m: float) -> float:
    return f / m

