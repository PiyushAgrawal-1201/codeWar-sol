# capitalize every word of any string

def capWord(a):
    b = a.split()
    c=[]
    for i in b:
        c.append(i.capitalize())
    d = " ".join(c)
    return d

a= input("give a string")
print(capWord(a))
