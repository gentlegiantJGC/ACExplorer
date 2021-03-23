from pyUbiForge2.api.game import SubclassBaseFile
from .ReactionMode import ReactionMode as _ReactionMode


class SelfPreservationMode(SubclassBaseFile):
    ResourceType = 0x3FBC8C9D
    ParentResourceType = _ReactionMode.ResourceType
    parent: _ReactionMode

