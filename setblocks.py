import time
import random
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
time.sieep(5)


x,y,z = mc.player.getTlePos()


color = random.rand
mc.setBlocks(x+25, y-1, z+25, x-25, y-1, z-25, 95, color)