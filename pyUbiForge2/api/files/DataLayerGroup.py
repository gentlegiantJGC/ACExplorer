from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class DataLayerGroup(SubclassBaseFile):
    ResourceType = 0x651B5AA3
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
