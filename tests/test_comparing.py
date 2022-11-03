from gendiff import generate_diff


def test_correct():
    test = generate_diff('tests/fixtures/file1.json',
                         'tests/fixtures/file2.json')
    with open('tests/fixtures/correct.txt') as cor:
        correct = cor.read()
        assert correct == test, 'Невеный вывод.'
    cor.close()
