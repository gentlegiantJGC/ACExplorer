from pyUbiForge2.api.game import SubclassBaseFile
from .ReactionMode import ReactionMode as _ReactionMode


class ObservationMode(SubclassBaseFile):
    ResourceType = 0x7AF5A5AD
    ParentResourceType = _ReactionMode.ResourceType
    parent: _ReactionMode
