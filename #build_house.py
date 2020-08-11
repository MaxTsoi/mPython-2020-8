from mcpi.minecraft import Minecraft
mc = Minecraft.create()

iength = 20
width = 10
height = 5
x,y,z - mc.player.getTilePos()

x2 =x+length
y2 = y+height
z2 = z+width

mc.setBlocks(x,y,z,x2,y2,5)
mc.setBlocks