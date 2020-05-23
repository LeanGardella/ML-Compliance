import platform, psutil, cpuinfo, requests, json, socket
    
class ServerInfoSnapshot():
    def __init__(self, ip, processor, processorName, processes, users, soName, soRelease, soVersion):
        self.ip = ip   
        self.processor = processor
        self.processorName = processorName
        self.users = users
        self.processes = processes
        self.soName = soName
        self.soRelease = soRelease
        self.soVersion = soVersion
        super().__init__()
    
    
    def printServerInfo(self):
        print("Processor: {}, Processor Name: {}, SO Name: {}, SO Release: {} ".format(self.processor, self.processorName, self.soName, self.soVersion))

def readConfig():
    configFile = open('agent.config', 'r') 
    url = configFile.readline()
    return url
    
# Función que recopila la información de compliance
# ●	Información sobre el procesador. 
# ●	Listado de procesos corriendo. 
# ●	Usuarios con una sesión abierta en el sistema. 
# ●	Nombre del sistema operativo. 
# ●	Versión del sistema operativo. 

def getComplianceInfo():
    # Genero el listado de procesos en ejecución
    listOfProcObjects = []
    for proc in psutil.process_iter():
        try:
           # Obtener los detalles de los procesos
           pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
           listOfProcObjects.append(pinfo);
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    
    # Datos de plataforma
    uname = platform.uname()
    
    # Obtengo y parseo los usuarios con sesión iniciada
    users = []
    for user in psutil.users():
        users.append({"username": user[0], "terminal": user[1]})

    ip = socket.gethostbyname(socket.gethostname())

    # Genero toda la información necesaria
    snapshot = ServerInfoSnapshot(ip, uname.processor, cpuinfo.get_cpu_info()['brand'],listOfProcObjects, users, uname.system, uname.release, uname.version)
    return json.dumps(snapshot.__dict__)

# Leer el archivo config
url = readConfig()

# Obtener toda la información sobre el servidor
infoJson = getComplianceInfo()

# Enviar información a la API
response = requests.post(url,json=infoJson)


