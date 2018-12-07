from decimal import Decimal
from dict_numbers import number_names


def identify_numbers(number):
    number_str = str(number).replace(',', '.')
    is_integer = float(number).is_integer()

    integer = Decimal(number_str)
    decimals = None
    if not is_integer:
        integer = Decimal(number_str[:number_str.find('.')])
        decimals = Decimal(number_str[number_str.find('.'):])

    thousand = integer / 1000 >= 1
    hundred = integer / 100 >= 1
    dozen = integer / 10 >= 1
    unit = integer / 1 >= 1
    decimal = bool(decimals)

    if thousand:
        string = None


def convert_integers(number):
    number_str = str(number).replace(',', '.')
    number_decimal = Decimal(number_str)
    is_integer = float(number).is_integer()
    integer = number_str
    decimal = None
    if not is_integer:
        integer = number_str[:number_str.find('.')]
        decimal = number_str[number_str.find('.'):]


    number_decimal = Decimal(number)
    if number_decimal == 1:
        if number_decimal % 1 == 0:
            return 'um'
        return
    if number_decimal <= 20:
        return '{number_name}'.format(number_name=number_names(number_decimal))
    if number_decimal <= 100 and str(number_decimal).endswith('0'):
        return '{number_name}'.format(number_name=number_names(number_decimal))

    if number_decimal < 100:
        first = str(number_decimal)[:1] + '0'
        last = str(number_decimal)[1:]
        return '{first} e {last}'.format(
            first=number_names(int(first)),
            last=number_names(int(last))
        )
    if number_decimal <= 1000 and str(number_decimal).endswith('00'):
        return '{number_name}'.format(number_name=number_names(number_decimal))


def test_integer_numbers():
    assert convert_integers(1) == 'um'
    # assert convert_integers(4) == 'quatro'
    # assert convert_integers(8) == 'oito'
    # assert convert_integers(10) == 'dez'
    # assert convert_integers(15) == 'quinze'
    # assert convert_integers(20) == 'vinte'
    # assert convert_integers(30) == 'trinta'
    # assert convert_integers(40) == 'quarenta'
    # assert convert_integers(50) == 'cinquenta'
    # assert convert_integers(60) == 'sessenta'
    # assert convert_integers(70) == 'setenta'
    # assert convert_integers(80) == 'oitenta'
    # assert convert_integers(90) == 'noventa'
    # assert convert_integers(100) == 'cem'


def test_integer_numbers_higher_than_twenty():
    assert convert_integers(21) == 'vinte e um'
    assert convert_integers(25) == 'vinte e cinco'
    assert convert_integers(27) == 'vinte e sete'
    assert convert_integers(31) == 'trinta e um'
    assert convert_integers(33) == 'trinta e três'
    assert convert_integers(36) == 'trinta e seis'
    assert convert_integers(39) == 'trinta e nove'
    assert convert_integers(44) == 'quarenta e quatro'
    assert convert_integers(48) == 'quarenta e oito'
    assert convert_integers(49) == 'quarenta e nove'
    assert convert_integers(51) == 'cinquenta e um'
    assert convert_integers(62) == 'sessenta e dois'
    assert convert_integers(73) == 'setenta e três'
    assert convert_integers(84) == 'oitenta e quatro'
    assert convert_integers(95) == 'noventa e cinco'
    assert convert_integers(99) == 'noventa e nove'


def test_integer_hundreds():
    assert convert_integers(100) == 'cem'
    assert convert_integers(200) == 'duzentos'
    assert convert_integers(300) == 'trezentos'
    assert convert_integers(400) == 'quatrocentos'
    assert convert_integers(500) == 'quinhentos'
    assert convert_integers(600) == 'seiscentos'
    assert convert_integers(700) == 'setecentos'
    assert convert_integers(800) == 'oitocentos'
    assert convert_integers(900) == 'novecentos'
    assert convert_integers(1000) == 'mil'
