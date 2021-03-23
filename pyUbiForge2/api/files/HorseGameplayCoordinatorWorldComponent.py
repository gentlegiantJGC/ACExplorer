from pyUbiForge2.api.game import SubclassBaseFile
from .MandatoryWorldComponent import MandatoryWorldComponent as _MandatoryWorldComponent


class HorseGameplayCoordinatorWorldComponent(SubclassBaseFile):
    ResourceType = 0x9311BE24
    ParentResourceType = _MandatoryWorldComponent.ResourceType
    parent: _MandatoryWorldComponent

