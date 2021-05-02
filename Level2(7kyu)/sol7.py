# list1 = [("passanger onboard","passanger deboard"),("passanger onboard","passanger deboard"),]
list1 = [[10,0],[3,5],[5,8]]

def number(list1):
    sum = 0
    for i in list1:
        s = i[0] - i[1]
        sum = sum + s

    return sum

print(number(list1))