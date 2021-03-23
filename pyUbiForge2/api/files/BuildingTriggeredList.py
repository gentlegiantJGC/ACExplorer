from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class BuildingTriggeredList(SubclassBaseFile):
    ResourceType = 0x6A358EAA
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

