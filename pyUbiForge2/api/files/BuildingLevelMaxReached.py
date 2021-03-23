from pyUbiForge2.api.game import SubclassBaseFile
from .BuildingCriteria import BuildingCriteria as _BuildingCriteria


class BuildingLevelMaxReached(SubclassBaseFile):
    ResourceType = 0x29A18CCB
    ParentResourceType = _BuildingCriteria.ResourceType
    parent: _BuildingCriteria
