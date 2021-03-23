from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class SoundSet(SubclassBaseFile):
    ResourceType = 0x2BC49864
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
