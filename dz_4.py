# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.

m_count = int(input("Число: "))

ost = m_count % 10
cel = m_count // 10

while ost < cel:
    cel = cel // 10
    ost = cel % 10
else:
    print(ost)
