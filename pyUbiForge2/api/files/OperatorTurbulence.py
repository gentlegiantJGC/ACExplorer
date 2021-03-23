from pyUbiForge2.api.game import SubclassBaseFile
from .BaseNoiseOperator import BaseNoiseOperator as _BaseNoiseOperator


class OperatorTurbulence(SubclassBaseFile):
    ResourceType = 0xF78BAF83
    ParentResourceType = _BaseNoiseOperator.ResourceType
    parent: _BaseNoiseOperator

