from Plotter import *

numfile = "num.csv"
total_csv= "confirm.csv" 
row_count = 0
with open(numfile, newline='') as f:
    reader = csv.reader(f)
    Days = list(reader)

with open(total_csv) as csvfile:
    tlines = [line.split("\n", ) for line in csvfile.readlines()]
    
    Cases = [" ".join(line) for line in tlines]


x=datetime.today()
y=x.replace(day=x.day+1, hour=6, minute=40, second=40, microsecond=0)
delta_t=y-x

secs=delta_t.seconds+1

def hello_world():
    import covid_data
    #...

t = Timer(secs, hello_world)
t.start()

with open(numfile,"r") as f:
    reader = csv.reader(f,delimiter = ",")
    data = list(reader)
    row_count = len(data)


dev = "/"
bt = "are"
on = "Predicted Cases On Selected Date : "

#print(Cases)