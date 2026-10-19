# Create a Python dictionary of 3 cities and their populations.
# Save it to "cities.json"
# 1. Then load the JSON and print each city and its population.
# 2.Ask the user for a new city & its population - update this info in the json file.

import json
f = open("cities.json", "r")
py_obj = json.load(f)
print(py_obj)
f.close()
# print(type(json_str))

city = input("Enter the new city name:")
population = input(f"Enter the population of {city}:")

py_obj.update({
    city:population
})

g = open("cities.json", "w")
json.dump(py_obj, g)
g.close()