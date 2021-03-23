from pyUbiForge2.api.game import SubclassBaseFile
from .ICustomShaderSetup import ICustomShaderSetup as _ICustomShaderSetup


class TimeOscillatorData(SubclassBaseFile):
    ResourceType = 0xECE5D96C
    ParentResourceType = _ICustomShaderSetup.ResourceType
    parent: _ICustomShaderSetup

