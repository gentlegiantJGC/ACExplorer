from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class PlayerAttributesBuilder(SubclassBaseFile):
    ResourceType = 0x588F7145
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

