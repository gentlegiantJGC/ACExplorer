from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class LineIdToSoundLengthPackage(SubclassBaseFile):
    ResourceType = 0xC66CFE99
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

