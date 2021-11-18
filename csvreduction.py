import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


df1 = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/Misttest2.csv")
df2 = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/testmatch.csv")
df3 = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/abcde.csv")
df4 = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/testmatchupdated2.csv")
df5 = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/769.csv")
df6 = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/76912.csv")
df7 = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/abcd2.csv")
df8 = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/a123.csv")
#df8 = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/asdasdasdasdasd.csv")
dfd = pd.DataFrame()

dfd = pd.merge(df3, df4, on='col1', how='outer') 
dfd = pd.merge(dfd, df2, on='col1', how='outer')  
dfd = pd.merge(df8, dfd, on='col1', how='outer')  
#df8 = df8.drop(df8[df8['Nsigma'] < 3 ].index)
#df8 = df8.drop(df8[df8['usigma'] < 3 ].index)
#dfd['totsigma'] = dfd['usigma'] + dfd['Nsigma'] + dfd['gsigma']
dfd = dfd.drop(dfd[dfd['reducedtotchisq2'] < dfd['reducedtotchisq'] ].index)
#dfd = dfd.drop(dfd[dfd['usigma'] < 3 ].index)
#dfd = dfd.drop(dfd[dfd['Nsigma'] < 3 ].index)
#dfd = dfd.drop(dfd[dfd['gsigma'] < 3 ].index)
#dfd = dfd.drop(dfd[dfd['totsigma'] < 9.210 ].index)
dfd = dfd.drop(dfd[dfd['diffN'] > 1 ].index)
dfd = dfd.drop(dfd[dfd['diffu'] > 1 ].index)
#dfd = dfd.drop(dfd[dfd['diffg'] > 1 ].index)

dfd.to_csv('asdasd7.csv')

