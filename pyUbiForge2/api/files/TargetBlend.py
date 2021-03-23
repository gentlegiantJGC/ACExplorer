from pyUbiForge2.api.game import SubclassBaseFile
from .Target import Target as _Target


class TargetBlend(SubclassBaseFile):
    ResourceType = 0x7CFDB751
    ParentResourceType = _Target.ResourceType
    parent: _Target
