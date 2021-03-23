from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class Checkpoint(SubclassBaseFile):
    ResourceType = 0x405DF46E
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

