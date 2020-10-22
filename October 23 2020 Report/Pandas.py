# Create a DataFrame from a dictionary
import pandas as pd

# Pre-defined lists: country [names], Drives_Right [dr], Cars per capital[cpc]
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr = [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
my_dict = {'country':names, 'drives_right':dr, 'cars_per_cap':cpc}
cars = pd.DataFrame(my_dict)
print(cars)

## Specify the row labels
row_labels = ['US', 'AUS', 'JAP', 'IN', 'RU', 'MOR', 'EG']
cars.index = row_labels
print(cars)

## header = None
cars = pd.read_csv('./Data/cars.csv', header=None)
print(cars)
    
## header = 0
cars = pd.read_csv('./Data/cars.csv', header=0)
print(cars)
    
col_names = ['A', 'B', 'C']
cars = pd.read_csv('./Data/cars.csv', names = col_names)
print(cars)

col_names = ['A', 'B', 'C']
cars = pd.read_csv('./Data/cars.csv', names = col_names, na_values = {'A':['18', '45']})
print(cars)

out_csv = 'newcsvFile.csv'
cars.to_csv(out_csv)


cars = pd.read_csv('./Data/cars.csv', index_col = 0)
print(cars)

## show the type of data frame
print(type(cars))

## show the shape
print(cars.shape)

## show the columns
print(cars.columns)
for item in cars.columns:
    print(item)

## show the index
print(cars.index)
for item in cars.index:
    print(item)
    
print(cars.iloc[:3,:])
print(cars.loc['US'])
print(cars.head(3))  # Default: 5
print(cars.tail())
print(cars.info())

import numpy as np
cars.iloc[:3,0] = np.nan
print(cars)

cars['NewColumn'] = 0.0

## add column in DataFrame
for lab, row in cars.iterrows():
    cars.loc[lab, "COUNTRY"] = row['country'].upper()
print(cars)
## More efficient way: using .apply
cars['COUNTRY'] = cars['country'].apply(str.upper)
print(cars)


## series
print(cars['cars_per_cap'])
print(type(cars['cars_per_cap']))
## DataFrame
print(cars[['cars_per_cap']])
print(type(cars[['cars_per_cap']]))



## import data
import pandas as pd
import matplotlib.pyplot as plt

iris = pd.read_csv('./Data/iris.csv')
col_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
iris.columns = col_names
iris.head()

print(iris.shape)
iris.info()

iris.describe()
iris['sepal_length'].count()
iris[['sepal_length', 'petal_length']].count()
iris['sepal_length'].mean()
iris.mean()
iris.std()
iris.median()
iris.quantile(0.5)
print(iris['sepal_length'].max())
iris.min()
iris['species'].unique()

import pandas as pd
sales = pd.read_csv('./Data/sales.csv')
sales.head()

sales = pd.read_csv('./Data/sales.csv', index_col = 'Date', parse_dates=True)
sales.head()
sales.info()

print(sales.loc['2015-02-26 08:57:45'])
print(sales.loc['2015-02-26 08:57:45','Company'])
print(sales.iloc[0,0])
print(sales.loc['2015-2-5'])

print(sales.loc['2015-2-16':'2015-2-20'])
print(sales.loc['2015-2-4':'2015-2-5', 'Units'])

dateSTR = pd.to_datetime(['2015-02-11 20:03:08', '2015-02-11 21:23', '2015-02-11 21:31'])
print(dateSTR)

sales.reindex(dateSTR)
sales = sales.sort_index()

sales.reindex(dateSTR, method = 'nearest')

sales.reindex(dateSTR, method = 'backfill')

sales.resample('D').mean()

sales.resample('d').mean().max()

sales.resample('w').count()
sales.loc[:, 'Units'].resample('2W').sum()
sales = pd.read_csv('./Data/sales.csv', parse_dates = ['Date'])

# String method
sales.Company.str.upper()

## Substring matching
sales['Product'].str.contains('ware')

print(sales.Product[ sales['Product'].str.contains('ware') ])
print(sales.Product.str.contains('ware').sum())

## daytime: year:month:day:hour:minute:second
print(sales['Date'].dt.day)


# Case Study
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv('./Data/2011_climate.txt', header=None)
df.head()

## Add columns
columns_label = "Wban,date,Time,StationType,sky_condition,sky_conditionFlag,visibility,visibilityFlag," \
                "wx_and_obst_to_vision,wx_and_obst_to_visionFlag,dry_bulb_faren,dry_bulb_farenFlag,dry_bulb_cel," \
                "dry_bulb_celFlag,wet_bulb_faren,wet_bulb_farenFlag,wet_bulb_cel,wet_bulb_celFlag,dew_point_faren," \
                "dew_point_farenFlag,dew_point_cel,dew_point_celFlag,relative_humidity,relative_humidityFlag," \
                "wind_speed,wind_speedFlag,wind_direction,wind_directionFlag,value_for_wind_character," \
                "value_for_wind_characterFlag,station_pressure,station_pressureFlag,pressure_tendency," \
                "pressure_tendencyFlag,presschange,presschangeFlag,sea_level_pressure,sea_level_pressureFlag," \
                "record_type,hourly_precip,hourly_precipFlag,altimeter,altimeterFlag,junk"

columns_list = columns_label.split(',')
df.columns = columns_list
df.head()

## Remove some columns
columns_drop = "sky_conditionFlag,visibilityFlag,wx_and_obst_to_vision,wx_and_obst_to_visionFlag," \
               "dry_bulb_farenFlag,dry_bulb_celFlag,wet_bulb_farenFlag,wet_bulb_celFlag,dew_point_farenFlag," \
               "dew_point_celFlag,relative_humidityFlag,wind_speedFlag,wind_directionFlag,value_for_wind_character," \
               "value_for_wind_characterFlag,station_pressureFlag,pressure_tendencyFlag,pressure_tendency," \
               "presschange,presschangeFlag,sea_level_pressureFlag,hourly_precip,hourly_precipFlag,altimeter," \
               "record_type,altimeterFlag,junk"

columns_drop_list = columns_drop.split(',')
df_dropped = df.drop(columns_drop_list, axis = 'columns')
#df.head()
df_dropped.head()


## OPTIONAL for columns name
with open('./Data/2011_climate_label.txt', 'r') as fid:
    s = fid.read().split('\n')
    columns_label = s[1]
    columns_drop = s[4]
    print(columns_label, '\n', columns_drop)

print(df_dropped.date)

## Convert columns to pandas datetime object
# print(df_dropped.info())
# print(df_dropped.head())
## convert dtypes from int64 to str(object)
df_dropped['date'] = df_dropped['date'].astype('str')
## convert time -> hour+minute: 453 -> 0453 | 53 -> 0053
df_dropped['Time'] = df_dropped['Time'].apply(lambda x: '{:0>4}'.format(x))
## pandas datetime object
date_times = pd.to_datetime(df_dropped['date'] + df_dropped['Time'], format = '%Y%m%d%H%M')
## set_index
df_clean = df_dropped.set_index(date_times)
df_clean.head()
df_dropped.info()



## Read 'dry_bulb_faren' Temperature
print(df_clean.loc['2011.6.20 8AM':'2011.6.20 9AM', 'dry_bulb_faren'])


df_clean['dry_bulb_faren'] = pd.to_numeric(df_clean['dry_bulb_faren'], errors = 'coerce') #coerce: set 'M' to NaN
print(df_clean.loc['2011.6.20 8AM':'2011.6.20 9AM', 'dry_bulb_faren'])


df_clean['wind_speed'] = pd.to_numeric(df_clean['wind_speed'], errors='coerce')
df_clean['dew_point_faren'] = pd.to_numeric(df_clean['dew_point_faren'], errors='coerce')
df_clean.head()


print(df_clean['dry_bulb_faren'].median())
print(df_clean.loc['2011-Apr':'2011-Jun','dry_bulb_faren'].max())
print(df_clean.loc['2011-Jan', 'dry_bulb_faren'].count())

daily_mean_2011 = df_clean.resample('D').mean()
print(daily_mean_2011)


# dataframe -> series -> numpy array, NOTICE: values is attribute, not method
daily_temperature_2011 = daily_mean_2011['dry_bulb_faren'].values
print(type(daily_mean_2011['dry_bulb_faren']))
print(type(daily_temperature_2011))

## add another dataset: weather_data_2010.csv
df_climate = pd.read_csv('./Data/2010_climate.csv', header = 0)
print(df_climate.head())
df_climate2 = df_climate.set_index('Date')
print(df_climate2.head())
df_climate3 = df_climate2.reset_index()
print(df_climate3.head())

df_climate['Date'] = pd.to_datetime(df_climate['Date'], format = '%Y%m%d %H:%M', errors='coerce')
df_climate = df_climate.set_index('Date')
df_climate.head()








