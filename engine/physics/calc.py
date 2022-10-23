from physics.gravity import SolarSystemGravityAccelerations

def uniformly_variable_motion(
    S0: float,
    V0: float,
    a: float,
    t: float
) -> float:
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
    a: float = SolarSystemGravityAccelerations.EARTH.value
) -> float:
    return f / a


def weight_accrl(f: float, m: float) -> float:
    return f / m
