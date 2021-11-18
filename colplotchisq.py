import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df1 = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/misttest2.csv")
df2 = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/testmatch.csv")
df3 = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/abcd.csv")

fig= plt.figure()
ax = fig.add_axes([0,0,1,1])
e = 132
ax.scatter(df3['reducedtotchisq'], df3['reducedtotchisq2'], s = 7, c = 'black',  marker = '^', label = 'data' )
ax.scatter(df3.iloc[e]['reducedtotchisq'], df3.iloc[e]['reducedtotchisq2'], s = 7, c = 'g',  marker = ',' )
#ax.scatter(df2['N/u'], df2['u/g'], s = 7, c = 'r',  marker = 'o', label = 'data', alpha = 0.8)
#ax.scatter(df2.iloc[e]['N/u'], df2.iloc[e]['u/g'], s = 7, c = 'g',  marker = ',' )

#x = [2.5e-1,2.5e-1]
#y = [0.8e-2,8e5]

#dashes = [5, 3]

#l, = plt.plot(x,y, '--', c = 'black')

#l.set_dashes(dashes)
ax.set_yscale('log')
ax.set_xscale('log')
ax.set_xlabel('reducedtotchisq')
ax.set_ylabel('reducedtotchisq2')
ax.set_title('test')
plt.legend(prop={"size":8})