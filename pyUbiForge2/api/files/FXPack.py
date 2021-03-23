from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class FXPack(SubclassBaseFile):
    ResourceType = 0x7608E2D9
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

