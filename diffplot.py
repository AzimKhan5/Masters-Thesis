import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df1 = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/Misttest2.csv")
df2 = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/testmatch.csv")
df3 = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/qef4.csv")


fig= plt.figure()
ax = fig.add_axes([0,0,1,1])

ax.scatter(df3['diffN'],df3['diffu'],s = 4, c = 'black',  marker = '^')
ax.scatter(df3.iloc[49]['diffN'],df3.iloc[49]['diffu'],s = 4, c = 'r',  marker = '^')
ax.scatter(df3.iloc[131]['diffN'],df3.iloc[131]['diffu'],s = 4, c = 'g',  marker = '^')
ax.scatter(df3.iloc[132]['diffN'],df3.iloc[132]['diffu'],s = 4, c = 'b',  marker = '^')
ax.set_yscale('log')
ax.set_xscale('log')
x = [1,1e-9]
y = [1,1e4]
dashes = [5, 3]
l, = plt.plot(x,y, '--', c = 'black')
