import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


df1 = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/misttest2.csv")
df2 = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/testmatch.csv")
df3 = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/testmistfluxes2a.csv")

fig= plt.figure()
ax = fig.add_axes([0,0,1,1])
e1 = 131
e2 = 49
e3 = 132
ax.scatter(df2['N/u'], df2['u/g'], s = 4, c = 'black',  marker = '^', label = 'data' )
ax.scatter(df2.iloc[e1]['N/u'], df2.iloc[e1]['u/g'],s = 4, c = 'b',  marker = 'o', label = 'PG0824')
ax.scatter(df2.iloc[e2]['N/u'], df2.iloc[e2]['u/g'], s = 4, c = 'r',  marker = ',', label = 'J084259')
ax.scatter(df2.iloc[e3]['N/u'], df2.iloc[e3]['u/g'], s = 4, c = 'g',  marker = '>', label = 'J1015')
#x = [0.25e0,0.25e0]
#y = [0.1e-3,1e6]
#dashes = [5, 3]
#l, = plt.plot(x,y, '--', c = 'black')
#ax.scatter(df2.iloc[e]['reducedtotchisq'], df2.iloc[e]['reducedtotchisq2'], s = 7, c = 'g',  marker = ',' )
ax.set_yscale('log')
ax.set_xscale('log')
ax.set_xlabel('N/u' + ' ' + '(mJy)')
ax.set_ylabel('u/g' + ' ' + '(mJy)')
#plt.xlim([1e-1, 1e0])
#plt.ylim([1e-1, 1e1])
plt.legend()