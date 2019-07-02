# ACExplorer
What is ACExplorer?
ACExplorer is a file explorer, exporter and framework for accessing data from the Assassin's Creed .forge file format. Written in python 3.7

I accept donations at the following link if you want to help: https://www.paypal.me/gentlegiantJGC

ACExplorer enables extracting assets from the save format including meshes, textures, assembled meshes as they appear in the world and the assembled low resolution meshes used far from the player. Adding support for other files or export methods is as simple as writing a little python code which can be done by an end user with some programming knowledge.

Currently only Assassin's Creed Unity is supported but the program has been designed to make adding other games almost as easy as adding a reader for the format.

A small amount of the code is based on code from ARchive_neXt which can be found here : http://www.tbotr.net

The long term goal is to include other games that use the forge file storage system but currently the goal is to be able to export the world models from AC Unity.

# Compiled Builds
We finally have a release version that you can download and run without having to install python or any of the dependencies. It can be found at the following link: https://github.com/gentlegiantJGC/ACExplorer/releases

Extract all files from the zip folder into a directory and run the exe file.

# Installing From Source
Prerequisites:
- Python 3.7
- numpy >= 1.15
- pyside2 >= 5.0
- Pillow >= 5.2

Download the whole repository and run ACExplorer.py

# Using ACExplorer
- Load the program (run ACExplorer.py or ACExplorer.exe depending on which of the above two methods you use).
- Select "Games" in the top left corner which will bring up a dialogue box of paths to each of the games.
- Click the right box for the games you want to add the path and navigate to the install location for that game.
- Click OK.
- The program will read the forge files to get some information and will build the file tree in the UI.
- Click on the arrow next to the entry to expand or contract that entry.
- Right click an entry to see which export methods there are for that file.

Some export methods will have a right click mouse button next to them. These have aditional options, such as the export format, which can be obtained by right clicking (the plugin command will be run when the last option screen is filled) or left click to use the previously used options (options do not persist after closing)

Some fun files to export are mesh files (usually end in LOD and a number 0-5 eg LOD0), Cell DataBlock files contain the data of how the individual models are pieced together. There is a plugin to export this data but the exports are incomplete due to incomplete support of the file format.

There is a discussion thread for this program over on Xentax where I will be making posts to answer frequently asked questions: https://forum.xentax.com/viewtopic.php?f=10&t=20061

# Screenshots
![ACExplorer User Interface](/resources/screenshots/ACExplorer.png)
![ACExplorer Context Menu](/resources/screenshots/context.png)
![ACExplorer Plugin Menu](/resources/screenshots/plugin_options.png)

# Example Exports
![Cell07603](/resources/screenshots/Cell07603.png)
![Notre Dame](/resources/screenshots/ND1.png)
![Notre Dame](/resources/screenshots/ND2.png)
![Notre Dame](/resources/screenshots/ND3.png)
