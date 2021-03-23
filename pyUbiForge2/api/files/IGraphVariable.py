from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class IGraphVariable(SubclassBaseFile):
    ResourceType = 0xE66A2C80
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
