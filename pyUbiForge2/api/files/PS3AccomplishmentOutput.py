from pyUbiForge2.api.game import SubclassBaseFile
from .AccomplishmentOutput import AccomplishmentOutput as _AccomplishmentOutput


class PS3AccomplishmentOutput(SubclassBaseFile):
    ResourceType = 0x9E457E2D
    ParentResourceType = _AccomplishmentOutput.ResourceType
    parent: _AccomplishmentOutput
