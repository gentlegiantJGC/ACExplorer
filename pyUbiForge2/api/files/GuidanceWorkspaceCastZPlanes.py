from pyUbiForge2.api.game import SubclassBaseFile
from .GuidanceTask import GuidanceTask as _GuidanceTask


class GuidanceWorkspaceCastZPlanes(SubclassBaseFile):
    ResourceType = 0x2AF50E8A
    ParentResourceType = _GuidanceTask.ResourceType
    parent: _GuidanceTask
