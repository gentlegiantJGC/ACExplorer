from pyUbiForge2.api.game import SubclassBaseFile
from .NodeInterface import NodeInterface as _NodeInterface


class Node(SubclassBaseFile):
    ResourceType = 0xD418CC4C
    ParentResourceType = _NodeInterface.ResourceType
    parent: _NodeInterface
