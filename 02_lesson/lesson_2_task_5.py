def month_to_season(month):
    if month in [12, 1, 2]:
        return "Зима"
    elif month in [3, 4, 5]:
        return "Весна"
    elif month in [6, 7, 8]:
        return "Лето"
    elif month in [9, 10, 11]:
        return "Осень"
    else:
        return None

try:
    month = int(input("Введите номер месяца (1-12): "))
    result = month_to_season(month)
    print(f"Сезон: {result}" if result else "Ошибка: число должно быть от 1 до 12!")
except ValueError:
    print("Ошибка: введите целое число!")
