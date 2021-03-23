from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class AnimusDatabaseLetter(SubclassBaseFile):
    ResourceType = 0x0C67004A
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

