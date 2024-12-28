def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

values_list = ['Alina', 4, True]
values_dict = {'a': 21.3, 'b': 2, 'c': 'Max'}
values_list_2 = [72, 'Sem']

print_params()
print_params(2, 'list')
print_params(4, 'Urban', False)
print_params(b = 25)
print_params(c = [1,2,3])
print_params(*values_list)
print_params(**values_dict)
print_params(12, *values_list_2)
print_params(*values_list_2, 42)