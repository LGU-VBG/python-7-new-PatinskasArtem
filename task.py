def merge_lists_to_dict(keys, values):
    return dict(zip(keys, values))


keys_list = ['a', 'b', 'c']
values_list = [1, 2, 3]

result = merge_lists_to_dict(keys_list, values_list)
print(result)

result_kw = merge_lists_to_dict(keys=keys_list, values=values_list)
print(result_kw)

result_mixed = merge_lists_to_dict(keys_list, values=[10, 20, 30])
print(result_mixed)
