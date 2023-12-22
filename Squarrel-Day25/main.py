import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20231221.csv")
grey_color = len(data["Primary Fur Color"] == "Gray")
print(grey_color)
red_color = len(data["Primary Fur Color"] == "Cinnamon")
print(red_color)
black_color = len(data["Primary Fur Color"] == "Black")
print(black_color)

data_dic = {
    "fur_color": ["Grey", "Cinnamon", "Black"],
    "count":[grey_color, red_color, black_color]
}

print(data_dic)

df = pandas.DataFrame(data_dic)
df.to_csv("squarriel_count.csv")