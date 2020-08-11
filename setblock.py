# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 16:00:25 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()

x,y,z=mc.player.getTilePos()

mc.setBlock(x+1,y,z,15)
mc.setBlock(x-1,y,z,15)
mc.setBlock(x,y,z+1,15)
mc.setBlock(x,y,z-1,15)            
            