from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class CameraTransformableSubObject(SubclassBaseFile):
    ResourceType = 0xBFE8C722
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

