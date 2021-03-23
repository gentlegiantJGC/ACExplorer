from pyUbiForge2.api.game import SubclassBaseFile
from .SpawnAbstractAcquisitionParams import SpawnAbstractAcquisitionParams as _SpawnAbstractAcquisitionParams


class SpawnAcquisitionParams(SubclassBaseFile):
    ResourceType = 0x52F96969
    ParentResourceType = _SpawnAbstractAcquisitionParams.ResourceType
    parent: _SpawnAbstractAcquisitionParams

