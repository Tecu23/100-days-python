import pandas as pd

data = pd.read_csv("weather_data.csv")
data_dict = data.to_dict()
data_list = data["temp"].to_list()

average = sum(data_list) / len(data_list)
average_v2 = data["temp"].mean()
print(data, average, average_v2, data_dict)


# Getting data in row
row_data = data[data["temp"] == data["temp"].max()]

print(row_data)
