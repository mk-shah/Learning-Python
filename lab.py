
def swap_variable (x,y):
    print(f'Original value for variable 1: {x} \nOriginal value for variable 2: {y}')
    x,y = y,x
    print(f'New value for variable 1: {x} \nNew value for variable 2: {y}')


def compare_int(x,y):
    if x > y:
        print(f'Greater value is {x}')
    elif x < y:
        print(f'Greater value is {y}')
    else:
        print(f'Both are same')

def compare_str_len(x,y):
    if len(x) > len(y):
        print(f'String "{x}" is longer')
    elif len(x) < len(y):
        print(f'String "{y}" is longer')
    else:
        print(f'Both strings have same length')

def even_numbers(x):
    # for num in range(1,x):
    #     if num%2 == 0:
    #         print(num)

    # using list comprehension
    # even_num = [num for num in range(1, x) if num%2 == 0]
    # print(even_num)

    # using while loop
    i = 1
    while i < x:
        if i%2 == 0:
            print(i)
        i+= 1


def design_1(x):
    # for num in range(1,x+1):
    #     print(x*'*')

    # Using nested loop
    for col in range(x):
        print('*', end='')
        for row in range(x-1):
            print('*', end='')
        print()


def design_2(y):
    for col in range(y+1):
        print(col*'*')

swap_variable("hello", "world")
compare_int(10, 20)
compare_str_len("Juniper", "Networks")
even_numbers(101)
design_1(3)
design_2(5)

