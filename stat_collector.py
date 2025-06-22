import json
from nba_api.stats.endpoints import leaguedashplayerstats
from datetime import datetime

def fetch_player_stats():
    print("Fetching NBA player stats...")
    data = leaguedashplayerstats.LeagueDashPlayerStats(season='2024-25').get_data_frames()[0]
    stats = data.to_dict(orient='records')
    
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    output = {
        "last_updated": timestamp,
        "season": "2024-25",
        "players": stats
    }

    with open("player_stats.json", "w") as f:
        json.dump(output, f, indent=2)

    print(f"Saved {len(stats)} players' stats.")

if __name__ == "__main__":
    fetch_player_stats()
