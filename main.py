from mcpi.minecraft import Minecraft
import time
from mcturtle import MCTurtle, direction
import random

mc = Minecraft.create("localhost")
playerId = mc.getPlayerEntityId("GnarlyLlama")
pos = mc.entity.getPos(playerId)
px = pos.x
py = pos.y
pz = pos.z

turtle = MCTurtle(mc, pos)
time.sleep(3)
turtle.penUp()
turtle.fd(15)
turtle.penDown()
turtle.bk(15)
turtle.updateStroke(165)
turtle.turn(direction.RIGHT)
turtle.fd(5)
turtle.updateStroke(35)
turtle.setSpeed(1)
turtle.turn(direction.RIGHT)
turtle.bk(10)
turtle.turn(direction.LEFT)
time.sleep(0.5)
turtle.turn(direction.LEFT)
time.sleep(1)
turtle.turn(direction.LEFT)
time.sleep(0.25)
for i in range(1,10):
    turtle.setSpeed(i)
    turtle.updateStroke(i+12)
    turtle.fd(1)
turtle.sety(60)
turtle.updateStroke(129)
for i in range(0,7):
    turtle.setHeading(i%5)
    time.sleep(0.5)
turtle.setSpeed(4)
turtle.setx(9778)
turtle.setz(9989)
turtle.sety(54)
turtle.updateStroke(155)
turtle.goto(9782,59,9997)
turtle.updateStroke(174)
turtle.goto(9791,65,9984)
turtle.updateStroke(46)
turtle.home()
