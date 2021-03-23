from pyUbiForge2.api.game import SubclassBaseFile
from .Light import Light as _Light


class OmniLight(SubclassBaseFile):
    ResourceType = 0x344780D6
    ParentResourceType = _Light.ResourceType
    parent: _Light
