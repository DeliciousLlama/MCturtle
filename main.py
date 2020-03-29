from mcpi.minecraft import Minecraft
import time
from mcturtle import MCTurtle

mc = Minecraft.create("localhost")
playerId = mc.getPlayerEntityId("GnarlyLlama")
pos = mc.entity.getPos(playerId)
px = pos.x
py = pos.y
pz = pos.z

turtle = MCTurtle(mc, playerId)
