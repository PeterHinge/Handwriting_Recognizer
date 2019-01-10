# Handwiting_Recognizer
An unsupervised AI-algorithm that recognizes handwritten digits (0-9)

Utilizing scikit-learn's KMeans clustering algorithm to create an unsupervised AI that recognizes handwritten digits based on a data set also provided by scikit-learn. More information on the data set can be found here: http://archive.ics.uci.edu/ml/datasets/Optical+Recognition+of+Handwritten+Digits

In short running the main program (Handwriting_Recognizer) creates a model based on the given data, then provides a small window (PygameDraw) where the user can draw/write their own digit. The pixel of the drawing is then feeded back to the main program, which will make a prediction of the user's digit based on the established model.

TIPS for the user:
For the best result the user is advised to use the entire window and try to write their number as centered as possible.
The user might notice that the AI is more accurate at guessing some numbers (e.g. 0) than others (e.g. 1). 
It is possible to gain a illustration of the clusters which the AI pairs the user input against (in Handwriting_Recognizer.py uncomment "# cluster_centers()").
If the user attempts to based their digit on one of these clusters, chances are they will observe a significant improvement in the AI's accuracy.
