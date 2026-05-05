from pymonad.tools import curry
from pymonad.maybe import Maybe, Just, Nothing
from pymonad.list import ListMonad

@curry(2)
def add(x, y):
    return x + y
    
add10 = add(10)

Just(1).then(add10)
ListMonad(1,2,3,4).map(add10)

print(Just(1).then(add10))
print(ListMonad(1,2,3,4).map(add10))
