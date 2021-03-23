from pyUbiForge2.api.game import SubclassBaseFile
from .GraphicObject import GraphicObject as _GraphicObject


class ParticleSystem(SubclassBaseFile):
    ResourceType = 0xCAAA7EE8
    ParentResourceType = _GraphicObject.ResourceType
    parent: _GraphicObject

