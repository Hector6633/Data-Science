import pandas as pad

game_data = pad.read_csv("sale_data.csv", header=0, sep=",")
print(game_data)

maximum_profit_game = max(86, 120, 68, 92, 256, 20, 15, 500, 1200, 5000)
print(maximum_profit_game)

print(game_data.info())

game_data.dropna(axis=0, inplace=True)
print(game_data)

print("\n",game_data.describe())
