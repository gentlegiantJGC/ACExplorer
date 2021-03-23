from pyUbiForge2.api.game import SubclassBaseFile
from .Component import Component as _Component


class LargeMeshChunkComponent(SubclassBaseFile):
    ResourceType = 0x132FE22D
    ParentResourceType = _Component.ResourceType
    parent: _Component
