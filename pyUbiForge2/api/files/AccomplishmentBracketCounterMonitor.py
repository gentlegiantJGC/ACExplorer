from pyUbiForge2.api.game import SubclassBaseFile
from .AccomplishmentBracketMonitor import (
    AccomplishmentBracketMonitor as _AccomplishmentBracketMonitor,
)


class AccomplishmentBracketCounterMonitor(SubclassBaseFile):
    ResourceType = 0xE3511E9E
    ParentResourceType = _AccomplishmentBracketMonitor.ResourceType
    parent: _AccomplishmentBracketMonitor
