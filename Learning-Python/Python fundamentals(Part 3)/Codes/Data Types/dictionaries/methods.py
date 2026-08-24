dict = {
"name" : "istak",
"cgpa" : "backlog",
"subjects":("math and chemistry"),
"ppr" : "yes",
"amount":"400"

}
dict_vals1 = list(dict.keys())
# to return all keys
print(dict_vals1)
print(type(dict_vals1))

dict_vals2 = (dict.values())
# to return all values
print(dict_vals2)
print(type(dict_vals2))

#To print the items
print(dict.items())

#Instead of error output for non-existing key, we use get key
print(dict.get("ppr3"))

# Without get key
# print(dict["ppr3"])
# print("End of code")

#Update a new key:value pair
dict.update({
    "city":"coochbehar"
})
print(dict)

#There is no indexing format in dictationery