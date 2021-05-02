#create phn number in format (123) 456-7890
n = [1,2,3,4,5,6,7,8,9,0]
def create_phone_number(n):
    listToStr = ''.join(map(str, n))  #converts list of int to string
    print(listToStr)
    a = "("+listToStr[0:3]+") "+listToStr[3:6]+"-"+listToStr[6:10]
    return a


print(create_phone_number(n))
