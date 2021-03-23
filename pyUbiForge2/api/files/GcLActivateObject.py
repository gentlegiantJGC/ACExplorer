from pyUbiForge2.api.game import SubclassBaseFile
from .GcLTalkToActivateAbstract import (
    GcLTalkToActivateAbstract as _GcLTalkToActivateAbstract,
)


class GcLActivateObject(SubclassBaseFile):
    ResourceType = 0x17FE22A6
    ParentResourceType = _GcLTalkToActivateAbstract.ResourceType
    parent: _GcLTalkToActivateAbstract
