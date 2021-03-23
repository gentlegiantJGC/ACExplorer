from pyUbiForge2.api.game import SubclassBaseFile
from .AbstractDeathHandler import AbstractDeathHandler as _AbstractDeathHandler


class DeathHandler(SubclassBaseFile):
    ResourceType = 0x3811C52C
    ParentResourceType = _AbstractDeathHandler.ResourceType
    parent: _AbstractDeathHandler
