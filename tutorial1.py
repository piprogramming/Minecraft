import minecraft
import block

#Initialise out Minecraft object instance which connects to the game
mc = minecraft.Minecraft.create()

#Post the message to the games chat window
mc.postToChat("Hello Minecraft World!")

#Place a stone block into the world
mc.setBlock(0, 10, 0, block.STONE)

#Place a melon next to the stone block
mc.setBlock(1, 10, 0, block.MELON)

#Place a diamond block above the stone one
mc.setBlock(0, 11, 0, block.DIAMOND_BLOCK)
