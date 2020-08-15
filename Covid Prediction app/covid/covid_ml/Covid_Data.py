from Death_cases import *

numfile = "num.csv"
total_csv= "confirm.csv"
death_csv = "Death.csv"
recovered_csv = "recovered.csv"
allData = "alldata.csv"
Date_csv = "Date.csv"
with open(numfile, newline='') as f:
    reader = csv.reader(f)
    Days = list(reader)

with open(total_csv) as csvfile:
    tlines = [line.split("\n", ) for line in csvfile.readlines()]
    Cases = [" ".join(line) for line in tlines]

with open(death_csv) as csvfile:
    tlines = [line.split("\n", ) for line in csvfile.readlines()]
    Death = [" ".join(line) for line in tlines]

with open(recovered_csv) as csvfile:
    tlines = [line.split("\n", ) for line in csvfile.readlines()]
    Recover = [" ".join(line) for line in tlines]

with open("Date.csv") as csvfile:
    tlines = [line.split("\n", ) for line in csvfile.readlines()]
    Date = [" ".join(line) for line in tlines]

#print("\n S.no =",Days)
#print("\n total cases = ",Cases)
#print("\n recover = ",recover)
#print("\n deaths = ",Death)

ded = Death
day = Date
rec = Recover
cas = Cases

f = open("alldata.csv", "w")

for i in range(len(day)):
    f.write("{},{},{},{}\n ".format(day[i], ded[i], rec[i], cas[i]))

f.close()

import csv
with open(allData,newline='') as f:
    r = csv.reader(f)
    data = [line for line in r]
with open('Data.csv','w',newline='') as f:
    w = csv.writer(f)
    w.writerow(['Day','Dead','Recover','Total Case'])
    w.writerows(data)




