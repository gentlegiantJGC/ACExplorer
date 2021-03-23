from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLInterceptEntity(SubclassBaseFile):
    ResourceType = 0xF94744B1
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract
