import csv
slangs = open('slangs.txt', 'r')
reader = csv.reader(slangs)
data=list(reader)
slangs.close()

real_trouble={}