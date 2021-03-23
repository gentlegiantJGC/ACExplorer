from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLHumanOnHorseInterceptEntity(SubclassBaseFile):
    ResourceType = 0x11F262AD
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract
