from pyUbiForge2.api.game import SubclassBaseFile
from .MandatoryWorldComponent import MandatoryWorldComponent as _MandatoryWorldComponent


class GameplayCoordinatorWorldComponent(SubclassBaseFile):
    ResourceType = 0xEC7E0424
    ParentResourceType = _MandatoryWorldComponent.ResourceType
    parent: _MandatoryWorldComponent

