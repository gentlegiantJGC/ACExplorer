from pyUbiForge2.api.game import SubclassBaseFile
from .Visual import Visual as _Visual


class VisualProxyComponent(SubclassBaseFile):
    ResourceType = 0x0CCF4ADB
    ParentResourceType = _Visual.ResourceType
    parent: _Visual
