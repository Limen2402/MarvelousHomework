#Принимаем на консольный вход римское число, выдаем число арабское

dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
s_input = input()
sum = 0

#Если буква одна, ее и выводим, если не одна, начинаем проверять порядок - если он правильный, складываем, если неправильный - вычитаем

if len(s_input) == 1:
    sum += dict[s_input]
else:
    for i in range(len(s_input) - 1):
        if dict[s_input[i]] >= dict[s_input[i + 1]]:
           sum += dict[s_input[i]]
        else:
           sum -= dict[s_input[i]]
    sum += dict[s_input[i + 1]]

print(sum)

#GIT