from Death_cases import *


fileName = "allData.csv"
numfile = "num.csv"

if os.path.exists(fileName):
    os.remove(fileName)


baseURL = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/"


def loadData(fileName, columnName): 
    data = pd.read_csv(baseURL + fileName) \
             .drop(['Lat', 'Long'], axis=1) \
             .drop(['Province/State'], axis=1) \
             .melt(id_vars=['Country/Region'], var_name='date', value_name=columnName) \
             .astype({'date':'datetime64[ns]', columnName:'Int64'}, errors='ignore')
    data[columnName].fillna(0, inplace=True)
    return data

def refreshData():
    allData = loadData("time_series_covid19_recovered_global.csv", "CumRecovered")
    allData.to_csv(fileName)
    return allData

def allData():
    if not isfile(fileName):
        refreshData()
    allData = pd.read_csv(fileName)
    return allData

countries = allData()['Country/Region'].unique()
countries.sort()

with open(fileName, 'r') as f:
    rows = f.read().split('\n')
rows_containing_keyword = [row for row in rows if 'India' in row]
# create and write lines to output file
with open(fileName, 'w+') as f:
    f.write('\n'.join(rows_containing_keyword))

## remove unwanted data
in_file = open(fileName, "r")
out_file = open("recovered.csv", "w", newline="")
in_csv = csv.reader(in_file)
out_csv = csv.writer(out_file)
row_count = 0
for row_number, row in enumerate(in_csv):
    row_count += 1
    n = row_count - 48
    if row_number > 47:
        out_csv.writerow(row[3:])
in_file.close()
out_file.close()

#print (n)


def createList(r1, r2): 
    return list(range(r1, r2+1))
r1, r2 = 1, n

a_list = createList(r1, r2)
list1 =  [element * 1.0 for element in a_list]
#print(z)

d = [list1]
export_data = zip_longest(*d, fillvalue = '')
with open(numfile, 'w', newline='') as myfile:
      wr = csv.writer(myfile)
      wr.writerows(export_data)
myfile.close()