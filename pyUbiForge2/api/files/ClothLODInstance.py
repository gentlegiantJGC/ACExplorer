from pyUbiForge2.api.game import SubclassBaseFile
from .SoftBodyLODInstance import SoftBodyLODInstance as _SoftBodyLODInstance


class ClothLODInstance(SubclassBaseFile):
    ResourceType = 0x8C655B8E
    ParentResourceType = _SoftBodyLODInstance.ResourceType
    parent: _SoftBodyLODInstance

