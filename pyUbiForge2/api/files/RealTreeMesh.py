from pyUbiForge2.api.game import SubclassBaseFile
from .GraphicObject import GraphicObject as _GraphicObject


class RealTreeMesh(SubclassBaseFile):
    ResourceType = 0xCD0D35E6
    ParentResourceType = _GraphicObject.ResourceType
    parent: _GraphicObject

