import csv, json
from datetime import datetime

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def defaultUrl():
    return 'Running'

@app.route('/save-snapshot', methods=['POST'])
def saveSnapshot():
    dataJson = request.json
    row = json.loads(dataJson)
    hostname = row.get('host')
    saveAsCsv(row, hostname)
    saveAsJSON(dataJson, hostname)
    return dataJson

def saveAsCsv(row, hostname):
    # <IP de servidor>_<AAAA-MM-DD>.csv
    filename = hostname + "_" + datetime.today().strftime('%Y-%m-%d')
    
    
    header = row.keys()
    values = row.values()

    with open('snapshots/' + filename + '.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(header)
        writer.writerow(values)

def saveAsJSON(jsonTxt, hostname):
    # <IP de servidor>_<AAAA-MM-DD>.csv
    filename = hostname + "_" + datetime.today().strftime('%Y-%m-%d')
    
    with open('snapshots/' + filename + '.txt', 'w') as file:
        file.write(jsonTxt+'\n')
    
        
