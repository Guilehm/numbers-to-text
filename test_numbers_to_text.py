from main import convert, decimal_numbers, small_numbers, thousand_numbers


def test_convert():
    assert convert(1000.10) == 'mil reais e dez centavos'
    assert convert(100000.10) == 'cem mil reais e dez centavos'
    assert convert(0.10) == 'dez centavos'
    assert convert(0.01) == 'um centavo'
    assert convert(0.99) == 'noventa e nove centavos'
    assert convert(1) == 'um real'
    assert convert(10) == 'dez reais'
    assert convert(999000.01) == 'novecentos e noventa e nove mil reais e um centavo'
    assert convert(100000.01) == 'cem mil reais e um centavo'
    assert convert(60000.11) == 'sessenta mil reais e onze centavos'
    assert convert(1000) == 'mil reais'
    assert convert(1000000) == 'um milhão de reais'
    assert convert(5000000) == 'cinco milhões de reais'
    assert convert(50000000) == 'cinquenta milhões de reais'
    assert convert(53128040.32) == 'cinquenta e três milhões cento e vinte e oito mil e quarenta reais ' \
                                   'e trinta e dois centavos'
    assert convert(99999999.99) == 'noventa e nove milhões novecentos e noventa e nove mil novecentos e ' \
                                   'noventa e nove reais e noventa e nove centavos'


def test_decimal_numbers():
    assert decimal_numbers(10.4) == 'quarenta'
    assert decimal_numbers(10.40) == 'quarenta'
    assert decimal_numbers(10.04) == 'quatro'
    assert decimal_numbers(1000.04) == 'quatro'
    assert decimal_numbers('1.000.04') == 'quatro'
    assert decimal_numbers(100000.99) == 'noventa e nove'


def test_small_numbers():
    assert small_numbers(1) == 'um'
    assert small_numbers(2) == 'dois'
    assert small_numbers(8) == 'oito'
    assert small_numbers(10) == 'dez'
    assert small_numbers(15) == 'quinze'
    assert small_numbers(20) == 'vinte'
    assert small_numbers(50) == 'cinquenta'
    assert small_numbers(100) == 'cem'
    assert small_numbers(500) == 'quinhentos'
    assert small_numbers(900) == 'novecentos'
    assert small_numbers(1000) == 'mil'
    assert small_numbers(21) == 'vinte e um'
    assert small_numbers(55) == 'cinquenta e cinco'
    assert small_numbers(99) == 'noventa e nove'
    assert small_numbers(101) == 'cento e um'
    assert small_numbers(122) == 'cento e vinte e dois'
    assert small_numbers(185) == 'cento e oitenta e cinco'
    assert small_numbers(199) == 'cento e noventa e nove'
    assert small_numbers(202) == 'duzentos e dois'
    assert small_numbers(220) == 'duzentos e vinte'
    assert small_numbers(260) == 'duzentos e sessenta'
    assert small_numbers(290) == 'duzentos e noventa'
    assert small_numbers(299) == 'duzentos e noventa e nove'
    assert small_numbers(354) == 'trezentos e cinquenta e quatro'
    assert small_numbers(485) == 'quatrocentos e oitenta e cinco'
    assert small_numbers(597) == 'quinhentos e noventa e sete'
    assert small_numbers(639) == 'seiscentos e trinta e nove'
    assert small_numbers(838) == 'oitocentos e trinta e oito'
    assert small_numbers(999) == 'novecentos e noventa e nove'


def test_thousand_numbers():
    assert thousand_numbers(1001) == 'mil e um'
    assert thousand_numbers(1010) == 'mil e dez'
    assert thousand_numbers(1090) == 'mil e noventa'
    assert thousand_numbers(1099) == 'mil e noventa e nove'
    assert thousand_numbers(1199) == 'mil cento e noventa e nove'
    assert thousand_numbers(1299) == 'mil duzentos e noventa e nove'
    assert thousand_numbers(1592) == 'mil quinhentos e noventa e dois'
    assert thousand_numbers(1658) == 'mil seiscentos e cinquenta e oito'
    assert thousand_numbers(1999) == 'mil novecentos e noventa e nove'
    assert thousand_numbers(2000) == 'dois mil'
    assert thousand_numbers(3000) == 'três mil'
    assert thousand_numbers(9000) == 'nove mil'
    assert thousand_numbers(10000) == 'dez mil'
    assert thousand_numbers(20000) == 'vinte mil'
    assert thousand_numbers(50000) == 'cinquenta mil'
    assert thousand_numbers(99000) == 'noventa e nove mil'
    assert thousand_numbers(150000) == 'cento e cinquenta mil'
    assert thousand_numbers(999000) == 'novecentos e noventa e nove mil'
    assert thousand_numbers(2012) == 'dois mil e doze'
    assert thousand_numbers(5095) == 'cinco mil e noventa e cinco'
    assert thousand_numbers(15092) == 'quinze mil e noventa e dois'
    assert thousand_numbers(515092) == 'quinhentos e quinze mil e noventa e dois'
    assert thousand_numbers(922022) == 'novecentos e vinte e dois mil e vinte e dois'
    assert thousand_numbers(1111111) == 'um milhão cento e onze mil cento e onze'
    assert thousand_numbers(1000000) == 'um milhão'
    assert thousand_numbers(1000001) == 'um milhão e um'
    assert thousand_numbers(1000011) == 'um milhão e onze'
    assert thousand_numbers(1000111) == 'um milhão cento e onze'
    assert thousand_numbers(100000000) == 'cem milhões'
    assert thousand_numbers(100000001) == 'cem milhões e um'
    assert thousand_numbers(100500001) == 'cem milhões quinhentos mil e um'
