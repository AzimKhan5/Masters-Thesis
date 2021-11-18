import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df1 = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/Mistmodel00.csv")




df1['uflux'] = (2 * 1.4e-10 * np.sinh(df1['SDSS_u']*np.log(10)/-2.5 - np.log(1.4e-10))*3631)*1000
df1['gflux'] = (2 * 0.9e-10 * np.sinh(df1['SDSS_g']*np.log(10)/-2.5 - np.log(0.9e-10))*3631)*1000
df1['rflux'] = (2 * 1.2e-10 * np.sinh(df1['SDSS_r']*np.log(10)/-2.5 - np.log(1.2e-10))*3631)*1000
df1['iflux'] = (2 * 1.8e-10 * np.sinh(df1['SDSS_i']*np.log(10)/-2.5 - np.log(1.8e-10))*3631)*1000
df1['zflux'] = (2 * 7.4e-10 * np.sinh(df1['SDSS_z']*np.log(10)/-2.5 - np.log(7.4e-10))*3631)*1000


df1['Ffluxt'] = 10**((df1['GALEX_FUV'] - 18.82)/-2.5) *1.4e-15
df1['Fflux'] = ((3.33564095*10**4) * df1['Ffluxt'] * (1528**2))*1000
df1['Nfluxt'] = 10**((df1['GALEX_NUV'] - 20.08)/-2.5) *2.06e-16
df1['Nflux'] = ((3.33564095*10**4) * df1['Nfluxt'] * (2271**2))*1000

df1['N/g']= df1['Nflux']/df1['gflux']
df1['g/r']= df1['gflux']/df1['rflux']
df1['i/z']= df1['iflux']/df1['zflux']
df1['N/u']= df1['Nflux']/df1['uflux']
df1['u/g']= df1['uflux']/df1['gflux']


df1.to_csv('Mistmodel00.csv')