'''Comparing the files'''
from gendiff.modules.parsing import parse_files


def generate_diff(file1, file2):
    dict1, dict2 = parse_files(file1, file2)
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
    result = '\n'.join(result)
    return result


def check_boolean(dict):
    for k in dict.keys():
        if dict.get(k) is False:
            dict[k] = 'false'
        if dict.get(k) is True:
            dict[k] = 'true'
    return dict
