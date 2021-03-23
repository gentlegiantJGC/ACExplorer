from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class UIVideoSet(SubclassBaseFile):
    ResourceType = 0xC30B8B5B
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
