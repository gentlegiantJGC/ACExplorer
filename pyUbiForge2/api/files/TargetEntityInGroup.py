from pyUbiForge2.api.game import SubclassBaseFile
from .Target import Target as _Target


class TargetEntityInGroup(SubclassBaseFile):
    ResourceType = 0x062FC835
    ParentResourceType = _Target.ResourceType
    parent: _Target
