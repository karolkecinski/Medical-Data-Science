import numpy as np
import os

#data = np.load(f'dataset{os.sep}training{os.sep}trainAccelerometer.npy')

def dataInfo():
    for file in os.listdir(f'dataset{os.sep}training{os.sep}'):
        print(f'{file:28} :   dimentions:   ', end = '')
        print(str(np.load(f'dataset{os.sep}training{os.sep}{file}').ndim) + ',   length:  ', end = '')
        print(len(np.load(f'dataset{os.sep}training{os.sep}{file}')))

dataInfo()
    
