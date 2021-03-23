from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class CameraSettings(SubclassBaseFile):
    ResourceType = 0x68CD2212
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
