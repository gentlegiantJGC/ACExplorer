from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class FireManager(SubclassBaseFile):
    ResourceType = 0x9623CB2D
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

