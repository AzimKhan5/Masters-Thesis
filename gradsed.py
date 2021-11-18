import matplotlib as plt
import pandas as pd
import numpy as np


dfa = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/misttest2.csv")
dfb = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/testmatch.csv")
dfc = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/testmistfluxes2a.csv")
a_list=[]
dfd = pd.DataFrame()
#df5 = pd.DataFrame(columns=[''])
#y=0
#for y in range(729):
#df3 = df3.drop(df3[df3['N/u']< 2.5e-1 ].index)

#print(df3)
for c in range(729):
   a = int(dfc.iloc[c]['modelindex'])
   b = int(dfc.iloc[c]['starindex'])
   #print(b, a)
   z = dfa.iloc[a]['gflux']/dfb.iloc[c]['gflux']
   ut1 = ((dfb.iloc[b]['uflux']) - (dfb.iloc[b]['Nflux'])) / (0.356-0.2271)
   ut2 =((dfa.iloc[a]['uflux']/z)-(dfa.iloc[a]['Nflux']/z) )/(0.356-0.2271)
   gt1 =((dfb.iloc[b]['gflux']) - (dfb.iloc[b]['uflux'])) / (0.483-0.356)
   gt2 =((dfa.iloc[a]['gflux']/z)-(dfa.iloc[a]['uflux']/z) )/(0.483-0.356)
   zt1 = ((dfb.iloc[b]['zflux']) - (dfb.iloc[b]['Nflux'])) / (0.910-0.2271)
   zt2 =((dfa.iloc[a]['zflux']/z)-(dfa.iloc[a]['Nflux']/z) )/(0.910-0.2271)
   ut3 = ut1 - ut2
   gt3 = gt1 - gt2
   zt3 = zt1 - zt2
   tt3 = ut3 + gt3 + zt3
   starindex = b
   dfd = dfd.append({'ut1': ut1, 'ut2': ut2, 'ut3':ut3, 'gt1': gt1, 'gt2': gt2, 'gt3':gt3, 'zt1': zt1, 'zt2': zt2, 'zt3':zt3,'tt3':tt3,'starindex':starindex},ignore_index=True)
   #dfd = dfd.append({'rt1': rt1, 'rt2': rt2, 'rt3':rt3,'starindex':starindex},ignore_index=True)
   
   #a_list = dfb['t1'].tolist()
   #a_list = dfb['t2'].tolist()
   #a_list = dfb['t3'].tolist()
   #if t1 <50.0 or t2 <2.0 or t3 <1.0:
      #dfb = dfb.drop(c)
   c+=1
#dfd = dfd.drop(dfd[dfd['ut1']>dfd['ut2']].index)
#dfd = dfd.drop(dfd[dfd['gt1']>dfd['gt2']].index)
#dfd = dfd.drop(dfd[dfd['tt3']>0].index)
print(dfd)
dfd.to_csv('testing128.csv')
