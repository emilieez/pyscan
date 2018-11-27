from ModelClassifier import ModelClassifier


def main():
    temp_list = []
    test_model = ModelClassifier('C:/Users/Public/scans/RectPrism_Test01_BestCase(0).obj')
    hist_data = test_model.generate_distribution_data(test_model.mesh_object.vertices)
    with open("training_data.txt", 'a') as training_data:
        temp_list.append(['Rectangular_Prism', hist_data])
        for line in temp_list:
            data = list(line[1])
            object_data = "{0},{1}\n".format(line[0], ",".join(map(str, data)))
            training_data.write(object_data)


def read_from_file():
    with open("training_data.txt", 'r') as data:
        lines = data.readlines()
        cube_data = lines[0].split(",")
        test = [float(i) for i in cube_data[1:41]]
        test2 = [float(i) for i in cube_data[41:len(cube_data)]]
        print(test2)


if __name__ == '__main__':
    main()
