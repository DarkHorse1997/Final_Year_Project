import numpy as np
from scipy.spatial import distance
import os
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
sns.set()

path="dataset/s1_an_1.avi"

def convert_xy_to_points(centroid_x,centroid_y):
    l=[]
    l11=[]
    centroid=[]
    for i in range(centroid_x.shape[0]):
        for j in range(centroid_x.shape[1]):
            l=[centroid_x[i,j],centroid_y[i,j]]
            #print(l)
            l11.append(l)
            #print(l11)
            #print("\n\n")
        centroid.append(l11)
        l11=[]

    cent=np.array(centroid)
    print(cent.shape)
    return cent
    #print(cent)


#z = scipy.spatial.distance.cdist(A,B,'chebyshev')
def find_distance(cent,no_of_clusters,distance_type,path):
    print(f"Finding {distance_type} distance between key points for {path[path.find('/')+1:]} ")
    
    distance_vector = []  
    print(cent[1].shape)
    for i in range(0,no_of_clusters-1,1):
        print(f"Calculating distance matrix between key-frame {i} and key-frame {i+1}")
        #print(cent[i])
        y = distance.cdist(cent[i],cent[i+1],distance_type)
        #print(y)
        print(y.shape)
        distance_vector.append(np.diag(y))
        #print(np.diag(y))
        
    #print(np.array(distance_vector))

    np.savetxt(path + "/displacement_vector.out",distance_vector)
    return np.array(distance_vector)


def plot_displacement(displacement):
    print(displacement.shape)
    x = range(5)
    t1=[]
    for i in range(68):
        t1.append(f'landmark_{i}')
    t2=[]

    for i in range(5):
        t2.append(f'frame {i} - {i+1}')    
    a = pd.DataFrame(data=displacement,index=t2,columns=t1)
    a = a.reset_index()
    print(a)
    #sns.lineplot(data=a)
    ax = sns.lineplot(data = a.reset_index(), x = 'index', y = 'landmark_0')
    #ax=plt.gca()
    #for i in range(68):

        #y=displacement[:, 0]
        #a.plot(y=f'landmark_{i}',ax=ax)
    return ax    
    

if __name__ == '__main__': 

    
    video_file_list=os.listdir("dataset")

    video_list = list(filter(lambda x: not(x.endswith('.avi')), video_file_list))
    print(f"List of videos: {video_list}")
    for filename in video_list:
        path = "dataset/" + filename 
        print(path)   
        centroid_x = np.loadtxt(path + '/centroid_x.out')
        centroid_y = np.loadtxt(path + '/centroid_y.out')
        cent = convert_xy_to_points(centroid_x,centroid_y)
        p1 =  np.load(path + '/landmark_points_array.out.npy')
        displacement=find_distance(cent,cent.shape[0],'euclidean',path)
        ax = plot_displacement(displacement)

    plt.show()




    