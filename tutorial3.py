import minecraft
import block
import math
import time
import random

#Initialise
mc = minecraft.Minecraft.create()

#Returns the distance between 2 positions
def getDistanceBetweenPoints(point1, point2):
    xDistance = point2.x - point1.x
    yDistance = point2.y - point1.y
    zDistance = point2.z - point1.z
    return math.sqrt((xDistance * xDistance) + (yDistance * yDistance) + (zDistance * zDistance))

#This will generate a new random gold block and returns its coordinates
def setRandomGoldBlock():
    #Initialise our position with 0,0,0
    goldBlock = minecraft.Vec3(0,0,0)
    #Randomise the x axis within 100 blocks from the player
    goldBlock.x = random.randrange(-100, 100) 
    #Initialise the y axis between -5 and 20 as we dont want it to be too low or high in the world
    goldBlock.y = random.randrange(-5, 20) 
    #Randomise the z axis within 100 blocks from the player like the x axis
    goldBlock.z = random.randrange(-100, 100) 
    #Place the block in the world
    mc.setBlock(goldBlock.x, goldBlock.y, goldBlock.z, block.GOLD_BLOCK)
    #Return the coordinates so we know where our gold block is
    return goldBlock

#Set our first Gold block
goldBlock = setRandomGoldBlock()

#Initialise our gold count to 0
goldCount = 0

#Print some instruction for the player
mc.postToChat("3 blocks of Gold have been hidden and you need to find them")

#Sleep for 3 seconds so the player has time to read the instruction
time.sleep(3)

#Keeps looping until the player finds 3 Gold blocks
while(goldCount < 3):
    #Get the players position
    playerPos = mc.player.getPos()

    #Calculate the distance to the start
    distanceFromStart = getDistanceBetweenPoints(goldBlock, playerPos)

    #Print the distance on the game chat
    mc.postToChat("Distance: " + str(int(distanceFromStart)) + " blocks")

    if(distanceFromStart < 2):
        #Clears the block from the game
        mc.setBlock(goldBlock.x, goldBlock.y, goldBlock.z, block.AIR)
        #Generates a new block
        goldBlock = setRandomGoldBlock()
        #Increments the gold count by one
        goldCount += 1

    #Sleep for a second so that we don't just flood the game
    time.sleep(1)

#Print a success mesage to the chat
mc.postToChat("Well done, you found all 3 blocks of Gold")
