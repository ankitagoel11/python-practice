import pytest



def fizzbuzz(n):
    list_return =[]
    for x in range(1,n+1):
        if x%3 ==0 and x%5 == 0:
            list_return.append('fizzbuzz')
        elif x%3 == 0:
            list_return.append('fizz')
        elif x%5 == 0:
            list_return.append('buzz')
        else:
            list_return.append(str(x))
    return list_return

print(fizzbuzz(25))



    