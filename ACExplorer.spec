# -*- mode: python -*-
import os
import shutil
for root, dirs, _ in os.walk("."):
	for d in dirs:
		if d == '__pycache__' and os.path.isdir(os.path.join(root, d)):
			shutil.rmtree(os.path.join(root, d))

block_cipher = None

a = Analysis(
	['ACExplorer.py'],
	pathex=['D:\\Programs\\AC-Explorer'],
	binaries=[],
	datas=[
		('./resources', './resources'),
		('./pyUbiForge', './pyUbiForge'),
		('./plugins', './plugins'),
		('./icon.ico', '.')
	],
	hiddenimports=['PIL.Image', 'PIL.ImageDraw'],
	hookspath=[],
	runtime_hooks=[],
	excludes=[],
	win_no_prefer_redirects=False,
	win_private_assemblies=False,
	cipher=block_cipher,
	noarchive=False
)

pyz = PYZ(
	a.pure,
	a.zipped_data,
	cipher=block_cipher
)

exe = EXE(
	pyz,
	a.scripts,
	[],
	exclude_binaries=True,
	name='ACExplorer',
	debug=False,
	bootloader_ignore_signals=False,
	strip=False,
	upx=True,
	console=True,
	icon='icon.ico'
)

coll = COLLECT(
	exe,
	a.binaries,
	a.zipfiles,
	a.datas,
	strip=False,
	upx=True,
	name='ACExplorer'
)
