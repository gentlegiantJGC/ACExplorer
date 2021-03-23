from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class SoundSettings(SubclassBaseFile):
    ResourceType = 0xD937E964
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
