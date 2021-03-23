from pyUbiForge2.api.game import SubclassBaseFile
from .GlobalNavigationTask import GlobalNavigationTask as _GlobalNavigationTask


class QuadrupedTask(SubclassBaseFile):
    ResourceType = 0x1FD9F38F
    ParentResourceType = _GlobalNavigationTask.ResourceType
    parent: _GlobalNavigationTask
