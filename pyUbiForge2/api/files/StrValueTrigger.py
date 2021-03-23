from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class StrValueTrigger(SubclassBaseFile):
    ResourceType = 0x821EEB2D
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

