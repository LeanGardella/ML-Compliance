import csv, json
from datetime import datetime

from flask import Flask, request, jsonify

app = Flask(__name__)

# Ruta que permite verificar que el servicio está ejecutándose correctamente
@app.route('/')
def defaultUrl():
    return 'Running'

# Ruta que implementa el guardado de la infromación reportada por los agentes, mediante POST
@app.route('/save-snapshot', methods=['POST'])
def saveSnapshot():
    dataJson = request.json
    row = json.loads(dataJson)
    hostname = row.get('host')
    saveAsCsv(row, hostname)
    saveAsJSON(dataJson, hostname)
    return dataJson

# Guarda info en csv
def saveAsCsv(row, hostname):
    filename = hostname + "_" + datetime.today().strftime('%Y-%m-%d')
    header = row.keys()
    values = row.values()
    with open('snapshots/' + filename + '.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(header)
        writer.writerow(values)

# Guarda info en json
def saveAsJSON(jsonTxt, hostname):
    filename = hostname + "_" + datetime.today().strftime('%Y-%m-%d')
    with open('snapshots/' + filename + '.txt', 'w') as file:
        file.write(jsonTxt+'\n')
    
        
