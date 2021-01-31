import requests
import json
import datetime
import ndjson
import csv
from configparser import ConfigParser

#read parameter file
parser = ConfigParser()
parser.read("parameter_swiss.ini")

#parse the parameter file
configObject = parser["PARAMS"]
id_arena = configObject["arenaID"]
file_name = configObject["output_file_name"]

#download arena data of lichess
url = "https://lichess.org/api/swiss/" + id_arena + "/results"
param = dict()
resp = requests.get(url=url, params=param)
list_resp = resp.text.splitlines()
data = list(map(lambda x: json.loads(x), list_resp))

#create CSV file
columns = ["rank", "username", "score", "tieBreak", "rating", "performance"]
now = datetime.datetime.today()
time = now.strftime('%Y%m%d_%H%M')
with open(file_name + time + '.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(columns)
    for i in data:
        rank = i.get("rank") + 1
        username = i.get("username")
        score = i.get("score")
        tieBreak = i.get("tieBreak")
        rating = i.get("rating")
        performance = i.get("performance")
        writer.writerow([rank, username, score, tieBreak, rating, performance])