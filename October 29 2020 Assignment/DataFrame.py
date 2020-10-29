import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)

print("\n" + "--" * 20 + "\n 1. Create Dataframe: \n")

df = pd.read_csv('./Data/world-happiness-report-2019.csv')
print(df.head(3))

df.rename(columns={"Country (region)": "Country", "Log of GDPnper capita": "Log_GDP_per_capita",
				   "Healthy lifenexpectancy":"Health_life_expect"}, inplace=True)
print(df.columns)

print("\n" + "--" * 20 + "\n 2. Pandas bar plot: \n")

df1 = df[:5]
df1.plot('Country', ['Corruption', 'Freedom', 'Generosity', 'Social support'], kind='bar')
plt.show()

print("\n" + "--" * 20 + "\n 3. Pandas Line Chart: \n")

df1 = df[:5]
df1.plot('Country', ['Corruption', 'Freedom', 'Generosity', 'Social support'], kind='line')
plt.show()

print("\n" + "--" * 20 + "\n 4. Pandas Box Plot: \n")

df[:5].plot(x='Country', kind='box')
plt.show()

print("\n" + "--" * 20 + "\n 5. Pandas Scatter Plot: \n")

df.plot(x='Corruption', y='Freedom', kind='scatter', color='r')
plt.show()

from pandas.plotting import table
# df1 = df[:5]
df1 = df.loc[:5, ['Country', 'Corruption', 'Freedom', 'Generosity', 'Social support']]
ax = df1.plot('Country', ['Corruption', 'Freedom', 'Generosity', 'Social support'], kind='bar', title='Bar Plot', legend=None)
table(ax, np.round(df1.describe(), 2), loc='upper right')
plt.show()

print("\n" + "--" * 20 + "\n 6. Pandas Plot set x and y range or xlims & ylims: \n")

df1 = df[:20]
df1['Freedom'].plot(kind='line', xlim=(0, 20), ylim=(0, 100))
plt.show()

print("\n" + "--" * 20 + "\n 7. Pandas plots x-ticks and y-ticks: \n")

df[:20]['Freedom'].plot(kind='line', xlim=(0, 20), ylim=(0, 100), color='red',
						xticks=([0, 10, 15, 20]), yticks=([0, 50, 70, 100]), title='xticks')
plt.show()

df[:20]['Freedom'].plot(kind='line', xlim=(0, 20), ylim=(0, 100), color='red',
						xticks=([w*1 for w in range(20)]), yticks=([w*10 for w in range(40)]))
plt.show()

print("\n" + "--" * 20 + "\n 8. Text Labels on axis: \n")

ax = df[:20]['Freedom'].plot(kind='line', xlim=(0, 20), ylim=(0, 100), color='red',
							 xticks=([0, 10, 20]), yticks=([w*30 for w in range(40)]))
ax.set_xticklabels(['Low', 'Med', 'High'])
plt.show()

print("\n" + "--" * 20 + "\n 9. Log Scaling: \n")

df[:20]['Freedom'].plot(kind='line', xlim=(0, 1000), ylim=(0, 100), color='red', logx=True)
plt.show()

print("\n" + "--" * 20 + "\n 10. Pandas plot line style: \n")

df1 = df[:20]
df1['Freedom'].plot(kind='line', xlim=(0, 20), ylim=(0, 100), style='go')
plt.show()

print("\n" + "--" * 20 + "\n 11. Pandas Stacked Bar: \n")

df1 = df[:20]
df1['Freedom'].plot(kind='bar', xlim=(0, 20), ylim=(0, 100), stacked=True)
plt.show()

print("\n" + "--" * 20 + "\n 12. Pandas Grid Lines: \n")

df.plot(x='Corruption', y='Freedom', kind='scatter', color='r', grid=True)
plt.show()

print("\n" + "--" * 20 + "\n 13. Pandas Subplots: \n")

df[:10].plot(kind='hist', subplots=True, layout=(4, 3))
plt.show()

print("\n" + "--" * 20 + "\n 14. Title above all subplots: \n")

df[:10].plot(kind='hist', subplots=True, layout=(3, 4), legend=False,
			 title=['Ladder', 'SD of Ladder', 'Positive affect', 'Negative affect', 'Social support',
					'Freedom', 'Corruption', 'Generosity', 'Log_GDP_per_capita', 'Health_Life_expect'])
plt.show()

print("\n" + "--" * 20 + "\n 15. Pandas colormap: \n")

df1 = df[:5]
df1.plot('Country', ['Corruption', 'Freedom', 'Generosity', 'Social support'], kind='area', colormap='gist_rainbow')
plt.show()

print("\n" + "--" * 20 + "\n 16. Pandas Plot Groupby count: \n")

df.groupby('Country')['Country'].agg('count').plot(kind='pie', title='Group-By Country')
plt.show()

print("\n" + "--" * 20 + "\n 17. Pandas Groupby Plot Sum: \n")

df.groupby('Healthy life\nexpectancy')['Healthy life\nexpectancy'].agg(lambda x: sum(x)).plot(kind='pie', title='High Health Life Expectancy')
plt.show()
