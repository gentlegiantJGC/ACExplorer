from pyUbiForge2.api.game import SubclassBaseFile
from .GraphicObjectInstanceData import GraphicObjectInstanceData as _GraphicObjectInstanceData


class LightInstance(SubclassBaseFile):
    ResourceType = 0x554C614C
    ParentResourceType = _GraphicObjectInstanceData.ResourceType
    parent: _GraphicObjectInstanceData

