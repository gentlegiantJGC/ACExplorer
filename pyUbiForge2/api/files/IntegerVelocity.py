from pyUbiForge2.api.game import SubclassBaseFile
from .ValueVelocity import ValueVelocity as _ValueVelocity


class IntegerVelocity(SubclassBaseFile):
    ResourceType = 0x5458741C
    ParentResourceType = _ValueVelocity.ResourceType
    parent: _ValueVelocity
