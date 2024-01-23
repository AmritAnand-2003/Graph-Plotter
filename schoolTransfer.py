import csv
from match.models import school
csv_file_path='/Users/amritanand/Desktop/E2E/django work/myProject/primaryschool.csv'
with open(csv_file_path,'r') as file:
    reader=csv.DictReader(file)
    for row in reader:
        school.objects.create(district=row['district_name'], category=row['cat'], language=row['moi'], name=row['name'])