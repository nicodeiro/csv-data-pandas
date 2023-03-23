# with open("weather_data.csv") as datas_file:
#     data = datas_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas

data = pandas.read_csv("weather_data.csv")

# DataFrame vs Series
print(type(data))
print(type(data["temp"]))

# Dictionnary & List
data_dict = data.to_dict()
print(data_dict)
temp_list = data["temp"].tolist()
print(temp_list)

# Average & Max
print(data["temp"].mean())
print(data["temp"].max())

# Get Data in Columns
print(data["condition"])
print(data.condition)

# Get Data in Rows
print(data[data.day == "Monday"])
print(data[data.temp == data["temp"].max()])
monday = data[data.day == "Monday"]
monday_temp = int(monday.temp)
monday_temp_F = (monday_temp * 9/5) + 32
print(monday_temp_F)

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")

# Create a dataframe from csv file
data = pandas.read_csv("Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrels_count.csv")

