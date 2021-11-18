import matplotlib as plt
import pandas as pd
import numpy as np


dfa = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/misttest2.csv")
dfb = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/testmatch.csv")
dfc = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/testmistfluxes2a.csv")
a_list=[]
dfd = pd.DataFrame(columns=['t1','t2','t3'])
#df5 = pd.DataFrame(columns=[''])
#y=0
#for y in range(729):
#df3 = df3.drop(df3[df3['N/u']< 2.5e-1 ].index)

#print(df3)
for c in range(729):
   a = int(dfc.iloc[c]['modelindex'])
   b = int(dfc.iloc[c]['starindex'])
   #print(b, a)
   z = dfa.iloc[a]['rflux']/dfb.iloc[c]['rflux']
   t1 = dfb.iloc[b]['Nflux']-(dfa.iloc[a]['Nflux']/z)  
   t2 =dfb.iloc[b]['uflux']-(dfa.iloc[a]['uflux']/z)  
   t3 = dfb.iloc[b]['gflux']-(dfa.iloc[a]['gflux']/z) 
   dfd = dfd.append({'t1': t1, 't2': t2, 't3': t3},ignore_index=True)
   #a_list = dfb['t1'].tolist()
   #a_list = dfb['t2'].tolist()
   #a_list = dfb['t3'].tolist()
   #if t1 <50.0 or t2 <2.0 or t3 <1.0:
      #dfb = dfb.drop(c)
   c+=1
print(dfd)
dfd.to_csv('testing123.csv')
#dfb.to_csv('testmistmatch5.csv')