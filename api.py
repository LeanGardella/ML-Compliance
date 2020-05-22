import csv, json
from datetime import datetime

ip = "192.168.1.1"
port = 4201

def getServerInfoSnapshot(ip, port):
    # processor, processorName, processes, users, soName, soRelease, soVersion
    row = [ "processor", "processorName", "processes", "users", "soName", "soRelease", "soVersion"]
    return row

def saveAsCsv(row):
    # <IP de servidor>_<AAAA-MM-DD>.csv
    filename = ip + "_" + datetime.today().strftime('%Y-%m-%d')
    with open(filename + '.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(row)

def saveAsJSON(row):
    # <IP de servidor>_<AAAA-MM-DD>.csv
    filename = ip + "_" + datetime.today().strftime('%Y-%m-%d')
    
    data = {}
    data['processor'] = row[0]
    data['processorName'] = row[1]
    data['processes'] = row[2]
    data['users'] = row[3]
    data['soName'] = row[4]
    data['soRelease'] = row[5]
    data['soVersion'] = row[6]
    
    with open(filename + '.txt', 'w') as file:
        json.dump(data, file)
    
        
saveAsCsv(getServerInfoSnapshot(ip, port))
saveAsJSON(getServerInfoSnapshot(ip, port))