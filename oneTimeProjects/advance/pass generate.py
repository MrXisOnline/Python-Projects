import random

ex = [
    ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", ",m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
     "w", "x", "y", "z", ],
    ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", ",M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
     "W", "X", "Y", "Z", ],
    ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"],
    ["!", "@", "#", "$", "&"]
    ]
'''
seq = [
    random.choice("abcdefghijklmnopqrstuvwxyz"),
    random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
    random.choice("0123456789"),
    random.choice("@!#$&")
       ]
'''
pass_length = int(input("Enter Length : "))
passwd = ""
while pass_length != 0:
    r = random.randint(0, 3)
    passwd = passwd + random.choice(ex[r])
    pass_length -= 1

print(passwd)

# print(random.choice(ex))
