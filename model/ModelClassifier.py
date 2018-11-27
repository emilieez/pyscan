import numpy as np
import trimesh as tmesh
from random import choice
import matplotlib.pyplot as plt
import os


class ModelClassifier:
    """ Uses the trimesh and matplotlib libraries to extract data for model classification
    """

    def __init__(self, model):
        """ Loads the .ply file for processing
        
        Arguments:
            model {file path} -- file path of the .ply file
        """
        self.filename = model
        self.mesh_object = tmesh.load(model)
        self.results = []
        self.data = []
        self.existing_data =[]

    def classify(self):
        #  TODO: Add model Scaling
        #  TODO: Add averages from multiple cube files for comparison
        #  TODO: Documentation
        self.data = self.generate_distribution_data(self.mesh_object.vertices)
        self.results = self.compare_models(self.data)

    def compare_models(self, data):
        file_data = self._get_shape_data()
        self.existing_data = [float(i) for i in file_data[1:len(file_data)]]
        classify_data, _ = np.histogram(self.existing_data, bins=40)
        loaded_file_data, _ = np.histogram(data, bins=40)

        minima = np.minimum(classify_data, loaded_file_data)
        intersection = np.true_divide(np.sum(minima), np.sum(loaded_file_data))

        return file_data[0], intersection * 100

    def generate_distribution_data(self, vertices):
        distribution_data = []
        for b in range(1024):
            for i in range(1024 ^ 2):
                distribution_data.append(self._calc_length(vertices))
        return distribution_data

    def _calc_length(self, vertices):
        used_coordinate_pairs = []
        first_rand_vertex = choice(vertices)
        second_rand_vertex = choice(vertices)

        while True:
            if set(first_rand_vertex).intersection(second_rand_vertex) != 3:
                if [first_rand_vertex, second_rand_vertex] not in used_coordinate_pairs:
                    used_coordinate_pairs.append([first_rand_vertex, second_rand_vertex])
                    break
                else:
                    first_rand_vertex = choice(vertices)
                    second_rand_vertex = choice(vertices)
            else:
                first_rand_vertex = choice(vertices)
                second_rand_vertex = choice(vertices)

        distance = self._get_euclidean_distance(first_rand_vertex, second_rand_vertex)

        return distance * 100

    @staticmethod
    def show_histogram(data1, data2):
        plt.hist([data1, data2], histtype='step', bins=40)
        plt.title('Shape Distribution Graph')
        plt.ylabel('Frequency')
        plt.xlabel('Distance')
        plt.show()

    @staticmethod
    def _get_average(lst):
        return sum(lst) / len(lst)

    @staticmethod
    def _get_euclidean_distance(a, b):
        return np.linalg.norm(a - b)

    @staticmethod
    def _get_shape_data():
        with open(os.path.join(os.path.dirname(__file__), "training_data.txt"), 'r') as data:
            lines = data.readlines()
            split_lines = lines[0].split(",")
            return split_lines


if __name__ == "__main__":
    mesh = ModelClassifier('./scans/test_scans/Cube_Test01_BoxSize_Small(0).obj')
    mesh.classify()
