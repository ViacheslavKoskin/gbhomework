#Представлен список чисел. Определить элементы списка, не имеющие повторений.
#Сформировать итоговый массив чисел, соответствующих требованию.
#Элементы вывести в порядке их следования в исходном списке.
#Для выполнения задания обязательно использовать генератор.

from random import randint

my_list = [randint(-10, 10) for _ in range(20)]
uniq_list = [el for el in my_list if my_list.count(el) == 1]
print(f"Source list\n{my_list}\nNo repetition list\n{uniq_list}")