# ACExplorer
What is ACExplorer?
ACExplorer is a file explorer, exporter and framework for accessing data from the Assassin's Creed .forge file format. Written in python 3.7

I accept donations at the following link if you want to help: https://www.paypal.me/gentlegiantJGC

ACExplorer enables extracting assets from the save format including meshes, textures, assembled meshes as they appear in the world and the assembled low resolution meshes used far from the player. Adding support for other files or export methods is as simple as writing a little python code which can be done by an end user with some programming knowledge.

Currently only Assassin's Creed Unity is supported but the program has been designed to make adding other games almost as easy as adding a reader for the format.

A small amount of the code is based on code from ARchive_neXt which can be found here : http://www.tbotr.net

The long term goal is to include other games that use the forge file storage system but currently the goal is to be able to export the world models from AC Unity.

# Installing From Source
Prerequisites:
- Python 3.7
- numpy >= 1.15
- pyside2 >= 5.0
- Pillow >= 5.2

Download the whole repository and run ACExplorer.py

# Compiled Builds
We finally have a release version that you can download and run without having to install python or any of the dependencies. It can be found at the following link:

https://github.com/gentlegiantJGC/ACExplorer/releases
