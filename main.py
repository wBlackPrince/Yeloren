from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from chunk import ChunkGenerator

# window settings
#window.fullscreen = True

app = Ursina()

sky = Sky()

player = FirstPersonController(model = "cube")
player.gravity = False


cg = ChunkGenerator(player)

def input(key):
    # game escape
    if key == "escape":
        quit()

def update():
    cg.update()
    if held_keys["space"]:
        player.y += 10*time.dt




app.run()