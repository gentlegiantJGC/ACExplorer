from pyUbiForge2.api.game import SubclassBaseFile
from .EntitySpecification import EntitySpecification as _EntitySpecification


class SpawningSpecification(SubclassBaseFile):
    ResourceType = 0xFC668456
    ParentResourceType = _EntitySpecification.ResourceType
    parent: _EntitySpecification
