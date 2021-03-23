from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class TriggerEnterEvent(SubclassBaseFile):
    ResourceType = 0x7754F346
    ParentResourceType = _Event.ResourceType
    parent: _Event

