import pandas as pd

df = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/Xmatchdcupdated3.csv")

df["e_umag"].replace({0: 0.001}, inplace=True)
df["e_gmag"].replace({0: 0.001}, inplace=True)
df["e_rmag"].replace({0: 0.001}, inplace=True)
df["e_imag"].replace({0: 0.001}, inplace=True)
df["e_zmag"].replace({0: 0.001}, inplace=True)

df.to_csv('Xmatchfinal.csv')

