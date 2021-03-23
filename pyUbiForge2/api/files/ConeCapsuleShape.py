from pyUbiForge2.api.game import SubclassBaseFile
from .ObjectShape import ObjectShape as _ObjectShape


class ConeCapsuleShape(SubclassBaseFile):
    ResourceType = 0x6AAD6AFA
    ParentResourceType = _ObjectShape.ResourceType
    parent: _ObjectShape
