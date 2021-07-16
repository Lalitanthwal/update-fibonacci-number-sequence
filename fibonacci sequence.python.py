# write a program for fibonacci sequence:o,1,1,2,3,5,8,13,21,34,55,89,144... ... ..
def fibonacci(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return fibonacci(i-2) + fibonacci(i-1)
for x in range(13):
    print(fibonacci(x))    
