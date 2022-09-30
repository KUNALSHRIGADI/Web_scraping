import requests
from bs4 import BeautifulSoup
import csv

URL = "https://www.animefillerlist.com/shows/naruto"

response = requests.get(url=URL)
soup = BeautifulSoup(response.text, "html.parser")

episode = soup.select("table.EpisodeList tr td.Number")
data_list = soup.select("table.EpisodeList tr td.Title a")
types = soup.select("table.EpisodeList tr td.Type span")
date = soup.select("table.EpisodeList tr td.Date")
naruto_episode = []
naruto_name = []
naruto_type = []
naruto_date = []
for e in episode:
    naruto_episode.append(e.getText())
for a in data_list:
    naruto_name.append(a.getText())
for t in types:
    naruto_type.append(t.getText())
for d in date:
    naruto_date.append(d.getText())

with open("naruto_filler.csv", mode="w") as naruto_file:
    write = csv.writer(naruto_file)
    write.writerow(["Ep No", "Name", "Type", "Date"])

    for num in range(len(naruto_episode)):
        write.writerow([naruto_episode[num], naruto_name[num], naruto_type[num], naruto_date[num]])
# print(data_list)
# data_players = soup.select("td.text-center.green")
# data_peak = soup.select("td.text-center")


# game_name = []
# game_players = []
# game_peak = []
# for game_data in data_list:
#     game_name.append(game_data.getText())

# for perk in data_players:
#     game_players.append(perk.getText())
#
# for peak in data_peak:
#     game_peak.append(peak.getText())

# print(game_name)
# print(game_players)
# print(game_peak)

# for k in range(len(game_peak)):
#     print(game_peak[k])
#
# for j in range(len(data_players)):
#     print(game_players[j])
#
# for i in range(len(game_name)):
#     print(game_name[i])

