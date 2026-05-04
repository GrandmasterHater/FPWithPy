from pymonad.tools import curry


# 2.3.1.

@curry(2)
def str_concat(first: str, second: str) -> str:
    return f'{first}{second}'
    

greeter = str_concat("Hello, ")
    
print(greeter('Sergey'))
print(greeter('Kristina'))
print(greeter('Yaroslav'))


# 2.3.2. 

@curry(4)
def first_step(greeting_word: str, punc_mark: str, final_mark: str, name: str) -> str:
    return f'{greeting_word}{punc_mark} {name}{final_mark}'
    
final = first_step("Hello")(",")("!")
print(final('Sergey'))
print(final('Kristina'))
print(final('Yaroslav'))
