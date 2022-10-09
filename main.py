import game
from object import Object
from vector import Vector
from physics.gravity import SolarSystemGravityAccelerations, g_to_mps2


obj = Object(Vector(10.0, 12.0, 0.0), Vector(12.0, 25.0, 0.0), (255, 0, 255))
obj.vel = Vector(0.0, 0.0, 0.0)
obj.mass = 0.1
obj.enable_free_fall(g_to_mps2(SolarSystemGravityAccelerations.SUN.value))
game.render_obj(obj)


game.init(
    game_name='jumping-dinosaur',
    window_size=(800, 600),
)
game.run()
