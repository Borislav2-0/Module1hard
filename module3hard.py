def flat(t):
    unpack = []
    if isinstance(t, list) or isinstance(t, set) or isinstance(t, tuple):
        return sum(map(flat, t), unpack)
    else:
        return [t]


def flat1(t):
    unpack = []
    if isinstance(t, list) or isinstance(t, set) or isinstance(t, tuple) or isinstance(t, dict):
        return sum(map(flat1, t), unpack)
    else:
        return [t]


def sum_data(data):
    num = 0
    lit = 0
    for i in range(len(data)):
        if type(data[i]) == type(1):
            num = num + data[i]
        else:
            lit = lit + len(data[i])
    return num + lit


def dict_unpack(dict1):
    dict_v = []
    for i in range(len(dict1)):
        if isinstance(dict1[i], dict):
            dict_v.append(dict1[i])
    dict_ov = []
    for i in range(len(dict_v)):
        dict_ov.append(sum(dict_v[i].values()))
    a = sum(dict_ov)
    return a


def calculate_structure_sum(data_sructure):
    result1 = flat1(data_structure)
    result2 = (sum_data(result1))
    result3 = flat(data_structure)
    result = dict_unpack(result3)
    print(result2 + result)


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])]

calculate_structure_sum(data_structure)
