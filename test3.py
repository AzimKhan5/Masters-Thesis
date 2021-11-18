import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df1 = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/Mistmodel00.csv")
df2 = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/Xmatchfinal2.csv")
#print(3.35 *10**4)
df1['Ffluxt'] = 10**((df1['GALEX_FUV'] - 18.82)/-2.5) *1.4e-15
df1['Fflux'] = ((3.33564095*10**4) * df1['Ffluxt'] * (1528**2))*1000
df1['Nfluxt'] = 10**((df1['GALEX_NUV'] - 20.08)/-2.5) *2.06e-16
df1['Nflux'] = ((3.33564095*10**4) * df1['Nfluxt'] * (2271**2))*1000

df1['N/g']= df1['Nflux']/df1['gflux']
df1['g/r']= df1['gflux']/df1['rflux']
df1['i/z']= df1['iflux']/df1['zflux']
df1['N/u']= df1['Nflux']/df1['uflux']
df1['u/g']= df1['uflux']/df1['gflux']
df1['r/i']= df1['rflux']/df1['iflux']

df1.to_csv('misttest2.csv')

df2['N/g']= df2['Nflux']/df2['gflux']
df2['e_N/g'] = (((100*(df2['e_Nflux']/df2['Nflux'])) + (100*(df2['e_gflux']/df2['gflux'])))/100) * df2['N/g']
df2['g/r']= df2['gflux']/df2['rflux']
df2['e_g/r'] = (((100*(df2['e_gflux']/df2['gflux'])) + (100*(df2['e_rflux']/df2['rflux'])))/100) * df2['g/r']
df2['r/i']= df2['rflux']/df2['iflux']
df2['e_r/i'] = (((100*(df2['e_rflux']/df2['rflux'])) + (100*(df2['e_iflux']/df2['iflux'])))/100) * df2['r/i']
df2['i/z']= df2['iflux']/df2['zflux']
df2['e_i/z'] = (((100*(df2['e_iflux']/df2['iflux'])) + (100*(df2['e_zflux']/df2['zflux'])))/100) * df2['i/z']
df2['N/u']= df2['Nflux']/df2['uflux']
df2['e_N/u'] = (((100*(df2['e_Nflux']/df2['Nflux'])) + (100*(df2['e_uflux']/df2['uflux'])))/100) * df2['N/u']
df2['u/g']= df2['uflux']/df2['gflux']
df2['e_u/g'] = (((100*(df2['e_uflux']/df2['uflux'])) + (100*(df2['e_gflux']/df2['gflux'])))/100) * df2['u/g']

df2.to_csv('testmatch.csv')