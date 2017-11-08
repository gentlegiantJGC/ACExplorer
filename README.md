# AC-Explorer
A file explorer and exporter for the Assassin's Creed Unity's forge file format. Written in python 2.7

A lot of the code is based on a program called ARchive_neXt which can be found here : http://www.tbotr.net.
The code was ported to python at which point further features were added.

The main aim of this project is to be able to export whole sections of the world correctly pieced together.

The long term goal is to include other games that use the forge file storage system but currently the goal is to be able to export the world models from AC Unity.

# Prerequisites
- Python 2.7

In theory that should be all.

# A summary of the forge file system
a forge file is a file that sits in a folder on your computer. It is similar in a way to a zip archive in the sense that it contains more files and is compressed.

For developers wanting more details on how a forge file is stored see the tbotr wiki page found here : http://wiki.tbotr.net/index.php?title=Assassins_Creed:File_Formats

Once the forge file has been unpacked (this program does that for you) the forge file can be represented as follows

- <forgeFileName>.forge

  - datafile
  
    - file
    
    - file
    
    - file
    
    - ...
    
  - datafile
  
    - file
    
    - file
    
    - file
    
    - ...
    
  - ...
  
A datafile will be called a name (usually giving a clue what it contains) and will contain more files. One of these files will have the same name as the datafile.

In the case of image files they are stored in their own datafile on their own. Other files such as CellXXXXX_DataBlock files contain many many files that describe how different sections of the world work. They include entity files that describe where 3D models need to go to build the world
