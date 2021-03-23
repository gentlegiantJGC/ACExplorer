from pyUbiForge2.api.game import SubclassBaseFile
from .FPSCamera import FPSCamera as _FPSCamera


class MarketingCamera(SubclassBaseFile):
    ResourceType = 0x5B7FC715
    ParentResourceType = _FPSCamera.ResourceType
    parent: _FPSCamera

