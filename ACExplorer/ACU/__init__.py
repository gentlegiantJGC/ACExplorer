import json

from . exportDataBlockModels_ import exportDataBlockModels

from . readFile_ import read_file

from . right_click_methods.exportTexture_ import plugin as export_texture
from . exportModel_ import export_obj
from ..ACU import formatFile
from . getMaterialIDs_ import get_material_ids

from . readModel_ import read_model
from . exportFakes_ import export_fakes

gameIdentifier = 'ACU'
file_types = json.load(open(r"./ACExplorer/ACU/fileFormats.json"))
