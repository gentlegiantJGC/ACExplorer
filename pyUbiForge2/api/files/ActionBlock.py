from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class ActionBlock(SubclassBaseFile):
    ResourceType = 0xEF82FCE4
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
