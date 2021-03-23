from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class FXMaterialOverlayContainer(SubclassBaseFile):
    ResourceType = 0x5FBD0E5D
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
