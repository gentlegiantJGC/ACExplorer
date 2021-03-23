from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class CreditsData(SubclassBaseFile):
    ResourceType = 0x88AEAEB2
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
