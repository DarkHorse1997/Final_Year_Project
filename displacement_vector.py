import numpy as np
from scipy.spatial import distance
import os

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
def find_distance(p1,cent,no_of_clusters,distance_type):
    
    leng=p1.shape[0]
    
    for i in range(no_of_clusters):

        dist=[]
        for j in range(leng):
            y = distance.cdist(p1[j],cent[i],distance_type)
            print(y.shape)
            #print(np.sum(np.diag(y)))
            #dist.append(np.trace(y))
            #print(str(i)+"  "+str(np.trace(y)))
        #dd=np.array(dist)
        #minframe.append(np.argmin(dd))
    #print(minframe)
    #return minframe
    



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
        find_distance(p1,cent,cent.shape[0],'euclidean')




    