from pyUbiForge2.api.game import SubclassBaseFile
from .ITargetPrecision import ITargetPrecision as _ITargetPrecision


class LockedTargetPrecision(SubclassBaseFile):
    ResourceType = 0x0DF47C87
    ParentResourceType = _ITargetPrecision.ResourceType
    parent: _ITargetPrecision

