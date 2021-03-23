from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class PlayerAttributeRowSelection(SubclassBaseFile):
    ResourceType = 0xEA74F02D
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

