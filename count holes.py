dict = {'0': 1, '1': 0, '2': 0, '3': 0, '4': 1, '5': 0, '6': 1, '7': 0, '8': 2, '9': 1}

def count_holes(n):
    count = 0
    if isinstance(n, int):
        n = abs(n)
    elif isinstance(n, float):
        return 'Error'

    try:
        int (n)
    except ValueError:
        #print('Error')
        return 'Error'
    #print (n)
    n = str(n)

    for i in n:
        if dict[i]>0:
            count +=1
    return count



print (count_holes('123'))
print (count_holes(906))
print (count_holes('001'))
print (count_holes(-8))
print (count_holes(-8.0))
print (count_holes('asas'))