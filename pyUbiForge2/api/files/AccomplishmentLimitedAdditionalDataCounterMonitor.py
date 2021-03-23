from pyUbiForge2.api.game import SubclassBaseFile
from .AccomplishmentAdditionalDataCounterMonitor import AccomplishmentAdditionalDataCounterMonitor as _AccomplishmentAdditionalDataCounterMonitor


class AccomplishmentLimitedAdditionalDataCounterMonitor(SubclassBaseFile):
    ResourceType = 0xD32EF06C
    ParentResourceType = _AccomplishmentAdditionalDataCounterMonitor.ResourceType
    parent: _AccomplishmentAdditionalDataCounterMonitor

