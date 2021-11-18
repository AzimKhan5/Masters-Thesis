import matplotlib as plt
import pandas as pd
import numpy as np

dfa = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/misttest2.csv")
dfb = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/testmatch.csv")
dfc = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/testmistfluxes2d.csv")

#df5 = pd.DataFrame(columns=[''])
#y=0
#for y in range(729):


dfb['test1'] = dfc['reducedtotchisq2']
dfb['test'] = (dfc['reducedtotchisq']*3.5)

dfb = dfb.drop(dfb[dfb['test1']< dfb['test'] ].index)

dfb.to_csv('asdad.csv')