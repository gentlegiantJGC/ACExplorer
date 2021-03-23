from pyUbiForge2.api.game import SubclassBaseFile
from .WorldComponent import WorldComponent as _WorldComponent


class RedBallManager(SubclassBaseFile):
    ResourceType = 0x0AB183B2
    ParentResourceType = _WorldComponent.ResourceType
    parent: _WorldComponent

