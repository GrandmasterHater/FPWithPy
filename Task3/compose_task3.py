from pymonad.tools import curry


# 3.1. 

@curry(2)
def tag(html_tag: str, value: str) -> str:
    return f'<{html_tag}>{value}</{html_tag}>'
    
bold = tag('b')
italic = tag('i')

print(bold("Hello!"))
print(italic("Hello!"))



#3.2. 

@curry(3)
def tag(html_tag: str, attrs: dict[str, str], tag_value: str) -> str:
    str_attrs = " ".join(f'{key}=\"{value}\"' for key, value in attrs.items())
    str_attrs = " " + str_attrs if str_attrs else '' 
    
    return f'<{html_tag}{str_attrs}>{tag_value}</{html_tag}>'
    
li_tag = tag('li', {'class': 'list-group'})

print(li_tag('item 23'))
