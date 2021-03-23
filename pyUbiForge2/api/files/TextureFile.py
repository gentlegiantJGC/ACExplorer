from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class TextureFile(SubclassBaseFile):
    ResourceType = 0x53CEC390
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
