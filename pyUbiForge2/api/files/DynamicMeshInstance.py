from pyUbiForge2.api.game import SubclassBaseFile
from .GraphicObjectInstanceData import GraphicObjectInstanceData as _GraphicObjectInstanceData


class DynamicMeshInstance(SubclassBaseFile):
    ResourceType = 0x6E877B3A
    ParentResourceType = _GraphicObjectInstanceData.ResourceType
    parent: _GraphicObjectInstanceData

