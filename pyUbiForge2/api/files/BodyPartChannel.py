from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class BodyPartChannel(SubclassBaseFile):
    ResourceType = 0x58B2578F
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
