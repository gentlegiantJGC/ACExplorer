from pyUbiForge2.api.game import SubclassBaseFile
from .QuadrupedTask import QuadrupedTask as _QuadrupedTask


class QuadrupedPadTask(SubclassBaseFile):
    ResourceType = 0xCC16E93A
    ParentResourceType = _QuadrupedTask.ResourceType
    parent: _QuadrupedTask

