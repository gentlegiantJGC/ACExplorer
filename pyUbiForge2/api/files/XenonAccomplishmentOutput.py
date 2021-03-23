from pyUbiForge2.api.game import SubclassBaseFile
from .AccomplishmentOutput import AccomplishmentOutput as _AccomplishmentOutput


class XenonAccomplishmentOutput(SubclassBaseFile):
    ResourceType = 0xC7888335
    ParentResourceType = _AccomplishmentOutput.ResourceType
    parent: _AccomplishmentOutput

