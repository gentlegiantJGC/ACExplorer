from pyUbiForge2.api.game import SubclassBaseFile
from .SpringDampingMethod import SpringDampingMethod as _SpringDampingMethod


class DistanceSpringDampingMethod(SubclassBaseFile):
    ResourceType = 0x976D1B9B
    ParentResourceType = _SpringDampingMethod.ResourceType
    parent: _SpringDampingMethod
