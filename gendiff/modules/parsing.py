import json
import yaml


def parse_files(file1, file2):
    with open(file1) as f1:
        with open(file2) as f2:
            # print(file1[-4::])
            # print('=====')
            # print(file2[-4::])
            if file1[-4::] == 'json' and file2[-4::] == 'json':
                dict1 = json.load(f1)
                # print('Read JSON 1.')
                dict2 = json.load(f2)
                # print('Read JSON 2.')
            else:
                dict1 = yaml.safe_load(f1)
                # print('Read YAML 1.')
                dict2 = yaml.safe_load(f2)
                # print('Read YAML 2.')
        f1.close()
        f2.close()
        # print(f'Dict1:\n{dict1}')
        # print('=======')
        # print(f'Dict2:\n{dict2}')
        return (dict1, dict2)
