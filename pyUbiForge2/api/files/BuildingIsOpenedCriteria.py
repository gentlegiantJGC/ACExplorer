from pyUbiForge2.api.game import SubclassBaseFile
from .BuildingCriteria import BuildingCriteria as _BuildingCriteria


class BuildingIsOpenedCriteria(SubclassBaseFile):
    ResourceType = 0xE7DFB756
    ParentResourceType = _BuildingCriteria.ResourceType
    parent: _BuildingCriteria
