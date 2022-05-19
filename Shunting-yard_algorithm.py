
# Метод сортировочной станции
from string import digits
import itertools

# input_string = "5+2*3-2*2"          # 523*+22*-
# input_string = "5+2*3"              # 523*+
# input_string = "5+1+2+3+4"          # 51+2+3+4+
input_string = "5*2+7*3-6-1"          # 52*73*+6-1-
# input_string = "5/2+7*3-6-1"        # 52/73*+6-1-
# input_string = "2/2-2*2*2+1"        # 22/22*2*-1+
# input_string = "3/1-2*2*2+1"        # 31/22*2*-1+
# input_string = "3/0-2*2*2+1"        # Выдаст исключение
# input_string = "3*2-1-*1"           # Выдаст исключение
# input_string = "3*2-1-+1"           # Выдаст исключение
# input_string = "sfsdfsd"            # Выдаст исключение


output_string = []
operator_stack = []
rank_operators = {"*": 2,"/": 2,"+": 1,"-": 1}
count_len_operators = []
param_for_break = 0
Letter_in_string = 0


list_for_compare = []
string_test = ""
for i in itertools.product('+-*/', repeat=2):
    a = string_test.join(i)
    list_for_compare = list_for_compare + [a]
for i in range(0,len(list_for_compare)):
    if list_for_compare[i] in input_string:
        param_for_break = param_for_break + 1
        print("Повтор знаков операций")



for i in range(0,len(input_string)):
    if input_string[i].isalpha():
        Letter_in_string = Letter_in_string + 1
        print("Некорректный вод:")
        break
    if input_string[i] in digits:
        output_string.append(input_string[i])
    if input_string[i] in ("+","-","*","/"):
        if operator_stack == []:
            # print("Пустой стек")
            operator_stack.append(input_string[i])
        else:
            if rank_operators[input_string[i]] > rank_operators[operator_stack[0]]:
                operator_stack.insert(0, input_string[i])

            elif rank_operators[input_string[i]] == rank_operators[operator_stack[0]]:
                output_string.append(operator_stack[0])
                operator_stack.reverse()
                operator_stack.pop()
                operator_stack.reverse()
                operator_stack.insert(0, input_string[i])

            elif rank_operators[input_string[i]] < rank_operators[operator_stack[0]]:
                output_string.append(operator_stack[0])
                operator_stack.reverse()
                operator_stack.pop()
                operator_stack.reverse()

                if operator_stack == []:
                    # print("Снова стал пустой стек")
                    operator_stack.append(input_string[i])

                elif rank_operators[input_string[i]] > rank_operators[operator_stack[0]]:
                    operator_stack.insert(0, input_string[i])

                elif rank_operators[input_string[i]] == rank_operators[operator_stack[0]]:
                    output_string.append(operator_stack[0])
                    operator_stack.reverse()
                    operator_stack.pop()
                    operator_stack.reverse()
                    operator_stack.insert(0, input_string[i])


output_string.extend(operator_stack)
Str_output_string = "".join(output_string)


ZeroDivision_in_String = "0/"
print("Была задана последовательность: ", input_string)
if ZeroDivision_in_String in Str_output_string:
    print("!!! === На ноль делить нельзя === !!!")
elif param_for_break != 0:
    print("Неверный ввод!!!")
elif Letter_in_string != 0:
    print("Были введены буквы!!! Нужно задавать только цифры и операции!!!")
else:
    print("Вывод в виде списка: ", output_string)
    print("Вывод в виде строки: ", Str_output_string)





