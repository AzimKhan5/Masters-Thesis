import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

dfa = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/misttest2.csv")
dfb = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/testmatch.csv")
dfc = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/testmistfluxes2a.csv")

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
for c in range(729):
    a = int(dfc.iloc[c]['modelindex'])
    z = dfa.iloc[a]['gflux']/dfb.iloc[c]['gflux']
    plt.errorbar(dfa.iloc[a]['Nflux']/z,dfb.iloc[c]['Nflux'], yerr = dfb.iloc[c]['e_Nflux'], markersize  = 3, c = 'black',  marker = 'o',capsize=2, capthick=1)
    c+=1
    
c1 = 49   
a1 = int(dfc.iloc[c1]['modelindex'])
z1 = dfa.iloc[a1]['gflux']/dfb.iloc[c1]['gflux']
plt.errorbar(dfa.iloc[a1]['Nflux']/z1,dfb.iloc[c1]['Nflux'], yerr = dfb.iloc[c1]['e_Nflux'], markersize  = 3, c = 'b',  marker = 'o',capsize=2, capthick=1)
c2 = 131   
a2 = int(dfc.iloc[c2]['modelindex'])
z2 = dfa.iloc[a2]['gflux']/dfb.iloc[c2]['gflux']
plt.errorbar(dfa.iloc[a2]['Nflux']/z2,dfb.iloc[c2]['Nflux'], yerr = dfb.iloc[c2]['e_Nflux'], markersize  = 3, c = 'g',  marker = 'o',capsize=2, capthick=1)
c3 = 132   
a3 = int(dfc.iloc[c3]['modelindex'])
z3 = dfa.iloc[a3]['gflux']/dfb.iloc[c3]['gflux']
plt.errorbar(dfa.iloc[a3]['Nflux']/z3,dfb.iloc[c3]['Nflux'], yerr = dfb.iloc[c3]['e_Nflux'], markersize  = 3, c = 'r',  marker = 'o',capsize=2, capthick=1)

ax.set_yscale('log')
ax.set_xscale('log')
plt.xlim([1e-6, 1e-5])
plt.ylim([1e-3, 1e-1])