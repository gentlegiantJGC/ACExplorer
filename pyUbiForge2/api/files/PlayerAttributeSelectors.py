from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class PlayerAttributeSelectors(SubclassBaseFile):
    ResourceType = 0x36F84077
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
