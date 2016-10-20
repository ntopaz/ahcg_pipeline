import sys
import pandas as pd
from pandas import Series,DataFrame
import matplotlib.pyplot as plt

input_file = sys.argv[1]
data = pd.read_table(input_file, names=['Chromosome','Base','Depth'])

data.plot(kind='line')
