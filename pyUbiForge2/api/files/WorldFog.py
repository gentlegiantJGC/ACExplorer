from pyUbiForge2.api.game import SubclassBaseFile
from .GraphicObject import GraphicObject as _GraphicObject


class WorldFog(SubclassBaseFile):
    ResourceType = 0xACF73D89
    ParentResourceType = _GraphicObject.ResourceType
    parent: _GraphicObject

