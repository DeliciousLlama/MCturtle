
# NOTE: Please check [demo1.py] for all explanation on how the set up works!
from mcpi.minecraft import Minecraft
import time
from MCpen.mcturtle import MCTurtle, direction
import random

mc = Minecraft.create("localhost")
playerId = mc.getPlayerEntityId("GnarlyLlama")
pos = mc.entity.getPos(playerId)
t = MCTurtle(mc, px, py-1, pz)
time.sleep(3)

#---------------------------------------------
# This makes the pen draw at differnt speeds.

t.updateStroke(159)
for i in range(15):
  t.setSpeed(i*2+1)
  t.fd(1)
