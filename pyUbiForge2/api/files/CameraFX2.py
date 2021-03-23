from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class CameraFX2(SubclassBaseFile):
    ResourceType = 0x61256CE2
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

