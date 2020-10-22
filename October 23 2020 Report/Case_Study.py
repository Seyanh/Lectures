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


# Practise
# add another dataset: weather_data_2010.csv
df_climate = pd.read_csv('./Data/2010_climate.csv', header = 0)
print(df_climate.head())
df_climate2 = df_climate.set_index('Date')
print(df_climate2.head())
df_climate3 = df_climate2.reset_index()
print(df_climate3.head())

df_climate['Date'] = pd.to_datetime(df_climate['Date'], format = '%Y%m%d %H:%M', errors='coerce')
df_climate = df_climate.set_index('Date')
df_climate.head()


daily_climate = df_climate.resample('D').mean()
print(daily_climate)
# daily_temperature_climate = daily_climate.reset_index()
# daily_temperature_climate.head()
#daily_temperature_climate =
daily_temperature_2010 = daily_climate['Temperature']


daily_mean_2011 = df_clean.resample('D').mean()

print(np.mean(daily_temperature_2011 - daily_temperature_2010))

is_sky_clear = df_clean['sky_condition'] == 'CLR'
sunny = df_clean[is_sky_clear]
sunny.head()

sunny_daily_max = sunny.resample('D').mean()
sunny_daily_max.head()
is_sky_overcast = df_clean['sky_condition'].str.contains('OVC')
overcast = df_clean.loc[is_sky_overcast]
overcast_daily_max = overcast.resample('D').mean()

# Calculate the mean of sunny_daily_max
sunny_daily_max_mean = sunny_daily_max.mean()
# Calculate the mean of overcast_daily_max
overcast_daily_max_mean = overcast_daily_max.mean()
# Print the difference (sunny minus overcast)
print(sunny_daily_max_mean - overcast_daily_max_mean)


# Visualization
# Show the visibility and dry_bulb_faren in figure
weekly_mean = df_clean['dry_bulb_faren'].resample('W').mean()
weekly_mean.plot()
plt.show()

monthly_max = df_clean[['dew_point_faren', 'dry_bulb_faren']].resample('M').max()
monthly_max.plot(kind='hist', bins=8, alpha=0.5, subplots=True)
plt.show()
