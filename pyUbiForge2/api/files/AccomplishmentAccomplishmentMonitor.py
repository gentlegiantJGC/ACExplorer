from pyUbiForge2.api.game import SubclassBaseFile
from .AccomplishmentMonitor import AccomplishmentMonitor as _AccomplishmentMonitor


class AccomplishmentAccomplishmentMonitor(SubclassBaseFile):
    ResourceType = 0x73EF3E50
    ParentResourceType = _AccomplishmentMonitor.ResourceType
    parent: _AccomplishmentMonitor
