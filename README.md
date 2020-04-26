Congratuations! You actually opened me, good for you!


Click [here](https://docs.google.com/spreadsheets/d/1EaPCtmgFJXqFyS40LDxkDq4oyzprftFgylym-faExAo/edit?usp=sharing) for the library's documentations:

What is it?
---
MCpen is a graphics drawing libary implemented in Minecraft, similar to that of Python's Turtle library.
It allows you to control a "pen" in Minecraft, making it draw all kinds of shapes and lines.
For starters, please download the `demos/` folder as it contains all necessary demos to get you started with MCpen.
Any questions about the functions and how to use them, please check the library's documentation, available on [here](https://docs.google.com/spreadsheets/d/1EaPCtmgFJXqFyS40LDxkDq4oyzprftFgylym-faExAo/edit?usp=sharing).

Notes on the updates so far:
---
  + Added a bunch of functions
  + Added a special demo code that demos everything (execute.py)
  + Added README


Instruction on how to use:
---
Basically treat it as a normal library. for any help on functions or just to see what they are, check the documentation of MCpen.
In order for this to function and work properly, you have to use the MCPI library, installed by using `pip install mcpi`.
For this to work, you will need to be on a server with the correct plugin, with your Minecraft version at **1.11.2** (yes the .2 matters).
To set up your server, goto [this](https://codingmindsacademy.com/mc.html) link and follow these instructions.
  - For Windows & Linux
    1. Select the `mcwin` option to download the needed .zip file
    2. Create a folder in which you wish to put your server in
    3. Extract all the content of `mcwin.zip` into the folder you dedicated the server to.
    4. goto `path-to-where-you-made-the-folder/mcserverwin/server/`. You should see a `start.bat` file
    5. Run the `start.bat` file
    6. When it succussfully launched, launch your Minecraft in the **1.11.2** version, and then goto Multiplayer -> Direct Connect, and type in `localhost`
    7. Connect to your server and enjoy your code!
(Note: For linux users you may need to copy everything besides for the `java ... spigot.jar` into a new executable, such as `start.sh`, and make the new file executable)

Stuff to look out for:
---
  - Pen will not store +NBT data of blocks, even with pen up (for now)
  - The draw line function will sometimes be janky and the line wont look perfectly straight. (It's Minecraft)
  - Try not to over speed the pen, as you won't see it go anywhere and possibly destroy some of your builds if you are not careful.
  - If there is something wrong immediatly pause or kill the program in your IDE or your TERMINAL, not minecraft chat
  - In order to set it up, you will need to connect to a minecraft server, either local with the correct plugins or distant with the corrent plugins. Please check the demos to see how to set up your code.

Installation:
---
To get this thing on your computer, type: `pip install MCpen` in your command line.
