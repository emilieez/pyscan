from ModelClassifier import ModelClassifier


def main():
    temp_list = []
    test_model = ModelClassifier('C:/Users/Public/scans/Cube_Test02_BoxSize_Small(0).obj')
    hist_data = test_model.generate_distribution_data(test_model.plyObject.vertices)
    with open("training_data.txt", 'w') as training_data:
        temp_list.append(['Cube', hist_data])
        for line in temp_list:
            data = list(line[1])
            object_data = "{0},{1}".format(line[0], ",".join(map(str, data)))
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
