from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class CameraFX(SubclassBaseFile):
    ResourceType = 0x41F941CA
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

