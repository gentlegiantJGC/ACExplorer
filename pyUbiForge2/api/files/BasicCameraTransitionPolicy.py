from pyUbiForge2.api.game import SubclassBaseFile
from .ICameraTransitionPolicy import ICameraTransitionPolicy as _ICameraTransitionPolicy


class BasicCameraTransitionPolicy(SubclassBaseFile):
    ResourceType = 0x1AA0F69D
    ParentResourceType = _ICameraTransitionPolicy.ResourceType
    parent: _ICameraTransitionPolicy
