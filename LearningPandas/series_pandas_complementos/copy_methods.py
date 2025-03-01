import pandas as pd

nba_players_df = pd.read_csv('~/Descargas/nba_players_a.csv', sep=',', usecols=['Name']).head(5)

nba_player_copy = nba_players_df.squeeze().copy()
nba_player_view = nba_players_df.squeeze()


nba_player_copy.iloc[0] = 'Lerma'
nba_player_view.iloc[0] = 'UTVT'
print(nba_players_df)
print(nba_player_copy)
print(nba_player_view)