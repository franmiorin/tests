import sys
import subprocess,os,time


class DevicesInfo(object):

	def nombre_dispositivo(self):
	"""
	Devuelve el nombre del dispositivo android conectado
	"""

		platform = sys.platform

		if platform == 'linux' or platform == 'linux2':
			comando = ['adb','devices']
		elif platform == 'win32':
			comando = 'C:/Program Files (x86)/Android/android-sdk/platform-tools/adb.exe devices'

		else:
			raise Exception('Verifique la version del sistema operativo')

		lista = subprocess.check_output(comando)
		lista = lista.replace('\n', ' ').replace('\t', ' ').replace('\r', ' ').split()
		device_id = lista[4]
		if lista[5] == 'unauthorized':
			raise Exception("El dispositivo no esta autorizado")

		return device_id

	def get_device_id(self):
	"""
	Devuelve el id del dispositivo ingresado en propiedades_appium.txt
	"""
		#obtiene un string con el contenido del txt
		with open("propiedades_appium.txt") as f:
		content = f.readlines()

		#convierte el string a lista
		list_content = [x.strip() for x in content]

		#devuelve el id
		return list_content[4].split("=")[1]


	def get_app_version(self):
	"""
	Devuelve la version de la app ingresado en propiedades_appium.txt
	"""
		#obtiene un string con el contenido del txt
		with open("propiedades_appium.txt") as f:
		content = f.readlines()

		#convierte el string a lista
		list_content = [x.strip() for x in content]

		#devuelve la version
		return list_content[6].split("=")[1]


	def get_android_version(self):
	"""
	obtiene la version de android y la devuelve en una lista
	"""

		comando = ["adb","shell","getprop","ro.build.version.release"]
		output = subprocess.check_output(comando)
		return [int(x) for x in output if x.isdigit()]

	def grant_permissions(self, permiso):
	"""
	otorga a la aplicacion el permiso para utilizar la camara de fotos y el gps 
	"""
		comando = ["adb","shell","pm","grant","'ar.com.zoologic.stockyprecios'","'android.permission." + permiso + "'"]
		subprocess.call(comando)

	def hide_keyboard(self):
	"""
	esconde el teclado que viene por estandar en la app
	"""
		comando = ['adb', 'shell', 'ime', 'set', 'io.appium.android.ime/.UnicodeIME']
		try:
			subprocess.call(comando)
		except:
			raise('Fallo escondiendo el teclado')
		return



class WifiStatus(object):

	def __init__(self,driver):

		self.driver = driver
		dispositivo = DevicesInfo()
		self.nombre_dispositivo = dispositivo.nombre_dispositivo()

	def disconnect(self):
	"""desconecta el wifi"""

		# si el nombre del dispositivo contiene un punto significa que es un emulador
		if '.' in self.nombre_dispositivo:
		os.system("adb shell svc wifi disable")

		# de lo contrario es un celular
		else:
		# scrollea hacia abajo para mostrar el panel
		self.driver.swipe(100, 1, 100, 500, 300)

		lista = self.driver.find_elements_by_class_name("android.widget.TextView")

		# hace click en el icono de wifi
		for l in lista:
		if l.text == u"Wi-Fi":
		l.click()

		# scrollea hacia arriba para quitar el panel
		self.driver.swipe(100, 500, 100, 1, 300)


	def connect(self):
	"""conecta el wifi"""

		# si el nombre del dispositivo contiene un punto significa que es un emulador
		if '.' in self.nombre_dispositivo:
		os.system("adb shell svc wifi enable")

		# de lo contrario es un celular
		else:
		# scrollea hacia abajo para mostrar el panel
		self.driver.swipe(100, 1, 100, 500, 300)

		lista = self.driver.find_elements_by_class_name("android.widget.TextView")

		# hace click en el icono de wifi
		for l in lista:
		if l.text == u"Wi-Fi":
		l.click()

		# scrollea hacia arriba para quitar el panel
		self.driver.swipe(100, 500, 100, 1, 300)

		# espera a que vuelva a conectarse
		time.sleep(20)