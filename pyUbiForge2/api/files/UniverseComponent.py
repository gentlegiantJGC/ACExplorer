from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class UniverseComponent(SubclassBaseFile):
    ResourceType = 0xEED18A51
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
