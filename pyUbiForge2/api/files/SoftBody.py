from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class SoftBody(SubclassBaseFile):
    ResourceType = 0x4B54C698
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
