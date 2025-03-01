import pandas as pd

# Serie
nba_players = pd.read_csv('~/Descargas/nba_players_a.csv', usecols=['DRtg']).squeeze()

some_values = nba_players.iloc[:5]

addition_1 = some_values + 10
addition_2 = some_values.add(10)

print(some_values)
print(addition_1)
print(addition_2)

substraction_1 = some_values - 10
substraction_2 = some_values.sub(10)

print(substraction_1)
print(substraction_2)