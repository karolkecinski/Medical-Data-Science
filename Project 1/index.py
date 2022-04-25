import numpy as np
import os

#data = np.load(f'dataset{os.sep}training{os.sep}trainAccelerometer.npy')

for file in os.listdir(f'dataset{os.sep}training{os.sep}'):
    print(np.load(f'dataset{os.sep}training{os.sep}{file}'))
