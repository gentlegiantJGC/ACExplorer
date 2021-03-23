from pyUbiForge2.api.game import SubclassBaseFile
from .ValueVelocity import ValueVelocity as _ValueVelocity


class FloatVelocity(SubclassBaseFile):
    ResourceType = 0x4D8EDD82
    ParentResourceType = _ValueVelocity.ResourceType
    parent: _ValueVelocity
