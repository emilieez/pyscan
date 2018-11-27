import numpy as np
import trimesh as tmesh
from random import choice
import matplotlib.pyplot as plt
import os
import pandas as pd
import zipfile
from sklearn import preprocessing


class ModelClassifier:
    """ Uses the trimesh and matplotlib libraries to extract data for model classification
        numpy is used to measure distances between any two points in 3 dimensional space as well as
        to compare histograms for classification
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
        self.existing_data = []

    def classify(self):
        """ Main function to generate user input data which is then compared to existing data 
            from the training_data.csv file

            Areas of improvement:
                - 3D Models are not scaled to match the comparisons size
                - Data is currently limited to a single cube and rectangle for comparisons
        """
        self.data = preprocessing.scale(self.generate_distribution_data(self.mesh_object.vertices))
        self.results = self.compare_models(self.data)

    def compare_models(self, data):
        """ Compares histograms by determining how much the two graphs intersect
        
        Arguments:
            data {List} -- contains a list of various distances taken between numerous random points
        
        Returns:
            Tuple -- a tuple containing the final results of the comparisons 
        """

        # Loads data from training_data.csv file
        file_data = self._get_shape_data()
        best_match = 0
        matching_shape = ''

        # Loop through file_data to find the best matching shape for the input scan
        for shape in file_data:

            # Convert list entries to float from strings
            compared_data = preprocessing.scale([float(i.strip()) for i in shape[1].split(',')])

            # Create histograms
            classify_data, _ = np.histogram(compared_data, bins=40)
            loaded_file_data, _ = np.histogram(data, bins=40)

            # Compare histograms
            minima = np.minimum(classify_data, loaded_file_data)
            intersection = np.true_divide(
                np.sum(minima), np.sum(loaded_file_data))

            if best_match == 0:
                matching_shape = shape[0]
                best_match = intersection * 100

            if intersection * 100 >= best_match:
                matching_shape = shape[0]
                best_match = intersection * 100
                self.existing_data = compared_data

        return matching_shape, best_match

    def generate_distribution_data(self, vertices):
        """ Generate enough data for precise model comparisons
        
        Arguments:
            vertices {List} -- a nested list containing the vertices of the loaded model object
        
        Returns:
            List -- a list containing distances measured between any two random vertices
        """

        distribution_data = []
        for b in range(1024):
            for i in range(1024 ^ 2):
                distribution_data.append(self._calc_length(vertices))
        return distribution_data

    def _calc_length(self, vertices):
        """ Measures the distance between two random points in 3 dimensional space. 
            No two points are measured twice to ensure more useful data is collected.

            Can be improved to measure the area of a triangle between any 3 random points.
        
        Arguments:
            vertices {List} -- a nested list containing the vertices of the loaded model object
        
        Returns:
            Float -- a distance between two points in 3 dimensional space
        """

        used_coordinate_pairs = []
        first_rand_vertex = choice(vertices)
        second_rand_vertex = choice(vertices)

        while True:
            if set(first_rand_vertex).intersection(second_rand_vertex) != 3:
                if [first_rand_vertex, second_rand_vertex] not in used_coordinate_pairs:
                    used_coordinate_pairs.append(
                        [first_rand_vertex, second_rand_vertex])
                    break
                else:
                    first_rand_vertex = choice(vertices)
                    second_rand_vertex = choice(vertices)
            else:
                first_rand_vertex = choice(vertices)
                second_rand_vertex = choice(vertices)

        distance = self._get_euclidean_distance(
            first_rand_vertex, second_rand_vertex)

        return distance * 100

    @staticmethod
    def _get_shape_data():
        """ Opens a file containing dimensions of previously scanned objects
        
        Returns:
            List -- contains list data of previous objects created from generate_distribution_data
        """
        try:
            with open(os.path.join(os.path.dirname(__file__), "training_data.csv"), 'r') as data:
                file_data = pd.read_csv(data, header=None)
                return list(file_data.values)
        except FileNotFoundError:
            zip_ref = zipfile.ZipFile(os.path.join(
                os.path.dirname(__file__), "training_data.zip"), "r")
            zip_ref.extractall(os.path.dirname(__file__))
            zip_ref.close()
            with open(os.path.join(os.path.dirname(__file__), "training_data.csv"), 'r') as data:
                file_data = pd.read_csv(data, header=None)
                return list(file_data.values)

    @staticmethod
    def show_histogram(data1, data2, shape):
        """ Displays a histogram that visualizes the comparison between the two
        histograms
        
        Arguments:
            data1 {List} -- Existing Data: contains list data of previous objects created from generate_distribution_data
            data2 {List} -- New Input Data: contains list data of previous objects created from generate_distribution_data
            shape {String} -- Name of the object the input scan is being compared to
        """

        plt.hist(data1, histtype='step', bins=40, color='blue', label=shape)
        plt.hist(data2, histtype='step', bins=40, color='red', label='Input Scan')
        plt.title('Shape Distribution Graph')
        plt.ylabel('Probability')
        plt.xlabel('Distance')
        plt.legend()
        plt.show()

    @staticmethod
    def _get_average(lst):
        """ Returns the average of a List
        
        Arguments:
            lst {List} -- a 1 dimensional list containing numbers
        
        Returns:
            Float -- average number of the input list
        """

        return sum(lst) / len(lst)

    @staticmethod
    def _get_euclidean_distance(a, b):
        """ Measures the distance between two points in 3D space
        
        Arguments:
            a {List} -- contains X, Y, and Z coordinates
            b {List} -- contains X, Y, and Z coordinates
        
        Returns:
            Float -- distance value calculated between two points
        """

        return np.linalg.norm(a - b)


if __name__ == "__main__":
    mesh = ModelClassifier(
        './scans/test_scans/Cube_Test01_BoxSize_Small(0).obj')
    mesh.classify()
