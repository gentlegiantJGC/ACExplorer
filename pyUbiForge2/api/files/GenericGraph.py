from pyUbiForge2.api.game import SubclassBaseFile
from .Graph import Graph as _Graph


class GenericGraph(SubclassBaseFile):
    ResourceType = 0xB7EA6DA8
    ParentResourceType = _Graph.ResourceType
    parent: _Graph
