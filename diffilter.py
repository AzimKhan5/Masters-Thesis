import matplotlib as plt
import pandas as pd
import numpy as np

df1 = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/Misttest2.csv")
df2 = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/testmatch.csv")
df3 = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/abcde.csv")
dfd = pd.DataFrame()

x = 0

for x in range(729):
    a = int(df3.iloc[x]['modelindex'])
    b = int(df3.iloc[x]['starindex'])
    z = df1.iloc[a]['rflux']/df2.iloc[b]['rflux'] 
    c = (df1.iloc[a]['Nflux']) / (df2.iloc[b]['Nflux']*z)
    d = (df1.iloc[a]['uflux']) / (df2.iloc[b]['uflux']*z)
    e = (df1.iloc[a]['gflux']) / (df2.iloc[b]['gflux']*z) 
    dfd = dfd.append({'diffN':c,'diffu':d,'diffg':e,},ignore_index = True)
    x+=1
#dfd = dfd.drop(dfd[dfd['diffN'] > 0.01237 ].index)    
dfd.to_csv('testmatchupdated2.csv')
    

