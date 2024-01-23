import csv
from match.models import matches
csv_file_path='/Users/amritanand/Desktop/E2E/django work/myProject/matches.csv'
with open(csv_file_path,'r') as file:
    reader=csv.DictReader(file)
    for row in reader:
        matches.objects.create(season=row['season'], winner=row['winner'])


