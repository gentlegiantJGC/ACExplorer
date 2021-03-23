from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class CrowdFractionMembers(SubclassBaseFile):
    ResourceType = 0x7C766DF8
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
