
# NOTE: Please check [demo1.py] for all explanation on how the set up works!
from mcpi.minecraft import Minecraft
import time
from MCpen.mcturtle import MCTurtle, direction
import random

mc = Minecraft.create("localhost")
playerId = mc.getPlayerEntityId("GnarlyLlama")
pos = mc.entity.getPos(playerId)
px = pos.x
py = pos.y
pz = pos.z
t = MCTurtle(mc, px, py-1, pz)
time.sleep(3)

#---------------------------------------------
#This one draws a bunch a different colored shulker boxes.

t.updateStroke(159)
for i in range(15):
  t.updateStroke(i+219)
  t.fd(1)
