from pyUbiForge2.api.game import SubclassBaseFile
from .PropertyPathNodeSolver import PropertyPathNodeSolver as _PropertyPathNodeSolver


class InertPropertyNodeSolver(SubclassBaseFile):
    ResourceType = 0x623476CE
    ParentResourceType = _PropertyPathNodeSolver.ResourceType
    parent: _PropertyPathNodeSolver
