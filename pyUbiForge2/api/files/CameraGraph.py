from pyUbiForge2.api.game import SubclassBaseFile
from .Graph import Graph as _Graph


class CameraGraph(SubclassBaseFile):
    ResourceType = 0x99D6A958
    ParentResourceType = _Graph.ResourceType
    parent: _Graph
