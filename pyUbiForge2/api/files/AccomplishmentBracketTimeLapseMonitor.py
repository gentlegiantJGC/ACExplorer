from pyUbiForge2.api.game import SubclassBaseFile
from .AccomplishmentBracketTimedMonitor import AccomplishmentBracketTimedMonitor as _AccomplishmentBracketTimedMonitor


class AccomplishmentBracketTimeLapseMonitor(SubclassBaseFile):
    ResourceType = 0x71FC0B5D
    ParentResourceType = _AccomplishmentBracketTimedMonitor.ResourceType
    parent: _AccomplishmentBracketTimedMonitor

