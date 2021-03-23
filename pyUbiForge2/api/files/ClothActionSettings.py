from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class ClothActionSettings(SubclassBaseFile):
    ResourceType = 0x52E5AA85
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

