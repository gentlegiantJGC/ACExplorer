from pyUbiForge2.api.game import SubclassBaseFile
from .GcLAbstract import GcLAbstract as _GcLAbstract


class GcLTalkToActivateAbstract(SubclassBaseFile):
    ResourceType = 0x3E20B7AC
    ParentResourceType = _GcLAbstract.ResourceType
    parent: _GcLAbstract
