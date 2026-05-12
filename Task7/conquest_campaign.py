from pymonad.tools import curry
from pymonad.state import State
from pymonad.maybe import Maybe, Just, Nothing
from pymonad.list import ListMonad
from typing import Callable

raw_adjacent_cells = lambda coordinate: ListMonad(
    (coordinate[0], coordinate[1] + 1),
    (coordinate[0], coordinate[1] - 1),
    (coordinate[0] + 1, coordinate[1]),
    (coordinate[0] - 1, coordinate[1])
)

@curry(3)
def is_cell_in_range(n: int, m: int, coordinate: tuple[int, int]):
    return ListMonad( (coordinate[0], coordinate[1]) ) if 1 <= coordinate[0] <= n and 1 <= coordinate[1] <= m else ListMonad()
  
@curry(3)
def get_adjanced_cells(n: int, m: int, coordinates: tuple[int, int]) -> set[int]:
    return set(ListMonad(*coordinates).bind(raw_adjacent_cells).bind(is_cell_in_range(n, m)))

array_to_coordinates_set = lambda array: set(zip(array[::2], array[1::2]))


def conquest_iteration(all_coordinates: tuple[int, int], border_coordinates: tuple[int, int], step: int, get_adjanced_cells_f: Callable) -> int:
    adjanced_empty_cells = get_adjanced_cells_f(border_coordinates) - all_coordinates
        
    if len(adjanced_empty_cells) == 0:
        return step
        
    all_coordinates = all_coordinates | adjanced_empty_cells
    
    return conquest_iteration(all_coordinates, adjanced_empty_cells, step + 1, get_adjanced_cells_f)


def conquest_campaign(n: int, m: int, l: int, battalion: list[int]) -> int:
    coordinates = array_to_coordinates_set(battalion)
    
    return conquest_iteration(coordinates, coordinates, 1, get_adjanced_cells(n, m))
        
        
print(conquest_campaign(3, 4, 2, [2,2, 3,4])) # 3
    
