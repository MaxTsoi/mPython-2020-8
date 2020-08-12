from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

while True:
    color = random.randrange(0,9)
    x,y,z = mc.player.getPos()
    mc.setBlock(x,y,z,38)
    time.sleep(0.2)