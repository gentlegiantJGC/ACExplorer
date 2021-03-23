from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class VillaItemSettings(SubclassBaseFile):
    ResourceType = 0xB2B2D090
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
