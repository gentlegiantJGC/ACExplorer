from pyUbiForge2.api.game import SubclassBaseFile
from .BaseFractionalBrownianMotion import BaseFractionalBrownianMotion as _BaseFractionalBrownianMotion


class FractionalBrownianMotion3D(SubclassBaseFile):
    ResourceType = 0xA662D15E
    ParentResourceType = _BaseFractionalBrownianMotion.ResourceType
    parent: _BaseFractionalBrownianMotion

