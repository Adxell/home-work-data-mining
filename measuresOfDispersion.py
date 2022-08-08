import csv
from math import sqrt
from readExcel import readExcel


input = open('./Outliers.csv', 'r')

csv_read = csv.reader(input, dialect='excel')


response = readExcel(csv_read)
data = response[0]
MEAN = response[1]
n = response[2]

RESULT = 0
for i in range(0, len(data)):
    numerator = (data[i]-MEAN)
    RESULT = RESULT + pow(numerator, 2)


standard_deviation = sqrt(RESULT/(n-1))

critical_poinst = []

for i in range(0, len(data)):
    distance = abs(data[i]-MEAN)
    if(distance/standard_deviation > 2.807):
        critical_poinst.append(data[i])
print(standard_deviation)





