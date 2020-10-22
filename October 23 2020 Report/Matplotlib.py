import matplotlib.pyplot as plt
import pandas as pd

cars = pd.read_csv('./Data/cars.csv', index_col=0)
print(cars)

cpc = cars['cars_per_cap'].values
xlabel = cars.index.values
ax = plt.bar(xlabel, cpc)
plt.savefig('cpc.pdf')
plt.show()

cpc = cars['cars_per_cap']
ax = cpc.plot.bar(rot = 90)
ax.set_xlabel('Country')
ax.set_ylabel('Cars per capital')
plt.show()

ax = cars['cars_per_cap'].plot.bar()
ax.set(xlabel='Country', ylabel='cars per capital', title = 'cars')
plt.show()




## import data
import pandas as pd
import matplotlib.pyplot as plt
iris = pd.read_csv('./Data/iris.csv')
col_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
iris.columns = col_names


iris.plot(x='sepal_length', y = 'sepal_width')
plt.show()

iris.plot(x='sepal_length', y = 'sepal_width',kind='scatter')
plt.xlabel('sepal length (cm)')
plt.ylabel('sepal width (cm)')
plt.show()


iris.plot(y = 'sepal_length', kind='box')
plt.ylabel('sepal length(cm)')
plt.show()

iris[['sepal_length', 'sepal_width']].plot(kind='box', subplots=True)
plt.show()

iris.sepal_length.plot(kind='box')

iris.plot(y = 'sepal_length', kind='hist')
plt.xlabel('sepal length (cm)')
plt.show()

## Options for histogram
# bins: integer, number of bins
# range: tuple, (min, max)
# density: boolean, normalized to 1
# cumulative: boolean, Compute Cumulative Distribution Function
iris.plot(y = 'sepal_length', kind='hist', bins=30, range=(5, 8), density=True)
plt.xlabel('sepal length (cm)')
plt.show()


iris['sepal_length'].hist(bins = 30, range=(5,8))
iris['sepal_length'].plot(bins = 30, range=(5,8), kind='hist')


import matplotlib.pyplot as plt
import pandas as pd

plt.cla()

sp500 = pd.read_csv('./Data/sp500.csv', parse_dates = True, index_col = 0)
# line plot
sp500['Close'].plot(title='S&P 500 Index')
plt.ylabel('Closing Price (USD)')
plt.show()


sp500.loc['2015-01-01':'2015-03-01', 'Close'].count()

sp500.loc['2015-01-01':'2015-03-01', 'Close'].plot(title='S&P 500', style='k.-')
plt.ylabel('Closing Price (USD)')
plt.show()

# subplots
sp500.loc['2015', ['Close', 'Volume']].plot(subplots = True)
plt.show()




