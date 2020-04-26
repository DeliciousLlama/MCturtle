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

t.updateStroke(159) # We draw white_hardened_clay again
for i in range(4):  # Repeats 4 times
  t.turn(direction.RIGHT) # Turn right
  t.fd(1) # Forward 1
  t.turn(direction.LEFT) # Turn Left
  t.fd(2) # Forward 2
  t.turn(direction.LEFT) # Turn Left again
  t.fd(1) # Forward 1
  t.turn(direction.RIGHT) # Turn Right
  t.fd(2) # Forward 2
