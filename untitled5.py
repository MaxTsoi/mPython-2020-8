from mcpi.minecraft import Minecraft
import time
mc =minecraft.create()

while true:
    x,y,z = mc,player.getTilepos()
    
    mc.postToChat("123X:"+str(x)+"Y:"+str(y)+"z:"+str(z))