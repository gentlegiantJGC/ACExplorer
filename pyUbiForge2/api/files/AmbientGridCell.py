from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class AmbientGridCell(SubclassBaseFile):
    ResourceType = 0x56558BC5
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
