import json

with open("data.json", "r") as f:
     py_obj = json.load(f)
     print(py_obj)


data = {
     "name":"Istak",
     "isStudent":True,
     "age":21
}

with open("data.json", "w") as f:
     json.dump(data, f, indent=4, sort_keys=True)
