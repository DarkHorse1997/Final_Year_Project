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
    for j in range(data.shape[0]):
        for i in range(68):
            s=" x_"+str(i)
            s1=" y_"+str(i)
            
                
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
    print(p[0][0][1])

    return p
#print(ly)

#def aligned_landmark(p):
#    for i in range(5):

def plot_landmark(frame,frame_no=-1):
    import matplotlib.pyplot as plt
    for i in range(len(frame)):
        x=frame[i][0]
        y=frame[i][1] #***Figure out why flipped in y-axis necessitating this -(minus) sign***
        #plt.text(x,y,i,ha="center", va="center",fontsize=8)
        plt.scatter(x,y,c='r', s=10)
    ax=plt.gca()
    ax.invert_yaxis()    
    plt.show()


def plot_landmark_on_frame(frame,path_of_image):
    import matplotlib.pyplot as plt
    im=plt.imread(path_of_image)
    implot = plt.imshow(im)
    #plt.show()
    
    for i in range(len(frame)):
        x=frame[i][0]
        y=frame[i][1]
        plt.text(x,y,i,ha="center", va="center",fontsize=8)
        plt.scatter(x,y,c='r', s=40)
    plt.show()   

if __name__ == '__main__': 
  
    # Calling the function 
    p=get_landmark(path_of_csv) 
    p1=np.array(p)
    print(p1.shape)
    #print(p1)
    mean_of_landmark=np.mean(p1,axis=0)
    print(mean_of_landmark.shape)
    #print(a)
    b=np.mean(p1,axis=1)
    print(b.shape)
    for i in range(len(p)):
        plot_landmark(p[i])
        path="/home/tanmoydas1997/Desktop/final_year/Frames/frame"+str(i)+".jpg"
        plot_landmark_on_frame(p[i],path)
    #print(b)



''' Try to convert this into matrix form using numpy instead of using Python list.(Done)
List  structure : 68 indexes, each index j indexes(where j=no of frames/no of people in one frame),
in each index 2 points x and y coordinate.
'''