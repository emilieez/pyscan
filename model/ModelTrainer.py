from ModelClassifier import ModelClassifier
from sklearn import preprocessing, svm
from sklearn.neighbors import KNeighborsClassifier
import _pickle as p
import os
import pandas as pd

""" 
NOT IMPLEMENTED IN ModelClassifier 
Currently inaccurate compared to current histogram classifier algorithm
Machine Learning classifier requires more data to be accurate

Run csv_file_editor write_to_file before running one of the training algorithms
"""


def train_svc():
    """
    Uses the data in the object_data.csv file to train the classifier.
    Uses the Support Vector Classifier machine learning algorithm.
    :return:
    """
    temp_list = []
    names = []

    with open("object_data.csv", 'r') as csv_data:
        file_data = pd.read_csv(csv_data, header=None)
        new_data = list(file_data.values)

        for i in new_data:
            extracted_data = i[1].split(',')
            distance_data = preprocessing.scale([float(j.strip()) for j in extracted_data])
            temp_list.append(distance_data)
            names.append(i[0])
            print(i[0], "added")

    print("Training...")
    with open("trained_data.pkl", 'wb') as training_data:
        clf = svm.SVC(gamma='scale')
        clf.fit(temp_list, names)
        p.dump(clf, training_data)


def train_neighbors():
    """
    Uses the data in the object_data.csv file to train the classifier.
    Uses the Nearest Neighbors K-D Tree machine learning algorithm.
    :return:
    """
    temp_list = []
    names = []

    with open("object_data.csv", 'r') as csv_data:
        file_data = pd.read_csv(csv_data, header=None)
        new_data = list(file_data.values)

        for i in new_data:
            extracted_data = i[1].split(',')
            distance_data = preprocessing.scale([float(j.strip()) for j in extracted_data])
            temp_list.append(distance_data)
            names.append(i[0])
            print(i[0], "added")

    print("Training...")
    with open("trained_data.pkl", 'wb') as training_data:
        n = KNeighborsClassifier(n_neighbors=len(temp_list), algorithm="kd_tree", weights='distance')
        n.fit(temp_list, names)
        p.dump(n, training_data)


def prediction():
    """
    This is a test function for to output machine learned results. This can be implemented into the main classifier
    algorithm by using it to sort the data retrieved from the object_data.csv. This will only improve the speed
    of the classifier; it will not necessarily make it more accurate.

    For Example:
    1.) Load object_data.csv into a List
    2.) Make a prediction
    3.) Use prediction output to sort predicted values first in the list
    :return:
    """
    mesh = ModelClassifier(os.path.join(os.path.join(os.path.dirname(__file__), "scans"), "Hand.obj"))
    hist_data = preprocessing.scale(mesh.generate_distribution_data(mesh.mesh_object.vertices))

    with open("trained_data.pkl", "rb") as dump_file:
        classifier = p.load(dump_file)
        print("It is a {}!".format(classifier.predict([hist_data])[0]))


if __name__ == '__main__':
    #train_neighbors()
    prediction()
