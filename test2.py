import matplotlib as plt
import pandas as pd
import numpy as np

df1 = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/Mistmodelfinal2.csv")
df2 = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/Xmatchfinal2.csv")

x=0


df3 = pd.DataFrame(columns=['fuvchisq','nuvchisq','uchisq','gchisq','rchisq','ichisq','zchisq','totchisq','reducedtotchisq'])
df4 = pd.DataFrame(columns=['fuvchisq','nuvchisq','uchisq','gchisq','rchisq','ichisq','zchisq','totchisq','reducedtotchisq','totchisq2','reducedtotchisq2','starindex','modelindex'])
for x in range(729):
    a = pd.isnull(df2.iloc[x]['Fflux'])

    if a == True:    
        df3['gchisq'] = (df2.iloc[x]['gflux'] - df1['gflux'])**2  / (df2.iloc[x]['e_gflux'])**2
        df3['rchisq'] = (df2.iloc[x]['rflux'] - df1['rflux'])**2  / (df2.iloc[x]['e_rflux'])**2
        df3['ichisq'] = (df2.iloc[x]['iflux'] - df1['iflux'])**2 / (df2.iloc[x]['e_iflux'])**2
        df3['zchisq'] = (df2.iloc[x]['zflux'] - df1['zflux'])**2  / (df2.iloc[x]['e_zflux'])**2
        df3['totchisq'] = df3['gchisq'] + df3['rchisq'] + df3['ichisq'] + df3['zchisq'] 
        df3['reducedtotchisq'] = df3['totchisq']/3
        minValuesObj = df3['reducedtotchisq'].idxmin()
        #print(minValuesObj)
        df3['fuvchisq'] = 0
        df3['nuvchisq'] = (df2.iloc[x]['Nflux'] - df1['GALEX_NUV'])**2  / (df2.iloc[x]['e_Nflux'])**2
        df3['uchisq'] = (df2.iloc[x]['uflux'] - df1['uflux'])**2 / (df2.iloc[x]['e_uflux'])**2
        df3['totchisq2'] = df3['uchisq'] + df3['gchisq'] + df3['rchisq'] + df3['ichisq'] + df3['zchisq'] + df3['nuvchisq']
        df3['reducedtotchisq2'] = df3['totchisq2']/5
        minValuesObj2 = df3['reducedtotchisq2'].idxmin()
        df3['starindex'] = x
        df3['modelindex'] = minValuesObj2
        test=df3.iloc[minValuesObj2].to_list()
        #df4 = df4.append(pd.DataFrame(test,columns=['fuvchisq','nuvchisq','uchisq','gchisq','rchisq','ichisq','zchisq','totchisq','reducedtotchisq','totchisq2','reducedtotchisq2','starindex','modelindex']),ignore_index=False)
        df4.loc[len(df4)] = test
        x += 1
    #print(df4)
    #print(minValuesObj2)
    #print(a)
    #print(test)

    else:
        df3['gchisq'] = (df2.iloc[x]['gflux'] - df1['gflux'])**2  / (df2.iloc[x]['e_gflux'])**2
        df3['rchisq'] = (df2.iloc[x]['rflux'] - df1['rflux'])**2  / (df2.iloc[x]['e_rflux'])**2
        df3['ichisq'] = (df2.iloc[x]['iflux'] - df1['iflux'])**2 / (df2.iloc[x]['e_iflux'])**2
        df3['zchisq'] = (df2.iloc[x]['zflux'] - df1['zflux'])**2  / (df2.iloc[x]['e_zflux'])**2
        df3['totchisq'] = df3['gchisq'] + df3['rchisq'] + df3['ichisq'] + df3['zchisq'] 
        df3['reducedtotchisq'] = df3['totchisq']/3
        minValuesObj = df3['reducedtotchisq'].idxmin()
        #print(minValuesObj)
        df3['fuvchisq'] = (df2.iloc[x]['Fflux'] - df1['GALEX_FUV'])**2  / (df2.iloc[x]['e_Fflux'])**2
        df3['nuvchisq'] = (df2.iloc[x]['Nflux'] - df1['GALEX_NUV'])**2  / (df2.iloc[x]['e_Nflux'])**2
        df3['uchisq'] = (df2.iloc[x]['uflux'] - df1['uflux'])**2 / (df2.iloc[x]['e_uflux'])**2
        df3['totchisq2'] = df3['uchisq'] + df3['gchisq'] + df3['rchisq'] + df3['ichisq'] + df3['zchisq'] + df3['fuvchisq'] + df3['nuvchisq']
        df3['reducedtotchisq2'] = df3['totchisq2']/6
        minValuesObj2 = df3['reducedtotchisq2'].idxmin()
        df3['starindex'] = x
        df3['modelindex'] = minValuesObj2
        test=df3.iloc[minValuesObj2].to_list()
        df4.loc[len(df4)] = test
        x+=1
    #print(minValuesObj2)
#df3.to_csv('testmistfluxes4.csv')   
df4.to_csv('testing.csv')