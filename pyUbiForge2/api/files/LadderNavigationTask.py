from pyUbiForge2.api.game import SubclassBaseFile
from .GlobalNavigationTask import GlobalNavigationTask as _GlobalNavigationTask


class LadderNavigationTask(SubclassBaseFile):
    ResourceType = 0xAF2FA63A
    ParentResourceType = _GlobalNavigationTask.ResourceType
    parent: _GlobalNavigationTask
