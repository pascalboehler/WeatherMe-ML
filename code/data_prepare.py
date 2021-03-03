import numpy as np
import pandas as pd

print("#### LOADING THE RAW DATASET FROM DISK ####")

path = "./weather_data_raw/"

humidity_raw = pd.read_csv(path + 'humidity.csv', index_col = 0)
pressure_raw = pd.read_csv(path + 'pressure.csv', index_col = 0)
temperature_raw = pd.read_csv(path + 'temperature.csv', index_col = 0)
wind_direction_raw = pd.read_csv(path + 'wind_direction.csv', index_col = 0)
wind_speed_raw = pd.read_csv(path + 'wind_speed.csv', index_col = 0)
weather_description_raw = pd.read_csv(path + 'weather_description.csv', index_col = 0)
city_attributes_raw = pd.read_csv(path + 'city_attributes.csv', index_col = 0)

print("#### SPLITTING THE DATASET ####")

cities = city_attributes_raw.index.values

humidity = {}
pressure = {}
temperature = {}
wind_direction = {}
wind_speed = {}
weather_description = {}
city_attributes = {}

for city in cities:
    humidity[city] = pd.DataFrame(humidity_raw[city]).rename(columns={city: 'humidity'})
    pressure[city] = pd.DataFrame(pressure_raw[city]).rename(columns={city: 'pressure'})
    temperature[city] = pd.DataFrame(temperature_raw[city]).rename(columns={city: 'temperature'})
    wind_direction[city] = pd.DataFrame(wind_direction_raw[city]).rename(columns={city: 'wind_direction'})
    wind_speed[city] = pd.DataFrame(wind_speed_raw[city]).rename(columns={city: 'wind_speed'})
    weather_description[city] = weather_description_raw[city]

print("done")

print("#### CONVERTING DATA FROM KELVIN TO CELCIUS ####")

for city in cities:
    for index, val in enumerate(temperature[city]['temperature']):
        temperature[city]['temperature'][index] = val - 273.15

print("done")

print("#### REBUILDING THE DATASET SPLITTED IN CITIES ####")
dataset = {}
for city in cities:
    dataset[city] = pd.concat([temperature[city], humidity[city], pressure[city], wind_speed[city], wind_direction[city]], axis=1)

print("done")

print("#### WRITING FILES TO DISK ####")
for city in dataset:
    filename = "weather_data/" + city.lower().replace(" ", "-") + "_weather_data_dataset.csv"
    dataset[city].to_csv(filename, encoding='utf-8')
    print("Wrote " + filename + " to disk")

print("done")

print("Dataset successfully prepared for further processing!")