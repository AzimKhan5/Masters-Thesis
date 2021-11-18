import pandas as pd

df1 = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/mistsdssisochrone00.csv")
df2 = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/mistgalexisochrone00.csv")

df3 = pd.merge(df1, df2, on='initial_mass', how='outer')

df3.to_csv('Mistmodel00.csv')