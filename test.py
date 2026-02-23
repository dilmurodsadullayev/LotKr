from api.cyrillic_to_latin import cyrillic_to_latin
from api.latin_to_cyrillic import latin_to_cyrillic

text = input()
translate = input("lot/kril: ")
if translate == "lotin": 
    print(cyrillic_to_latin(text))
elif translate == "kril":
    print(latin_to_cyrillic(text))