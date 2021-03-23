from pyUbiForge2.api.game import SubclassBaseFile
from .GcLTalkToActivateAbstract import (
    GcLTalkToActivateAbstract as _GcLTalkToActivateAbstract,
)


class GcLTalkTo(SubclassBaseFile):
    ResourceType = 0x84D05ECA
    ParentResourceType = _GcLTalkToActivateAbstract.ResourceType
    parent: _GcLTalkToActivateAbstract
