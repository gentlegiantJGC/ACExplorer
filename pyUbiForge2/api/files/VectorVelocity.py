from pyUbiForge2.api.game import SubclassBaseFile
from .ValueVelocity import ValueVelocity as _ValueVelocity


class VectorVelocity(SubclassBaseFile):
    ResourceType = 0xD0ACD010
    ParentResourceType = _ValueVelocity.ResourceType
    parent: _ValueVelocity
