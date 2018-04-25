def counter(a, b):
    a_str = list(str(a))
    b_str = list(set(str(b)))
    count = 0
    for i in b_str:
        if i in a_str:
            count +=1

    return(count)


print (counter(12345, 567))
print (counter(1233211, 12128))
print (counter(123, 45))

