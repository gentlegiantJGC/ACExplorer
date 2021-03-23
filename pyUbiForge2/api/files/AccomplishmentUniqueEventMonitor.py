from pyUbiForge2.api.game import SubclassBaseFile
from .AccomplishmentEventMonitor import (
    AccomplishmentEventMonitor as _AccomplishmentEventMonitor,
)


class AccomplishmentUniqueEventMonitor(SubclassBaseFile):
    ResourceType = 0x8384BF50
    ParentResourceType = _AccomplishmentEventMonitor.ResourceType
    parent: _AccomplishmentEventMonitor
