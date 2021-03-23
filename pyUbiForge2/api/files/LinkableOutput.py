from pyUbiForge2.api.game import SubclassBaseFile
from .Linkable import Linkable as _Linkable


class LinkableOutput(SubclassBaseFile):
    ResourceType = 0xE9CDC116
    ParentResourceType = _Linkable.ResourceType
    parent: _Linkable
