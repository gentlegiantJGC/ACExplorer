from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class MetricsQuery(SubclassBaseFile):
    ResourceType = 0x0E7F7BCF
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
