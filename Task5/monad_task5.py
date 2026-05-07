from pymonad.tools import curry
from pymonad.maybe import Maybe, Just, Nothing
from pymonad.list import ListMonad


@curry(2)
def to_left(num: int, birds: tuple[int, int]):
    l, r = birds
    return Nothing if abs((l + num) - r) > 4 else Just((l + num, r))

@curry(2)
def to_right(num: int, birds: tuple[int, int]):
    l, r = birds
    return Nothing if abs((r + num) - l) > 4 else Just((l, r + num))

banana = lambda x: Nothing

def show(maybe):
    print(maybe.maybe(False, lambda _: True))


start = Just((0,0))

show(start.bind(to_left(2)).bind(to_right(5)).bind(to_left(-2)))
show(start.bind(to_left(2)).bind(to_right(5)).bind(to_left(-1)))
show(start.bind(to_left(2)).bind(banana).bind(to_right(5)).bind(to_left(-1)))
