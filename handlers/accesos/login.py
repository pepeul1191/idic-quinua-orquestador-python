#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.web
import requests
import datetime
import json
from handlers.base import BaseHandler
from config.helper import *
from config.services import *

class AccesosLoginIndexHandler(BaseHandler):
	def set_default_headers_nuevo(self):
		self.logueado()
		self.validar_permisos([3,5])

	def get(self):
		self.set_default_headers_nuevo()

		self.set_status(400)
		self.write("<h1>LOGIN</h1>")

	def post(self):
		services = Services()
		helper = Helper()
		rpta = ""

		usuario = self.get_argument('usuario')
		#contrasenia =  requests.post(services.get('cipher') + 'encode?key=' + helper.get('cipher_key') + '&texto=' + str(self.get_argument('contrasenia'))).text
		contrasenia = self.get_argument('contrasenia')

		url = services.get('servicios') + 'usuario/validar?usuario=' + str(usuario) + '&contrasenia=' + str(contrasenia)
		response = requests.post(url)
		#print response.text
		if str(response.text) == '1':
			temp = requests.get(services.get('token') + 'generar?usuario=' + str(usuario))
			token = json.loads(temp.text)
			rpta = {'token' : token['mensaje'][0], 'existe' : 1}
		else:
			rpta = {'existe' : 0}
		print json.dumps(rpta)
		self.write(json.dumps(rpta))