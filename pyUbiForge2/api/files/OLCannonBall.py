from pyUbiForge2.api.game import SubclassBaseFile
from .OLAbstract import OLAbstract as _OLAbstract


class OLCannonBall(SubclassBaseFile):
    ResourceType = 0xEFE98569
    ParentResourceType = _OLAbstract.ResourceType
    parent: _OLAbstract
