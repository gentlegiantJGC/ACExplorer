import json

from ..ACU import framework
from . getMaterialIDs_ import get_material_ids

game_identifier = 'ACU'
file_types = json.load(open(r"./ACExplorer/ACU/fileFormats.json"))
file_id_datatype = 'Q'
file_type_length = 4
