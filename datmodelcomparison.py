import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df1 = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/misttest2.csv")
df2 = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/testmatch.csv")
df3 = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/testmistfluxes2a.csv")

c = 0

a = int(df3.iloc[c]['modelindex'])

#d = df1.iloc[a]['N/u'] - df2.iloc[c]['N/u']
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])


for c in range(729):
    a = int(df3.iloc[c]['modelindex'])
    plt.errorbar(df1.iloc[a]['N/g'],df2.iloc[c]['N/g'], markersize  = 3, c = 'black',  marker = 'o',capsize=2, capthick=1)
    c+=1
    

    
d = 49    
e = int(df3.iloc[d]['modelindex'])
plt.errorbar(df1.iloc[e]['N/g'],df2.iloc[d]['N/g'],  markersize = 3, c = 'g',  marker = 'o',capsize=2, capthick=1, label = 'J084259')
d = 131    
e = int(df3.iloc[d]['modelindex'])
plt.errorbar(df1.iloc[e]['N/g'],df2.iloc[d]['N/g'],  markersize  = 3, c = 'blue',  marker = 'o',capsize=2, capthick=1, label = 'PG0824')
d = 132    
e = int(df3.iloc[d]['modelindex'])
plt.errorbar(df1.iloc[e]['N/g'],df2.iloc[d]['N/g'],  markersize  = 3, c = 'r',  marker = 'o',capsize=2, capthick=1, label = 'J1015')
#x = [0.1e-4,1e1]
#y = [0.3e0,0.3e0]
#dashes = [5, 3]
#l, = plt.plot(x,y, '--', c = 'black')
ax.set_yscale('log')
ax.set_xscale('log')
ax.set_xlabel('N/g' + ' ' +'Model')
ax.set_ylabel('N/g' + ' ' +'data')
ax.set_title('Comparison of colours data and model')
plt.legend()
plt.show()