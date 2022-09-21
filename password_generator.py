import random


uppercase_letters = "ABCDEFGGIJKLMNOPQRSTUVWXYZ"
lowercase_letters = "abcdefghijklmnopqrstufwxyz"
digits = "0123456789"
symbols = " ~`! @#$%^&*()_-+={[}]|\\:;'<,>.?// "

upper, lower, nums, syms = True, True, True, True

all = "" 

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if nums:
    all += digits
if syms:
    all += symbols

lenght = 20
amount = 2

for x  in range(amount):
    password = "".join(random.sample(all, lenght))
    print(password)
