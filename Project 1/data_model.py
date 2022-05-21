from inspect import stack
import numpy as np
import os
from scipy.ndimage import zoom

data_path = f'dataset{os.sep}'
test_path = data_path + f'testing{os.sep}'
training_path = data_path + f'testing{os.sep}'

class DataModel:

    ignored_files = ("Labels.npy")

    def __init__(self, measurement_frequency, are_training_data, training_path = training_path, test_path = test_path):
        self.training_path = training_path
        self.test_path = test_path
        self.measurement_frequency = measurement_frequency
        self.data = self.load_dataset(are_training_data)

    def load_dataset(self, are_training_data = True):
        path = self.training_path if are_training_data else self.test_path
        stacking_list = []
        for file in path:
            if file.endswith(self.ignored_files):
                continue
            if file.endswith(".npy"):
                data = np.load(os.path.join(path, file))
                measurements_per_second = np.ize(data, axis = 1)
                zooming_factor = self.measurement_frequency / measurements_per_second
                normalised_data = zoom(data, (1, zooming_factor, 1))
                stacking_list.append(normalised_data)

        return np.stack(stacking_list, axis = -1)
        

    

    
