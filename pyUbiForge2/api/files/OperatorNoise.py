from pyUbiForge2.api.game import SubclassBaseFile
from .BaseNoiseOperator import BaseNoiseOperator as _BaseNoiseOperator


class OperatorNoise(SubclassBaseFile):
    ResourceType = 0xC0A0384C
    ParentResourceType = _BaseNoiseOperator.ResourceType
    parent: _BaseNoiseOperator
