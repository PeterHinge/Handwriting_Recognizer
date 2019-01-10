import numpy as np
from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans


"""scikit-learn training dataset of handwritten digits of 30 Turkish men from 1998:"""
digits = datasets.load_digits()


"""Creating the clustering unsupervised model: Number of clusters is set to 10 (digits 0-9). 
A fixed state ensures that the model is build in the same way across multiple runs. 
This is important insofar as our model is not aware that the clusters represent the 0-9 digits. 
(This will be explained and visualized in detail later on.) 
As such the actual value of "random_state" is irrelevant as long as it is consistent:"""
model = KMeans(n_clusters=10, random_state=1)


"""Fitting the data to the model"""
model.fit(digits.data)


"""This function provides visualization of the cluster's centers look like in the data-fitted model. 
No matter the origin state of our KMeans model the cluster-centers conversion will be almost identical, 
however the order of the centers may vary. But we know that the cluster centers represent digits 0 through 9, 
which is why we fix "random_state". As can be bif we run this function: the cluster-centers at "random_state = 1" 
represents as follows: 0,9,8,7,1,6,5,3,4,2. The function creates a subplot in matplotlib that displays 
the array data as 8x8 binary color images, where one value in the array corresponds to one pixel in the image."""
def cluster_centers():
    fig = plt.figure(figsize=(10, 5))
    for i in range(10):
        axis_x = fig.add_subplot(2, 5, i + 1)
        axis_x.imshow(model.cluster_centers_[i].reshape((8, 8)), cmap=plt.cm.binary)
    return plt.show()


"""Uncomment to display cluster centers."""
# cluster_centers()


"""This is gonna receive array data from a drawing Pygame application so the user can draw/write their own number 
and the algorithm will predict what number was drawn."""
new_sample = np.array(
    []
)


"""Reshapes sample (a 1 dimensional array) to fit the model (fitted for a 2 dimensional array)."""
new_sample = new_sample.reshape(1, -1)


"""A prediction of the sample is made based on which cluster mostly resembles the data input."""
new_label = model.predict(new_sample)


"""To get the right number a translation is needed in order to account for our models random_state. 
The translation would have looked different if another value for random_state was chosen."""
def translation(new_label):
    if new_label == 0:
        return 0
    elif new_label == 1:
        return 9
    elif new_label == 2:
        return 8
    elif new_label == 3:
        return 7
    elif new_label == 4:
        return 1
    elif new_label == 5:
        return 6
    elif new_label == 6:
        return 5
    elif new_label == 7:
        return 3
    elif new_label == 8:
        return 4
    elif new_label == 9:
        return 2


"""The predicted digit."""
new_digit = translation(new_label)
print(new_digit)
