from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class FireItem(SubclassBaseFile):
    ResourceType = 0x1DAB1CFE
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

