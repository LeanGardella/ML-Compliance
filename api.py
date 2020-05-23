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
    ipTxt = row.get('ip')
    saveAsCsv(row, ipTxt)
    saveAsJSON(dataJson, ipTxt)
    return dataJson

def saveAsCsv(row, ip):
    # <IP de servidor>_<AAAA-MM-DD>.csv
    filename = ip + "_" + datetime.today().strftime('%Y-%m-%d')
    
    
    header = row.keys()
    values = row.values()

    with open(filename + '.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(header)
        writer.writerow(values)

def saveAsJSON(jsonTxt, ip):
    # <IP de servidor>_<AAAA-MM-DD>.csv
    filename = ip + "_" + datetime.today().strftime('%Y-%m-%d')
    
    with open(filename + '.txt', 'w') as file:
        file.write(jsonTxt+'\n')
    
        
