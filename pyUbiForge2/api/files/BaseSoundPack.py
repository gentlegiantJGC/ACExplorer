from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class BaseSoundPack(SubclassBaseFile):
    ResourceType = 0x85FC184D
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

