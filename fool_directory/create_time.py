import datetime
import csv

print(datetime.datetime.now().replace(microsecond=0))


with open('global_time.csv', 'w', newline='') as csvfile:
    fieldnames = ['time']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    times = datetime.datetime.strptime("2023-05-06 03:00:00", "%Y-%m-%d %H:%M:%S")

    while times<datetime.datetime.strptime("2023-05-07 02:00:00", "%Y-%m-%d %H:%M:%S"):
        writer.writerow({'time': times})
        times += datetime.timedelta(seconds=20)