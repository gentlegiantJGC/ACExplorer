from pyUbiForge2.api.game import SubclassBaseFile
from .Target import Target as _Target


class TargetPosition(SubclassBaseFile):
    ResourceType = 0xCD1EA66D
    ParentResourceType = _Target.ResourceType
    parent: _Target
