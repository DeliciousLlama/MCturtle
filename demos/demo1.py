from mcpi.minecraft import Minecraft #Importing MCPI, which is necessary for MCpen
import time #Yet another import (not that important)
from MCpen.mcturtle import MCTurtle, direction #Imports imports imports. (This one is important because it actually import the MCpen library)
#Please note: when you do [pip install MCpen], you do not need to include the MCpen before the [mcturtle]. This is for the convience for those who cannot use the pip install method.
import random
#More unnecesasry imports

mc = Minecraft.create("localhost") #This initializes the connection to a server, in this case it is 'local host', meaning that the server is local on your computer.
playerId = mc.getPlayerEntityId("GnarlyLlama") #This gets the Player ID, which contains all sorts of stuff ranging from the player's position and stuff like that.
# Note: if you wish to use your own player ID, please replace the current user name with your user name.
pos = mc.entity.getPos(playerId) # We get the position of the player we appointed to earlier.
px = pos.x # Get the X coordinate of the player's position
py = pos.y # Get the Y coordinate of the player's position
pz = pos.z # Get the Z coordinate of the player's position
t = MCTurtle(mc, px, py-1, pz) # This actually initialize and create the turtle, in this case under the player's feet.
time.sleep(3) # Time sleep 3 second so we can have time to switch over and see what is going on

#       SET UP STUFF
#---------------------------------------------
#       ACTUAL STUFF

t.updateStroke(159) # We update the stroke to 159, which is white_hardened_clay. This makes the pen draw that block when it is moved around.
t.forward(15) # We move the pen forward 15 blocks
time.sleep(1) # We wait 1 second
t.turn(direction.UP) # Turn the pen UP
time.sleep(1) # Wait another second
t.forward(10) # Move the pen forward 10 blocks (In this case it moves up because the pen it pointing upwards. Think of your self as the pen. When you turn up, going forward means going in that direction)
time.sleep(1)
t.turn(direction.DOWN) # We turn the pen back down
time.sleep(1)
t.home() # And finally, we go to the original place where the turtle came from.
