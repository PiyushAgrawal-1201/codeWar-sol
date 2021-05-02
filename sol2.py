# capitalize every word of any string
#trying to push from IntelliJ
def capWord(a):
    b = a.split()
    c=[]
    for i in b:
        c.append(i.capitalize())
    d = " ".join(c)
    return d

a= input("give a string")
print(capWord(a))