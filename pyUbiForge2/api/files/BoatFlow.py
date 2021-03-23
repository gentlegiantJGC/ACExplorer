from pyUbiForge2.api.game import SubclassBaseFile
from .NavFlow import NavFlow as _NavFlow


class BoatFlow(SubclassBaseFile):
    ResourceType = 0x6F281A57
    ParentResourceType = _NavFlow.ResourceType
    parent: _NavFlow
