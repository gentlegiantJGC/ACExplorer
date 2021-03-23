from pyUbiForge2.api.game import SubclassBaseFile
from .GcLAbstract import GcLAbstract as _GcLAbstract


class GcLTreasure(SubclassBaseFile):
    ResourceType = 0xCB1325A0
    ParentResourceType = _GcLAbstract.ResourceType
    parent: _GcLAbstract

