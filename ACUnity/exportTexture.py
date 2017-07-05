def exportTexture(fileTree, fileList, config, fileID):
	from misc.dataTypes import LE2DEC2
	from misc import tempFiles
	import os

	if not tempFiles.exists(config, fileID):
		from ACUnity.decompressDatafile import decompressDatafile
		decompressDatafile(fileTree, fileList, config, fileID)
	data = tempFiles.read(config, fileID)
	if len(data) == 0:
		raise Exception('file '+fileID+' is empty')
	data = data[0]
	path1 = data['dir']
	fileName = data['fileName']
	path2 = config['dumpFolder'] + os.sep + fileName + '.dds'
	if os.path.isfile(path2):
		return
	fi = open(path1, 'rb')
	_ = fi.read(14)
	num1 = fi.read(4)
	num2 = fi.read(4)
	_ = fi.read(4)
	imgDXT = LE2DEC2(fi.read(4))
	_ = fi.read(8)
	num3 = fi.read(4)
	_ = fi.read(84)
	count = fi.read(4)
	buffer = fi.read(LE2DEC2(count))
	
	fi.close()
	

	fi = open(path2, 'wb')
	fi.write('DDS ')
	fi.write('\x7C\x00\x00\x00\x07\x10\x0A\x00')
	fi.write(num2)
	fi.write(num1)
	fi.write(count)
	fi.write('\x00\x00\x00\x00')
	fi.write(num3)
	for index in range(11):
		fi.write('\x00\x00\x00\x00')
	fi.write('\x20\x00\x00\x00')
	if imgDXT == 0 or imgDXT == 7:
		fi.write('\x40\x00\x00\x00')
	else:
		fi.write('\x04\x00\x00\x00')
	if imgDXT in [0, 7]:
		fi.write('\x44\x58\x54\x30') #DXT0
	elif imgDXT in [1, 2, 3]:
		fi.write('\x44\x58\x54\x31') #DXT1
	elif imgDXT == 4:
		fi.write('\x44\x58\x54\x33') #DXT3
	elif imgDXT == 5:
		fi.write('\x44\x58\x54\x35') #DXT5
	elif imgDXT == 8:
		fi.write('\x44\x58\x31\x30') #DX10
		
	for index in range(5):
		fi.write('\x00\x00\x00\x00')
	fi.write('\x08\x10\x40\x00')
	for index in range(4):
		fi.write('\x00\x00\x00\x00')
	if imgDXT == 8:
		fi.write('\x62\x00\x00\x00')
		fi.write('\x03\x00\x00\x00')
		fi.write('\x00\x00\x00\x00')
		fi.write('\x01\x00\x00\x00')
		fi.write('\x00\x00\x00\x00')
	fi.write(buffer)
	fi.close()
	if imgDXT == 8:
		texconv = '"' + config['texconv'] + '" '
		# else
		# {
			# str4 = arxForm.tempDir + "\\" + tNode.Parent.Parent.Parent.Text + "\\dx9_";
			# path2 = arxForm.tempDir + "\\" + tNode.Parent.Parent.Parent.Text + "\\dx9_" + tNode.Text + "." + strArray3[1];
		# }
		arguments = "-fl 9.1 -px " + config['dumpFolder'] + os.sep + " -f BC3_UNORM " + path2
		os.system(texconv+arguments)