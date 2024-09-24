import json

def SerializzaJson(in_dict, file_path) -> bool:
    try:
        f = open(file_path, 'w')
        json.dump(in_dict, f, indent=6)
        f.close()
        return True
    
    except Exception:
        return False

def DeserializzaJson(file_path) -> dict:
    try:
        f = open(file_path, "r")
        ret_dict = dict()
        ret_dict = json.load(f)
        f.close()
        return ret_dict
    except Exception:
        return None
    

mydict_1 = { "brand": "Ford",
"electric": False,
"year": 1964,
"colors": ["red", "white", "blue"]}

mydict_2 = "{ 'brand':   'Ford'," + \
"'electric': False," + \
"'year': 1964," + \
"'colors': ['red', 'white', 'blue']}" 


print(SerializzaJson(mydict_1, "provaSerializzaJson.json"))
dict_deserializzato = DeserializzaJson("provaSerializzaJson.json")
print(type(dict_deserializzato))
print(dict_deserializzato)