import math


def square(items):
    return math.ceil(items*items)


num_items = int("Введите сторону квадрата: ")
print(f"Площадь квадрата: {square(num_items)}")


# как переданный аргумент может быть не целым,
#  если принимает только целое 
# число?
