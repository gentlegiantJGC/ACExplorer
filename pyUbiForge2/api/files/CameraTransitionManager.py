from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class CameraTransitionManager(SubclassBaseFile):
    ResourceType = 0x7D3BB0A2
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
