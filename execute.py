# https://repl.it/@KJones94/MinecraftReference
from mcpi.minecraft import Minecraft
# from mcpi import block
from math import *
import time
import enum
import random

# mc = Minecraft.create("52.8.34.121", 4711)
mc = Minecraft.create("localhost")
playerId = mc.getPlayerEntityId("GnarlyLlama")
pos = mc.entity.getPos(playerId)
px = pos.x
py = pos.y
pz = pos.z

# def set_pen(x, y, z):
#   mc.setBlock(x, y, z, block.DIAMOND_BLOCK)
#   mc.entity.setPos(x, y, z)

# def forward(steps):
#   mc.setBlock()
#   time.sleep


#----enums----
class direction(enum.Enum):
    LEFT = 0
    RIGHT = 1
    UP = 2
    DOWN = 3
    KEEP_SAME = 4
    
class heading(enum.Enum):
    DOWN = 0
    UP = 1
    NORTH = 2
    SOUTH = 3
    WEST = 4
    EAST = 5

def headingToString(heading):
    if heading == 0 or heading == heading.UP:
        return "Facing Down"
    if heading == 1 or heading == heading.DOWN:
        return "Facing Up"
    if heading == 2 or heading == heading.NORTH:
        return "Facing North"
    if heading == 3 or heading == heading.SOUTH:
        return "Facing South"
    if heading == 4 or heading == heading.WEST:
        return "Facing West"
    if heading == 5 or heading == heading.EAST:
        return "Facing East"
#----enums----


#------------PEN PROPERTIES------------
lifted = False

yawDirections = [5, 3, 4, 2]  # list of turn faces
yaw = 0  # current pointer of yaw
# v This you have to multiply by the current yaw direction v
pitch = 1  # 1 = neural; 1/yaw = up; 0 = down
rotation = yawDirections[yaw] * pitch
strokeBlock = 0
isDown = True
x = 0
y = 0
z = 0
homeX = 0
homeY = 0
HomeZ = 0
speed = 0.25
incomeStorage = None
trailStorage = None
#------------PEN PROPERTIES------------


#---------------PEN CONFIG---------------------
def createPen(cx, cy, cz):
    # make a pen facing eas
    global rotation
    global x
    global y
    global z
    global homeX
    global homeY
    global homeZ
    global incomeStorage
    global trailStorage
    x = floor(cx)
    y = floor(cy)
    z = floor(cz)
    rotation = 5
    trailStorage = mc.getBlockWithData(cx, cy, cz)
    incomeStorage = __get_block_on_side(rotation)
    homeX = x
    homeY = y
    homeZ = z
    mc.setBlock(cx, cy, cz, 33, 5)
    
    print(cx, cz)


def updatePos(ux, uy, uz):
    global x
    global y
    global z
    x = ux
    y = uy
    z = uz


def updateStroke(block):
    global strokeBlock
    strokeBlock = block


def __cycle_yaw(direction):
    global yaw
    if direction == direction.RIGHT:
        # cycle it to the RIGHT
        if yaw == 3:  # reached end, reset
            yaw = 0
        else:
            yaw += 1
    elif direction == direction.LEFT:
        # cycle to left
        if yaw == 0:  # reached end, reset
            yaw = 3
        else:
            yaw -= 1
    elif direction == direction.KEEP_SAME:
        pass
    else:
        print("error: illegal direction argument " +
            direction + ". Direction can only be left/right")


def __update_rotation(yawDirection, pitchDirection):
    # based on the yaw*pitch formula, update the master rotation value
    global pitch
    global yawDirections
    global yaw
    global rotation
    
    #first, we update the yaw
    __cycle_yaw(yawDirection)
    
    #second, we update the pitch
    if pitch == 1: #normal state
        if pitchDirection == direction.DOWN: #if user wants to face down
            pitch = 0
        elif pitchDirection == direction.UP: #if user wants to face up
            pitch = 1/yawDirections[yaw]
        elif pitchDirection == direction.KEEP_SAME:
            pass
        else:
            print("illegal pitch direction statement. Pitch can only be UP or DOWN")
    elif pitch == 0: #if it is currently facing down
        if pitchDirection == direction.UP: #then make it face up
            pitch = 1
        elif pitchDirection == direction.DOWN or pitchDirection == direction.KEEP_SAME: #these won't be able to do anything
            pass
        else:
            print("illegal pitch direction statement. Pitch can only be UP or DOWN")
    else: #then it must be facing up, as it its not down or neutral
        if pitchDirection == direction.DOWN:
            pitch = 1
        elif pitchDirection == direction.UP or pitchDirection == direction.KEEP_SAME: #these won't do anything either
            pass
        else:
            print("illegal pitch direction statement. Pitch can only be UP or DOWN")
            
    #third, we update the master rotational value
    rotation = yawDirections[yaw] * pitch
    #end of rotation update
            
    #---------------PEN CONFIG---------------------

def __get_block_on_side(direction, onBack = False):
    global x
    global y
    global z
    
    #onBack's function serves to reverse the direction of where it is getting the block from.
    #Ex: direction = UP, onBack = True --> blockData(DOWN)
    
    if direction == 5 or direction == heading.EAST:
        if not onBack:
            return mc.getBlockWithData(x+1,y,z)
        else:            
            return mc.getBlockWithData(x-1,y,z)
    if direction == 4 or direction == heading.WEST:
        if not onBack:
            return mc.getBlockWithData(x-1,y,z)
        else:            
            return mc.getBlockWithData(x+1,y,z)
    if direction == 3 or direction == heading.SOUTH:
        if not onBack:
            return mc.getBlockWithData(x,y,z+1)
        else:            
            return mc.getBlockWithData(x,y,z-1)
    if direction == 2 or direction == heading.NORTH:
        if not onBack:
            return mc.getBlockWithData(x,y,z-1)
        else:            
            return mc.getBlockWithData(x,y,z+1)
    if direction == 1 or direction == heading.UP:
        if not onBack:
            return mc.getBlockWithData(x,y+1,z)
        else:            
            return mc.getBlockWithData(x,y-1,z)
    if direction == 0 or direction == heading.DOWN:
        if not onBack:
            return mc.getBlockWithData(x,y-1,z)
        else:            
            return mc.getBlockWithData(x,y+1,z)

#use param for positive and negative and xyz
# def __get_block_behind():
#     global rotation
#     global x
#     global y
#     global z
#     if rotation == 5:
#         return mc.getBlockWithData(x-1,y,z)
#     if rotation == 4:
#         return mc.getBlockWithData(x+1,y,z)
#     if rotation == 3:
#         return mc.getBlockWithData(x,y,z-1)
#     if rotation == 2:
#         return mc.getBlockWithData(x,y,z+1)
#     if rotation == 1:
#         return mc.getBlockWithData(x,y-1,z)
#     if rotation == 0:
#         return mc.getBlockWithData(x,y+1,z)
    
def home(offsetX = 0, offsetY = 0, offsetZ = 0):
    global rotation
    global x
    global y
    global z
    global homeX
    global homeY
    global homeZ
    mc.setBlock(homeX + offsetX, homeY + offsetY, homeZ + offsetZ, 33, rotation)
    mc.setBlock(x, y, z, strokeBlock)
    updatePos(homeX + offsetX, homeY + offsetY, homeZ + offsetZ)
    
def forward(amount):
    global speed
    global incomeStorage
    global trailStorage
    
    incomeStorage = __get_block_on_side(rotation)    
    for i in range(0, amount):
    # move the piston in the specified rotation
        if not isDown:
            #store the block data infront into "incomeStorage"
            #move forward and place block in "trailStorage"
            #transfer the block data in "incomeStorage" into "trailStorage"
            updateStroke(trailStorage)
            
    
        if rotation == 0:
            # down
            mc.setBlock(x, y - 1, z, 33, 0)                
            mc.setBlock(x, y, z, strokeBlock)
            updatePos(x, y - 1, z)
            time.sleep(speed)
        if rotation == 1:
            # up
            mc.setBlock(x, y + 1, z, 33, 1)
            mc.setBlock(x, y + 1, z, strokeBlock, 1)
            mc.setBlock(x, y, z, strokeBlock)
            updatePos(x, y + 1, z)
            time.sleep(speed)
        if rotation == 2:
            # north
            mc.setBlock(x, y, z - 1, 33, 2)               
            mc.setBlock(x, y, z, strokeBlock)
            updatePos(x, y, z - 1)
            time.sleep(speed)
        if rotation == 3:
            # south
            mc.setBlock(x, y, z + 1, 33, 3)
            mc.setBlock(x, y, z, strokeBlock)
            updatePos(x, y, z + 1)
            time.sleep(speed)
        if rotation == 4:
            # west
            mc.setBlock(x - 1, y, z, 33, 4)
            mc.setBlock(x, y, z, strokeBlock)
            updatePos(x - 1, y, z)
            time.sleep(speed)
        if rotation == 5:
            # east
            mc.setBlock(x + 1, y, z, 33, 5)
            mc.setBlock(x, y, z, strokeBlock)
            updatePos(x + 1, y, z)
            time.sleep(speed)
        
        trailStorage = incomeStorage
        incomeStorage = __get_block_on_side(rotation)

def fd(amount):
    forward(amount)

def backward(amount):
    global incomeStorage
    global trailStorage
    
    incomeStorage = __get_block_on_side(rotation, True)
    for i in range(0, amount):
        if not isDown:
            #store the block data infront into "incomeStorage"
            #move forward and place block in "trailStorage"
            #transfer the block data in "incomeStorage" into "trailStorage"
            updateStroke(trailStorage)
        # move the piston in the specified rotation
        if rotation == 0:
            # down
            mc.setBlock(x, y + 1, z, 33, 0)
            mc.setBlock(x, y, z, strokeBlock)
            updatePos(x, y + 1, z)
            time.sleep(speed)
        if rotation == 1:
            # up
            mc.setBlock(x, y - 1, z, 33, 1)
            mc.setBlock(x, y, z, strokeBlock)
            updatePos(x, y - 1, z)
            time.sleep(speed)
        if rotation == 2:
            # north
            mc.setBlock(x, y, z + 1, 33, 2)
            mc.setBlock(x, y, z, strokeBlock)
            updatePos(x, y, z + 1)
            time.sleep(speed)
        if rotation == 3:
            # south
            mc.setBlock(x, y, z - 1, 33, 3)
            mc.setBlock(x, y, z, strokeBlock)
            updatePos(x, y, z - 1)
            time.sleep(speed)
        if rotation == 4:
            # west
            mc.setBlock(x + 1, y, z, 33, 4)
            mc.setBlock(x, y, z, strokeBlock)
            updatePos(x + 1, y, z)
            time.sleep(speed)
        if rotation == 5:
            # east
            mc.setBlock(x - 1, y, z, 33, 5)
            mc.setBlock(x, y, z, strokeBlock)
            updatePos(x - 1, y, z)
            time.sleep(speed)
        trailStorage = incomeStorage
        incomeStorage = __get_block_on_side(rotation, True)

def bk(amount):
    backward(amount)
    
def setx(newX):
    global x
    global rotation
    global trailStorage
    global incomeStorage
    
    if newX > int(x):
        incomeStorage = __get_block_on_side(heading.EAST)           
        for i in range(int(abs(newX-x))):
            if not isDown:
                updateStroke(trailStorage)
            mc.setBlock(x+1, y, z, 33, rotation)
            mc.setBlock(x, y, z, strokeBlock)
            updatePos(x+1, y, z)
            trailStorage = incomeStorage
            incomeStorage = __get_block_on_side(heading.EAST)            
            time.sleep(speed)
    else:
        incomeStorage = __get_block_on_side(heading.EAST, True)        
        for i in range(int(abs(newX-x))):
            if not isDown:
                updateStroke(trailStorage)
            mc.setBlock(x-1, y, z, 33, rotation)
            mc.setBlock(x, y, z, strokeBlock)
            updatePos(x-1, y, z)
            trailStorage = incomeStorage
            incomeStorage = __get_block_on_side(heading.EAST, True)            
            time.sleep(speed)
            
def sety(newY):
    global y
    global rotation
    global trailStorage
    global incomeStorage

    if newY > int(y):
        incomeStorage = __get_block_on_side(heading.UP)            
        for i in range(int(abs(newY-y))):
            if not isDown:
                updateStroke(trailStorage)
            mc.setBlock(x, y+1, z, 33, rotation)
            mc.setBlock(x, y, z, strokeBlock)
            updatePos(x, y+1, z)
            trailStorage = incomeStorage
            incomeStorage = __get_block_on_side(heading.UP)            
            time.sleep(speed)
    else:
        incomeStorage = __get_block_on_side(heading.UP, True)            
        for i in range(int(abs(newY-y))):
            if not isDown:
                updateStroke(trailStorage)
            mc.setBlock(x, y-1, z, 33, rotation)
            mc.setBlock(x, y, z, strokeBlock)
            updatePos(x, y-1, z)
            trailStorage = incomeStorage
            incomeStorage = __get_block_on_side(heading.UP, True)            
            time.sleep(speed)
            
def setz(newZ):
    global z
    global rotation
    if newZ > int(z):
        incomeStorage = __get_block_on_side(heading.SOUTH)            
        for i in range(int(abs(newZ-z))):
            if not isDown:
                updateStroke(trailStorage)
            mc.setBlock(x, y, z+1, 33, rotation)
            mc.setBlock(x, y, z, strokeBlock)
            updatePos(x, y, z+1)
            trailStorage = incomeStorage
            incomeStorage = __get_block_on_side(heading.SOUTH)            
            time.sleep(speed)
    else:
        incomeStorage = __get_block_on_side(heading.SOUTH, True)            
        for i in range(int(abs(newZ-z))):
            if not isDown:
                updateStroke(trailStorage)
            mc.setBlock(x, y, z-1, 33, rotation)
            mc.setBlock(x, y, z, strokeBlock)
            updatePos(x, y, z-1)
            trailStorage = incomeStorage
            incomeStorage = __get_block_on_side(heading.SOUTH, True)            
            time.sleep(speed)

def goto(newX, newY, newZ):
    #reference: https://en.wikipedia.org/wiki/Line_drawing_algorithm
    global x
    global y
    global z
    
    staticx = x
    staticy = y
    staticz = z
    
    deltax = newX - x
    deltay = newY - y
    deltaz = newZ - z
    
    print(x)
    
    for i in range(1,abs(newX - x)+1):
        if (newX-x) > 0:
            setx(staticx+i)
            sety(staticy+round(i*(deltay/deltax)))
            setz(staticz+round(i*(deltaz/deltax)))
        else:            
            setx(staticx-i)
            sety(staticy-round(i*(deltay/deltax)))
            setz(staticz-round(i*(deltaz/deltax)))
    
    #TODO finish path algorithm

def setSpeed(newSpeed):
    # x blocks per second
    global speed
    speed = 1/newSpeed

def turn(direction):  # turn based on a circle of rotation
    global rotation
    global speed
    if direction == direction.RIGHT or direction == direction.LEFT:
        __update_rotation(direction, direction.KEEP_SAME)
        mc.setBlock(x, y, z, 33, rotation)
        time.sleep(speed)
    elif direction == direction.UP or direction == direction.DOWN:
        __update_rotation(direction.KEEP_SAME, direction)
        mc.setBlock(x, y, z, 33, rotation)
    elif direction == direction.KEEP_SAME:
        pass
    else:
        print("illegal turn direction argument. Direction can only be LEFT, RIGHT, UP, or DOWN")
    
def xcor():
    global x
    return x
def ycor():
    global y
    return y
def zcor():
    global z
    return z
def isDown():
    global isDown
    return isDown
def penUp():
    global isDown
    isDown = False
def penDown():
    global isDown
    isDown = True
def facing():
    global rotation
    return headingToString(rotation)
def position():
    global x
    global y
    global z
    return (x,y,z)
def setHeading(direction):
    global rotation
    global speed
    if isinstance(direction, heading):
        rotation = direction.value()
        mc.setBlock(x, y, z, 33, rotation)
        time.sleep(speed)
    if type(direction) != int and direction <= 5 and direction >=0:
        print('Error: direction can only be integer or a heading enum. You passed in a ', type(direction),'. This step will not run due to the error.')
        return TypeError
    rotation = direction
    mc.setBlock(x, y, z, 33, rotation)
    time.sleep(speed)
    
def seth(direction):
    setHeading(direction)

def distance(nx, ny, nz):
    global x
    global y
    global z
    xz = sqrt((nx-x)**2 + (nz-z)**2)
    print(x, z)
    return sqrt(xz**2 + (ny-y)**2)

def stamp():
    pass

createPen(px, py-1, pz)
time.sleep(3)
updateStroke(0)

print(distance(0,54,0))
# 9786 54 9991
# for i in range(1,abs(9786 - 9779)+1):
#     setx(9779+i);
#     print('i', i)
#     print('newX values: ', 9779+i)
#     print(9779+i+2)
#     print('currentPenx: ', x)
#     print('------')
