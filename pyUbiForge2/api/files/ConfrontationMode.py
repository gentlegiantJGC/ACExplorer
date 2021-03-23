from pyUbiForge2.api.game import SubclassBaseFile
from .ReactionMode import ReactionMode as _ReactionMode


class ConfrontationMode(SubclassBaseFile):
    ResourceType = 0x62945E82
    ParentResourceType = _ReactionMode.ResourceType
    parent: _ReactionMode

