# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

time = int(input("Введите время в секнудах: "))

hours_rez = time // 360
hours_ost = time % 360
minute_rez = hours_ost // 60
sec_rez = hours_ost % 60

print(f"{hours_rez}:{minute_rez}:{sec_rez}")
