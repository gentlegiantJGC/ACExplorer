from pyUbiForge2.api.game import SubclassBaseFile
from .AccomplishmentCounterMonitor import (
    AccomplishmentCounterMonitor as _AccomplishmentCounterMonitor,
)


class AccomplishmentLimitedCounterMonitor(SubclassBaseFile):
    ResourceType = 0x85D7C27C
    ParentResourceType = _AccomplishmentCounterMonitor.ResourceType
    parent: _AccomplishmentCounterMonitor
