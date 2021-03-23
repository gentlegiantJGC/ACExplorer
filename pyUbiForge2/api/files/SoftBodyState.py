from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class SoftBodyState(SubclassBaseFile):
    ResourceType = 0xA83A3056
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

