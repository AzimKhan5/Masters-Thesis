import matplotlib as plt
import pandas as pd
import numpy as np

df1 = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/Misttest2.csv")
df2 = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/testmatch.csv")

x=0


df3 = pd.DataFrame(columns=['N/gchisq','g/rchisq','r/ichisq','i/zchisq','totchisq','reducedtotchisq','totchisq2','reducedtotchisq2','starindex','modelindex'])
df4 = pd.DataFrame(columns=['N/gchisq','g/rchisq','r/ichisq','i/zchisq','totchisq','reducedtotchisq','totchisq2','reducedtotchisq2','starindex','modelindex'])
#df2.iloc[x].fillna(0, inplace=True)

for x in range(729):
    #a = pd.isnull(df2.iloc[x]['F-Nflux'])
    #if a == True:
    df3['g/rchisq'] = (df2.iloc[x]['g/r'] - df1['g/r'])**2  / (df2.iloc[x]['e_g/r'])**2
    df3['r/ichisq'] = (df2.iloc[x]['r/i'] - df1['r/i'])**2  / (df2.iloc[x]['e_r/i'])**2
    df3['i/zchisq'] = (df2.iloc[x]['i/z'] - df1['i/z'])**2 / (df2.iloc[x]['e_i/z'])**2
    df3['totchisq'] = df3['g/rchisq'] + df3['i/zchisq'] + df3['r/ichisq']
    df3['reducedtotchisq'] = df3['totchisq']/2
    result_index = df3['reducedtotchisq'].sub(1).abs().idxmin()
    #print(result_index)
    #minValuesObj = df3['reducedtotchisq'].idxmin()
        #print(minValuesObj)
        #df3['F-Nchisq'] = 0
    df3['N/gchisq'] = (df2.iloc[x]['N/g'] - df1.iloc[result_index]['N/g'])**2  / (df2.iloc[x]['e_N/g'])**2
    #df3['u-gchisq'] = (df2.iloc[x]['u-gflux'] - df1.iloc[minValuesObj]['u-gflux'])**2 / (df2.iloc[x]['e_u-gflux'])**2
    df3['totchisq2'] =  df3['g/rchisq'] + df3['i/zchisq'] + df3['N/gchisq'] + df3['r/ichisq']
    df3['reducedtotchisq2'] = df3['totchisq2']/3
        #minValuesObj2 = df3['reducedtotchisq2'].idxmin()
    df3['starindex'] = x
    df3['modelindex'] = result_index
        #print(minValuesObj2)
    test=df3.iloc[result_index].to_list()
    df4.loc[len(df4)] = test
    
        #df3.drop(df3.index[0:minValuesObj],0,inplace=True)
        #df3.drop(df3.index[minValuesObj:1000],0,inplace=True)
        #print(df3)
        #print(a)
    x+=1
    #else:
     #   df3['g-rchisq'] = (df2.iloc[x]['g-rflux'] - df1['g-rflux'])**2  / (df2.iloc[x]['e_g-rflux'])**2
      #  df3['r-ichisq'] = (df2.iloc[x]['r-iflux'] - df1['r-iflux'])**2  / (df2.iloc[x]['e_r-iflux'])**2
       # df3['i-zchisq'] = (df2.iloc[x]['i-zflux'] - df1['i-zflux'])**2 / (df2.iloc[x]['e_i-zflux'])**2
        #df3['totchisq'] = df3['g-rchisq'] + df3['r-ichisq'] + df3['i-zchisq']
        #df3['reducedtotchisq'] = df3['totchisq']/2
        #minValuesObj = df3['reducedtotchisq'].idxmin()
        #print(minValuesObj)
        #df3['F-Nchisq'] = (df2.iloc[x]['F-Nflux'] - df1.iloc[minValuesObj]['F-Nflux'])**2  / (df2.iloc[x]['e_F-Nflux'])**2
        #df3['N-uchisq'] = (df2.iloc[x]['n-uflux'] - df1.iloc[minValuesObj]['n-uflux'])**2  / (df2.iloc[x]['e_n-uflux'])**2
        #df3['u-gchisq'] = (df2.iloc[x]['u-gflux'] - df1.iloc[minValuesObj]['u-gflux'])**2 / (df2.iloc[x]['e_u-gflux'])**2
        #df3['totchisq2'] = df3['u-gchisq'] + df3['g-rchisq'] + df3['r-ichisq'] + df3['i-zchisq'] + df3['N-uchisq'] + df3['F-Nchisq']
        #df3['reducedtotchisq2'] = df3['totchisq2']/5
        ##print(minValuesObj)
        #minValuesObj2 = df3['reducedtotchisq2'].idxmin()
        #df3['starindex'] = x
        #df3['modelindex'] = minValuesObj
        #print(minValuesObj2)
        #test=df3.iloc[minValuesObj].to_list()
        #df4.loc[len(df4)] = test
           #df3.drop(df3.index[0:minValuesObj],0,inplace=True)
           #df3.drop(df3.index[minValuesObj:1000],0,inplace=True)
           #print(df3)
        #print(a)
        #x+=1
#df4['test'] = df4['reducedtotchisq']*3.5
df4['test2'] = df4['reducedtotchisq2']/df4['reducedtotchisq']
#df4 = df4.drop(df4[df4['reducedtotchisq2']< df4['reducedtotchisq'] ].index)
df4.to_csv('testmistfluxes2s.csv')






