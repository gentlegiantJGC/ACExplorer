from pyUbiForge2.api.game import SubclassBaseFile
from .GuidanceSystemOptimizer import GuidanceSystemOptimizer as _GuidanceSystemOptimizer


class GuidanceSystemOptimizerGroundWall(SubclassBaseFile):
    ResourceType = 0x4EF5DB67
    ParentResourceType = _GuidanceSystemOptimizer.ResourceType
    parent: _GuidanceSystemOptimizer
