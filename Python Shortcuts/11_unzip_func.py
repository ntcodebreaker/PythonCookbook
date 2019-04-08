def unzip(p, n):
    quotient, remainder = divmod(len(p), n)

    if remainder != 0:
        quotient += 1

    lst = [[None] * quotient for i in range(n)]
    
    for i in range(len(p)):
        j, k = divmod(i, n)
        lst[k][j] = p[i]
    # print(lst)
    return map(tuple, lst)



lst = [n for n in range(10)]

unzipped = unzip(lst, 2)

for item in unzipped: print(item)

