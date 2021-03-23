from pyUbiForge2.api.game import SubclassBaseFile
from .MaterialAddon import MaterialAddon as _MaterialAddon


class ParticleScatter(SubclassBaseFile):
    ResourceType = 0xAF4299F9
    ParentResourceType = _MaterialAddon.ResourceType
    parent: _MaterialAddon

