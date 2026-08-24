dict = {
"name" : "istak",
"cgpa" : "backlog",
"subjects":("math", "chemistry"),
"ppr" : "yes",
"amount":"400"

}
print(dict["name"])
print(dict)
print(type(dict))
print(dict["name"])
print(dict["ppr"])

#Dictionary is mutable
dict["cgpa"]= 7.26
print(dict)