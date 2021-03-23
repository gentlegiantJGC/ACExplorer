from pyUbiForge2.api.game import SubclassBaseFile
from .ITargetPrecision import ITargetPrecision as _ITargetPrecision


class BoneTargetPrecision(SubclassBaseFile):
    ResourceType = 0xE7A514A2
    ParentResourceType = _ITargetPrecision.ResourceType
    parent: _ITargetPrecision
