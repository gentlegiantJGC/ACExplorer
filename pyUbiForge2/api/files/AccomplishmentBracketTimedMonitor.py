from pyUbiForge2.api.game import SubclassBaseFile
from .AccomplishmentBracketMonitor import (
    AccomplishmentBracketMonitor as _AccomplishmentBracketMonitor,
)


class AccomplishmentBracketTimedMonitor(SubclassBaseFile):
    ResourceType = 0xBC399355
    ParentResourceType = _AccomplishmentBracketMonitor.ResourceType
    parent: _AccomplishmentBracketMonitor
