from pyUbiForge2.api.game import SubclassBaseFile
from .Light import Light as _Light


class DirectionalLight(SubclassBaseFile):
    ResourceType = 0x7E15FD50
    ParentResourceType = _Light.ResourceType
    parent: _Light
