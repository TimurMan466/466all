def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1


def sort_list(lst):
    return sorted(lst)


input_str = input("Введите последовательность чисел через пробел: ")
user_num = input("Введите любое число: ")

try:
    lst = [int(num) for num in input_str.split()]
    user_num = int(user_num)
except ValueError:
    print("Ошибка ввода! Проверьте введенные данные и повторите попытку.")
else:
    sorted_lst = sort_list(lst)
    index = binary_search(sorted_lst, 0, len(sorted_lst) - 1, user_num)
    if index == -1:
        print(f"Введенное число {user_num} не найдено в последовательности.")
    elif index == len(sorted_lst) - 1:
        print(f"Введенное число {user_num} меньше всех элементов последовательности.")
    else:
        print(f"Номер позиции элемента, который меньше {user_num}, "
              f"а следующий за ним больше или равен этому числу, равен {index + 1}.")
