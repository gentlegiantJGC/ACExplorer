from pyUbiForge2.api.game import SubclassBaseFile
from .BaseFractionalBrownianMotion import BaseFractionalBrownianMotion as _BaseFractionalBrownianMotion


class FractionalBrownianMotion1D(SubclassBaseFile):
    ResourceType = 0x9454B3DC
    ParentResourceType = _BaseFractionalBrownianMotion.ResourceType
    parent: _BaseFractionalBrownianMotion

