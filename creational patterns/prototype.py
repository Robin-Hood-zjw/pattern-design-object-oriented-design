import copy
from abc import ABC

class GenePrototype(ABC):
    _cell_wall = None
    _cell_nucleus = None

    def __init__(self) -> None:
        pass 
    
    def clone(self) -> None:
        pass

class Concrete_GenePrototype(GenePrototype):
    _cell_wall = None
    _cell_nucleus = None

    def __init__(self, cell_wall: str, cell_nucleus: str) -> None:
      self._cell_wall = cell_wall
      self._cell_nucleus = cell_nucleus

    def clone(self) -> GenePrototype:
        return copy.deepcopy(self)
    

def clone_gene(prototype: GenePrototype) -> None:
    object = prototype.clone()
    print(f"\nCell Wall Type: {object._cell_wall}")
    print(f"Cell Wall Type: {object._cell_nucleus}\n")



if __name__ == "__main__":
    cloned_gene = Concrete_GenePrototype('1', '2')
    clone_gene(cloned_gene)