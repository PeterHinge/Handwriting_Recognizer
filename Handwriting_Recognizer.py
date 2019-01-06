import numpy as np
from matplotlib import pyplot as plt
from sklearn import datasets

digits = datasets.load_digits()

print(digits.DESCR)
print(digits.data)
