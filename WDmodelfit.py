import matplotlib as plt
import pandas as pd
import numpy as np

df1 = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/WDmodels.csv")
df2 = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/asdasd4.csv")
df3 = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/misttest2.csv")
df4 = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/testmatch.csv")
df5 = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/abcd.csv")
dfd = pd.DataFrame()
dfe = pd.DataFrame()
#df2.iloc[x].fillna(0, inplace=True)
x=0
for x in range(30):
    starindex = df2.iloc[x]['starindex_y']
    print(starindex)
    a = int(df5.iloc[starindex]['modelindex'])
    b = int(df5.iloc[starindex]['starindex'])
    #z2 = df3.iloc[a]['rflux']/df4.iloc[b]['rflux']
    #print(z2)
    y = 0
    for y in range(133):
        a = pd.isnull(df2.iloc[x]['Fflux'])
        if a == False:
            z2 = df1.iloc[y]['uflux']/df2.iloc[x]['uflux']
            a1 = (df2.iloc[x]['Nflux']  - (df1.iloc[y]['Nflux']/z2))**2  / (df2.iloc[x]['e_Nflux'])**2
            a2 = (df2.iloc[x]['Fflux'] - (df1.iloc[y]['Fflux']/z2))**2  / (df2.iloc[x]['e_Fflux'])**2
            #a5 = ((df2.iloc[x]['uflux'] - (df1.iloc[y]['uflux']/z2))**2  / (df2.iloc[x]['e_uflux'])**2
            t1 = (df1.iloc[y]['Nflux']/z2)/df2.iloc[x]['Nflux']
            a3 = a1 + a2 
            a4 = a3
            dfd = dfd.append({'Nchisq': a1,'Fchisq':a2, 'totchisq':a3, 'reducedtotchisq': a4, 'Nratio': t1},ignore_index=True) 
        else:
            z2 = df1.iloc[y]['uflux']/df2.iloc[x]['uflux']
            a1 = (df2.iloc[x]['Nflux']  - (df1.iloc[y]['Nflux']/z2))**2  / (df2.iloc[x]['e_Nflux'])**2
            #a5 = (df2.iloc[x]['uflux'] - (df1.iloc[y]['uflux']/z2))**2  / (df2.iloc[x]['e_uflux'])**2
            a2 = 0
            t1 = (df1.iloc[y]['Nflux']/z2)/df2.iloc[x]['Nflux']
            a3 = a1 + a2 
            a4 = a3
            dfd = dfd.append({'Nchisq': a1,'Fchisq':a2, 'totchisq':a3, 'reducedtotchisq': a4, 'Nratio': t1},ignore_index=True)
        y+=1
    #dfd = dfd.drop(dfd[dfd['Nratio'] > 1 ].index)
    result_index = dfd['reducedtotchisq'].sub(1).abs().idxmin()    
    b1 = dfd.iloc[result_index]['Nchisq']
    b2 = dfd.iloc[result_index]['Fchisq']
    b3 = dfd.iloc[result_index]['totchisq']
    b4 = dfd.iloc[result_index]['reducedtotchisq']
    dfd.drop(dfd.index[0:133],0,inplace=True)
    dfe = dfe.append({'Nchisq': b1, 'Fchisq':b2, 'totchisq':b3, 'reducedtotchisq': b4, 'starindex':starindex, 'modelindex':result_index},ignore_index=True)
    print(result_index)
    #print(dfd)
        
    x+=1
    
dfe.to_csv('WDtestingUB.csv')