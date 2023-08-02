#implement the method of Dictionary
my_dict={"name":"genzeon","languase":"",1:2,"address":"hyd"}
print(my_dict['name'])
print(my_dict.keys())
print(my_dict.values())
print(my_dict.get(1))
my_dict.setdefault("country", "India")
print(my_dict)
a=my_dict.pop("languase")
print(a)
print(my_dict)
my_dict.update({"Tech":["dotnet","Java","Python"]})
print(my_dict)