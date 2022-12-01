from ursina import Mesh,Entity,rgb

block_data = {}

# block generation
def gen_block(x,y,z,color):
    if (x,y,z) in block_data.keys():
        return None
    mesh = Mesh(vertices = ((x, y, z), (x+1, y, z), (x+1, y, z+1),(x, y, z+1),
                        (x, y+1, z), (x+1, y+1, z), (x+1, y+1, z+1),(x, y+1, z+1)),
                triangles = (0,1,5,0,5,4,1,2,6,1,6,5,2,3,6,3,7,6,0,4,3,3,4,7,5,6,7,4,5,7,0,1,2,0,2,3))
    block_data[(x,y,z)] = True

    return Entity(model = mesh,color = color)
