# with open("weather_data.csv - weather_data.csv", mode="r") as file:
#     data = file.readlines()
#     print(data)

import csv

with open("weather_data.csv - weather_data.csv", mode="r") as file:
    data = csv.reader(file)
    temperatures = []
    next(data, None)
    for row in data:
        temperatures.append(int(row[1]))
    print(temperatures)
