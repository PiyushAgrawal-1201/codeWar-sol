#next square number

from math import sqrt
def find_next_square(sq):
    if int(sqrt(sq)) == sqrt(sq):
        a = sqrt(sq) + 1
        return int(a*a)
    else:
        return -1

sq = int(input("give a number"))
print(find_next_square(sq))