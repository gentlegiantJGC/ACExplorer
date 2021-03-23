from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class FXMaterialOverlayPropertyMapping(SubclassBaseFile):
    ResourceType = 0x71704EA6
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
