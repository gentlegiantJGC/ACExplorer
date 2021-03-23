from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class SoftBodySettings(SubclassBaseFile):
    ResourceType = 0xF7A7E4DF
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

