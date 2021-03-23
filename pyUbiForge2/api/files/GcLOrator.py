from pyUbiForge2.api.game import SubclassBaseFile
from .GcLTalkToActivateAbstract import GcLTalkToActivateAbstract as _GcLTalkToActivateAbstract


class GcLOrator(SubclassBaseFile):
    ResourceType = 0x7025FEB1
    ParentResourceType = _GcLTalkToActivateAbstract.ResourceType
    parent: _GcLTalkToActivateAbstract

