from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class TextureSet(SubclassBaseFile):
    ResourceType = 0xD70E6670
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
