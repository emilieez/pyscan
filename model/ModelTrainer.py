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
"""

def train_svc():
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
    mesh = ModelClassifier(os.path.join(os.path.join(os.path.dirname(__file__), "scans"), "Hand.obj"))
    hist_data = preprocessing.scale(mesh.generate_distribution_data(mesh.mesh_object.vertices))

    with open("trained_data.pkl", "rb") as dump_file:
        classifier = p.load(dump_file)
        print("It is a {}!".format(classifier.predict([hist_data])[0]))


if __name__ == '__main__':
    #train_neighbors()
    prediction()
