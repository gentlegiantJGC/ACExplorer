from pyUbiForge2.api.game import SubclassBaseFile
from .Target import Target as _Target


class TargetEntityOffset(SubclassBaseFile):
    ResourceType = 0x7055C0F0
    ParentResourceType = _Target.ResourceType
    parent: _Target
