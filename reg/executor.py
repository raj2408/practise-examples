from reg.models import Regform
import csv

def inputdata():
 reader = csv.DictReader(open("book.csv"))
 for row in reader:
       Regform.objects.create(name=row['name'] ,email=row['email'] ,website=row['website'])