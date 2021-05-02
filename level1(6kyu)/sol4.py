# Sum of natural numbers divisible by 3 and 5
number = 10
def solution(number):
    list1 = []
    if number<0:
        return 0
    else:
        for i in range(1,number):
            if i%3 == 0 or i%5 ==0:
                list1.append(i)
            else:
                continue
        print(list1)
    return sum(list1)

print(solution(number))