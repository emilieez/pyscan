from ModelClassifier import ModelClassifier
from sklearn import preprocessing, svm
import _pickle as p
import matplotlib.pyplot as plt
import os
import itertools

""" 
NOT IMPLEMENTED IN ModelClassifier 
Currently inaccurate compared to current histogram classifier algorithm
Machine Learning classifier requires more data to be accurate
"""

def train():
    temp_list = []
    names = []
    training_files = os.listdir('./training')

    for file in training_files:
        test_model = ModelClassifier(os.path.join(os.path.join(os.path.dirname(__file__), "training"), file))
        hist_data = preprocessing.scale(test_model.generate_distribution_data(test_model.mesh_object.vertices))
        hist = plt.hist(hist_data, bins=40)
        converted = list(itertools.chain.from_iterable([hist[0], hist[1]]))
        temp_list.append(converted)
        names.append(file.split("_")[0])
        print(file.split("_")[0], "added")

    print(len(names))
    print(len(temp_list))
    with open("trained_data.pkl", 'wb') as training_data:
        clf = svm.SVC(gamma='scale')
        clf.fit(temp_list, names)
        p.dump(clf, training_data)


def prediction():
    mesh = ModelClassifier(os.path.join(os.path.join(os.path.dirname(__file__), "scans"), "RectPrism_Test01_BestCase(0).obj"))
    hist_data = preprocessing.scale(mesh.generate_distribution_data(mesh.mesh_object.vertices))
    hist = plt.hist(hist_data, bins=40)
    converted = list(itertools.chain.from_iterable([hist[0], hist[1]]))

    with open("trained_data.pkl", "rb") as dump_file:
        clf = p.load(dump_file)
        print("It is a {}!".format(clf.predict([converted])[0]))


if __name__ == '__main__':
    #train()
    prediction()
