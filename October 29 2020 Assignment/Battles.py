"""
1. Get to know the data
"""

print("\n" + "--" * 20 + "\n 1. Get to know the data: \n")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)

df = pd.read_csv("./Data/battles.csv")
print(df.head())

battles = df[['name', 'year', 'battle_number', 'attacker_king', 'defender_king', 'attacker_outcome',
			  'battle_type', 'attacker_1', 'defender_1',  'attacker_size', 'defender_size',
			  'attacker_commander', 'defender_commander', 'summer', 'location', 'region']].copy()
battles.set_index('battle_number', inplace=True)
print(battles.head())

battles['year'].value_counts().sort_index().plot.bar(figsize=(8, 6))
plt.xlabel("year")
plt.ylabel("battle_number")
plt.xticks(rotation=0)

plt.show()
plt.cla()

"""
2. The "wolf and lion" controversy
"""

print("\n" + "--" * 20 + "\n 2. The 'wolf' and 'lion' controversy: \n")

battles_298 = battles[battles['year'] == 298]
print(battles_298)
print(battles_298['name'])
print(battles_298[['attacker_king', 'defender_king', 'attacker_outcome', 'attacker_size', 'defender_size']])

all_size = battles_298['attacker_size'] + battles_298['defender_size']

df_298 = battles_298.copy()
df_298['all_size'] = all_size
print(df_298[df_298['all_size'] >= 15000])

# battles_298['all_size'] = battles_298['attacker_size'] + battles_298['defender_size']

df_298.set_index('name').all_size.plot.barh(figsize=(8, 6))
plt.xlabel('battles_size')
plt.show()
plt.cla()

"""
3. Five kings
"""

print("\n" + "--" * 20 + "\n 3. Five kings: \n")


battles_299 = battles.loc[battles['year'] == 299]
print(battles_299.head())

battles_299.set_index('name', inplace=True)
print(battles_299.head())

print(battles_299.loc['The Red Wedding', 'attacker_commander'])

battles_kings = battles_299.loc[:, ['attacker_king', 'defender_king']]
print(battles_kings.head())

set(battles_kings.attacker_king.unique()) | set(battles_kings.defender_king.unique())

attacker_num = battles_299.loc[:, 'attacker_king'].value_counts()
defender_num = battles_299.loc[:, 'defender_king'].value_counts()
attacker_num.add(defender_num, fill_value=0).plot.barh(figsize=(8, 6))  # add()函数中的fill_value参数可以解决不重叠位置相加出现缺失值的现象
plt.xlabel("Battle_number")
plt.ylabel("Kings")

plt.show()
plt.cla()

battle_299_vital = battles_299.loc[["Siege of Storm's End", "Battle of the Blackwater", "The Red Wedding"], :]
print(battle_299_vital)

"""
4 Winter is coming
"""

print("\n" + "--" * 20 + "\n 4 Winter is coming: \n")

battles_300 = battles.iloc[list(battles['year'] == 300)]
print(battles_300.head())
print(battles.iloc[0])
print(battles.iloc[[0]])
print(battles.iloc[0:2, 0:2])
print(battles.iloc[list(battles['summer'] == 0.0)].head(5))

all_size_300 = battles_300.attacker_size.add(battles_300.defender_size, fill_value=0)
df_300 = battles_300.copy()
df_300['all_size_300'] = all_size_300
print(df_300.iloc[list(df_300.all_size_300 >= 15000)])

df_300.set_index('name').iloc[:,-1].plot.barh(figsize=(8, 6))
plt.xlabel('battles_size')
plt.show()

battles.iloc[battles.index == 28, 2] = 'Mance Rayder'
battles.loc[battles.index == 28, 'defender_king'] = 'Stannis Baratheon'
print(battles.iloc[[27]])
