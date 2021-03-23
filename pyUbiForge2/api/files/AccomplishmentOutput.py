from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class AccomplishmentOutput(SubclassBaseFile):
    ResourceType = 0x1A7B2F89
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
