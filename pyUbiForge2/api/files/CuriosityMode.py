from pyUbiForge2.api.game import SubclassBaseFile
from .ReactionMode import ReactionMode as _ReactionMode


class CuriosityMode(SubclassBaseFile):
    ResourceType = 0xF580A25B
    ParentResourceType = _ReactionMode.ResourceType
    parent: _ReactionMode

