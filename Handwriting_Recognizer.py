import numpy as np
from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans

# scikit-learn training dataset of handwritten digits of 30 Turkish men from 1998:
digits = datasets.load_digits()

# Creating the clustering unsupervised model - number of clusters is set to 10 (digits 0-9):
model = KMeans(n_clusters=10, random_state=1)

# Fitting the data to the model:
model.fit(digits.data)
