from functions import convert

print('Digite "s" para sair.')
while True:
    number = input('Digite um número:\n').strip()
    if number == 's':
        break
    print(convert(number), '\n')
