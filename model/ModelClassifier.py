import numpy as np
import trimesh as tmesh
from random import choice
import matplotlib.pyplot as plt
import os


class ModelClassifier:
    """ Uses the trimesh and matplotlib libraries to extract data for model classification
    """

    def __init__(self, model):
        """ Loads the model file for processing
            Currently compatible with .obj and .ply files
        
        Arguments:
            model {file path} -- file path of the model file
        """
        self.filename = model
        self.mesh_object = tmesh.load(model)
        self.results = []
        self.data = []
        self.existing_data =[]

    def classify(self):
        #  TODO: Add model Scaling
        self.data = self.generate_distribution_data(self.mesh_object.vertices)
        self.results = self.compare_models(self.data)

    def compare_models(self, data):
        file_data = self._get_shape_data()
        best_match = 0
        matching_shape = ''
        for shape in file_data:
            compared_data = [float(i.strip()) for i in shape[1:len(shape)]]
            classify_data, _ = np.histogram(compared_data, bins=40)
            loaded_file_data, _ = np.histogram(data, bins=40)

            minima = np.minimum(classify_data, loaded_file_data)
            intersection = np.true_divide(np.sum(minima), np.sum(loaded_file_data))

            if best_match == 0:
                matching_shape = shape[0]
                best_match = intersection * 100

            if intersection * 100 >= best_match:
                matching_shape = shape[0]
                best_match = intersection * 100
                del self.existing_data[:]
                self.existing_data = compared_data

        return matching_shape, best_match

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
    def _get_shape_data():
        with open(os.path.join(os.path.dirname(__file__), "training_data.txt"), 'r') as data:
            lines = data.readlines()
            temp = []
            for l in lines:
                split_lines = l.split(",")
                temp.append(split_lines)
            return temp

    @staticmethod
    def show_histogram(data1, data2, shape):
        plt.hist(data1, histtype='step', bins=40, color='green', label=shape)
        plt.hist(data2, histtype='step', bins=40, color='red', label='Input Scan')
        plt.title('Shape Distribution Graph')
        plt.ylabel('Probability')
        plt.xlabel('Distance')
        plt.legend()
        plt.show()

    @staticmethod
    def _get_average(lst):
        return sum(lst) / len(lst)

    @staticmethod
    def _get_euclidean_distance(a, b):
        return np.linalg.norm(a - b)


if __name__ == "__main__":
    mesh = ModelClassifier('./scans/test_scans/Cube_Test01_BoxSize_Small(0).obj')
    mesh.classify()
