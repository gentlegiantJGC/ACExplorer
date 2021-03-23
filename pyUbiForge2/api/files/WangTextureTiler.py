from pyUbiForge2.api.game import SubclassBaseFile
from .WangTiler import WangTiler as _WangTiler


class WangTextureTiler(SubclassBaseFile):
    ResourceType = 0xEBB84377
    ParentResourceType = _WangTiler.ResourceType
    parent: _WangTiler
