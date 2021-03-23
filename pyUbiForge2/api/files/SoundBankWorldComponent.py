from pyUbiForge2.api.game import SubclassBaseFile
from .MandatoryWorldComponent import MandatoryWorldComponent as _MandatoryWorldComponent


class SoundBankWorldComponent(SubclassBaseFile):
    ResourceType = 0x4DA30368
    ParentResourceType = _MandatoryWorldComponent.ResourceType
    parent: _MandatoryWorldComponent

