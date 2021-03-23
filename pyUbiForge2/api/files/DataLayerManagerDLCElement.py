from pyUbiForge2.api.game import SubclassBaseFile
from .ContentElement import ContentElement as _ContentElement


class DataLayerManagerDLCElement(SubclassBaseFile):
    ResourceType = 0xD88FDCCD
    ParentResourceType = _ContentElement.ResourceType
    parent: _ContentElement
