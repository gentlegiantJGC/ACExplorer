from pyUbiForge2.api.game import SubclassBaseFile
from .BaseFractionalBrownianMotion import BaseFractionalBrownianMotion as _BaseFractionalBrownianMotion


class FractionalBrownianMotion2D(SubclassBaseFile):
    ResourceType = 0xBF79E01F
    ParentResourceType = _BaseFractionalBrownianMotion.ResourceType
    parent: _BaseFractionalBrownianMotion

