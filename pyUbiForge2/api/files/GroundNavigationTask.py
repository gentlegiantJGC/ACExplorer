from pyUbiForge2.api.game import SubclassBaseFile
from .GlobalNavigationTask import GlobalNavigationTask as _GlobalNavigationTask


class GroundNavigationTask(SubclassBaseFile):
    ResourceType = 0x7C2AC1B1
    ParentResourceType = _GlobalNavigationTask.ResourceType
    parent: _GlobalNavigationTask

