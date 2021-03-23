from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class AnimSetLayer(SubclassBaseFile):
    ResourceType = 0x23C3E834
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
