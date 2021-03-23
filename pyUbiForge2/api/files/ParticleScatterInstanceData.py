from pyUbiForge2.api.game import SubclassBaseFile
from .MaterialAddonInstanceData import (
    MaterialAddonInstanceData as _MaterialAddonInstanceData,
)


class ParticleScatterInstanceData(SubclassBaseFile):
    ResourceType = 0x8A5F4A93
    ParentResourceType = _MaterialAddonInstanceData.ResourceType
    parent: _MaterialAddonInstanceData
