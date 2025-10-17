
try:
    lst=[5,4,6,7]
    lst[10]
except IndexError:
    print("something is wrong")
print(lst)