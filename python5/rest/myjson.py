import json
import jsonschema
import requests
import sys

def SerializeJson(in_dict, file_path) -> bool:
    try:
        f = open(file_path, 'w')
        json.dump(in_dict, f, indent=6)
        f.close()
        return True
    
    except Exception:
        return False

def DeserializeJson(file_path) -> dict:
    try:
        f = open(file_path, "r")
        ret_dict = dict()
        ret_dict = json.load(f)
        f.close()
        return ret_dict
    
    except Exception:
        return None