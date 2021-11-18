import pandas as pd


filename = 'C:/Users/Azim/Desktop/Azim/University work/Disso Research/Table_Mass_06.txt'

df = pd.read_csv(filename, delim_whitespace=True, comment='#')

df.to_csv('WDmodels.csv')

