from plugins import BasePlugin
from typing import Union, List
import pyUbiForge
import logging
from pyUbiForge.misc import mesh
import json
import os


class Plugin(BasePlugin):
    plugin_name = "Mesh Heirarchy"
    plugin_level = 2
    dev = True

    def run(
        self,
        file_id: Union[str, int],
        forge_file_name: str,
        datafile_id: int,
        options: Union[List[dict], None] = None,
    ):
        save_folder = pyUbiForge.CONFIG.get("dumpFolder", "output")
        if os.path.isfile(os.path.join(save_folder, "bone_hierarchy.json")):
            with open(os.path.join(save_folder, "bone_hierarchy.json")) as f:
                bone_hierarchy = json.load(f)
        else:
            bone_hierarchy = {}
        count = 0
        count_max = len(pyUbiForge.forge_files[forge_file_name].datafiles)
        for datafile_id, datafile in pyUbiForge.forge_files[
            forge_file_name
        ].datafiles.items():
            if datafile.file_type == "415D9568":
                data = pyUbiForge.temp_files(datafile_id, forge_file_name, datafile_id)
                if data is None:
                    logging.warning(f"Failed to find file {file_id:016X}")
                    continue
                model: mesh.BaseModel = pyUbiForge.read_file(data.file)
                if model is None:
                    continue

                bone_ids = {bone.bone_id for bone in model.bones}

                for bone_id in bone_ids:
                    if bone_id in bone_hierarchy:
                        bone_hierarchy[bone_id] = [
                            v for v in bone_hierarchy[bone_id] if v in bone_ids
                        ]
                    else:
                        bone_hierarchy[bone_id] = list(bone_ids)
            count += 1
            if count % 99 == 0:
                print(f"{count}/{count_max}")

        with open(os.path.join(save_folder, "bone_hierarchy.json"), "w") as f:
            json.dump(bone_hierarchy, f)
