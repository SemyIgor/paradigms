# Задача №1
# Дан список целых чисел numbers.
# Необходимо написать в императивном стиле процедуру для сортировки
# числа в списке в порядке убывания.
# Можно использовать любой алгоритм сортировки.


# Сортировка по убыванию двух соседних чисел


def sortTwoNumbers(a, b):
    return [a, b] if a > b else [b, a]

# Вытеснение наименьшего "пузырька" в конец массива


def moveMinNumToEnd(k):
    for i in range(len(numList) - k):
        numList[i], numList[i+1] = \
            sortTwoNumbers(numList[i], numList[i+1])


def sort_list_imperative(numbers):
    for j in range(1, len(numbers)):
        moveMinNumToEnd(j)


def printArray(comment, arr):
    print(comment)
    for i in arr:
        print(i, " ", end="")


numList = [12, 2, -7, 25, 0, 12, 14, 7]

printArray('\nМассив до сортировки:', numList)
sort_list_imperative(numList)
printArray('\nМассив после сортировки:', numList)
