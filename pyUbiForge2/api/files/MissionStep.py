from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class MissionStep(SubclassBaseFile):
    ResourceType = 0xB3195056
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
