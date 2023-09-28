""" Ваша задача
Написать скрипт для расчета корреляции Пирсона между 
двумя случайными величинами (двумя массивами). 
Можете использовать любую парадигму, 
но рекомендую использовать функциональную, 
т.к. в этом примере она значительно 
упростит вам жизнь. """

""" 
1  24	100
2	27	115
3	26	117
4	21	119
5	20	134
6	31	94
7	26	105
8	22	103
9	20	111
10	18	124
11	30	122
12	29	109
13	24	110
14	26	86 
"""

import math
arrayX = [24, 27, 26, 21, 20, 31, 26, 22, 20, 18, 30, 29, 24, 26]
arrayY = [100, 115, 117, 119, 134, 94, 105, 103, 111, 124, 122, 109, 110, 86]


# Среднее арифметическое
def average(arr):
    return sum(arr) / len(arr)


# Отклонения от среднего арифметического (массив разностей x(i) - M(x))
def deviations(arr):
    return list(map(lambda x: round(average(arr) - x, 3), arr))


# Сумма произведений отклонений от среднего арифметического (числитель)
def numerator(arr1, arr2):
    return sum(list(map(lambda x, y: x*y, deviations(arr1), deviations(arr2))))


# Квадратный корень из суммы произведения квадратов отклонений от среднего арифметического (знаменатель)
# Применена формула из условия задачи в ДЗ (но это ошибочная формула Пирсона !)
def denominatorHW(arr1, arr2):
    return math.sqrt(sum(list(map(lambda x, y: x**2 * y**2, deviations(arr1), deviations(arr2)))))


# Rоэффициент корреляции по формуле из ДЗ
def pearsonCorrelationHW(arr1, arr2):
    return numerator(arr1, arr2) / denominatorHW(arr1, arr2)


# Сумма квадратов отклонений от среднего арифметического для массива
def deviationsSquareSum(arr):
    return sum(list(map(lambda x: (round(average(arr) - x, 3)) ** 2, arr)))


# Квадратный корень из произведения сумм квадратов отклонения от среднего арифметического (знаменатель)
def denominator(arr1, arr2):
    return math.sqrt(deviationsSquareSum(arr1) * deviationsSquareSum(arr2))


# Коэффициент корреляции по формуле Пирсона
def pearsonCorrelation(arr1, arr2):
    return numerator(arr1, arr2) / denominator(arr1, arr2)


""" Печать промежуточных результатов для наглядности
# Печать исходных массивов
print(arrayX)
print(arrayY)


# Печать значения среднего арифметического для каждого массива
print("%.3f" % average(arrayX))
print("%.3f" % average(arrayY))


# Печать массивов отклонений от среднего для каждого массива
print(deviations(arrayX))
print(deviations(arrayY))


# Печать числителя формулы корреляции Пирсона
print(numerator(arrayX, arrayY))


# Печать знаменателя формулы корреляции из ДЗ
print(denominatorHW(arrayX, arrayY))


# Печать сумм квадратов отклонений от среднего арифметического
print(deviationsSquareSum(arrayX))
print(deviationsSquareSum(arrayY)) 
"""


# Печать коэффициента корреляции по формуле из ДЗ
print(pearsonCorrelationHW(arrayX, arrayY))


# Печать коэффициента корреляции Пирсона
print(pearsonCorrelation(arrayX, arrayY))
