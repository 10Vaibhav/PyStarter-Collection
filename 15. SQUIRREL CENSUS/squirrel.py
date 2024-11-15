import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

colors = data["Primary Fur Color"]
unique_color = colors.unique()
print(unique_color)

Grays = len(data[data["Primary Fur Color"] == "Gray"])
Blacks = len(data[data["Primary Fur Color"] == "Black"])
Cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])

data_dict = {
    "Fur Color": ["gray", "black", "cinnamon"],
    "Count": [Grays, Blacks, Cinnamon]
}

info1 = pandas.DataFrame(data_dict)

info1.to_csv("squirrel_count.csv")

