from .ModelClassifier import ModelClassifier
import os
import pandas as pd


def write_to_file(open_type, file_location):
    """
    Download files to the scans folder before running. This will allow for more objects to be classified
    and for more precise comparisons

    Disclaimer: This function will take a long time to run!
    :return:
    """
    temp_list = []
    training_files = os.listdir(file_location)
    for file in training_files:
        test_model = ModelClassifier(os.path.join(os.path.join(os.path.dirname(__file__), "scans"), file))
        hist_data = test_model.generate_distribution_data(test_model.mesh_object.vertices)
        shape_name = file.split("_")
        temp_list.append([shape_name[0], ','.join(map(str, hist_data))])
    with open("training_data.csv", open_type) as training_data:
        writer = csv.writer(training_data)
        for line in temp_list:
            writer.writerow(line)


def read_from_file():
    """
    This is just a test function to determine how the file data will be manipulated or
    if the data was stored correctly
    :return:
    """
    with open("training_data.csv", 'r') as data:
        file_data = pd.read_csv(data, header=None)
        for i in list(file_data.values):
            print(len(i[1].split(',')))

if __name__ == '__main__':
    write_to_file('w', './scans')
    #read_from_file()