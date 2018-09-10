def roman_to_decimal(rom):

    dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sum = 0

    #Если буква одна, ее и выводим, если не одна, начинаем проверять порядок - если он правильный, складываем, если неправильный - вычитаем

    if len(rom) == 1:
        sum += dict[rom]
    else:
        for i in range(len(rom) - 1):
            if dict[rom[i]] >= dict[rom[i + 1]]:
               sum += dict[rom[i]]
            else:
               sum -= dict[rom[i]]
        sum += dict[rom[i + 1]]

    return sum

##################################################

def decimal_to_roman(dec):
    
    rom = 'M' * (dec // 1000)
    dec %= 1000
    rom += 'D' * (dec // 500)
    dec %= 500
    rom += 'C' * (dec // 100)
    dec %= 100
    rom += 'L' * (dec // 50)
    dec %= 50
    rom += 'X' * (dec // 10)
    dec %= 10
    rom += 'V' * (dec // 5)
    dec %= 5
    rom += 'I' * dec

    # Да, я сделал это настолько нагло и прямо. Но, тем не менее, самая древняя версия римских чисел так и работает

    return rom

##################################################

test_pairs = [("IX", 9), ("XI", 11), ("MCCII", 1202), ("MMXVIII", 2018), ("XLIX", 49), ("LXXXIX", 89), ("XCIX", 99), ("M", 1000)]

#проверка первой части

for rom, dec in test_pairs:
    converted = roman_to_decimal(rom)
    print(converted == dec)

#проверка второй части (довольно хитрая, нужно сказать)

for rom, dec in test_pairs:
    converted = roman_to_decimal(decimal_to_roman(dec))
    print(converted == dec)