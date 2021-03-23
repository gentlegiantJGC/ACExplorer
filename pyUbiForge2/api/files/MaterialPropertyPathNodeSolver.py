from pyUbiForge2.api.game import SubclassBaseFile
from .PropertyPathNodeSolver import PropertyPathNodeSolver as _PropertyPathNodeSolver


class MaterialPropertyPathNodeSolver(SubclassBaseFile):
    ResourceType = 0xBC5B87AF
    ParentResourceType = _PropertyPathNodeSolver.ResourceType
    parent: _PropertyPathNodeSolver

