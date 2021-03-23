from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class AmbientGrid(SubclassBaseFile):
    ResourceType = 0xAD1D08C3
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

