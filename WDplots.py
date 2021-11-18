import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df1 = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/misttest2.csv")
df2 = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/testmatch.csv")
df3 = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/abcd.csv")
df4 = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/WDmodels.csv")
df5 = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/asdasd4.csv")
df6 = pd.read_csv("C:/Users/Azim/Desktop/Azim/University work/Disso Research/WDtesting.csv")

c = 49
#print(int(df3.iloc[c]['modelindex']))
a = int(df3.iloc[c]['modelindex'])
b = int(df3.iloc[c]['starindex'])
t1= int(df6[df6['starindex']== b].index.values)
wd = int(df6.iloc[t1]['modelindex'])
#wd = 44
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
#z = 1
#z = df1.iloc[a]['rflux'] - df2.iloc[b]['rflux']
#print(z)
ax.scatter(0.1528, df4.iloc[wd]['Fflux']/z2 + df1.iloc[a]['Fflux']/z, s = 7, c = 'g',  marker = 'o',alpha = 1, label = 'Combined Model')
ax.scatter(0.2271, df4.iloc[wd]['Nflux']/z2 + df1.iloc[a]['Nflux']/z , s = 7, c = 'g',  marker = 'o',alpha = 1)
ax.scatter(0.356, df4.iloc[wd]['uflux']/z2 + df1.iloc[a]['uflux']/z, s = 7, c = 'g',  marker = 'o',alpha = 1)
ax.scatter(0.483, df4.iloc[wd]['gflux']/z2 + df1.iloc[a]['gflux']/z, s = 7, c = 'g',  marker = 'o',alpha = 1)
ax.scatter(0.626, df4.iloc[wd]['rflux']/z2 + df1.iloc[a]['rflux']/z, s = 7, c = 'g',  marker = 'o',alpha = 1)
ax.scatter(0.767, df4.iloc[wd]['iflux']/z2 + df1.iloc[a]['iflux']/z, s = 7, c = 'g',  marker = 'o',alpha = 1)
ax.scatter(0.910, df4.iloc[wd]['zflux']/z2 + df1.iloc[a]['zflux']/z, s = 7, c = 'g',  marker = 'o',alpha = 1)

ax.scatter(0.1528, df4.iloc[wd]['Fflux']/z2, s = 7, c = 'b',  marker = 'o',alpha = 0.3, label ='WDmodel'+ ' ' + wd2 + 'K' +' ' + wd3)
ax.scatter(0.2271, df4.iloc[wd]['Nflux']/z2, s = 7, c = 'b',  marker = 'o',alpha = 0.3)
ax.scatter(0.356, df4.iloc[wd]['uflux']/z2, s = 7, c = 'b',  marker = 'o',alpha = 0.3)
ax.scatter(0.483, df4.iloc[wd]['gflux']/z2, s = 7, c = 'b',  marker = 'o',alpha = 0.3)
ax.scatter(0.626, df4.iloc[wd]['rflux']/z2, s = 7, c = 'b',  marker = 'o',alpha = 0.3)
ax.scatter(0.767, df4.iloc[wd]['iflux']/z2, s = 7, c = 'b',  marker = 'o',alpha = 0.3)
ax.scatter(0.910, df4.iloc[wd]['zflux']/z2, s = 7, c = 'b',  marker = 'o',alpha = 0.3)

ax.scatter(0.1528, df1.iloc[a]['Fflux']/z, s = 7, c = 'r',  marker = 'o',alpha = 0.3, label ='Optical SED model')
ax.scatter(0.2271, df1.iloc[a]['Nflux']/z, s = 7, c = 'r',  marker = 'o',alpha = 0.3)
ax.scatter(0.356, df1.iloc[a]['uflux']/z, s = 7, c = 'r',  marker = 'o',alpha = 0.3)
ax.scatter(0.483, df1.iloc[a]['gflux']/z, s = 7, c = 'r',  marker = 'o',alpha = 0.3)
ax.scatter(0.626, df1.iloc[a]['rflux']/z, s = 7, c = 'r',  marker = 'o',alpha = 0.3)
ax.scatter(0.767, df1.iloc[a]['iflux']/z, s = 7, c = 'r',  marker = 'o',alpha = 0.3)
ax.scatter(0.910, df1.iloc[a]['zflux']/z, s = 7, c = 'r',  marker = 'o',alpha = 0.3)

ax.errorbar(0.1528, df2.iloc[b]['Fflux'], yerr= df2.iloc[b]['e_Fflux'], c = 'purple',  marker = 'o',label = 'data', markersize = 2, alpha = 1,capsize=2, capthick=1)
ax.errorbar(0.2271, df2.iloc[b]['Nflux'], yerr= df2.iloc[b]['e_Nflux'], c = 'purple',  marker = 'o', markersize = 0.5, alpha = 1,capsize=2, capthick=1)
ax.errorbar(0.356, df2.iloc[b]['uflux'], yerr= df2.iloc[b]['e_uflux'], c = 'purple',  marker = 'o', markersize = 0.5, alpha = 1,capsize=2, capthick=1)
ax.errorbar(0.483,df2.iloc[b]['gflux'], yerr= df2.iloc[b]['e_gflux'], c = 'purple',  marker = 'o', markersize = 0.5, alpha = 1,capsize=2, capthick=1)
ax.errorbar(0.626, df2.iloc[b]['rflux'], yerr= df2.iloc[b]['e_rflux'], c = 'purple',  marker = 'o', markersize = 0.5, alpha = 1,capsize=2, capthick=1)
ax.errorbar(0.767, df2.iloc[b]['iflux'], yerr= df2.iloc[b]['e_iflux'], c = 'purple',  marker = 'o', markersize = 0.5, alpha = 1,capsize=2, capthick=1)
ax.errorbar(0.910, df2.iloc[b]['zflux'], yerr= df2.iloc[b]['e_zflux'], c = 'purple',  marker = 'o', markersize = 0.5, alpha = 1,capsize=2, capthick=1)



ax.set_yscale('log')
ax.set_xlabel('Wavelength' + '  ' + '(' + chr(956) + 'm' + ')')
ax.set_ylabel('F' + chr(957) + '  ' + '(mJy)')
ax.set_title('SED ' + 'of' + '  ' + df2.iloc[c]['name'])
#ax.set_facecolor("black")
plt.legend()
