import pandas as pd

def comvert_upper(value):
    return value.upper()

nba_players = pd.read_csv('~/Descargas/nba_players_a.csv', sep=',', usecols=['Name']).squeeze()
result = nba_players.apply(comvert_upper).head()

print(result)