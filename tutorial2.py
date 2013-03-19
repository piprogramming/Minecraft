import minecraft
import block

#Initialise
mc = minecraft.Minecraft.create()

#Produce a line of blocks
for x in xrange(0, 10):
    mc.setBlock(x, 15, 0, block.STONE)

#Create a wall
for x in xrange(10, 10):
    for y in xrange(0, 10):
        mc.setBlock(x, y, 0, block.STONE)

#Create a solid cube
for x in xrange(20, 30):
    for y in xrange(0, 10):
        for z in xrange(0, 10):
            mc.setBlock(x, y, z, block.STONE)

#Create a hollow cube
for x in xrange(30, 40):
    for y in xrange(0, 10):
        for z in xrange(0, 10):
            if(x==30 or x==39 or y==0 or y==9 or z==0 or z==9):
                mc.setBlock(x, y, z, block.STONE)

#Create a sphere
for x in range(-10, 10):
    for y in xrange(-10,10):
        for z in xrange(-10, 10):
            if(x**2 + y**2 + z**2 < 10**2):
                mc.setBlock(x,y,z,block.STONE)

