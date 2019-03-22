''' Snippet #1

    This is a code snippet from github issue dlib
    which converts dlib.vector class to numpy array
'''


def dlibVect_to_numpyNDArray(vector):
    array = np.zeros(shape=128)
   for i in range(0, len(vector)):
        array[i] = vector[i]
    return array


test_landmarks = dlibVect_to_numpyNDArray(face_descriptor)
dist = np.linalg.norm(database_landmarks - test_landmarks)


''' Snippet #2

    This code snippet is used in dlib_land.py in apply_kmeans() function
    to plot the k centroid clusters in a scatterplot. The axis is inverted 
    to make it analogous to a human face
'''


plt.scatter(centroid_x, centroid_y)
    ax = plt.gca()
    ax.invert_yaxis()
    plt.show()
