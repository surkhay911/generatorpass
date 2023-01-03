import random


def generator(length: int, number: bool, simbol: bool, number_and_simbol: bool):
    a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
         'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    simbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', ';', ':', ',', '.', '/', '?', '\\',
               '|', '`', '~', '[', ']', '{', '}']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    s = ""
    for i in range(length):
        if number:
            s += random.choice(a+numbers)
        elif simbol:
            s += random.choice(a+simbols)
        elif number_and_simbol:
            s += random.choice(a+simbols+numbers)
        else:
            s += random.choice(a)
    return s


a = int(input("Введите кол-во символов="))
b = True
c = True
d = True 

count = int(input("Сколько паролей вам нужно?="))

for i in range(count):
    if __name__ == '__main__':
        print(generator(a, b, c, d))
