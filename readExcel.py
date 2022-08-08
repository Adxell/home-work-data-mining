def readExcel(inputExcel):
    data = []
    SUMVALUES = 0
    n = 0
    for line in inputExcel:
        value= int(line[0])
        data.append(value)
        SUMVALUES = SUMVALUES + value
        n = n + 1
    MEAN = SUMVALUES/n
    return [data, MEAN, n]