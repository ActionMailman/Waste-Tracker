import psutil
import time
import pyRAPL
import datetime

elec = []

def bunguius():
    pyRAPL.setup()
    measure = pyRAPL.Measurement('bar')
    while psutil.cpu_percent(interval=1) < 10:
        measure.begin()
        time.sleep(1)
        measure.end()
        try:
            elec.append(measure.result.pkg[0] / 1000000)
        except:
            elec.append(0)

try:
    start_time = datetime.datetime.now()
    while True:
        bunguius()
except KeyboardInterrupt:
    pass
    end_time = datetime.datetime.now()
    file = open('usage-info.txt', 'w+')
    file.write('Starting Time: ' + str(start_time) + '\n'+
    'Starting Time: ' + str(end_time) + '\n' +
    'Electricity Used: ' + str(sum(elec)) + ' Joules \n'
    )
