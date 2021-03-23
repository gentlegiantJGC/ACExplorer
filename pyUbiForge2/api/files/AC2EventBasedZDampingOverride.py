from pyUbiForge2.api.game import SubclassBaseFile
from .ITargetDampingOverride import ITargetDampingOverride as _ITargetDampingOverride


class AC2EventBasedZDampingOverride(SubclassBaseFile):
    ResourceType = 0x52625864
    ParentResourceType = _ITargetDampingOverride.ResourceType
    parent: _ITargetDampingOverride
