#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Services:
	def __init__(self):
		self.diccionario = {
			'accesos' : 'http://10.151.52.107:5001/',
			'servicios' : 'http://10.151.52.107:3000/',
			'maestros' : 'http://10.151.52.107:3001/',
			'gestion' : 'http://10.151.52.107:3002/',
			'cipher' : 'http://10.151.52.107:5000/',
			'token' : 'http://10.151.52.107:2000/',
		}

	def get(self, key):
		return self.diccionario[key]