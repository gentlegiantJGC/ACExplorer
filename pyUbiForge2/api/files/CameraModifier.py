from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class CameraModifier(SubclassBaseFile):
    ResourceType = 0x26375B2A
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

