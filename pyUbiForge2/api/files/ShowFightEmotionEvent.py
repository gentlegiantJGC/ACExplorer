from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class ShowFightEmotionEvent(SubclassBaseFile):
    ResourceType = 0x37E1DDA6
    ParentResourceType = _Event.ResourceType
    parent: _Event

