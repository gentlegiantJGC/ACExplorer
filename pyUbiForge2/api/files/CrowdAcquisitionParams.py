from pyUbiForge2.api.game import SubclassBaseFile
from .SpawnAbstractAcquisitionParams import (
    SpawnAbstractAcquisitionParams as _SpawnAbstractAcquisitionParams,
)


class CrowdAcquisitionParams(SubclassBaseFile):
    ResourceType = 0x14B7ACBD
    ParentResourceType = _SpawnAbstractAcquisitionParams.ResourceType
    parent: _SpawnAbstractAcquisitionParams
