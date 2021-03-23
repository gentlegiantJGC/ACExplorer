from pyUbiForge2.api.game import SubclassBaseFile
from .AccomplishmentOutput import AccomplishmentOutput as _AccomplishmentOutput


class DebugAccomplishmentOutput(SubclassBaseFile):
    ResourceType = 0xCC00B08B
    ParentResourceType = _AccomplishmentOutput.ResourceType
    parent: _AccomplishmentOutput
