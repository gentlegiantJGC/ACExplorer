from pyUbiForge2.api.game import SubclassBaseFile
from .NodeInterface import NodeInterface as _NodeInterface


class LabelNode(SubclassBaseFile):
    ResourceType = 0x4AA21909
    ParentResourceType = _NodeInterface.ResourceType
    parent: _NodeInterface
