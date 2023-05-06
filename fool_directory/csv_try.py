import datetime
import csv

'''
with open('participants.csv', 'w', newline='') as csvfile:
    fieldnames = ['id', 'index_numb','starttime','round1end','rest1end','round2end','rest2end','round3end','rest3end','round4end','rest4end','round5end','rest5end','round6end']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
   
    nowi = datetime.datetime.now().replace(microsecond=0)
    spis = []
    spis.append(nowi)
    nowi += datetime.timedelta(minutes=10)
    spis.append(nowi)
    writer.writerow({'id': 1, 'starttime': spis[0],'round1end':spis[1]})
    writer.writerow({'id': 2, 'starttime': spis[0], 'round1end': spis[1]})
    
    writer.writerow({'id': '123', 'index_numb': 'Beans'})
    writer.writerow({'id': '43242', 'index_numb': 'Spam'})
    writer.writerow({'id': '7852', 'index_numb': 'Spam'})
    
csvfile.close()
'''

with open('participants.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        print(str(datetime.datetime.now().replace(microsecond=0)))
        for row in reader:
            print(row)
            if row['starttime']<row['round1end']:
                print(4)

