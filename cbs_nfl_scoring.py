"""
cbs_nfl_scoring.py
Scrapes NFL player scoring statistics from CBS Sports
Source: https://www.cbssports.com/nfl/stats/player/scoring/nfl/regular/qualifiers/
"""

import requests
from bs4 import BeautifulSoup

url = "https://www.cbssports.com/nfl/stats/player/scoring/nfl/regular/qualifiers/"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

tables = soup.find_all("table")

scoring_table = tables[0]

print("NFL Player Scoring Leaders\n")

rows = scoring_table.find_all("tr")[1:]  # skip header row

for row in rows[:10]:
    cols = row.find_all("td")

    if len(cols) >= 9:
        rank = cols[0].get_text(strip=True)
        player = cols[1].get_text(strip=True)
        team = cols[2].get_text(strip=True)
        position = cols[3].get_text(strip=True)
        games = cols[4].get_text(strip=True)
        touchdowns = cols[5].get_text(strip=True)
        extra_points = cols[6].get_text(strip=True)
        field_goals = cols[7].get_text(strip=True)
        points = cols[8].get_text(strip=True)

        print(
            f"#{rank} {player} ({team}, {position}) | "
            f"GP: {games} | TD: {touchdowns} | "
            f"XP: {extra_points} | FG: {field_goals} | "
            f"PTS: {points}"
        )