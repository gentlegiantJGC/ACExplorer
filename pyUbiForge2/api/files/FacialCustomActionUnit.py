from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class FacialCustomActionUnit(SubclassBaseFile):
    ResourceType = 0x8804195C
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

