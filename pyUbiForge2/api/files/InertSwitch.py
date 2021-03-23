from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class InertSwitch(SubclassBaseFile):
    ResourceType = 0x308DEBF6
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

