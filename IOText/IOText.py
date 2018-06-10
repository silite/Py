for j in range(10):
    j = str(j)
    result = ''
    for i in range(1000):
        i = "%03d" % i
        i = str(i)
        if j in i:
            result += i + ','
    result = result[:-1]
    with open(j + '.txt', 'a') as f:
        f.write(result)