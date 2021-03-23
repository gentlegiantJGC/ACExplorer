from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class TextureBase(SubclassBaseFile):
    ResourceType = 0x1FE50BE1
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
