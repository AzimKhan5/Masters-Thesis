import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df1 = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/testing124.csv")

fig= plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.scatter(df1['rt1'], df1['rt2'], s = 7, c = 'black',  marker = '^')
ax.scatter(df1.iloc[49]['rt1'], df1.iloc[49]['rt2'], s = 7, c = 'b',  marker = ',')
ax.scatter(df1.iloc[131]['rt1'], df1.iloc[131]['rt2'], s = 7, c = 'g',  marker = 'o')
ax.scatter(df1.iloc[132]['rt1'], df1.iloc[132]['rt2'], s = 7, c = 'r',  marker = '>')
#ax.set_xscale('log')
#ax.set_yscale('log')