from pyUbiForge2.api.game import SubclassBaseFile
from .AccomplishmentOutput import AccomplishmentOutput as _AccomplishmentOutput


class UplayAccomplishmentOutput(SubclassBaseFile):
    ResourceType = 0x26DA75EF
    ParentResourceType = _AccomplishmentOutput.ResourceType
    parent: _AccomplishmentOutput

