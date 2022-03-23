from csv import reader
from time import sleep
url_inside = '../../data/processed/touch_event_out.csv'

with open(url_inside, 'r') as read_obj:
    csv_reader = reader(read_obj)
    header = next(csv_reader)
    if header != None:
        for row in csv_reader:
            print(row)
            sleep(4)

