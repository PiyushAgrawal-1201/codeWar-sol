# return number of repeated letters(case in-sensitive) or numbers from a string.

text = input("input any thing")

def duplicate_count(text):
    a= text.upper()
    b = set(a)
    l=list(b)
    print(b)
    c=0
    for i in range(len(l)):
        if a.count(l[i]) > 1:
            c+=1

    return c


print(duplicate_count(text))