from pyUbiForge2.api.game import SubclassBaseFile
from .AccomplishmentManagerData import AccomplishmentManagerData as _AccomplishmentManagerData


class AccomplishmentManagerAssassinData(SubclassBaseFile):
    ResourceType = 0x1E9E9B86
    ParentResourceType = _AccomplishmentManagerData.ResourceType
    parent: _AccomplishmentManagerData

