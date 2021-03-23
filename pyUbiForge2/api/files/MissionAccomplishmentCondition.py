from pyUbiForge2.api.game import SubclassBaseFile
from .MissionCondition import MissionCondition as _MissionCondition


class MissionAccomplishmentCondition(SubclassBaseFile):
    ResourceType = 0xD779E328
    ParentResourceType = _MissionCondition.ResourceType
    parent: _MissionCondition
