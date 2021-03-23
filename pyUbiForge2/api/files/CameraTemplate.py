from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class CameraTemplate(SubclassBaseFile):
    ResourceType = 0x1AE89D54
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
