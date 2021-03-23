from pyUbiForge2.api.game import SubclassBaseFile
from .GuidanceTask import GuidanceTask as _GuidanceTask


class GuidanceWorkspaceCastPlanes(SubclassBaseFile):
    ResourceType = 0xBE13EB35
    ParentResourceType = _GuidanceTask.ResourceType
    parent: _GuidanceTask

