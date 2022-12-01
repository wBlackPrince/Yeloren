from block import *
from math import sin
from ursina import rgb,Entity,Vec3,destroy
from random import randint

chunkWidth = 10

# terrain fragment class, consists of blocks
class Chunk():
    chunkWidth = 10

    def __init__(self,position):
        self.blocks = []
        self.x = position[0]
        self.z = position[1]

        for x in range(-self.chunkWidth//2 + position[0], self.chunkWidth//2+1 + position[0]):
            for z in range(-self.chunkWidth//2 + position[1], self.chunkWidth//2+1 + position[1]):
                color = rgb(randint(10,20),randint(100,140),randint(10,20))
                y = round(sin(x*0.2)*0.9) + round(sin(z*0.2)*0.9)

                block = gen_block(x,y,z,color)
                if block != None:
                    self.blocks.append(block)
                
        self.blocks = tuple(self.blocks)


# control chunk generation
class ChunkGenerator(Entity):
    # all game chunks
    all_chunks = tuple([[Vec3(x*chunkWidth,0,z*chunkWidth) for z in range(-10,11)] for x in range(-10,11)])
    all_chunks_data = {}
    # chunks on scene
    scene_chunks = []

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

        self.main_chunk_defain(player_x,player_z)
        self.nearby_chunk_defain(player_x,player_z)

        for i in range(len(self.all_chunks)):
            for j in range(len(self.all_chunks[i])):
                Entity(model = "sphere",position = self.all_chunks[i][j])


    def main_chunk_defain(self,player_x,player_z):
        self.main_chunk = Chunk((player_x,player_z))
        self.scene_chunks.append(self.main_chunk)
        self.all_chunks_data[(self.main_chunk.x,self.main_chunk.z)] = self.main_chunk
    
    def nearby_chunk_defain(self,player_x,player_z):
        for i in self.chunk_vector:
            new_chunk_coords = ((i[0] + player_x, i[1] + player_z))

            if new_chunk_coords not in self.all_chunks_data.keys():
                curr_chunk = Chunk((new_chunk_coords[0],
                    new_chunk_coords[1]))
                self.scene_chunks.append(curr_chunk)
                self.all_chunks_data[(curr_chunk.x,curr_chunk.z)] = curr_chunk



    
    def update(self):
        if abs(self.player.x) > self.main_chunk.x or (abs(self.player.z) > self.main_chunk.z):
            for chunk in self.scene_chunks:
                if chunk.x - chunkWidth < self.player.x < chunk.x + chunkWidth and chunk.z - chunkWidth < self.player.z < chunk.z + chunkWidth:
                    self.main_chunk = chunk
                    
                    self.nearby_chunk_defain(round(chunk.x),
                                            round(chunk.z))





