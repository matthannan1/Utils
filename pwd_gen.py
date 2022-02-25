import random

alphabet = "abcdefghijkmnopqrstuvwxyz23456789ABCDEFGHJKLMNPQRSTUVWXYZ!@#$%^&*()-=_+{}[]"
# pw_length = 8
pw_length = int(input("How many characters? "))
mypw = ""

for _ in range(pw_length):
    next_index = random.randrange(len(alphabet))
    mypw += alphabet[next_index]

print(mypw)
