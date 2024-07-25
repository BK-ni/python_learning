# # with open("weather_data.csv") as data_file:
# #     data = data_file.readlines()
# #     print(data)
#
# # import csv
# #
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperature = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperature.append(int(row[1]))
# #
# # print(temperature)
#
# import pandas
# #
# # data = pandas.read_csv("weather_data.csv")
# # print(data["temp"])
#
# # data_dict = data.to_dict()
# # temp_list = data["temp"].to_list()
# # temp_avg = data["temp"].mean()
# # print(data)
# # print(data[data.temp == data.temp.max()])
# # monday = data[data.day == "Monday"]
# # print(monday.temp * 9 / 5 + 32)
#
# data_dict = {
#     "student": ["Amy", "James", "Will"],
#     "scores": [100, 90, 85]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
# print(data)


#
#
# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240719.csv")

# for i in data["Primary Fur Color"]:
#     if i == "Gray":
#         gray += 1
#     elif i == "Cinnamon":
#         cinnamon += 1
#     elif i == "Black":
#         black += 1
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240719.csv")
gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])

squirrel_dict = {
    "Fur color": ["Gray", "Red", "Black"],
    "Count": [gray_squirrel_count, cinnamon_squirrel_count, black_squirrel_count],
}

squirrel_count = pandas.DataFrame(squirrel_dict)
squirrel_count.to_csv("squirrel_count.csv")
print(squirrel_count)
