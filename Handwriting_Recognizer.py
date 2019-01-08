import numpy as np
from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans

"""scikit-learn training dataset of handwritten digits of 30 Turkish men from 1998:"""
digits = datasets.load_digits()

"""Creating the clustering unsupervised model: Number of clusters is set to 10 (digits 0-9). A fixed state ensures that 
the model is build in the same way across multiple runs. This is important insofar as our model is not aware that the clusters represent the 0-9 digits. (This will be explained and visualized in detail later on.) As such the actual value of "random_state" is irrelevant as long as it is consistant:"""
model = KMeans(n_clusters=10, random_state=1)

"""Fitting the data to the model"""
model.fit(digits.data)

"""This function provides visualization of the cluster's centers look like in the data-fitted model. No matter the origin state of our KMeans model the cluster-centers conversion will be almost identical, however the order of the centers may vary. But we know that the cluster-centers represent digits 0 through 9, which is why we fix "random_state". As can be opserved if we run this function: the cluster-centers at "random_state = 1" represents as follows: 0,9,8,7,1,6,5,3,4,2. The function creates a subplot in matplotlib that desplies the array data as 8x8 binary color images, where one value in the array corresponds to one pixel in the image."""
def cluster_centers():
    fig = plt.figure(figsize=(10, 5))
    for i in range(10):
        axis_x = fig.add_subplot(2, 5, i + 1)
        axis_x.imshow(model.cluster_centers_[i].reshape((8, 8)), cmap=plt.cm.binary)
    return plt.show()

# cluster_centers()

new_sample = np.array([])