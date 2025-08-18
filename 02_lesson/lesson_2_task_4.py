n = int(input("Введите число:"))


def fizz_buzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0:
           print(f"Fizz")
        if i % 5 == 0:
           print(f"Buzz")
        if i % 15 == 0: # или i % 3 == 0 and i % 5 == 0:
           print(f"FizzBuzzz")
        else:
           print(i)   


fizz_buzz(n)


# не понимаю почему у меня выводятся не только слова, но и сами цифры