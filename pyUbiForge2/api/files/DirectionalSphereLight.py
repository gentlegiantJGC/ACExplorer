from pyUbiForge2.api.game import SubclassBaseFile
from .Light import Light as _Light


class DirectionalSphereLight(SubclassBaseFile):
    ResourceType = 0xC159B05D
    ParentResourceType = _Light.ResourceType
    parent: _Light
