from pyUbiForge2.api.game import SubclassBaseFile
from .IGraphRule import IGraphRule as _IGraphRule


class ICameraRule(SubclassBaseFile):
    ResourceType = 0x4F614733
    ParentResourceType = _IGraphRule.ResourceType
    parent: _IGraphRule

