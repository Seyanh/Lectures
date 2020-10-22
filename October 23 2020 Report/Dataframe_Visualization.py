import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv('./Data/world-happiness-report-2019.csv')
print(df.head(3))

df.rename(columns={"Country (region)": "Country", "Log of GDPnper capita": "Log_GDP_per_capita",
                  "Healthy lifenexpectancy":"Health_life_expect"},inplace=True)
print(df.columns)

df1 = df[:5]
df1.plot('Country',['Corruption','Freedom','Generosity','Social support'],kind = 'bar')

df1=df[:5]
df1.plot('Country',[7,6,8,5],kind = 'bar')

df1=df[:5]
df1.plot('Country',['Corruption','Freedom','Generosity','Social support'],kind = 'line')

df[:5].plot(x='Country',kind='box')
df.plot(x='Corruption',y='Freedom',kind='scatter',color='r')

plt.show()

