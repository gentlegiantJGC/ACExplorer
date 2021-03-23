from pyUbiForge2.api.game import SubclassBaseFile
from .RigidBodyComponent import RigidBodyComponent as _RigidBodyComponent


class SuspendedObjectComponent(SubclassBaseFile):
    ResourceType = 0xD4A16D1A
    ParentResourceType = _RigidBodyComponent.ResourceType
    parent: _RigidBodyComponent
