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


test_pairs = [("IX", 9), ("XI", 11), ("MCCII", 1202), ("MMXVIII", 2018), ("XLIX", 49), ("LXXXIX", 89), ("XCIX", 99)]

for rom, dec in test_pairs:
    converted = roman_to_decimal(rom)
    print(converted == dec)