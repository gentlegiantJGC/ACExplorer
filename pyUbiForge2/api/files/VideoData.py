from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class VideoData(SubclassBaseFile):
    ResourceType = 0x38C20200
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

