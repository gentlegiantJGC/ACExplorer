from pyUbiForge2.api.game import SubclassBaseFile
from .DampingMethod import DampingMethod as _DampingMethod


class SpringDampingMethod(SubclassBaseFile):
    ResourceType = 0xCCDE452B
    ParentResourceType = _DampingMethod.ResourceType
    parent: _DampingMethod

