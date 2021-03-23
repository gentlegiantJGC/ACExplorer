from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class SoundBao(SubclassBaseFile):
    ResourceType = 0xD8295DCB
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
