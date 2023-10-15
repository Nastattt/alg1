#
# number = int(input())
# Flag = True
#
# for i in range(2, number // 2 + 1):
#     if number % i == 0:
#         Flag = False
#         break
#
# if Flag and number > 1:
#     print("Простое число")
# else:
#     print("Не подходит")
#
# def bubbleSort(array):
#     swapped = False
#     for i in range(len(array ) -1 ,0 ,-1):
#         for j in range(i):
#             if array[j ] >array[ j +1]:
#                 array[j], array[ j +1] = array[ j +1], array[j]
#                 swappe d= True
#         if swapped:
#             swappe d =False
#         else:
#             break
#     return array
#
# def maxiNum(array):
#     maxi = array[0]
#     for i in array:
#         if i > maxi:
#             maxi = i
#     return maxi
#
#
# maxiNum([1 ,4 ,5 ,2 ,6])
#
#
# def fibonacci(n):
#     if n <= 0:
#         return "Номер числа должен быть больше 0"
#     elif n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
#
# n = int(input("Введите номер числа Фибоначчи: "))
# result = fibonacci(n)
# print(f"Число Фибоначчи с номером {n} равно {result}")
# def repeat_words(array_):
#     repeat_words = []
#
#     for i in range(0, array_size):
#         repeat_words.append(0)
#
#     for i in range(0, len(array_)):
#         for j in range(0, len(array_)):
#             if array_[i] == array_[j]:
#                 repeat_words[i] += 1
#
#     index_repeat_word = -1
#
#     for i in range(0, len(array_)):
#         if repeat_words[i] > index_repeat_word:
#             index_repeat_word = i
#
#     if index_repeat_word == -1:
#         return 'Строки не повторяются'
#     else:
#         return index_repeat_word
#
# array = []
# array_size = int(input('Введите количество элементов массива: '))
#
# for i in range(0, array_size):
#     array.append(input('Введите строку для элемента массива ' + str(i)+': '))
#
# print(array[repeat_words(array)])
