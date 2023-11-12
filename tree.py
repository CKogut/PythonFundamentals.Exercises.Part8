import os


def walk(dirname):
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)
        fout = open('output.txt', 'a')

        if os.path.isfile(path):
            fout.write(path + '\n')
        else:
            walk(path)


def clear_file(filename):
    with open(filename, 'r+') as file:
        file.truncate(0)


clear_file('output.txt')
walk('/Users/corinne/DataProjects/PythonFundamentals.Exercises.Part8')
