from pyUbiForge2.api.game import SubclassBaseFile
from .AsymetricSpringDampingMethod import (
    AsymetricSpringDampingMethod as _AsymetricSpringDampingMethod,
)


class SignedAsymetricSpringDampingMethod(SubclassBaseFile):
    ResourceType = 0x18C84199
    ParentResourceType = _AsymetricSpringDampingMethod.ResourceType
    parent: _AsymetricSpringDampingMethod
