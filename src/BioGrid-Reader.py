import pandas as pd
import numpy as np
import matplotlib as plt

dtypes = { }
d = pd.read_csv("../data/BIOGRID-ALL-4.4.197.tab3.txt", delimiter="\t")
print(d.columns)
print(d.head())

