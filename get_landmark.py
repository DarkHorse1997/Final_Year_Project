import pandas
data=pandas.read_csv("../processed/VID_20181113_133217.csv")
print(data.head())

lx=[]
ly=[]
p=[]
for i in range(68):
    s=" x_"+str(i)
    s1=" y_"+str(i)
    lx=[data[s][0],data[s1][0]]
    #lx.append(data[s][0])
    #ly.append(data[s1][0])
    p.append(lx)
#print(data.columns.values)
print(p)
print(len(p))
print(len(p[0]))
#print(ly)