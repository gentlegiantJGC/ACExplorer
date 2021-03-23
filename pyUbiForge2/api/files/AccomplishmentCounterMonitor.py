from pyUbiForge2.api.game import SubclassBaseFile
from .AccomplishmentMonitor import AccomplishmentMonitor as _AccomplishmentMonitor


class AccomplishmentCounterMonitor(SubclassBaseFile):
    ResourceType = 0x91565C39
    ParentResourceType = _AccomplishmentMonitor.ResourceType
    parent: _AccomplishmentMonitor
