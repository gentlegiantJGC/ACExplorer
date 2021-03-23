from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class SubRealTreeMesh(SubclassBaseFile):
    ResourceType = 0xFE8CCC18
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
