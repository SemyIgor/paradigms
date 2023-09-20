# Задача №2
# Дан список целых чисел numbers.
# Необходимо написать в декларативном стиле процедуру для сортировки
# числа в списке в порядке убывания.
# Можно использовать любой алгоритм сортировки.


def sort_list_declarative(numbers):
    numbers.sort(reverse=True)


def printArray(comment, arr):
    print(comment)
    for i in arr:
        print(i, " ", end="")


numList = [12, 2, -7, 25, 0, 12, 14, 7]

printArray('\nМассив до сортировки:', numList)
sort_list_declarative(numList)
printArray('\nМассив после сортировки:', numList)
