import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

dfa = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/misttest2.csv")
dfb = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/testmatch.csv")
dfc = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/testmistfluxes2d.csv")

dfa['u-g'] = dfa['SDSS_u'] - dfa['SDSS_g']
dfa['Luminosity'] =  10**dfa['log_L_x']
dfb['u-g'] = dfb['umag'] - dfb['gmag']
dfb['Mg'] = dfb ['gmag'] - 5*np.log(((1/dfb['parallax'])/10))
print(dfb['Mg'])
fig= plt.figure()
ax = fig.add_axes([0,0,1,1])

ax.scatter(dfb['u-g'],dfb['Mg'], s = 4, c = 'b', marker = 'o')
ax.scatter(dfa['u-g'],dfa['SDSS_g'], s = 4, c = 'b', marker = 'o')
#ax.set_yscale('log')
#ax.set_xscale('log')
plt.gca().invert_yaxis()