def print_func_name_1():
    print('print_func_name_1')


def print_func_name_2():
    print('print_func_name_2')


def print_func_name_3():
    print('print_func_name_3')


def print_func_name_4():
    print('print_func_name_4')


def higher_order_func(func, n):
    for i in range(n):
        func()
