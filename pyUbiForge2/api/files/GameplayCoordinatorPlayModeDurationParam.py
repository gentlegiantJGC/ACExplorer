from pyUbiForge2.api.game import SubclassBaseFile
from .GameplayCoordinatorPlayModeParam import (
    GameplayCoordinatorPlayModeParam as _GameplayCoordinatorPlayModeParam,
)


class GameplayCoordinatorPlayModeDurationParam(SubclassBaseFile):
    ResourceType = 0xF743A3AC
    ParentResourceType = _GameplayCoordinatorPlayModeParam.ResourceType
    parent: _GameplayCoordinatorPlayModeParam
