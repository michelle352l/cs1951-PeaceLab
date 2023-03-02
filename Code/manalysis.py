import pandas as pd
import numpy as np
from collections import defaultdict
# import matplotlib - very important
import matplotlib.pyplot as plt
# import the toolkit for plotting matplotlib 3D
from mpl_toolkits import mplot3d

#retrieving the data
weapons_data = pd.read_csv("Weapons_Database/DealsAndTIVs.csv", sep=';')

def data_head():
    return "hello"
