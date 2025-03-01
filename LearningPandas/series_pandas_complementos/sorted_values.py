import pandas as pd

# Serie
nba_players = pd.read_csv('~/Descargas/nba_players_a.csv', usecols=['Name']).squeeze()

result_from_a = nba_players.sort_values()
result_from_z = nba_players.sort_values(ascending=False)

print(f'De la A a la Z: {result_from_a}')
print(f'De la Z a la A: {result_from_z}')
