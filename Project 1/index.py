import numpy as np
import os

#data = np.load(f'dataset{os.sep}training{os.sep}trainAccelerometer.npy')

def dataInfo():
    for file in os.listdir(f'dataset{os.sep}training{os.sep}'):
        data = np.load(f'dataset{os.sep}training{os.sep}{file}')
        print(f'{file:28} :   dimentions:   ', end = '')
        print(str(data.ndim) + ',   length:  ', end = '')
        print(data.shape)

dataInfo()

data_path = f'dataset{os.sep}'
test_path = data_path + f'testing{os.sep}'
training_path = data_path + f'testing{os.sep}'


def load_data(path: str):
    dictionary = {str: [[[float]]]}
    labels = []

    for file_name_ext in os.listdir(path):
        if 'label' in file_name_ext.lower():
            labels = np.load(path + file_name_ext)
            continue

        file_name = file_name_ext[:-4]

        dictionary[file_name] = np.load(path + file_name_ext)
        #print(dictionary[file_name])

    return dictionary, labels

test_data, test_labels = load_data(test_path)
training_data, training_labels = load_data(training_path)

data_length = len(training_data['testAccelerometer'])
print(data_length)
    
