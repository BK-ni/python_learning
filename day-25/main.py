# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperature = []
    for row in data[1:]:
        temperature.append(row[1])
        print(temperature)
