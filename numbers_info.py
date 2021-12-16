import math


def is_number(a_string):
    try:
        float(a_string)
        return True
    except ValueError:
        return False


def minimum(arr: list):
    if arr:
        min_num = arr[0]
        for i in arr:
            if i < min_num:
                min_num = i
    else:
        min_num = None

    return min_num


def maximum(arr: list):
    if arr:
        max_num = arr[0]
        for i in arr:
            if i > max_num:
                max_num = i
    else:
        max_num = None

    return max_num


def addition(arr: list):
    if arr:
        addition_num = 0
        for i in arr:
            addition_num += i
    else:
        addition_num = None

    return addition_num


def multiplication(arr: list):
    if arr:
        multiplication_num = 1
        for i in arr:
            try:
                multiplication_num *= i
            except:
                multiplication_num = math.inf
    else:
        multiplication_num = None

    return multiplication_num


def file_opener(filename):

    a_file = []

    with open(filename, 'r') as f:
        for line in f:
            if is_number(line):
                a_file.append(float(line))
            else:
                return []
    return a_file


def body(filename):

    a_file = file_opener(filename=filename)
    if a_file:
        minn = minimum(a_file)
        maxx = maximum(a_file)
        addit = addition(a_file)
        mult = multiplication(a_file)
    else:
        return print('File is empty or contains not numbers!')

    print(
        'Minimal:', minn,
        '\nMaximal:', maxx,
        '\nAdding:', addit,
        '\nMultiplication:', 'Very big number!' if mult == math.inf else mult
    )


body(filename='numbers.txt')
