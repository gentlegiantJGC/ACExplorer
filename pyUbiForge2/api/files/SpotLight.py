from pyUbiForge2.api.game import SubclassBaseFile
from .Light import Light as _Light


class SpotLight(SubclassBaseFile):
    ResourceType = 0x80320FB8
    ParentResourceType = _Light.ResourceType
    parent: _Light

