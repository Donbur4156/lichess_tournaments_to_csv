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
rank_bool = configObject["rank"]
username_bool = configObject["username"]
score_bool = configObject["score"]
tieBreak_bool = configObject["tieBreak"]
rating_bool = configObject["rating"]
performance_bool = configObject["performance"]


#download arena data of lichess
url = "https://lichess.org/api/swiss/" + id_arena + "/results"
param = dict()
resp = requests.get(url=url, params=param)
list_resp = resp.text.splitlines()
data = list(map(lambda x: json.loads(x), list_resp))

#create CSV file
columns = []

if rank_bool == "true":
    columns.append("rank")
if username_bool == "true":
    columns.append("username")
if score_bool == "true":
    columns.append("score")
if tieBreak_bool == "true":
    columns.append("tieBreak")
if rating_bool == "true":
    columns.append("rating")
if performance_bool == "true":
    columns.append("performance")


print(columns)
now = datetime.datetime.today()
time = now.strftime('%Y%m%d_%H%M')
with open(file_name + time + '.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(columns)
    for i in data:
        column = []
        if rank_bool == "true":
            rank = i.get("rank") + 1
            column.append(rank)
        if username_bool == "true":
            username = i.get("username")
            column.append(username)
        if score_bool == "true":
            score = i.get("score")//1000000/10
            column.append(score)
        if tieBreak_bool == "true":
            tieBreak = i.get("tieBreak")
            column.append(tieBreak)
        if rating_bool == "true":
            rating = i.get("rating")
            column.append(rating)
        if performance_bool == "true":
            performance = i.get("performance")
            column.append(performance)
        writer.writerow(column)