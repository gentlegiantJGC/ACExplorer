from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class PersistableDisplayOptions(SubclassBaseFile):
    ResourceType = 0xA6A25173
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
