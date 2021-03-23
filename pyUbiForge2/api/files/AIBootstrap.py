from pyUbiForge2.api.game import SubclassBaseFile
from .Bootstrap import Bootstrap as _Bootstrap


class AIBootstrap(SubclassBaseFile):
    ResourceType = 0x6F55EC09
    ParentResourceType = _Bootstrap.ResourceType
    parent: _Bootstrap

