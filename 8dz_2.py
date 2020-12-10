class MyZeDiEr(Exception):
    def __init__(self, txt):
        self.txt = txt


def div(s_1, s_2):
    try:
        s_1, s_2 = int(s_1), int(s_2)
        if s_2 == 0:
            raise MyZeDiEr("Division by zero forbidden!!!")
        return round(s_1 / s_2, 3)
    except ValueError:
        return "Value Error"
    except MyZeDiEr as my:
        return my


print(div(input("Enter first number - "), input("Enter first second - ")))