from pyUbiForge2.api.game import SubclassBaseFile
from .OLAbstract import OLAbstract as _OLAbstract


class OLGlider(SubclassBaseFile):
    ResourceType = 0xF7DAE43A
    ParentResourceType = _OLAbstract.ResourceType
    parent: _OLAbstract

