from pyUbiForge2.api.game import SubclassBaseFile
from .GraphicObject import GraphicObject as _GraphicObject


class Mesh(SubclassBaseFile):
    ResourceType = 0x415D9568
    ParentResourceType = _GraphicObject.ResourceType
    parent: _GraphicObject
