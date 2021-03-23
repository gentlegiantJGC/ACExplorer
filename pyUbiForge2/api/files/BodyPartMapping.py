from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class BodyPartMapping(SubclassBaseFile):
    ResourceType = 0xB3ADF542
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

