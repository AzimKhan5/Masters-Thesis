import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


df1 = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/Misttest2.csv")
df2 = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/testmatch.csv")
df3 = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/abcd1.csv")
df4 = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/qef4.csv")
df5 = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/769.csv")
df6 = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/76912.csv")
df7 = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/abcd2.csv")
df8 = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/769123.csv")
dfd = pd.DataFrame()

#df7 = df7.drop(df7[df7['diffN'] > 1 ].index)
#df7 = df7.drop(df7[df7['diffu'] > 1 ].index)
#df7 = df7.drop(df7[df7['diffg'] > 1 ].index)
#dfd = pd.merge(df3, df4, on='col1', how='outer')   
#df7.to_csv('769123.csv')

x = 0 
for x in range(729):
    a = int(df3.iloc[x]['modelindex'])
    b = int(df3.iloc[x]['starindex'])
    z = df1.iloc[a]['rflux']/df2.iloc[b]['rflux']
    sigma1 = abs(df2.iloc[b]['Nflux'] - (df1.iloc[a]['Nflux']/z))/ df2.iloc[b]['e_Nflux']
    sigma2 = abs(df2.iloc[b]['uflux'] - (df1.iloc[a]['uflux']/z))/ df2.iloc[b]['e_uflux']
    sigma3 = abs(df2.iloc[b]['gflux'] - (df1.iloc[a]['gflux']/z))/ df2.iloc[b]['e_gflux']
    dfd = dfd.append({'Nsigma':sigma1, 'usigma':sigma2,'gsigma':sigma3, 'starindex':b},ignore_index=True)
    x+=1
    
dfd.to_csv('a123.csv')
    

    
