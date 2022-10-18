'''Comparing the files'''

import json


def generate_diff(file1, file2):
    result = []
    with open(file1) as f1:
        with open(file2) as f2:
            json1 = json.load(f1)
            json2 = json.load(f2)
            result = print(*compare_dicts(json1, json2), sep='\n')
    f1.close()
    f2.close()
    return result


def compare_dicts(dict1, dict2):
    result = []
    dict1 = check_boolean(dict(sorted(dict1.items())))
    dict2 = check_boolean(dict(sorted(dict2.items())))
    for i in dict1:
        if i not in dict2:
            result.append(f'  - {i}: {dict1[i]}')
        else:
            if dict1[i] == dict2[i]:
                result.append(f'    {i}: {dict1[i]}')
            else:
                result.append(f'  - {i}: {dict1[i]}')
                result.append(f'  + {i}: {dict2[i]}')
    for j in dict2:
        if j not in dict1:
            result.append(f'  + {j}: {dict2[j]}')
    return result


def check_boolean(dict):
    for k in dict.keys():
        if dict.get(k) is False:
            dict[k] = 'false'
        if dict.get(k) is True:
            dict[k] = 'true'
    return dict
