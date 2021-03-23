from pyUbiForge2.api.game import SubclassBaseFile
from .Target import Target as _Target


class TargetObject(SubclassBaseFile):
    ResourceType = 0x81A302B2
    ParentResourceType = _Target.ResourceType
    parent: _Target
