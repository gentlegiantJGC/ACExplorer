from pyUbiForge2.api.game import SubclassBaseFile
from .SoftBody import SoftBody as _SoftBody


class Cloth(SubclassBaseFile):
    ResourceType = 0xE33044BA
    ParentResourceType = _SoftBody.ResourceType
    parent: _SoftBody
