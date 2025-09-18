n = int(input("Введите число:"))


def fizz_buzz(n):
        if n % 3 == 0:
           print(f"Fizz")
        if n % 5 == 0:
           print(f"Buzz")
        if n % 15 == 0: # или i % 3 == 0 and i % 5 == 0:
           print(f"FizzBuzzz")
        else:
           print(n)   


fizz_buzz(n)


# не понимаю почему у меня выводятся не только слова, но и сами цифры