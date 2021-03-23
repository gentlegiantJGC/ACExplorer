from pyUbiForge2.api.game import SubclassBaseFile
from .WorldAmbianceManager import WorldAmbianceManager as _WorldAmbianceManager


class TimeOfDayManager(SubclassBaseFile):
    ResourceType = 0xD1510422
    ParentResourceType = _WorldAmbianceManager.ResourceType
    parent: _WorldAmbianceManager

