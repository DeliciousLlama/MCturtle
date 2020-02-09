# https://repl.it/@KJones94/MinecraftReference
from mcpi.minecraft import Minecraft
from mcpi import block
import time
import random
import enum

# mc = Minecraft.create("52.8.34.121", 4711)
mc = Minecraft.create("localhost")
playerId = mc.getPlayerEntityId("Flying_Llama666")
pos = mc.entity.getPos(playerId)
px = pos.x
py = pos.y
pz = pos.z

# def set_pen(x, y, z):
#   mc.setBlock(x, y, z, block.DIAMOND_BLOCK)
#   mc.entity.setPos(x, y, z)

# def move_forward(steps):
#   mc.setBlock()
#   time.sleep











#----enums----
class direction(enum.Enum):
  LEFT = 0
  RIGHT = 1
  UP = 2
  DOWN = 3
#----enums----

#------------PEN PROPERTIES------------
lifted = False

yawDirections = [5,3,4,2]
yaw = 0
#v This you have to multiply by the current yaw direction v
pitch = 1 #1 = neural; 1/rotation = up; 0 = down
rotation = yawDirections[yaw] * pitch
strokeBlock = 0
x = 0
y = 0
z = 0
#------------PEN PROPERTIES------------

#---------------PEN CONFIG---------------------
def create_pen(cx, cy, cz):
  #make a pen facing east
  mc.setBlock(cx, cy, cz, 33, 5)
  global rotation
  global x
  global y
  global z
  rotation = 5
  x = cx
  y = cy
  z = cz

def update_pos(ux, uy, uz):
  global x
  global y
  global z
  x = ux
  y = uy
  z = uz

def update_stroke(block):
  global strokeBlock
  strokeBlock = block

def __cycle_yaw(direction):
  global yaw
  if direction == direction.RIGHT:
    #cycle it to the RIGHT
    if yaw == 3: #reached end, reset
      yaw = 0
    else:
      yaw += 1
  elif direction == direction.LEFT:
    #cycle to left
    if yaw == 0: #reached end, reset
      yaw = 3
    else:
      yaw -= 1
  else:
    print("error: illegal direction argument " + direction + ". Direction can only be left/right")


def update_rotation(yAxis, pitch):
  global rotation
  #first, update the abstract data of the rotation
  #the pitch data:
  if rotation == 1: #normal state
    if pitch == direction.UP:
      #then pitch is 1/yaw
      pass
  if yAxis == direction.RIGHT:
    #then cycle to the RIGHT
    __cycle_yaw(direction.RIGHT)
  elif yAxis == direction.LEFT:
    __cycle_yaw(direction.LEFT)
  #calculate new rotation based on pseudoenum
#---------------PEN CONFIG---------------------


def move_forward(amount):
  for i in range(0,amount):
    #move the piston in the specified rotation
    if rotation == 0:
      #down
      mc.setBlock(x, y-1, z, 33, 0)
      mc.setBlock(x, y, z, strokeBlock)
      update_pos(x, y-1, z)
      time.sleep(0.5)
    if rotation == 1:
      #up
      mc.setBlock(x,y+1,z,33,1)
      mc.setBlock(x, y, z, strokeBlock)
      update_pos(x, y+1, z)
      time.sleep(0.5)
    if rotation == 2:
      #north
      mc.setBlock(x,y,z-1,33,2)
      mc.setBlock(x, y, z, strokeBlock)
      update_pos(x, y, z-1)
      time.sleep(0.5)
    if rotation == 3:
      #south
      mc.setBlock(x,y,z+1,33,3)
      mc.setBlock(x, y, z, strokeBlock)
      update_pos(x, y, z+1)
      time.sleep(0.5)
    if rotation == 4:
      #west
      mc.setBlock(x-1,y,z,33,4)
      mc.setBlock(x, y, z, strokeBlock)
      update_pos(x-1, y, z)
      time.sleep(0.5)
    if rotation == 5:
      #east
      mc.setBlock(x+1,y,z,33,5)
      mc.setBlock(x, y, z, strokeBlock)
      update_pos(x+1, y, z)
      time.sleep(0.5)

def rotate(direction): #turn based on a circle of rotation
  global rotation
  if direction == "right":
    if rotation == 5:
      rotation = 3
      mc.setBlock(x,y,z,33,rotation)
    elif rotation == 4:
      rotation = 2
      mc.setBlock(x,y,z,33,rotation)
    elif rotation == 3:
      rotation = 4
      mc.setBlock(x,y,z,33,rotation)
    elif rotation == 2:
      rotation = 5
      mc.setBlock(x,y,z,33,rotation)

  elif direction == "left":
    if rotation == 5:
      rotation = 2
      mc.setBlock(x,y,z,33,rotation)
    elif rotation == 2:
      rotation = 4
      mc.setBlock(x,y,z,33,rotation)
    elif rotation == 4:
      rotation = 3
      mc.setBlock(x,y,z,33,rotation)
    elif rotation == 3:
      rotation = 5
      mc.setBlock(x,y,z,33,rotation)

create_pen(px,py-1,pz)
time.sleep(1)
move_forward(5)
rotate("right")
move_forward(5)
rotate("left")
move_forward(5)





