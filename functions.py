from dict_numbers import full_number_names

unities_singular = ['', 'mil', 'milhão', 'bilhão']
unities_plural = ['', 'mil', 'milhões', 'bilhões']


def split_in_three(number):
    number_str = str(number)
    numbers = []
    while True:
        numbers.insert(0, number_str[-3:])
        number_str = number_str[:-3]
        if not number_str:
            break
    for weight, number in enumerate(reversed(numbers)):
        yield (number, weight)


def small_numbers(number):
    number_int = int(number)
    number_str = str(number_int)
    if number_int > 1000:
        return thousand_numbers(number)
    if number_int == 0:
        return full_number_names.get(0)
    if number_int == 1:
        return full_number_names.get(1)
    if number_int <= 20:
        return '{number_name}'.format(number_name=full_number_names.get(number_int))
    if number_int <= 100 and number_str.endswith('0'):
        return '{number_name}'.format(number_name=full_number_names.get(number_int))
    if number_int <= 1000 and number_str.endswith('000'):
        return '{number_name}'.format(number_name=full_number_names.get(number_int))

    if number_int < 100:
        first = number_str[:1] + '0'
        last = number_str[1:]
        return '{first} e {last}'.format(
            first=full_number_names.get(int(first)),
            last=full_number_names.get(int(last)),
        )
    if number_int <= 1000 and number_str.endswith('00'):
        return '{number_name}'.format(number_name=full_number_names.get(number_int))
    if number_int <= 200 > 100:
        dozens = number_str[-2:]
        return 'cento' + ' e ' + small_numbers(dozens)
    elif number_int <= 1000 > 100:
        hundred = number_str[:1] + '00'
        dozens = number_str[-2:]
        return full_number_names.get(int(hundred)) + ' e ' + small_numbers(dozens)


def thousand_numbers(number):
    number_int = int(number)
    number_str = str(number)
    thousands = number_str[: len(number_str) - 3]
    if number_int < 100000 and number_str.endswith('000'):
        return '{} {}'.format(small_numbers(thousands), small_numbers(1000))
    if number_int < 1100:
        return full_number_names.get(int((number_str[:1] + '000'))) + ' e ' + small_numbers(number_str[1:])
    if number_int < 2000:
        return small_numbers(number_str[:1] + '000') + ' ' + small_numbers(number_str[1:])
    else:
        result = []
        split_list = reversed(list(split_in_three(number_int)))
        for group, weight in split_list:
            weights = unities_plural if int(group) > 1 else unities_singular
            if not group.startswith('0'):
                result.append('{} {} '.format(small_numbers(group), weights[weight]))
            elif not group.startswith('000'):
                result.append('e {} {} '.format(small_numbers(group), weights[weight]))
        return ''.join(result).strip()


def decimal_numbers(number):
    number_str = str(number).replace(',', '.')
    if '.' in number_str:
        decimals = number_str.split('.', -1)[-1]
        if len(decimals) == 1:
            return small_numbers(decimals + '0')
        return small_numbers(decimals)
    return small_numbers(number)


def convert(number):
    number_str = str(number).replace(',', '.')
    thousands, decimals = number_str.split('.', -1)
    sn = small_numbers(thousands)
    dn = decimal_numbers(number_str)
    if dn != 'zero':
        return '{}{}{}{}{}'.format(
            sn if sn != 'zero' else '',
            ' de reais' if sn != 'zero' and 'milhão' in sn else '',
            ' reais' if sn != 'zero' and 'milhão' not in sn else '',
            ' e ' if sn != 'zero' else '',
            dn + ' centavo' if dn and dn == 'um' else dn + ' centavos',
        )
    return '{}{}{}{}{}'.format(
        sn,
        'reais' if sn == 'zero' else '',
        ' real' if sn == 'um' else '',
        ' de reais' if 'milhão' in sn or 'milhões' in sn else '',
        ' reais' if sn != 'zero' and sn != 'um' and not ('milhão' in sn or 'milhões' in sn) else ''
    )
