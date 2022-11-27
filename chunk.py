from block import *
from math import sin
from ursina import rgb,Entity
from random import randint

# terrain fragment class, consists of blocks
class Chunk():
    chunkWidth = 10

    def __init__(self,player_x,player_z):
        self.blocks = []

        for x in range(-self.chunkWidth//2 + player_x, self.chunkWidth//2+1 + player_x):
            for z in range(-self.chunkWidth//2 + player_z, self.chunkWidth//2+1 + player_z):
                color = rgb(randint(10,20),randint(100,140),randint(10,20))
                y = round(sin(x*0.2)*0.9) + round(sin(z*0.2)*0.9)
                self.blocks.append(gen_block(x,y,z,color))
        self.blocks = tuple(self.blocks)


# control chunk generation
class ChunkGenerator(Entity):
    chunkWidth = 10
    #  vector for generation hearby chunks
    chunk_vector = ((-chunkWidth,chunkWidth),
                (0,chunkWidth),
                (chunkWidth,chunkWidth),
                (chunkWidth,0),
                (chunkWidth,-chunkWidth),
                (0,-chunkWidth),
                (-chunkWidth,-chunkWidth),
                (-chunkWidth,0))

    def __init__(self,player):
        self.player = player
        player_x = round(player.position.x)
        player_z = round(player.position.z)

        self.main_chunk = Chunk(player_x,
                                player_z)

        for i in self.chunk_vector:
            Chunk(i[0] + player_x,
                    i[1] + player_z)
        
    
    def update():...





