from enum import Enum


__G_STANDARD_VALUE: float = 9.8


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


@property
def G_STANDARD_VALUE() -> float:
    return __G_STANDARD_VALUE


def g_to_mps2(g: float) -> float:
    return __G_STANDARD_VALUE * g


def mps2_tp_g(mps: float) -> float:
    return mps / __G_STANDARD_VALUE
