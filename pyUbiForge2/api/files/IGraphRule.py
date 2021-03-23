from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class IGraphRule(SubclassBaseFile):
    ResourceType = 0x9DAC16CD
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

