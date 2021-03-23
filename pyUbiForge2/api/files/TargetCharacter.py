from pyUbiForge2.api.game import SubclassBaseFile
from .Target import Target as _Target


class TargetCharacter(SubclassBaseFile):
    ResourceType = 0x6D259900
    ParentResourceType = _Target.ResourceType
    parent: _Target
