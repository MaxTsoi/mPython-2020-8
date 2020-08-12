import time
import random
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
time.sleep(5)

x,y,z = mc.player.getTilePos()

color = random.randrange(0,16)
mc.setBlocks(x+25,y-1,z+25,x-25,y-1,z-25,95)