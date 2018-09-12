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
    
    s = ''
    dict = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'} 
    # все исключения стырил с википедии

    for i in dict.keys():
        k = dec // i
        dec %= i
        s += dict[i] * k
    
    return rom

##################################################

test_pairs = [("IX", 9), ("XI", 11), ("MCCII", 1202), ("MMXVIII", 2018), ("XLIX", 49), ("LXXXIX", 89), ("XCIX", 99), ("M", 1000)]

#проверка первой части

for rom, dec in test_pairs:
    converted = roman_to_decimal(rom)
    print(converted == dec)

#проверка второй части

for rom, dec in test_pairs:
    converted = decimal_to_roman(dec)
    print(converted == rom)
