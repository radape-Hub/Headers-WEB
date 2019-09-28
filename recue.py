"""Este script nos servirá para verificar los banner y headers de las paginas web que se introduzca
 en los parámetros, adiciona guarda los datos en un archivo si se requiere"""

import argparse, os, sys, platform, logging, requests, socket
from datetime import datetime
from colorama import init, Fore, Back, Style

init(autoreset= True)

logging.basicConfig(level=logging.INFO, format= '%(asctime)s %(name)s :%(levelname)s: %(message)s', 
					filename='archiRecuest_log')


logging.debug('Comienza a ejecutar el programa')
logging.info('Proceso del Programa con normalidad')
logging.warning('Advertencia: algo sucedio')

datoentrada= argparse.ArgumentParser(prog= "CapturaBanner", usage= '%(prog)s', description= '%s captura de headers y banner' % "realizar".capitalize(), epilog ="esto realiza la captura de banner y headers".capitalize(), formatter_class=argparse.RawTextHelpFormatter)
datoentrada.add_argument("-p", dest="pagina", help= 'indica la pagina web para analizar ejemplo http://...', required=True)
pagentrada= datoentrada.parse_args()

res= requests.get(pagentrada.pagina)
direccionn = res.url + '\n'
host = direccionn.split('/')
host1= host[2]


ipdir = socket.gethostbyname(host1)
print (Fore.YELLOW+Style.BRIGHT+"La ip de este dominio es: {}".format(ipdir))

if res.status_code == 200:
	print (Fore.RED+Style.BRIGHT+"Conexión establecida".title().center(80,'='))
elif res.status_code == 302:
	print ("Cambiado temporalmente el servidor")
elif res.status_code == 404:
	print ("Recurso no encontrado")

print (Back.YELLOW+"La direccion para analizar es {}".format(direccionn))

conlis= res.headers
mensa1 = ""
for cla, val in conlis.items():

	mensa = cla + '-->' + val + '\n'
	mensa1 += mensa  

	print (Fore.GREEN+cla, Fore.YELLOW+'-->>', val)

try:

	veri = True

	while veri:

		docu= input ("\nDesea guardar esta información en un documento. Digite S para Si o N para no\n")
		docuMa= docu.upper()

		if docuMa == 'S' :
			

			repo = open ("InforPagi.txt", 'a+')
			repo.write("\nLa direccion es:{}".format(direccionn))
			repo.write("La direccion IP de este dominio es:{}\n".format(ipdir))
			repo.write(mensa1)
			repo.close()

			veri = False
			print (Fore.GREEN+"La informacion se guardo en el documento...")

		elif docuMa == 'N':

			print ("Gracias por utilizar nuestra herramienta")
			break


		else:
			print ("\nDigite S para Si o N para no\n")



except:

	print ("otra vez")

