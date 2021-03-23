from pyUbiForge2.api.game import SubclassBaseFile
from .ExtensionContextData import ExtensionContextData as _ExtensionContextData


class HeadOrientationData(SubclassBaseFile):
    ResourceType = 0x88E66A2B
    ParentResourceType = _ExtensionContextData.ResourceType
    parent: _ExtensionContextData
