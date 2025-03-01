import pandas as pd

# Serie
nba_players = pd.read_csv('~/Descargas/nba_players_a.csv', usecols=['Name']).squeeze()

single_value = nba_players.iloc[100]

print(single_value)

multi_value = nba_players.iloc[:50].tolist()

print(multi_value)
print(len(multi_value))
