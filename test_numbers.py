from dict_numbers import number_names


def convert(number):
    if number <= 20:
        return '{number_name} reais'.format(number_name=number_names(number))
    if number <= 100 and str(number).endswith('0'):
        return '{number_name} reais'.format(number_name=number_names(number))
    if number < 100:
        first = str(number)[:1] + '0'
        last = str(number)[1:]
        return '{first} e {last} reais'.format(
            first=number_names(int(first)),
            last=number_names(int(last))
        )


def test_integer_numbers():
    assert convert(4) == 'quatro reais'
    assert convert(8) == 'oito reais'
    assert convert(10) == 'dez reais'
    assert convert(15) == 'quinze reais'
    assert convert(20) == 'vinte reais'
    assert convert(30) == 'trinta reais'
    assert convert(40) == 'quarenta reais'
    assert convert(50) == 'cinquenta reais'
    assert convert(60) == 'sessenta reais'
    assert convert(70) == 'setenta reais'
    assert convert(80) == 'oitenta reais'
    assert convert(90) == 'noventa reais'
    assert convert(100) == 'cem reais'


def test_integer_numbers_higher_than_twenty():
    assert convert(21) == 'vinte e um reais'
    assert convert(25) == 'vinte e cinco reais'
    assert convert(27) == 'vinte e sete reais'
    assert convert(31) == 'trinta e um reais'
    assert convert(33) == 'trinta e três reais'
    assert convert(36) == 'trinta e seis reais'
    assert convert(39) == 'trinta e nove reais'
    assert convert(44) == 'quarenta e quatro reais'
    assert convert(48) == 'quarenta e oito reais'
    assert convert(49) == 'quarenta e nove reais'
    assert convert(51) == 'cinquenta e um reais'
    assert convert(62) == 'sessenta e dois reais'
    assert convert(73) == 'setenta e três reais'
    assert convert(84) == 'oitenta e quatro reais'
    assert convert(95) == 'noventa e cinco reais'
    assert convert(99) == 'noventa e nove reais'

