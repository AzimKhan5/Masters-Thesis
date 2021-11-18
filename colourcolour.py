import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df1 = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/misttest2.csv")
df2 = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/testmatch.csv")

df1['u-r'] = df1['SDSS_u'] - df1['SDSS_r']
df1['r-z'] = df1['SDSS_r'] - df1['SDSS_z']
df2['u-r'] = df2['umag'] - df2['rmag_x']
df2['r-z'] = df2['rmag_x'] - df2['zmag']
df2['e_u-r'] = df2['e_umag'] + df2['e_rmag']
df2['e_r-z'] = df2['e_zmag'] + df2['e_rmag']


fig= plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.scatter(df1['r-z'], df1['u-r'], s = 4, c = 'b', label = 'model', marker = '^')
ax.scatter(df2['r-z'], df2['u-r'], s = 4, c = 'r', label = 'data', marker = ',')
ax.set_xlabel('R-Z')
ax.set_ylabel('U-R')
ax.set_title('Colour-Colour Diagram')
plt.legend()

#plt.show()