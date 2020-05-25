# Compliance continuo
Desarrollo de actividad vinculada a compliance continuo

# Requisitos

> Agente
Para poder ejecutar el agente en los servidores es necesario instalar las dependencias “psutils”, “py-cpuinfo” y “requests”, en caso de que aún no estén presentes. Adicionalmente, copiar los archivos “agent.py” y “agent.config” en un directorio destinado tal fin, dentro del propio servidor.
Para completar el primer paso, e instalar las dependencias mediante pip, se utilizarán los siguientes 3 comandos. El orden de ejecución es indistinto en este caso:

```sh
	$ pip3 install psutil
	$ pip3 install py-cpuinfo
	$ pip3 install requests
```

> API
El primer paso consiste en instalar las dependencias mediante pip. Para ello, ejecutar el siguiente comando en la terminal:

```sh
	$ pip3 install Flask
```

Una vez completado este paso, se deberá crear el directorio de la aplicación. Copiar en este directorio el archivo “api.py” y crear un subdirectorio llamado “snapshots”. Luego, se requerirá establecer la variable “FLASK_APP” que indica a Flask el nombre del archivo a ejecutar y, finalmente, iniciar el servicio indicando la IP y el puerto adecuado para el mismo.

```sh
$ export FLASK_APP=<archivo.py>
$ flask run --host=<IP> --port=<Puerto>
```
