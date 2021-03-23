from pyUbiForge2.api.game import SubclassBaseFile
from .GcLAbstract import GcLAbstract as _GcLAbstract


class GcLNpcBoatDriver(SubclassBaseFile):
    ResourceType = 0x17DFF5F3
    ParentResourceType = _GcLAbstract.ResourceType
    parent: _GcLAbstract
