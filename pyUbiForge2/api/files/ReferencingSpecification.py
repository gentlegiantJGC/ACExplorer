from pyUbiForge2.api.game import SubclassBaseFile
from .EntitySpecification import EntitySpecification as _EntitySpecification


class ReferencingSpecification(SubclassBaseFile):
    ResourceType = 0xFFA6D96A
    ParentResourceType = _EntitySpecification.ResourceType
    parent: _EntitySpecification

