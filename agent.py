import platform
import psutil
import cpuinfo
import requests

class ServerInfoSnapshot():
    
    def __init__(self, processor, processorName, processes, users, soName, soRelease, soVersion):
        self.processor = processor
        self.processorName = processorName
        self.users = users
        self.processes = processes
        self.soName = soName
        self.soRelease = soRelease
        self.soVersion = soVersion
        super().__init__()
        
    # def toJSON(self):
    
    # def toCSV(self):
    
    def printServerInfo(self):
        print("Processor: {}, Processor Name: {}, SO Name: {}, SO Release: {} ".format(self.processor, self.processorName, self.soName, self.soVersion))
        
# Función que recopila la información de compliance
# ●	Información sobre el procesador. OK
# ●	Listado de procesos corriendo. OK
# ●	Usuarios con una sesión abierta en el sistema. OK
# ●	Nombre del sistema operativo. OK
# ●	Versión del sistema operativo. OK

def getComplianceInfo():
    listOfProcObjects = []
    for proc in psutil.process_iter():
        try:
           # Fetch process details as dict
           pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
           # Append dict to list
           listOfProcObjects.append(pinfo);
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    uname = platform.uname()
    
    # Genero toda la información necesaria
    snapshot = ServerInfoSnapshot(uname.processor, cpuinfo.get_cpu_info()['brand'],listOfProcObjects, psutil.users(), uname.system, uname.release, uname.version)
    snapshot.printServerInfo()

# Inicializo el agente
print("Starting agent...")
getComplianceInfo()
# requests.post('https://httpbin.org/post', data={'key':'value'})
# requests.post('http://localhost:5000', data={'test': 'ok'})

response = requests.get('http://127.0.0.1:5000')
print(response)

