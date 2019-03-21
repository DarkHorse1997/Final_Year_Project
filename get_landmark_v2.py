'''
===================================================
              Obtain Landmark Points 
===================================================
Author: Tanmoy Das
Email : tanmoydas1997@gmail.com


get_landmarks(path)

Parameters:	
path : string
    The file path to the input file which contains csv data 

Returns:	
p : list
    Vector of Landmark Points
'''
path_of_csv="/home/tanmoydas1997/Desktop/processed/s1_an_1.csv"
import numpy as np
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
    #print(p)
    print(len(p))
    print(len(p[0]))
    print(len(p[0][0]))
    return p
#print(ly)

#def aligned_landmark(p):
#    for i in range(5):



if __name__ == '__main__': 
  
    # Calling the function 
    p=get_landmark(path_of_csv) 
    p1=np.array(p)
    print(p1.shape)
    #print(p1)
    a=np.mean(p1,axis=0)
    print(a.shape)
    #print(a)
    b=np.mean(p1,axis=1)#THIS IS WHAT I NEED *PROBABLY*
    print(b.shape)
    #print(b)



''' Try to convert this into matrix form using numpy instead of using Python list.
List  structure : 68 indexes, each index j indexes(where j=no of frames/no of people in one frame),
in each index 2 points x and y coordinate.
'''

