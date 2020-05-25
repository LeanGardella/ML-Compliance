import platform, psutil, cpuinfo, requests, json, socket
   
class ServerInfoSnapshot():
    def __init__(self, host, processor, processorName, processes, users, soName, soRelease, soVersion):
        self.host = host   
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

# Función para leer la URL parametrizada en el archivo agent.config
def readConfig():
    configFile = open('agent.config', 'r') 
    url = configFile.readline()
    return url
    
# Función que recopila la información de compliance
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

    # Se utiliza el hostname en lugar de la IP para evitar ambigüedad (múltiples IPs, incluyendo la localhost)
    host = socket.gethostname()

    # Genero toda la información necesaria
    snapshot = ServerInfoSnapshot(host, uname.processor, cpuinfo.get_cpu_info()['brand'],listOfProcObjects, users, uname.system, uname.release, uname.version)
    return json.dumps(snapshot.__dict__)

# Leer el archivo config
url = readConfig()

# Obtener toda la información sobre el servidor
infoJson = getComplianceInfo()

# Enviar información a la API
response = requests.post(url,json=infoJson)

# Verifica que se haya ejecutado en forma exitosa.
if(response.status_code == 200):
    print('Ejecución exitosa finalizada.')
else:
    print('Ocurrió un error. Status code: '+response.status_code)


