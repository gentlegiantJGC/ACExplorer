from pyUbiForge2.api.game import SubclassBaseFile
from .Node import Node as _Node


class BitWiseAnd(SubclassBaseFile):
    ResourceType = 0x6F9EBCEA
    ParentResourceType = _Node.ResourceType
    parent: _Node

