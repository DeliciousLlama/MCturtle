
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
# Place some blocks infront of the Pen, and see what happens!

t.updateStroke(159)
t.penUp()
t.fd(15)
