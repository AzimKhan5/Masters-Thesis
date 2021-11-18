import matplotlib as plt
import pandas as pd
import numpy as np

df1 = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/WDmodels.csv")
df2 = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/asdasd4.csv")

x=0


df3 = pd.DataFrame(columns=['N/uchisq','totchisq','reducedtotchisq','starindex','modelindex'])
df4 = pd.DataFrame(columns=['N/uchisq','totchisq','reducedtotchisq','starindex','modelindex'])
#df2.iloc[x].fillna(0, inplace=True)

for x in range(347):

    df3['N/uchisq'] = (df2.iloc[x]['N/u'] - df1['N/u'])**2  / (df2.iloc[x]['e_N/u'])**2
    #df3['u/gchisq'] = (df2.iloc[x]['u/g'] - df1['u/g'])**2 / (df2.iloc[x]['e_u/g'])**2
    df3['totchisq'] = df3['N/uchisq']
    df3['reducedtotchisq'] = df3['totchisq']
    minValuesObj = df3['reducedtotchisq'].idxmin()

    df3['starindex'] = x
    df3['modelindex'] = minValuesObj
       
    test=df3.iloc[minValuesObj].to_list()
    df4.loc[len(df4)] = test
        
    x+=1
    
df4.to_csv('testmistfluxes4.csv')