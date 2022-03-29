from lib2to3.pytree import LeafPattern


letters= "abcdefghijklmnopqrstuvwxyz"

backward= letters[25::-1]
backward= letters[::-1]
print(backward)

print(letters[16:13:-1])
# slice the string to produce edcba
print(letters[4::-1])
print(letters[:-9:-1])

print(letters[-4:])
print(letters[1:])
print(letters[-2:])
print(letters[:1])
print(letters[:-25])