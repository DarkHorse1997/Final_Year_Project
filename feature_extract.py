path_of_csv="../processed/multi.csv"
def get_landmark(path):
    import pandas

    data=pandas.read_csv(path_of_csv)
    #print(data.head())

    l1=[]
    l2=[]
    p=[]
    for i in range(68):
        s=" x_"+str(i)
        s1=" y_"+str(i)
        for j in range(len(data[s])):
            
            l1=[data[s][j],data[s1][j]]
            l2.append(l1)
        #lx.append(data[s][0])
        #ly.append(data[s1][0])
        p.append(l2)
        l2=[]
    #print(data.columns.values)
    print(p)
    print(len(p))
    print(len(p[0]))

    return p

