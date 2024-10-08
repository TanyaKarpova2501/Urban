def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(b= 25, c= [1, 2, 3])

value_list = [25.01, "мышка"]
value_disc = {"c": "макарена"}

print_params(*value_list, 142)
print_params(*value_list, **value_disc)