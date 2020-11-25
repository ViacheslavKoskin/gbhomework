from random import randint

with open("text.txt", "w", encoding="utf-8") as my_file:
    my_list = [randint(1, 100) for _ in range(100)]
    my_file.write(" ".join(map(str, my_list)))

print(f"Sum of elements - {sum(my_list)}")