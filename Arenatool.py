import requests
import json
import datetime
import ndjson
import csv
from configparser import ConfigParser

#  with open('results.ndjson') as file:
#     data = ndjson.reader(file)

# for i in data:
#    print(i["rank"])

parser = ConfigParser()
parser.read("Parameter.ini")

configObject = parser["PARAMS"]
id_Arena = configObject["ArenaID"]
x_te_Arena = configObject["xteArena"]

url = "https://lichess.org/api/tournament/" + id_Arena + "/results"
param = dict()
resp = requests.get(url=url, params=param)
list_resp = resp.text.splitlines()
data = list(map(lambda x: json.loads(x), list_resp))

# for i in data:
#    print(i["rank"])
#    print(i["username"])

columns = ["Rang", "Username", "Punkte", "Turnierleistung"]
now = datetime.datetime.today()
time = now.strftime('%Y%m%d_%H%M')
with open('Ergebnis_' + x_te_Arena + '_Arena_' + time + '.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(columns)
    for i in data:
        try:
            writer.writerow(
            [i["rank"], i["username"], i["score"], i["performance"]])
        except:
            writer.writerow(
            [i["rank"], i["username"], i["score"], "nicht gespielt!"])

