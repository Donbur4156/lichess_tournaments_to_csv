# lichess_tournaments_to_csv
The Script downloads the Players of an arena or swiss tournament, with their scores etc. and export this as a csv file.

1. Download ReadLichessArena.rar for Arenas or ReadLichessSwiss.rar for Swiss tournament
2. Unzip the archieve
3. configure the parameter.ini with your data
4. run the .exe and wait a few moments
5. as a result it creates a csv file which you can e.g. import in an Excel sheet.

parameter_arena.ini:
output_file_name is how the csv is named. It adds the actual time.
arenaID is the last part of the tournament link: lichess.org/tournament/{arenaID}

parameter_swiss_ini:
output_file_name is how the csv is named. It adds the actual time.
arenaID is the last part of the tournament link: lichess.org/tournament/{arenaID}
for the following variables you can choose with true or false whether it should be displayed or not.
