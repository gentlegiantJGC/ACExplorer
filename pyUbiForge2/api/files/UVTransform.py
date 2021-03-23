from pyUbiForge2.api.game import SubclassBaseFile
from .ICustomShaderSetup import ICustomShaderSetup as _ICustomShaderSetup


class UVTransform(SubclassBaseFile):
    ResourceType = 0xC52E2125
    ParentResourceType = _ICustomShaderSetup.ResourceType
    parent: _ICustomShaderSetup

