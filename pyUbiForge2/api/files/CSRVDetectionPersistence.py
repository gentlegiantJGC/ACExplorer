from pyUbiForge2.api.game import SubclassBaseFile
from .CSrvAbstract import CSrvAbstract as _CSrvAbstract


class CSRVDetectionPersistence(SubclassBaseFile):
    ResourceType = 0x875C3444
    ParentResourceType = _CSrvAbstract.ResourceType
    parent: _CSrvAbstract

