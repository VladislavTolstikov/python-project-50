from gendiff.modules.generatediff import generate_diff


def test_correct():
    test = generate_diff('tests/fixtures/file1.json',
                         'tests/fixtures/file2.json')
    testyaml = generate_diff('tests/fixtures/file1.yaml',
                             'tests/fixtures/file2.yml')
    with open('tests/fixtures/correct.txt') as cor:
        correct = cor.read()
        assert correct == test, 'Неверный вывод при сравнении JSON.'
        assert correct == testyaml, 'Неверый вывод при сравении YAML.'
    cor.close()
