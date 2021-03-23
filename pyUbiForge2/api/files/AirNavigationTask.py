from pyUbiForge2.api.game import SubclassBaseFile
from .GlobalNavigationTask import GlobalNavigationTask as _GlobalNavigationTask


class AirNavigationTask(SubclassBaseFile):
    ResourceType = 0xA2F9597B
    ParentResourceType = _GlobalNavigationTask.ResourceType
    parent: _GlobalNavigationTask

