from pyUbiForge2.api.game import SubclassBaseFile
from .AccomplishmentEventMonitor import AccomplishmentEventMonitor as _AccomplishmentEventMonitor


class AccomplishmentAdditionalDataCounterMonitor(SubclassBaseFile):
    ResourceType = 0x1DF2724B
    ParentResourceType = _AccomplishmentEventMonitor.ResourceType
    parent: _AccomplishmentEventMonitor

