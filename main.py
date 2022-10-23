from unicodedata import name
from engine.game import Game

game = Game('jumping dinosaur')
game.init()

while True:
    print('running')

game.quit()