from pyUbiForge2.api.game import SubclassBaseFile
from .GcLAbstract import GcLAbstract as _GcLAbstract


class GcLRace(SubclassBaseFile):
    ResourceType = 0x54BA97B8
    ParentResourceType = _GcLAbstract.ResourceType
    parent: _GcLAbstract

