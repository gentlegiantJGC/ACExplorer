from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class FX(SubclassBaseFile):
    ResourceType = 0x824A23BA
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

