from pyUbiForge2.api.game import SubclassBaseFile
from .SoftBodySettings import SoftBodySettings as _SoftBodySettings


class ClothSettings(SubclassBaseFile):
    ResourceType = 0x804FE334
    ParentResourceType = _SoftBodySettings.ResourceType
    parent: _SoftBodySettings
