import matplotlib as plt
import pandas as pd
import numpy as np

df1 = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/mistmodelfinal2.csv")
df2 = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/Xmatchfinal2.csv")

df3 = pd.DataFrame(columns=['uchisq','gchisq','rchisq','ichisq','zchisq','totchisq','reducedtotchisq'])

x = 5

df3['umagdif'] = df2.iloc[x]['umag'] - df1['SDSS_u'] 
df3['gmagdif'] = df2.iloc[x]['gmag'] - df1['SDSS_g'] 
df3['rmagdif'] = df2.iloc[x]['rmag_x'] - df1['SDSS_r']
df3['imagdif'] = df2.iloc[x]['imag_x'] - df1['SDSS_i']
df3['zmagdif'] = df2.iloc[x]['zmag'] - df1['SDSS_z'] 

df3.drop(df3[df3['umagdif'] >5].index, inplace= True)
df3.drop(df3[df3['umagdif'] <-5].index, inplace= True)

df3.drop(df3[df3['gmagdif'] >5].index, inplace= True)
df3.drop(df3[df3['gmagdif'] <-5].index, inplace= True)


df3.drop(df3[df3['rmagdif'] >5].index, inplace= True)
df3.drop(df3[df3['rmagdif'] <-5].index, inplace= True)


df3.drop(df3[df3['imagdif'] >5].index, inplace= True)
df3.drop(df3[df3['imagdif'] <-5].index, inplace= True)


df3.drop(df3[df3['zmagdif'] >5].index, inplace= True)
df3.drop(df3[df3['zmagdif'] <-5].index, inplace= True)

df3.to_csv('magdiff.csv')