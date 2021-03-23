from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class VillaItemList(SubclassBaseFile):
    ResourceType = 0x1B3D0580
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

