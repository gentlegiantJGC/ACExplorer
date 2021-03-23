from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class BodyPartTemplate(SubclassBaseFile):
    ResourceType = 0x02251ED8
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

