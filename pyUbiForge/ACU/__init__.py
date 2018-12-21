import json
import os
from .getMaterialIDs_ import get_material_ids
from . import forge

game_identifier = 'ACU'
file_types = json.load(open(f"{os.path.dirname(__file__)}/fileFormats.json"))
file_id_datatype = 'Q'
file_type_length = 4
