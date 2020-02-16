# https://repl.it/@KJones94/MinecraftReference
from mcpi.minecraft import Minecraft
# from mcpi import block
import time
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
#----enums----


#------------PEN PROPERTIES------------
lifted = False

yawDirections = [5, 3, 4, 2]  # list of turn faces
yaw = 0  # current pointer of yaw
# v This you have to multiply by the current yaw direction v
pitch = 1  # 1 = neural; 1/yaw = up; 0 = down
rotation = yawDirections[yaw] * pitch
strokeBlock = 0
x = 0
y = 0
z = 0
homeX = 0
homeY = 0
HomeZ = 0
speed = 0.25
#------------PEN PROPERTIES------------


#---------------PEN CONFIG---------------------
def create_pen(cx, cy, cz):
    # make a pen facing east    
    mc.setBlock(cx, cy, cz, 33, 5)
    global rotation
    global x
    global y
    global z
    global homeX
    global homeY
    global homeZ
    rotation = 5
    x = cx
    y = cy
    z = cz
    homeX = cx
    homeY = cy
    homeZ = cz


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
    update_pos(homeX + offsetX, homeY + offsetY, homeZ + offsetZ)
    
def forward(amount):
    global speed
    for i in range(0, amount):
    # move the piston in the specified rotation
        if rotation == 0:
            # down
            mc.setBlock(x, y - 1, z, 33, 0)
            mc.setBlock(x, y, z, strokeBlock)
            update_pos(x, y - 1, z)
            time.sleep(speed)
        if rotation == 1:
            # up
            mc.setBlock(x, y + 1, z, 33, 1)
            mc.setBlock(x, y, z, strokeBlock)
            update_pos(x, y + 1, z)
            time.sleep(speed)
        if rotation == 2:
            # north
            mc.setBlock(x, y, z - 1, 33, 2)
            mc.setBlock(x, y, z, strokeBlock)
            update_pos(x, y, z - 1)
            time.sleep(speed)
        if rotation == 3:
            # south
            mc.setBlock(x, y, z + 1, 33, 3)
            mc.setBlock(x, y, z, strokeBlock)
            update_pos(x, y, z + 1)
            time.sleep(speed)
        if rotation == 4:
            # west
            mc.setBlock(x - 1, y, z, 33, 4)
            mc.setBlock(x, y, z, strokeBlock)
            update_pos(x - 1, y, z)
            time.sleep(speed)
        if rotation == 5:
            # east
            mc.setBlock(x + 1, y, z, 33, 5)
            mc.setBlock(x, y, z, strokeBlock)
            update_pos(x + 1, y, z)
            time.sleep(speed)

def fd(amount):
    forward(amount)

def backward(amount):
    for i in range(0, amount):
    # move the piston in the specified rotation
        if rotation == 0:
            # down
            mc.setBlock(x, y + 1, z, 33, 0)
            mc.setBlock(x, y, z, strokeBlock)
            update_pos(x, y + 1, z)
            time.sleep(speed)
        if rotation == 1:
            # up
            mc.setBlock(x, y - 1, z, 33, 1)
            mc.setBlock(x, y, z, strokeBlock)
            update_pos(x, y - 1, z)
            time.sleep(speed)
        if rotation == 2:
            # north
            mc.setBlock(x, y, z + 1, 33, 2)
            mc.setBlock(x, y, z, strokeBlock)
            update_pos(x, y, z + 1)
            time.sleep(speed)
        if rotation == 3:
            # south
            mc.setBlock(x, y, z - 1, 33, 3)
            mc.setBlock(x, y, z, strokeBlock)
            update_pos(x, y, z - 1)
            time.sleep(speed)
        if rotation == 4:
            # west
            mc.setBlock(x + 1, y, z, 33, 4)
            mc.setBlock(x, y, z, strokeBlock)
            update_pos(x + 1, y, z)
            time.sleep(speed)
        if rotation == 5:
            # east
            mc.setBlock(x - 1, y, z, 33, 5)
            mc.setBlock(x, y, z, strokeBlock)
            update_pos(x - 1, y, z)
            time.sleep(speed)

def bk(amount):
    backward(amount)

def setSpeed(newSpeed):
    # x blocks per second
    global speed
    speed = 1/newSpeed

def turn(direction):  # turn based on a circle of rotation
    global rotation
    if direction == direction.RIGHT or direction == direction.LEFT:
        __update_rotation(direction, direction.KEEP_SAME)
        mc.setBlock(x, y, z, 33, rotation)
    elif direction == direction.UP or direction == direction.DOWN:
        __update_rotation(direction.KEEP_SAME, direction)
        mc.setBlock(x, y, z, 33, rotation)
    elif direction == direction.KEEP_SAME:
        pass
    else:
        print("illegal turn direction argument. Direction can only be LEFT, RIGHT, UP, or DOWN")
    

create_pen(px, py, pz)
update_stroke(35)
time.sleep(3)

for i in range(20):
    setSpeed((i+1)/2)
    fd(1)
turn(direction.RIGHT)
bk(5)
