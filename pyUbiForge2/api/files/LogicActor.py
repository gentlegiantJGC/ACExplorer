from pyUbiForge2.api.game import SubclassBaseFile
from .SceneActor import SceneActor as _SceneActor


class LogicActor(SubclassBaseFile):
    ResourceType = 0xED2092AD
    ParentResourceType = _SceneActor.ResourceType
    parent: _SceneActor
