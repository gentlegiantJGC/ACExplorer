import json

from readForge_ import read_forge

from decompressDatafile_ import decompress_datafile
from exportDataBlockModels_ import exportDataBlockModels

from readFile_ import readFile

from exportTexture_ import export_texture
from exportModel_ import export_obj
import formatFile
from getMaterialIDs_ import get_material_ids

from readModel_ import read_model
from ACExplorer.ACUnity.exportFakes_ import export_fakes

gameIdentifier = 'ACU'
file_types = json.load(open(r"./ACExplorer/ACUnity/fileFormats.json"))
