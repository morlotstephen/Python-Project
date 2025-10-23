import asyncio
from crawl4ai import AsyncWebCrawler
from bs4 import BeautifulSoup
import csv

def crawl_get(url: str):
    async def _run():
        async with AsyncWebCrawler() as crawler:
            return await crawler.arun(url=url)
    return asyncio.run(_run())

def stats(category):
    # Liste des saisons à parcourir
    years = range(2017, 2025)
    
    leagues = {
        "Premier-League": "9",
        "La-Liga": "12",
        "Bundesliga": "20",
        "Serie-A": "11",
        "Ligue-1": "13"
    }

    # Liste pour stocker toutes les données de toutes les saisons
    all_players = []


    for league_name, league_id in leagues.items():
        
        for year in years:
            url = str(f"https://fbref.com/en/comps/{league_id}/{year}-{year+1}/{category}/{year}-{year+1}-{league_name}-Stats")
            season = f"{year}-{year+1}"
            
            print(f"scraping : {league_name} / {season} / {category}...")
            
            
            response = crawl_get(url)

            content_html = response.html
            soup = BeautifulSoup(content_html, "html.parser")
            
            # Récupérer la table et les lignes
            player_table = soup.find("table", class_="min_width sortable stats_table shade_zero now_sortable sticky_table eq2 re2 le2")
            player_rows = player_table.find_all("tr", {"data-row": True})
            
            
            if category == "gca":
                data_stats = [
                    "player",
                    "nationality",
                    "position",
                    "team",
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
            elif category == "shooting":
                data_stats = [
                    "player",
                    "team",
                    "goals",
                    "shots",
                    "shots_on_target",
                    "goals_per_shot_on_target",
                    "xg",
                    "npxg"
                    ]
            elif category == "playingtime":
                data_stats = [
                    "player",
                    "team",
                    "games",
                    "minutes",
                    "games_starts",
                    "minutes_per_start",
                    "games_complete"
                    ]
            elif category == "possession":
                data_stats = [
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
            elif category == "passing":
                data_stats = [
                    "player",
                    "team",
                    "passes",
                    "passes_completed",
                    "passes_pct",
                    "passes_total_distance",
                    "passes_progressive_distance"
                    ]
            else:
                data_stats = []

            players = []
            for tr in player_rows:
                player_data = {}
                for data_stat in data_stats:
                    cell = tr.find("td", {"data-stat": data_stat})
                    player_data[data_stat] = cell.get_text(strip=True) if cell else ""
                
                player_data["season"] = season
                player_data["league"] = league_name 
                
                # N'ajouter que si on a bien un joueur (par sécurité)
                if player_data["player"]:
                    players.append(player_data)
                    all_players.append(player_data)  # ajouter à la liste globale
    
    
    filename = f"top_5_leagues_{category}_{years.start}-{years.stop}.csv"
    
    # Vérifier qu'il y a des joueurs
    if all_players:
        # On prend les clés du premier joueur pour définir les colonnes
        keys = all_players[0].keys()
        # Ouvrir le fichier en écriture
        with open(filename, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=keys)
            # Écrire l'en-tête (noms des colonnes)
            writer.writeheader()
            # Écrire chaque joueur
            for player in all_players:
                writer.writerow(player)
        print(f"Données exportées dans '{filename}'")

categories = ["possession", "passing", "gca", "shooting", "playingtime"]
for category in categories:
    stats(category)