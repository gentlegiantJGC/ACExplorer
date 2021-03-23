from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class GroupManipulationReleaseTargetEvent(SubclassBaseFile):
    ResourceType = 0xF86E79B8
    ParentResourceType = _Event.ResourceType
    parent: _Event

