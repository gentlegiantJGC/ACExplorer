from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class PropertySheet(SubclassBaseFile):
    ResourceType = 0xB7BE3A32
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

