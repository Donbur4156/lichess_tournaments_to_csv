import requests
import json
import datetime
import ndjson
import csv
from configparser import ConfigParser

#read parameter file
parser = ConfigParser()
parser.read("parameter.ini")

#parse the parameter file
configObject = parser["PARAMS"]
id_arena = configObject["arenaID"]
file_name = configObject["output_file_name"]

#download arena data of lichess
url = "https://lichess.org/api/tournament/" + id_arena + "/results"
param = dict()
resp = requests.get(url=url, params=param)
list_resp = resp.text.splitlines()
data = list(map(lambda x: json.loads(x), list_resp))

#create CSV file
columns = ["rank", "username", "points", "performance"]
now = datetime.datetime.today()
time = now.strftime('%Y%m%d_%H%M')
with open(file_name + time + '.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(columns)
    for i in data:
        try:
            writer.writerow(
            [i["rank"], i["username"], i["score"], i["performance"]])
        except: #if no games played, it results in an error
            writer.writerow(
            [i["rank"], i["username"], i["score"], "no games!"])

