from pyUbiForge2.api.game import SubclassBaseFile
from .GraphicObjectInstanceData import GraphicObjectInstanceData as _GraphicObjectInstanceData


class ParticleSystemInstanceData(SubclassBaseFile):
    ResourceType = 0x212DD44A
    ParentResourceType = _GraphicObjectInstanceData.ResourceType
    parent: _GraphicObjectInstanceData

