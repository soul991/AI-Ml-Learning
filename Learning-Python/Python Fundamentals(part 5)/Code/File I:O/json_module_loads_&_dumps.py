import json

json_str = '{"name":"Istak","isStudent":true,"balance":null}'
print(type(json_str))

py_obj = json.loads(json_str) 
print(type(py_obj), py_obj)


json_str = json.dumps(py_obj)
print(type(json_str), json_str)