import matplotlib as plt
import pandas as pd
import numpy as np

df1 = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/Misttest2.csv")
df2 = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/testmatch.csv")

x=0


df3 = pd.DataFrame(columns=['Nchisq','uchisq','gchisq','rchisq','ichisq','zchisq','totchisq','reducedtotchisq','totchisq2','reducedtotchisq2','starindex','modelindex'])
df4 = pd.DataFrame(columns=['','Nchisq','uchisq','gchisq','rchisq','ichisq','zchisq','totchisq','reducedtotchisq','totchisq2','reducedtotchisq2','starindex','modelindex'])
#df2.iloc[x].fillna(0, inplace=True)
dfd = pd.DataFrame()

for x in range(729):
    y = 0
    for y in range(1486):
        z = df2.iloc[x]['rflux']/df1.iloc[y]['rflux']
        a1 = (df2.iloc[x]['gflux'] - (df1.iloc[y]['gflux']/z))**2  / (df2.iloc[x]['e_gflux'])**2
        a2 = (df2.iloc[x]['rflux'] - (df1.iloc[y]['rflux']/z))**2  / (df2.iloc[x]['e_rflux'])**2
        a3 = (df2.iloc[x]['iflux'] - (df1.iloc[y]['iflux']/z))**2  / (df2.iloc[x]['e_iflux'])**2
        a4 = (df2.iloc[x]['zflux'] - (df1.iloc[y]['zflux']/z))**2  / (df2.iloc[x]['e_zflux'])**2
        tota =a1 + a2 + a3 + a4
        redtota = tota/3
        dfd = dfd.append({'gchisq':a1,'rchisq':a2,'ichisq':a3,'zchisq':a4,'totchisq':tota,'reducedtotchisq':redtota},ignore_index=True)
        y+=1
    result_index = dfd['reducedtotchisq'].sub(1).abs().idxmin()
    print(result_index)
    dfd.drop(dfd.index[0:1486],0,inplace=True)
    print(dfd)
    b1 = (df2.iloc[x]['Nflux'] - (df1.iloc[result_index]['Nflux']/z))**2  / (df2.iloc[x]['e_Nflux'])**2
    b2 = (df2.iloc[x]['uflux'] - (df1.iloc[result_index]['uflux']/z))**2  / (df2.iloc[x]['e_uflux'])**2
    b3 = (df2.iloc[x]['gflux'] - (df1.iloc[result_index]['gflux']/z))**2  / (df2.iloc[x]['e_gflux'])**2
    b4 = (df2.iloc[x]['rflux'] - (df1.iloc[result_index]['rflux']/z))**2  / (df2.iloc[x]['e_rflux'])**2
    b5 = (df2.iloc[x]['iflux'] - (df1.iloc[result_index]['iflux']/z))**2  / (df2.iloc[x]['e_iflux'])**2
    b6 = (df2.iloc[x]['zflux'] - (df1.iloc[result_index]['zflux']/z))**2  / (df2.iloc[x]['e_zflux'])**2
    totb = b3+ b4+ b5+ b6
    redtotb = totb/3
    totb2 = b1+ b2+ b3+ b4+ b5+ b6
    redtotb2 = totb2/5
    starindex = x
    modelindex = result_index
    df4 = df4.append({'Nchisq':b1,'uchisq':b2, 'gchisq':b3,'rchisq':b4,'ichisq':b5,'zchisq':b6,'totchisq':totb,'reducedtotchisq':redtotb, 'totchisq2': totb2, 'reducedtotchisq2':redtotb2,'starindex': x, 'modelindex':result_index},ignore_index=True)
    x+=1

df4.to_csv('testmistfluxes2f.csv')