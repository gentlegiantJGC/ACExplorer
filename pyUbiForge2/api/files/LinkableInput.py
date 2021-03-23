from pyUbiForge2.api.game import SubclassBaseFile
from .Linkable import Linkable as _Linkable


class LinkableInput(SubclassBaseFile):
    ResourceType = 0xA42F1A65
    ParentResourceType = _Linkable.ResourceType
    parent: _Linkable

