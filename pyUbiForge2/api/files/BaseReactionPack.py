from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class BaseReactionPack(SubclassBaseFile):
    ResourceType = 0x6E46192C
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

