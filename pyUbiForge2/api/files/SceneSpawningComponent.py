from pyUbiForge2.api.game import SubclassBaseFile
from .AbstractSceneSpawningComponent import (
    AbstractSceneSpawningComponent as _AbstractSceneSpawningComponent,
)


class SceneSpawningComponent(SubclassBaseFile):
    ResourceType = 0xFD6C1C73
    ParentResourceType = _AbstractSceneSpawningComponent.ResourceType
    parent: _AbstractSceneSpawningComponent
