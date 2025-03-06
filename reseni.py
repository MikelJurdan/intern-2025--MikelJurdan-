import sys
import operator

# Načtení dat ze standardního vstupu
data = sys.stdin.read()
prvni_radek = sys.stdin.readline().strip()

dictionary = {prvni_radek}
operators = {
    "+": operator.add,
    "*": operator.mul
}

# for numbers in dictionary:
#     if " " in numbers:
print(operators["+"](dictionary))

