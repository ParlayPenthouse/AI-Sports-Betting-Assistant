import json
import time
import os
from nba_api.stats.endpoints import leaguedashplayerstats
from nba_api.stats.library.parameters import Season
from nba_api.stats.library.http import NBAStatsHTTP
from datetime import datetime
from requests.exceptions import ReadTimeout

def fetch_player_stats():
    print("Fetching NBA player stats...")

    # Try 3 times before giving up
    for attempt in range(3):
        try:
            # Set a custom User-Agent to mimic a real browser
            NBAStatsHTTP._nba_stats_http_headers.update({
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
            })

            data = leaguedashplayerstats.LeagueDashPlayerStats(
                season='2024-25'
            ).get_data_frames()[0]

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
            return
        except ReadTimeout as e:
            print(f"Timeout on attempt {attempt + 1}/3: {e}")
            time.sleep(5)
        except Exception as e:
            print(f"Unexpected error: {e}")
            break

    print("Failed to fetch stats after 3 attempts.")

if __name__ == "__main__":
    fetch_player_stats()
    print("Checking if file exists...")
    print("Files in directory:", os.listdir('.'))
    print("File created:", os.path.exists("player_stats.json"))
