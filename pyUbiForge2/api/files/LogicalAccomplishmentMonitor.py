from pyUbiForge2.api.game import SubclassBaseFile
from .AccomplishmentMonitor import AccomplishmentMonitor as _AccomplishmentMonitor


class LogicalAccomplishmentMonitor(SubclassBaseFile):
    ResourceType = 0x614A11C3
    ParentResourceType = _AccomplishmentMonitor.ResourceType
    parent: _AccomplishmentMonitor
