from pyUbiForge2.api.game import SubclassBaseFile
from .GraphicObjectInstanceData import GraphicObjectInstanceData as _GraphicObjectInstanceData


class RealTreeMeshInstanceData(SubclassBaseFile):
    ResourceType = 0x1290E59E
    ParentResourceType = _GraphicObjectInstanceData.ResourceType
    parent: _GraphicObjectInstanceData

