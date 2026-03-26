"""
superbowl_champions.py
Scrapes Super Bowl championship results from Wikipedia
Source: https://en.wikipedia.org/wiki/List_of_Super_Bowl_champions
"""

import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_Super_Bowl_champions"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

champions_table = None
for table in soup.find_all("table", class_="wikitable"):
    caption = table.find("caption")
    if caption and "Super Bowl championships" in caption.text:
        champions_table = table
        break

if champions_table is None:
    raise RuntimeError("Super Bowl championships table not found.")

print("Super Bowl Champions\n")

rows = champions_table.find_all("tr")[1:]

for row in rows[:10]:
    cols = row.find_all("td")

    if len(cols) >= 9:
        game = cols[0].get_text(strip=True)
        date = cols[1].get_text(strip=True)
        winning_team = cols[2].get_text(strip=True)
        score = cols[3].get_text(strip=True)
        losing_team = cols[4].get_text(strip=True)
        venue = cols[5].get_text(strip=True)
        city = cols[6].get_text(strip=True)
        attendance = cols[7].get_text(strip=True)
        referee = cols[8].get_text(strip=True)

        print(
            f"{game} | {date} | {winning_team} def. {losing_team} | "
            f"Score: {score} | Venue: {venue}, {city} | Attendance: {attendance}"
        )