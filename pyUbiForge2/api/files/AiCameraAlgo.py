from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class AiCameraAlgo(SubclassBaseFile):
    ResourceType = 0x201314A3
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

