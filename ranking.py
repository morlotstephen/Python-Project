import pandas as pd
from pandas.api.types import is_numeric_dtype
import shortuuid

# I) Importer les fichiers csv :

possession = pd.read_csv("top_5_leagues_possession_2017-2025.csv")
gca = pd.read_csv("top_5_leagues_gca_2017-2025.csv")
playing_time = pd.read_csv("top_5_leagues_playingtime_2017-2025.csv")
shooting = pd.read_csv("top_5_leagues_shooting_2017-2025.csv")
passing = pd.read_csv("top_5_leagues_passing_2017-2025.csv")
country_code = pd.read_csv("country.csv")
final_scoring = pd.DataFrame()

# Créations des ID ;

gca["player_id"] = [shortuuid.uuid() for _ in range(len(gca))]
reference_players = gca[["player", "team", "season", "league", "player_id"]].drop_duplicates()
playing_time = playing_time.merge(reference_players, on=["player", "team", "season", "league"], how="left")
shooting = shooting.merge(reference_players, on=["player", "team", "season", "league"], how="left")
possession = possession.merge(reference_players, on=["player", "team", "season", "league"], how="left")
passing = passing.merge(reference_players, on=["player", "team", "season", "league"], how="left")


# II) Transformer les nationalités afin qu'elles soient clean :

dict_country = dict(zip(country_code["Code"], country_code["Country"]))
gca["nationality"] = gca["nationality"].map(dict_country)

# III) Sélectionner uniquement les postes principaux :

# 1) Séparer la colonne position et supprimer la 2e colonne du split :

gca_position = gca['position'].str.split(",", expand=True)
gca_position.columns = ["Position", "Second Position"]

# 2) Ajout des nouvelles colonnes :

gca = pd.concat([gca, gca_position], axis=1)

playing_time['minutes'] = playing_time['minutes'].str.replace(',', '.', regex=False)
playing_time['minutes'] = pd.to_numeric(playing_time['minutes'], errors='coerce')
print(playing_time['minutes'].dtype)


# IV) Supprimer les colonnes 'position' et 'Second Position' :

gca.drop(columns=['position'], inplace=True)
gca.drop(columns=['Second Position'], inplace=True)
playing_time.drop(columns=['minutes_per_start'], inplace=True)

# V) Création du scoring :

# 1) Liste des catégories :

categories = [
    'gca',
    'playing_time',
    'shooting',
    'possession',
    'passing'
]

# 2) Liste des statistiques de chaque catégorie :

gca_stats = [
    'player_id',
    'player',
    'nationality',
    'Position',
    'team',
    "age",
    "sca",
    "sca_per90",
    "sca_fouled",
    "sca_defense",
    "gca",
    "gca_shots",
    "gca_fouled",
    "gca_defense"
]

playing_time_stats = [
    'player_id',
    "player",
    "team",
    "games",
    "minutes",
    "games_starts",
    "minutes_per_start",
    "games_complete"
]

shooting_stats = [
    'player_id',
    "player",
    "team",
    "goals",
    "shots",
    "shots_on_target",
    "goals_per_shot_on_target",
    "xg",
    "npxg"
]

possession_stats = [
    'player_id',
    "player",
    "team",
    "touches",
    "touches_att_3rd",
    "touches_att_pen_area",
    "take_ons_won",
    "take_ons_won_pct",
    "take_ons_tackled",
    "take_ons_tackled_pct",
    "carries_distance",
    "carries_progressive_distance",
    "carries_into_final_third",
    "carries_into_penalty_area",
    "miscontrols",
    "dispossessed",
    "passes_received",
    "progressive_passes_received"
]

passing_stats = [
    'player_id',
    "player",
    "team",
    "passes",
    "passes_completed",
    "passes_pct",
    "passes_total_distance",
    "passes_progressive_distance"
]

for category in categories:
    if category == 'gca':
        gca_scoring = gca
        cols_excluded = ['player', 'nationality', 'Position', 'team', 'age']
        sum_of_cols = [
            col for col in gca_scoring.columns if is_numeric_dtype(gca_scoring[col]) and col not in cols_excluded
        ]
        for stat in gca_stats:
            if stat in gca_scoring.columns and stat not in cols_excluded:
                if is_numeric_dtype(gca_scoring[stat]):
                    gca_scoring[stat] = gca_scoring[stat] / gca_scoring[stat].max()
                else:
                    print('No column finded')
            else:
                print("Aucune stat trouver dans le tableau")
        gca_scoring['Performance'] = gca_scoring[sum_of_cols].sum(axis=1)
        gca_scoring.to_csv('gca_scoring.csv', index=False)
        print(gca_scoring['Performance'].head(5))
        print(gca_scoring.iloc[:, :5].head(5))
    elif category == 'playing_time':
        playing_time_scoring = playing_time
        cols_excluded = ['player', 'team', 'minutes_per_start', 'season', 'league']
        sum_of_cols = [
            col for col in playing_time_scoring.columns if is_numeric_dtype(playing_time_scoring[col]) and col not in cols_excluded
        ]
        for stat in playing_time_stats:
            if stat in playing_time_scoring.columns and stat not in cols_excluded:
                if is_numeric_dtype(playing_time_scoring[stat]):
                    playing_time_scoring[stat] = playing_time_scoring[stat] / playing_time_scoring[stat].max()
                else:
                    print('No column finded')
            else:
                print("Aucune stat trouver dans le tableau")
        playing_time_scoring['Impact'] = playing_time_scoring[sum_of_cols].sum(axis=1)
        playing_time_scoring.to_csv('playing_time_scoring.csv', index=False)
        print(playing_time_scoring['Impact'].head(5))
        print(playing_time_scoring.iloc[:, :5].head(5))
    elif category == 'shooting':
        shooting_scoring = shooting
        cols_excluded = ['player', 'team', 'season', 'league']
        sum_of_cols = [
            col for col in shooting_scoring.columns if is_numeric_dtype(shooting_scoring[col]) and col not in cols_excluded
        ]
        for stat in shooting_stats:
            if stat in shooting_scoring.columns and stat not in cols_excluded:
                if is_numeric_dtype(shooting_scoring[stat]):
                    shooting_scoring[stat] = shooting_scoring[stat] / shooting_scoring[stat].max()
                else:
                    print('No column finded')
            else:
                print("Aucune stat trouver dans le tableau")
        shooting_scoring['Finition'] = shooting_scoring[sum_of_cols].sum(axis=1)
        shooting_scoring.to_csv('shooting_scoring.csv', index=False)
        print(shooting_scoring['Finition'].head(5))
        print(shooting_scoring.iloc[:, :5].head(5))
    elif category == 'possession':
        possession_scoring = possession
        cols_excluded = ['player', 'team', 'season', 'league']
        sum_of_cols = [
            col for col in possession_scoring.columns if is_numeric_dtype(possession_scoring[col]) and col not in cols_excluded
        ]
        for stat in possession_stats:
            if stat in possession_scoring.columns and stat not in cols_excluded:
                if is_numeric_dtype(possession_scoring[stat]):
                    possession_scoring[stat] = possession_scoring[stat] / possession_scoring[stat].max()
                else:
                    print('No column finded')
            else:
                print("Aucune stat trouver dans le tableau")
        possession_scoring['Dribble'] = possession_scoring[sum_of_cols].sum(axis=1)
        possession_scoring.to_csv('possession_scoring.csv', index=False)
        print(possession_scoring['Dribble'].head(5))
        print(possession_scoring.iloc[:, :5].head(5))
    elif category == 'passing':
        passing_scoring = passing
        cols_excluded = ['player', 'team', 'season', 'league']
        sum_of_cols = [
            col for col in passing_scoring.columns if is_numeric_dtype(passing_scoring[col]) and col not in cols_excluded
        ]
        for stat in passing_stats:
            if stat in passing_scoring.columns and stat not in cols_excluded:
                if is_numeric_dtype(passing_scoring[stat]):
                    passing_scoring[stat] = passing_scoring[stat] / passing_scoring[stat].max()
                else:
                    print('No column finded')
            else:
                print("Aucune stat trouver dans le tableau")
        passing_scoring['Creativity'] = passing_scoring[sum_of_cols].sum(axis=1)
        passing_scoring.to_csv('passing_scoring.csv', index=False)
        print(passing_scoring['Creativity'].head(5))
        print(passing_scoring.iloc[:, :5].head(5))
    else:
        print("Aucun tableau trouvé")

# 3) Création du Tableau de scoring Finale :

final_scoring = gca[['player_id','player','nationality','Position','team','season','league']].copy()

final_scoring = final_scoring.merge(
    playing_time_scoring[['player_id','Impact']], on='player_id', how='left'
).merge(
    shooting_scoring[['player_id','Finition']], on='player_id', how='left'
).merge(
    possession_scoring[['player_id','Dribble']], on='player_id', how='left'
).merge(
    passing_scoring[['player_id','Creativity']], on='player_id', how='left'
)

# pondération
final_scoring_cols = ['Performance', 'Impact', 'Finition', 'Dribble', 'Creativity']
final_scoring['Performance'] = gca['Performance']
final_scoring['Impact'] = final_scoring['Impact']
final_scoring['Finition'] = final_scoring['Finition']
final_scoring['Dribble'] = final_scoring['Dribble']
final_scoring['Creativity'] = final_scoring['Creativity']
final_scoring['Note Globale'] = final_scoring[final_scoring_cols].sum(axis=1)

final_scoring.to_csv('final.csv', index=False)
ranking = final_scoring.copy()
ranking['rank'] = final_scoring['Note Globale'].rank(
    ascending=False,   # plus la note est haute, meilleur est le rang
    method='min'       # si égalité, tous les ex-aequo prennent le même rang
).astype(int)
