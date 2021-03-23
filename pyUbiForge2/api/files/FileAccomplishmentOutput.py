from pyUbiForge2.api.game import SubclassBaseFile
from .AccomplishmentOutput import AccomplishmentOutput as _AccomplishmentOutput


class FileAccomplishmentOutput(SubclassBaseFile):
    ResourceType = 0xF5528193
    ParentResourceType = _AccomplishmentOutput.ResourceType
    parent: _AccomplishmentOutput
