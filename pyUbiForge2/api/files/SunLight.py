from pyUbiForge2.api.game import SubclassBaseFile
from .DirectionalLight import DirectionalLight as _DirectionalLight


class SunLight(SubclassBaseFile):
    ResourceType = 0x5EDC3E04
    ParentResourceType = _DirectionalLight.ResourceType
    parent: _DirectionalLight
