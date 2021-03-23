from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class UIFxSet(SubclassBaseFile):
    ResourceType = 0x9CF6DD7E
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
