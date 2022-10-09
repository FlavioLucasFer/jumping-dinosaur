from physics.gravity import SolarSystemGravityAccelerations


def uniformly_variable_motion(So, Vo, a, t) -> float:
    # S = So + Vo.t + (a.t²) / 2
    return So + Vo * t + (a * t ** 2) / 2.0


def weight_calc(a: float, m: float) -> float:
    return a * m


def weight_mass(
    f: float,
    a: float = SolarSystemGravityAccelerations.EARTH.value
) -> float:
    return f / a


def weight_accrl(f: float, m: float) -> float:
    return f / m
