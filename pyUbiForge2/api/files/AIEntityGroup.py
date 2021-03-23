from pyUbiForge2.api.game import SubclassBaseFile
from .AbstractAIEntityGroup import AbstractAIEntityGroup as _AbstractAIEntityGroup


class AIEntityGroup(SubclassBaseFile):
    ResourceType = 0x96561F07
    ParentResourceType = _AbstractAIEntityGroup.ResourceType
    parent: _AbstractAIEntityGroup

