from pyUbiForge2.api.game import SubclassBaseFile
from .ValueVelocity import ValueVelocity as _ValueVelocity


class QuaternionVelocity(SubclassBaseFile):
    ResourceType = 0x3999858F
    ParentResourceType = _ValueVelocity.ResourceType
    parent: _ValueVelocity

