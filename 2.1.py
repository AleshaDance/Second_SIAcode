import math
from datetime import datetime, date, time

# Bine formula : 0.0
# Iterative formula : 0.000025
# Ascending dp : 0.000036
# Downstream dp : 0.000044
# Divide & rule : 5.508511


def formula_bine():
    start = datetime.now()
    result = (pow((1 + math.sqrt(5)) / 2, 35) - pow((1 - math.sqrt(5)) / 2, 35)) / math.sqrt(5)
    return result, datetime.now() - start


def iterative_formula():
    start = datetime.now()
    a, b = 1, 1
    for i in range(3, 36):
        if i % 2 == 0:
            a += b
        else:
            b += a
    result = max(a, b)
    return result, datetime.now() - start


def divide_rule():
    start = datetime.now()
    n = 35
    result = lambda n: f_rv(n - 1) + f_rv(n - 2) if n > 2 else 1
    return result, datetime.now() - start


def top_down():
    start = datetime.now()
    dictionary = {0: 0,
                  1: 1}

    def cycle(elem):
        if elem in dictionary:
            return dictionary[elem]
        dictionary[elem] = cycle(elem - 1) + cycle(elem - 2)
        return dictionary[elem]

    result = cycle(35)
    return result, datetime.now() - start


def top_up():
    start = datetime.now()

    def cycle(n):
        a, b = 0, 1
        for __ in range(n):
            a, b = b, a + b
        return a

    result = cycle(35)
    return result, datetime.now() - start


def cmd():
    first_res, first_time = formula_bine()
    second_res, second_time = iterative_formula()
    third_res, third_time = divide_rule()
    four_res, four_time = top_down()
    five_res, five_time = top_up()

    print("1) Bine formula\n2) Iterative formula\n3) Divide & rule\n"
          "4) Downstream dp\n5) Ascending dp\n6) *Compare time*\n7) Exit")
    act = int(input(""))
    if act == 1:
        print('Result: ' + str(first_res))
        print('Lead time: ') + str(first_time)
    if act == 2:
        print('Result: ' + str(second_res))
        print('Lead time: ') + str(second_time)
    if act == 3:
        print('Result: ' + str(third_res))
        print('Lead time: ') + str(third_time)
    if act == 4:
        print('Result: ' + str(four_res))
        print('Lead time: ') + str(four_time)
    if act == 5:
        print('Result: ' + str(five_res))
        print('Lead time: ') + str(five_time)
    if act == 6:
        time_list = [('Bine formula', first_time),
                     ('Iterative formula', second_time),
                     ('Divide & rule', third_time),
                     ('Downstream dp', four_time),
                     ('Ascending dp', five_time)]
        time_list.sort(key=lambda i: i[1])
        for i in time_list:
            print(i[0], ':', i[1])


cmd()


