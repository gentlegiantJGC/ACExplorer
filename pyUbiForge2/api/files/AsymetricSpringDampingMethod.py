from pyUbiForge2.api.game import SubclassBaseFile
from .DampingMethod import DampingMethod as _DampingMethod


class AsymetricSpringDampingMethod(SubclassBaseFile):
    ResourceType = 0x8963016C
    ParentResourceType = _DampingMethod.ResourceType
    parent: _DampingMethod
