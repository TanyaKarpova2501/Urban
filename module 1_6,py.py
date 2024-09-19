from ast import Param

my_dict = {"Nelly":2015, "Alisa":2020}
print(my_dict)
my_dict ['Andrey'] = 1991
print(my_dict["Nelly"])
print(my_dict['Andrey'])
my_dict.update({'Pavel':1985,
                "Olesya":1987})
print(my_dict)
del my_dict['Nelly']
print(my_dict)


my_set = {2,3,5,4,9,5,5,9,8}
print(my_set)
my_set = {2,3,5,4,9,5,5,9,8, "sport", True}
print(my_set)
print(my_set.discard(4))
print(my_set)