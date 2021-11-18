import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df1 = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/misttest2.csv")
df2 = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/testmatch.csv")
df3 = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/abcd.csv")
df4 = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/WDmodels.csv")
df5 = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/asdasd4.csv")
df6 = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/WDtesting.csv")

c = 215
a = int(df3.iloc[c]['modelindex'])
b = int(df3.iloc[c]['starindex'])
print(b)
t1= int(df6[df6['starindex']== b].index.values)
wd = int(df6.iloc[t1]['modelindex'])
#wd = 29
wd2 = str(int(df4.iloc[wd]['Teff']))
if wd <= 64:
    wd3 = 'DA'
else:
    wd3 = 'DB'
print(wd)
fig= plt.figure()
ax = fig.add_axes([0,0,1,1])
z = df1.iloc[a]['rflux']/df2.iloc[b]['rflux']
z2 = df4.iloc[wd]['uflux']/df2.iloc[b]['uflux']

ax.errorbar(0.1528, df2.iloc[b]['Fflux']-(df4.iloc[wd]['Fflux']/z2 + df1.iloc[a]['Fflux']/z), yerr= df2.iloc[b]['e_Fflux'], c = 'black',  marker = 'o',label = 'residuals', markersize = 2, alpha = 1,capsize=2, capthick=1)
ax.errorbar(0.2271, df2.iloc[b]['Nflux']-(df4.iloc[wd]['Nflux']/z2 + df1.iloc[a]['Nflux']/z ), yerr= df2.iloc[b]['e_Nflux'], c = 'black',  marker = 'o', markersize = 0.5, alpha = 1,capsize=2, capthick=1)
ax.errorbar(0.356, df2.iloc[b]['uflux']-(df4.iloc[wd]['uflux']/z2 + df1.iloc[a]['uflux']/z), yerr= df2.iloc[b]['e_uflux'], c = 'black',  marker = 'o', markersize = 0.5, alpha = 1,capsize=2, capthick=1)
ax.errorbar(0.483,df2.iloc[b]['gflux']-(df4.iloc[wd]['gflux']/z2 + df1.iloc[a]['gflux']/z), yerr= df2.iloc[b]['e_gflux'], c = 'black',  marker = 'o', markersize = 0.5, alpha = 1,capsize=2, capthick=1)
ax.errorbar(0.626, df2.iloc[b]['rflux']-(df4.iloc[wd]['rflux']/z2 + df1.iloc[a]['rflux']/z), yerr= df2.iloc[b]['e_rflux'], c = 'black',  marker = 'o', markersize = 0.5, alpha = 1,capsize=2, capthick=1)
ax.errorbar(0.767, df2.iloc[b]['iflux']-(df4.iloc[wd]['iflux']/z2 + df1.iloc[a]['iflux']/z), yerr= df2.iloc[b]['e_iflux'], c = 'black',  marker = 'o', markersize = 0.5, alpha = 1,capsize=2, capthick=1)
ax.errorbar(0.910, df2.iloc[b]['zflux']-(df4.iloc[wd]['zflux']/z2 + df1.iloc[a]['zflux']/z), yerr= df2.iloc[b]['e_zflux'], c = 'black',  marker = 'o', markersize = 0.5, alpha = 1,capsize=2, capthick=1)

#ax.set_yscale('log')
ax.set_xlabel('Wavelength' + '  ' + '(' + chr(956) + 'm' + ')')
ax.set_ylabel('F' + chr(957) + '  ' + '(mJy)')
ax.set_title('Residuals ' + 'of ' + df2.iloc[c]['name'])
#ax.set_facecolor("black")
plt.legend()
