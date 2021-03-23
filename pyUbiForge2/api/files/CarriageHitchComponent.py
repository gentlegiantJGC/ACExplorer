from pyUbiForge2.api.game import SubclassBaseFile
from .Component import Component as _Component


class CarriageHitchComponent(SubclassBaseFile):
    ResourceType = 0x0ADA9CD4
    ParentResourceType = _Component.ResourceType
    parent: _Component

