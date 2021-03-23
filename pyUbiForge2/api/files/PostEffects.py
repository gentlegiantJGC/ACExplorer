from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class PostEffects(SubclassBaseFile):
    ResourceType = 0xC83B8907
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
