class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


my_list = []

while True:
    inp_data = input("Введите число: ")
    if inp_data == "":
        break
    try:
        if inp_data.replace("-", "").replace(".", "").isdigit():
            my_list.append(float(inp_data))
        else:
            raise OwnError("введено не число")
    except OwnError as err:
        print(err)
        continue

print(my_list)