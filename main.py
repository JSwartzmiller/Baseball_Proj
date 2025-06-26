from bs4 import BeautifulSoup
import requests
import pandas as pd

# Features to scrape:
# Type of pitch
#
# 

# Download the page
url = "https://www.baseball-reference.com/leagues/majors/2025-standard-pitching.shtml"
resp = requests.get(url)
resp.raise_for_status()

soup = BeautifulSoup(resp.text, "html.parser")

comments = soup.find_all(string=lambda text: isinstance(text, BeautifulSoup.Comment))

table = None
for c in comments:
    if 'id="players_standard_pitching"' in c:
        comment_soup = BeautifulSoup(c, "html.parser")
        table = comment_soup.find("table", {"id": "players_standard_pitching"})
        break

if table is None:
    raise ValueError("Couldn't find the standard pitching table on the page.")

df = pd.read_html(str(table))[0]

print(df.head())
        
