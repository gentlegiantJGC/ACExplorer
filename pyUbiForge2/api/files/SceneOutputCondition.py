from pyUbiForge2.api.game import SubclassBaseFile
from .AICondition import AICondition as _AICondition


class SceneOutputCondition(SubclassBaseFile):
    ResourceType = 0xC831A06C
    ParentResourceType = _AICondition.ResourceType
    parent: _AICondition
