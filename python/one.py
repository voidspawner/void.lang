'''
	V O I D
'''

# Import

import io
import os
import sys
import subprocess
import json
import csv
import time
import math
import hashlib
import base64
import re
import uuid
import gzip
import binascii
import random
import string
import shutil
import urllib.parse
import ssl
import zlib
import traceback
from functools import reduce
from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ForkingMixIn
from http import cookies
from datetime import datetime

# Class

class One:

	# Data

	data = {
		'about': {
			'name': 'V O I D one Python',
			'version': {
				'tag': None,
				'time': None,
				'date': None
			},
			'required': {
				'python': {
					'version': 3.10,
					'pip': [
						'rsa',
						'ruamel.yaml',
						'requests',
						'pymemcache',
						'bcrypt',
						'mysql-connector-python'
					]
				}
			}
		},
		"settings": {
			"http": {
				"type": {
					"aac": "audio/aac",
					"abw": "application/x-abiword",
					"arc": "application/x-freearc",
					"avi": "video/x-msvideo",
					"avif": "image/avif",
					"azw": "application/vnd.amazon.ebook",
					"bin": "application/octet-stream",
					"bmp": "image/bmp",
					"bz": "application/x-bzip",
					"bz2": "application/x-bzip2",
					"csh": "application/x-csh",
					"css": "text/css",
					"csv": "text/csv",
					"doc": "application/msword",
					"docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
					"eot": "application/vnd.ms-fontobject",
					"epub": "application/epub+zip",
					"gz": "application/gzip",
					"gif": "image/gif",
					"htm": "text/html",
					"html": "text/html",
					"ico": "image/vnd.microsoft.icon",
					"ics": "text/calendar",
					"jar": "application/java-archive",
					"jpeg": "image/jpeg",
					"jpg": "image/jpeg",
					"js": "text/javascript",
					"json": "application/json",
					"jsonld": "application/ld+json",
					"m4a": "audio/m4a",
					"m4v": "video/mp4",
					"mid": "audio/midi",
					"midi": "audio/x-midi",
					"mjs": "text/javascript",
					"mka": "audio/x-matroska",
					"mkv": "video/x-matroska",
					"mp3": "audio/mpeg",
					"mp4": "video/mp4",
					"mpeg": "video/mpeg",
					"mpkg": "application/vnd.apple.installer+xml",
					"odp": "application/vnd.oasis.opendocument.presentation",
					"ods": "application/vnd.oasis.opendocument.spreadsheet",
					"odt": "application/vnd.oasis.opendocument.text",
					"oga": "audio/ogg",
					"ogv": "video/ogg",
					"ogx": "application/ogg",
					"opus": "audio/opus",
					"otf": "font/otf",
					"png": "image/png",
					"pdf": "application/pdf",
					"php": "application/php",
					"ppt": "application/vnd.ms-powerpoint",
					"pptx": "application/vnd.openxmlformats-officedocument.presentationml.presentation",
					"rar": "application/vnd.rar",
					"rtf": "application/rtf",
					"sh": "application/x-sh",
					"svg": "image/svg+xml",
					"srt": "text/plain",
					"swf": "application/x-shockwave-flash",
					"tar": "application/x-tar",
					"tif": "image/tiff",
					"tiff": "image/tiff",
					"ts": "video/mp2t",
					"ttf": "font/ttf",
					"txt": "text/plain",
					"vsd": "application/vnd.visio",
					"wav": "audio/wav",
					"weba": "audio/webm",
					"webm": "video/webm",
					"webp": "image/webp",
					"wmv": "video/x-ms-wmv",
					"woff": "font/woff",
					"woff2": "font/woff2",
					"xhtml": "application/xhtml+xml",
					"xls": "application/vnd.ms-excel",
					"xlsx": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
					"xml": "text/xml",
					"xul": "application/vnd.mozilla.xul+xml",
					"zip": "application/zip",
					"3gp": "video/3gpp",
					"3g2": "video/3gpp2",
					"7z": "application/x-7z-compressed"
				}
			},
			"autorun": True,
			"run": {
				"import": True,
				"newline": os.linesep,
				"pathsep": os.path.sep,
				"argument": sys.argv
			},
			"verbose": True,
			"path": {
				"python": "python3.10"
			},
			"void": {
				"domain": "",
				"key": None
			}
		},
		"action": {
			"runner": {
				"cli": [
					[".", "Will be available in June 2022"]
				]
			},
			"load": [
				["param", [
					["path", "string"],
					["type", "string", None]
				]],
				["?", ["{type}", "=", None], [
					["file.extension", "{path}"],
					["?", ["{}", "=", "gz"], [
						["=", "compress", True],
						["file.name", "{path}"],
						"file.extension"
					], [
						["=", "compress", False]
					]]
				], [
					["file.extension", "{type}"],
					["?", ["{}", "=", "gz"], [
						["=", "compress", True],
						["file.name", "{type}"]
					], [
						["=", "compress", False]
					]]
				]],
				"lower",
				["=", "type"],
				["?", [["starts", "{path}", "http://"], "||", ["starts", "{path}", "https://"]], [
					["request", "{path}", [
						["=", "", "{.text}"]
					], [
						["error", 1005, "{path}"]
					]]
				], [
					["?", ["file.exists", "{path}"], [
						["file.read", "{path}"]
					], [
						["error", 1005, "{path}"]
					]]
				]],
				["?", ["{compress}"], ["gzip.decode"]],
				["??", "{type}", [
					["json", ["json.decode"]],
					["csv", ["csv.decode"]],
					["yaml", ["yaml.decode"]],
					["ini", ["ini.decode"]],
					["xml", ["xml.decode"]]
				]],
				"->"
			],
			"save": [
				["param", [
					["path", "string"],
					["value", "any", "{}"],
					["type", "string", None]
				]],
				["?", ["{type}", "=", None], [
					["file.extension", "{path}"],
					["?", ["{}", "=", "gz"], [
						["=", "compress", True],
						["file.name", "{path}"],
						"file.extension"
					], [
						["=", "compress", False]
					]]
				], [
					["file.extension", "{type}"],
					["?", ["{}", "=", "gz"], [
						["=", "compress", True],
						["file.name", "{type}"]
					], [
						["=", "compress", False]
					]]
				]],
				"lower",
				["=", "type"],
				["??", "{type}", [
					["json", [
						["json.encode", "{value}"]
					]],
					["csv", [
						["csv.encode", "{value}"]
					]],
					["yaml", [
						["yaml.encode", "{value}"]
					]],
					["ini", [
						["ini.encode", "{value}"]
					]],
					["xml", [
						["xml.encode", "{value}"]
					]]
				], [
					["=", "", "{value}"]
				]],
				["?", ["{compress}"], ["gzip.encode"]],
				["file.write", "{path}"]
			],
			"sql.user.list": [],
			"sql.user.create": [],
			"sql.user.update": [],
			"sql.user.remove": [],
			"sql.db.list": [],
			"sql.db.create": [],
			"sql.db.update": [],
			"sql.db.remove": [],
			"sql.function.list": [],
			"sql.function.create": [],
			"sql.function.update": [],
			"sql.function.remove": [],
			"sql.view.list": [],
			"sql.view.create": [],
			"sql.view.update": [],
			"sql.view.remove": [],
			"sql.table.list": [],
			"sql.table.create": [],
			"sql.table.update": [],
			"sql.table.remove": [],
			"sql.column.list": [],
			"sql.column.create": [],
			"sql.column.update": [],
			"sql.column.remove": [],
			"sql.index.list": [],
			"sql.index.create": [],
			"sql.index.update": [],
			"sql.index.remove": [],
			"sql.row.list": [],
			"sql.row.create": [],
			"sql.row.update": [],
			"sql.row.remove": [],
			"ui": {
				"web": {
					"text": [
						["param", [
							["text", "string"],
							["plain", "bool", False],
							["data", "param", None]
						]],
						["?", "{paragraph}", [
							["->", "<p{attrib}>{text}</p>"]
						], [
							["->", "{text}"]
						]]
					],
					"header": [
						["param", [
							[""]
						]]
					],
					"button": [],
					"image": [],
					"video": [],
					"map": [],
					"progress": [],
					"upload": [],
					"edit": [],
					"tab": [],
					"hsplit": [],
					"vsplit": [],
					"panel": [],
					"select": [],
					"top": [],
					"footer": [],
					"chat": [],
					"tile": [],
					"list": [],
					"link": [],
					"slides": [],
					"camera": [],
					"view": [],
					"settings": []
				}
			},
			"json": {
				"encode": [],
				"decode": [],
			},
			"one": {
				"encode": [],
				"decode": []
			},
			"yaml": {
				"encode": [],
				"decode": []
			},
			"html": {
				"encode": [
					["param", [
						["tag", "string"],
						["param", "param", None]
					]],
					["?", ["{body}", "!=", None], [
						["->", "<{tag}{attr}>{body}</tag>"]
					], [
						["->", "<{tag}{attr}>"]
					]]
				],
				"decode": [
					[".", "Will be available in June 2022"]
				]
			},
			"css": {
				"encode": [
					[".", "Will be available in June 2022"]
				],
				"decode": [
					[".", "Will be available in June 2022"]
				]
			},
			"ini": {
				"encode": [
					[".", "Will be available in June 2022"]
				],
				"decode": [
					[".", "Will be available in June 2022"]
				]
			},
			"sms": [
				["param", [
					["phone", "string"],
					["text", "string"]
				]],
				["void", "sms", "{phone}", "{text}"],
				"->"
			],
			"call": [
				["param", [
					["phone", "string"],
					["text", "string"]
				]],
				["void", "call", "{phone}", "{text}"],
				"->"
			],
			"email": [
				["param", [
					["from", "string"],
					["to", "string"],
					["subject", "string"],
					["text", "string"]
				]],
				["void", "email", "{from}", "{to}", "{subject}", "{text}"],
				"->"
			],
			"notification": [
				["param", [
					["platform", "string"],
					["token", "string"],
					["title", "string"],
					["text", "string"],
					["image", "string"],
					["badge", "string"],
					["group", "string"],
					["sound", "string"]
				]],
				["void", "notification", "{platform}", "{token}", "{title}", "{text}", "{image}", "{badge}", "{group}", "{sound}"],
				"->"
			],
			"social": [
				["param", [
					["social", "string"],
					["account", "string"],
					["text", "string", None],
					["image", "string", None],
					["video", "string", None],
					["sound", "string", None],
					["location", ["param", "list"], None]
				]],
				["void", "social", "{social}", "{account}", "{text}", "{image}", "{video}", "{sound}", "{location}"],
				"->"
			],
			"void": [
				["param", [
					["name", "string"],
					["param", ["many"]]
				]],
				["request.post", "api.{settings.void.domain}/{name}", "{param}"],
				"->"
			],
			"update": [
				[".", "Will be available in June 2022"]
			],
			"test": [
				["param", [
					["name", "string", None]
				]],
				[".", "Test"],
				[":", "one", ["load", "{settings.void.url}/code/one/one.json"]],
				["?", ["{one.list}", "!is", "full"], [
					["error", 1005, "{settings.void.url}/code/one/one.json"]
				]],
				["each", "{one.list}", [
					["?", [["{name}", "is", "string"], "&&", ["{name}", "!=", "all"], "&&", ["{name}", "!=", "{value.0}"]], ["continue"]],
					["?", ["{value.4}", "is", "full"], [
						["=", "name", "{value.0}"],
						["each", "{value.4}", [
							["?", [
								[["{value}", "!has", "enable"], "||", ["{value.enable}", "=", True]],
								"&&",
								[["{param.name}", "=", "all"], "||", ["{param.name}", "is", "string"], "||", ["{value.slow}", "!=", True]]
							], [
								["=", "test", "{value}"],
								["action", "{test.in}"],
								["?", ["{}", "!=", "{test.out}"], [
									["=", "test.result"],
									["=", "test", {
										"name": "{name}",
										"index": "{index}",
										"case": "{test}"
									}],
									["error", 1006, "{test}"]
								]]
							]]
						]]
					]]
				]],
				[".", "ok"]
			],
			"error_": [
				["param", [
					["reason", ["string", "int"]],
					["data", "param", None]
				]],
				["?", [["type", "{reason}"], "is", "string"], [
					[".", "Error: {reason}"]
				], [
					[".", "Error: {@error.{reason}}"]
				]],
				[".", "{data}"],
				["exit", -1]
			]
		},
		"text": {
			"error": {
				"1001": {"en": ""},
				"1002": {"en": ""}
			}
		}
	}

	# Run

	@staticmethod
	def autorun():
		if One.data['settings']['autorun']:
			if len(sys.argv) > 1:
				if type(sys.argv[1]) is str:
					arg = sys.argv
					arg.pop(0)
					if arg[0].endswith('.json'):
						One.run(arg[0])
					else:
						One.run([arg])

	@staticmethod
	def run(action):
		kind = type(action)
		if kind is list:
			One.data['run'] = action
		elif kind is str:
			if action.endswith('.json'):
				app = One.load(action)
				if type(app) is list:
					One.data['run'] = app
				elif type(app) is dict:
					One.merge(One.data, app)
				else:
					One.error(f'check file \'{action}\'')
			elif action.find('{') >= 0:
				data = One.Json.decode(action)
				if data != None:
					One.merge(One.data, data)
			elif action.find('[') >= 0:
				data = One.Json.decode(action)
				if data != None:
					One.merge(One.data, data)
			else:
				One.data['run'] = [action]
		elif kind is dict:
			One.merge(One.data, action)
		if 'run' in One.data and type(One.data['run']) is list:
			One.action(One.data['run'])
		if 'web' in One.data or 'api' in One.data or 'socket' in One.data or 'stream' in One.data:
			One.Server.Http.run()
		elif 'cli' in One.data:
			One.action(['runner.cli'])

	# Value

	@staticmethod
	def value(name: str):
		return re.sub(r'\{([^}]*?)\}', One.value_replace, name)

	@staticmethod
	def value_replace(match: str):
		value = One.get(match.group(1))
		if match.group(0) == match.string:
			return value
		return str(value)

	@staticmethod
	def get(name: str, default = None):
		part = name.split('.')
		data = One.data
		index = 1
		length = len(part)
		for subname in part:
			if subname not in data:
				break
			if index == length:
				return data[subname]
			else:
				data = data[subname]
				index += 1
		return default

	@staticmethod
	def set(name: str, value):
		part = name.split('.')
		data = One.data
		index = 1
		length = len(part)
		for subname in part:
			if subname.isdigit():
				subname = int(subname)
				if type(data) is list:
					if subname < len(data):
						if index == length:
							data[subname] = value
						else:
							data = data[subname]
							index += 1
					else:
						return
				else:
					return
			else:
				if subname not in data:
					data[subname] = {}
				if index == length:
					data[subname] = value
				else:
					data = data[subname]
					index += 1

	@staticmethod
	def remove(name: str):
		part = name.split('.')
		data = One.data
		index = 1
		length = len(part)
		for subname in part:
			if subname not in data:
				return
			if index == length:
				del data[subname]
			else:
				data = data[subname]
				index += 1

	@staticmethod
	def add(name: str, value):
		part = name.split('.')
		data = One.data
		index = 1
		length = len(part)
		for subname in part:
			if subname not in data:
				return
			if index == length:
				data[subname].append(value)
			else:
				data = data[subname]
				index += 1

	# Expression

	@staticmethod
	def expression(expression: list):
		# Will be available in June 2022
		for value in expression:
			match value:
				case '+':
					pass
				case '-':
					pass
				case '*':
					pass
				case '/':
					pass
				case 'sin':
					pass

	# Load/Save

	@staticmethod
	def load(path, format: str = None):
		if One.File.exists(path):
			data = One.File.read(path)
			if format == None:
				format = One.File.extension(path).lower()
			match format:
				case 'json':
					return One.Json.decode(data)
				case 'csv':
					return One.Csv.decode(data)
				case 'yaml':
					return One.Yaml.decode(data)				
		return None

	@staticmethod
	def save(path, data, format: str = None):
		if format == None:
			format = One.File.extension(path).lower()
		match format:
			case 'json':
				data = One.Json.encode(data)
			case 'csv':
				data = One.Csv.encode(data)
			case 'yaml':
				data = One.Yaml.encode(data)
		One.File.write(path, data)

	# Control

	@staticmethod
	def echo(value, end: str = None):
		kind = type(value)
		if kind is list or kind is dict:
			value = One.Json.encode(value)
		print(value, end=end)

	@staticmethod
	def param(param, info: list):
		param_length = len(param)
		param_kind = type(param)
		if param_length == 0 or param_kind not in [list, dict]:
			raise Exception('Check params')
		result = {} if param_kind is list else param
		for index, info in enumerate(info):
			info_length = len(info)
			if info_length == 0:
				raise Exception('Check params')
			info_name = info[0]
			info_kind = info[1] if info_length > 1 else 'any'
			if type(info_kind) is not list:
				info_kind = [info_kind]
			info_default = info[2] if info_length > 2 else 0
			if param_kind is list:
				if param_length - 1 > index:
					result[info_name] = param[index + 1]
				else:
					if info_length > 2:
						result[info_name] = info_default
						if info_default == None:
							info_kind.append('null')
					else:
						raise Exception('Check params')
			else:
				if info_name not in param:
					if info_length > 2:
						result[info_name] = info_default
						if info_default == None:
							info_kind.append('null')
					else:
						raise Exception('Check params')
			if result[info_name] == '{}':
				result[info_name] = One.data['data']['list'][-1]['result']
			if type(result[info_name]) is str:
				if result[info_name].find('{') != -1:
					result[info_name] = One.value(result[info_name])
			elif type(result[info_name]) is list:
				for index, value in enumerate(result[info_name]):
					if type(value) is str:
						if value.find('{') != -1:
							result[info_name][index] = One.value(value)
			elif type(result[info_name]) is dict:
				for index, value in result[info_name].items():
					if type(value) is str:
						if value.find('{') != -1:
							result[info_name][index] = One.value(value)
			found = False
			for kind in info_kind:
				match kind:
					case 'any':
						found = True
						break
					case 'string':
						if type(result[info_name]) is str:
							found = True
							break
					case 'int':
						if type(result[info_name]) is int:
							found = True
							break
					case 'float':
						if type(result[info_name]) is float:
							found = True
							break
					case 'number':
						if type(result[info_name]) in [int, float]:
							found = True
							break
					case 'list':
						if type(result[info_name]) is list:
							found = True
							break
					case 'param':
						if type(result[info_name]) is dict:
							found = True
							break
					case 'array':
						if type(result[info_name]) in [dict, list]:
							found = True
							break
					case 'bool':
						if type(result[info_name]) is bool:
							found = True
							break
					case 'null' | None:
						if result[info_name] == None:
							found = True
							break
					case _:
						pass
			if not found:
				raise Exception('Check params')
		return result

	@staticmethod
	def shell(command: str, input: str = None, verbose: bool = False):
		if verbose:
			return subprocess.call(command, shell=True)
		else:
			if input == None:
				input = ''
			result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, input=input.encode("utf-8"))
			error = result.stderr.decode("utf-8")
			return {
				"code": result.returncode,
				"error": error if error != '' else None,
				"text": result.stdout.decode("utf-8")
			}

	@staticmethod
	def code(code: str):
		exec(code)

	@staticmethod
	def exit(code: int = 0):
		exit(code)

	@staticmethod
	def error(error = 'error', data = None):
		One.echo('Error: ' + str(error))
		if data != None:
			if 'trace' in data:
				One.echo(data['trace'])
			else:
				One.echo(One.Json.encode(data))
		exit(-1)

	@staticmethod
	def action(action):
		if type(action) is not list:
			action = [action]
		else:
			action = list(action)
		action.reverse()
		One.data['data'] = {
			'list': [
				{
					"top": 0,
					"result": None,
					"data": {},
					"param": {}
				}
			]
		}
		action_data = One.data['data']
		data = One.data['data']['list'][-1]
		while len(action) > 0:
			action_current = action.pop()
			action_type = type(action_current)
			if action_type is list:
				if len(action_current) > 0:
					action_name = action_current[0]
					action_param = action_current
				else:
					continue
			elif action_type is dict:
				if '' in action_current:
					action_name = action_current['']
					action_param = action_current
				else:
					continue
			elif action_type is str:
				action_name = action_current
				action_param = [action_name]
			else:
				continue
			try:
				match action_name:
					case '=':
						param = One.param(action_param, [
							["name", "string"],
							["value", "any", True]
						]),
						One.set(param['name'], param['value'])
					case ':':
						param = One.param(action_param, [
							["name", "string"],
							["expression", "many"]
						])
						One.expression(param['name'], param['expression'])
					case '~':
						param = One.param(action_param, [
							["name", "string"]
						]),
						One.get(param['name'])
					case 'action':
						param = One.param(action_param, [
							["action", ["string", "list"]],
							["param", ["param", "list"], None]
						])
						action_data['list'].append({
							"top": len(action),
							"result": None,
							"param": param['param'],
							"data": {}
						})
						if type(param['action']) is str:
							param['action'] = One.get(param['action'])
							if type(param['action']) is not list:
								continue
						action_new = list(param['action'])
						action_new.reverse()
						action += action_new
					case 'return' | '->':
						param = One.param(action_param, [
							["value", "any", None]
						])
						if type(param['value']) is str:
							param['value'] = One.get(param['value'])
						if data['top'] > 0:
							del action[data['top']:]
							del action_data['list'][-1]
							data = action_data['list'][-1]
						else:
							action = []
						data['result'] = param['value']
					case '?':
						param = One.param(action_param, [
							["expression", "list"],
							["action", "list"],
							["else", "list", None]
						])
						if One.expression(param['expression']):
							action_new = list(param['action'])
							action_new.reverse()
							action += action_new
						elif param['else'] != None:
							action_new = list(param['else'])
							action_new.reverse()
							action += action_new
					case '??':
						param = One.param(action_param, [
							["value", "number"],
							["case", "list"],
							["default", "list", None]
						])
						found = False
						for case in param['case']:
							if type(case) is list and len(case) > 1:
								if not (len(case) > 2 and case[2] and One.expression(case[0])) or (case[0] != param['value']):
									continue
								action_new = list(case[1])
								action_new.reverse()
								action += action_new
								found = True
								break

						if not found and param['default'] != None:
							action_new = list(param['default'])
							action_new.reverse()
							action += action_new

					case 'each' | '@':
						param = One.param(action_param, [
							["value", "number"]
						])
					case 'break' | 'x':
						param = One.param(action_param, [
							["value", "number"]
						])
						# Will be available in June 2022
					case 'continue' | '>>>':
						param = One.param(action_param, [
							["value", "number"]
						])
						# Will be available in June 2022
					case 'repeat' | '<<<':
						param = One.param(action_param, [
							["value", "number"]
						])
						# Will be available in June 2022
					case '+':
						param = One.param(action_param, [
							["value", "number"]
						])
						data['result'] += param['value']
					case '-':
						param = One.param(action_param, [
							["value", "number"]
						])
						data['result'] -= param['value']
					case '*':
						param = One.param(action_param, [
							["value", "number"]
						])
						data['result'] *= param['value']
					case '/':
						param = One.param(action_param, [
							["value", "number"]
						])
						data['result'] /= param['value']
					case '%':
						param = One.param(action_param, [
							["value", "number"]
						])
					case '^':
						param = One.param(action_param, [
							["value", "number"]
						])
					case '>>':
						param = One.param(action_param, [
							["value", "number"]
						])
					case '<<':
						param = One.param(action_param, [
							["value", "number"]
						])
					case '++':
						param = One.param(action_param, [
							["value", "number"]
						])
					case '--':
						param = One.param(action_param, [
							["value", "number"]
						])
					case '+=':
						param = One.param(action_param, [
							["value", "number"]
						])
					case '=+':
						param = One.param(action_param, [
							["value", "number"]
						])
					case '-=':
						param = One.param(action_param, [
							["value", "number"]
						])
					case '*=':
						param = One.param(action_param, [
							["value", "number"]
						])
					case '/=':
						param = One.param(action_param, [
							["value", "number"]
						])
					case '%=':
						param = One.param(action_param, [
							["value", "number"]
						])
					case '^=':
						param = One.param(action_param, [
							["value", "number"]
						])
					case '>>=':
						param = One.param(action_param, [
							["value", "number"]
						])
					case '<<=':
						param = One.param(action_param, [
							["value", "number"]
						])
					case '=!':
						param = One.param(action_param, [
							["name", "string"]
						])
						One.set(param['name'], not bool(One.get(param['name'])))
					case '==':
						param = One.param(action_param, [
							["value", "number"]
						])
					case '!=':
						param = One.param(action_param, [
							["value", "number"]
						])
					case '>':
						param = One.param(action_param, [
							["value", "number"]
						])
					case '<':
						param = One.param(action_param, [
							["value", "number"]
						])
					case '>=':
						param = One.param(action_param, [
							["value", "number"]
						])
					case '<=':
						param = One.param(action_param, [
							["value", "number"]
						])
					case '&&':
						param = One.param(action_param, [
							["value", "number"]
						])
					case '||':
						param = One.param(action_param, [
							["value", "number"]
						])
					case 'is':
						param = One.param(action_param, [
							["value", "number"]
						])
					case '!is':
						param = One.param(action_param, [
							["value", "number"]
						])
					case 'in':
						param = One.param(action_param, [
							["value", "number"]
						])
					case '!in':
						param = One.param(action_param, [
							["value", "number"]
						])
					case '|':
						param = One.param(action_param, [
							["value", "number"]
						])
						data['result'] |= param['value']
					case '&':
						param = One.param(action_param, [
							["value", "number"]
						])
						data['result'] &= param['value']
					case '!':
						param = One.param(action_param, [
							["value", "number"]
						])
						data['result'] = not bool(param['result'])
					case '#':
						param = One.param(action_param, [
							["value", "number"]
						])
						data['result'] ^= param['value']
					case 'sin':
						param = One.param(action_param, [
							["value", "number"]
						])
						data['result'] = One.sin(param['value'])
					case 'cos':
						param = One.param(action_param, [
							["value", "number"]
						])
						data['result'] = One.cos(param['value'])
					case 'tan':
						param = One.param(action_param, [
							["value", "number"]
						])
						data['result'] = One.tan(param['value'])
					case 'asin':
						param = One.param(action_param, [
							["value", "number"]
						])
						data['result'] = One.asin(param['value'])
					case 'acos':
						param = One.param(action_param, [
							["value", "number"]
						])
						data['result'] = One.acos(param['value'])
					case 'atan':
						param = One.param(action_param, [
							["value", "number"]
						])
						data['result'] = One.atan(param['value'])
					case 'sinh':
						param = One.param(action_param, [
							["value", "number"]
						])
						data['result'] = One.sinh(param['value'])
					case 'cosh':
						param = One.param(action_param, [
							["value", "number"]
						])
						data['result'] = One.cosh(param['value'])
					case 'tanh':
						param = One.param(action_param, [
							["value", "number"]
						])
						data['result'] = One.tanh(param['value'])
					case 'asinh':
						param = One.param(action_param, [
							["value", "number"]
						])
						data['result'] = One.asin(param['value'])
					case 'acosh':
						param = One.param(action_param, [
							["value", "number"]
						])
						data['result'] = One.acosh(param['value'])
					case 'atanh':
						param = One.param(action_param, [
							["value", "number"]
						])
						data['result'] = One.atanh(param['value'])
					case 'round':
						param = One.param(action_param, [
							["value", "number"],
							["digits", "int", 0]
						])
						data['result'] = One.round(param['value'], param['digits'])
					case 'floor':
						param = One.param(action_param, [
							["value", "number"]
						])
						data['result'] = One.floor(param['value'])
					case 'ceil':
						param = One.param(action_param, [
							["value", "number"]
						])
						data['result'] = One.ceil(param['value'])
					case 'random':
						param = One.param(action_param, [
							["from", "number", 0],
							["to", "number", 1]
						])
						data['result'] = One.random(param['from'], param['to'])
					case 'abs':
						param = One.param(action_param, [
							["value", "number"]
						])
						data['result'] = One.abs(param['value'])
					case 'min':
						param = One.param(action_param, [
							["value", ["number", "list"]]
						])
						data['result'] = One.min(param['value'])
					case 'max':
						param = One.param(action_param, [
							["value", ["number", "list"]]
						])
						data['result'] = One.max(param['value'])
					case 'average':
						param = One.param(action_param, [
							["value", ["number", "list"]]
						])
						data['result'] = One.average(param['value'])
					case 'factorial':
						param = One.param(action_param, [
							["value", "int"]
						])
						data['result'] = One.factorial(param['value'])
					case 'lg':
						param = One.param(action_param, [
							["value", "number"],
							["base", "number", None]
						])
						data['result'] = One.lg(param['value'], param['base'])
					case 'hex':
						param = One.param(action_param, [
							["value", "int"]
						])
						data['result'] = One.hex(param['value'])
					case 'bin':
						param = One.param(action_param, [
							["value", "int"]
						])
						data['result'] = One.bin(param['value'])
					case 'oct':
						param = One.param(action_param, [
							["value", "int"]
						])
						data['result'] = One.oct(param['value'])
					case 'dec':
						param = One.param(action_param, [
							["value", ["string", "int"]],
							["type", "string"]
						])
						data['result'] = One.dec(param['value'], param['type'])
					case 'rad':
						param = One.param(action_param, [
							["value", "number"]
						])
						data['result'] = One.rad(param['value'])
					case 'deg':
						param = One.param(action_param, [
							["value", "number"]
						])
						data['result'] = One.deg(param['value'])
					case 'string':
						param = One.param(action_param, [
							["value"]
						])
						data['result'] = str(param['value'])
					case 'int':
						param = One.param(action_param, [
							["value"]
						])
						data['result'] = int(param['value'])
					case 'float':
						param = One.param(action_param, [
							["value", "number"]
						])
						data['result'] = float(param['value'])
					case 'number':
						param = One.param(action_param, [
							["value", "number"]
						])
						data['result'] = One.number(param['value'])
					case 'list':
						param = One.param(action_param, [
							["value", "number"]
						])
						data['result'] = One.list(param['value'])
					case 'bool':
						param = One.param(action_param, [
							["value", "number"]
						])
						data['result'] = bool(param['value'])
					case 'type':
						param = One.param(action_param, [
							["value", "number"]
						])
						data['result'] = One.type(param['value'])
					case 'date':
						param = One.param(action_param, [
							["value", ["string", "number"]],
							["format", "string"]
						])
						data['result'] = One.data(param['value'], param['format'])
					case 'time':
						data['result'] = One.time()
					case 'wait':
						param = One.param(action_param, [
							["delay", "number", 1]
						])
						One.wait(param['delay'])
					case 'speed.start':
						param = One.param(action_param, [
							["tag", "string", None]
						])
						data['result'] = One.Speed.start(param['tag'])
					case 'speed.check':
						param = One.param(action_param, [
							["tag", "string", None]
						])
						data['result'] = One.Speed.check(param['tag'])
					case 'speed.reset':
						data['result'] = One.Speed.reset()
					case 'speed.total':
						data['result'] = One.Speed.total()
					case 'upper':
						param = One.param(action_param, [
							["text", "string"]
						])
						data['result'] = One.upper(param['text'])
					case 'lower':
						param = One.param(action_param, [
							["value", "number"]
						])
						data['result'] = One.lower(param['text'])
					case 'format':
						param = One.param(action_param, [
							["value", "number"],
							["format", "string"]
						])
						data['result'] = One.format(param['value'])
					case 'split':
						param = One.param(action_param, [
							["text", "string"],
							["delimiter", "string", ',']
						])
						data['result'] = One.split(param['text'], param['delimiter'])
					case 'join':
						param = One.param(action_param, [
							["value", "number"]
						])
					case 'trim':
						param = One.param(action_param, [
							["text", "string"],
							["remove", "string", None]
						])
						data['result'] = One.trim(param['trim'], param['remove'])
					case 'ltrim':
						param = One.param(action_param, [
							["text", "string"],
							["remove", "string", None]
						])
						data['result'] = One.ltrim(param['trim'], param['remove'])
					case 'rtrim':
						param = One.param(action_param, [
							["text", "string"],
							["remove", "string", None]
						])
						data['result'] = One.rtrim(param['trim'], param['remove'])
					case 'find':
						param = One.param(action_param, [
							["value", ["string", "list", "param"]],
							["search"]
						])
						kind = type(param['value'])
						if kind is str:
							data['result'] = param['value'].find(param['search'])
							if data['result'] == -1:
								data['result'] = None
						elif kind is list:
							pass
						elif kind is dict:
							pass
					case 'count':
						param = One.param(action_param, [
							["value", ["list", "param", "string"]]
						])
						data['result'] = len(param['value'])
					case 'fill':
						param = One.param(action_param, [
							["value", "number"]
						])
					case 'encode':
						param = One.param(action_param, [
							["value", "number"]
						])
					case 'replace':
						param = One.param(action_param, [
							["value", "number"]
						])
					case 'regex.find':
						param = One.param(action_param, [
							["value", "number"]
						])
					case 'regex.replace':
						param = One.param(action_param, [
							["value", "number"]
						])
					case 'escape.html':
						param = One.param(action_param, [
							["value", "number"]
						])
					case 'escape.json':
						param = One.param(action_param, [
							["value", "number"]
						])
					case 'escape.url':
						param = One.param(action_param, [
							["value", "number"]
						])
					case 'escape.slash':
						param = One.param(action_param, [
							["value", "number"]
						])
					case 'escape.sql':
						param = One.param(action_param, [
							["value", "number"]
						])
					case 'escape.one':
						param = One.param(action_param, [
							["value", "number"]
						])
					case 'unescape.html':
						param = One.param(action_param, [
							["value", "number"]
						])
					case 'unescape.json':
						param = One.param(action_param, [
							["value", "number"]
						])
					case 'unescape.url':
						param = One.param(action_param, [
							["value", "number"]
						])
					case 'unescape.slash':
						param = One.param(action_param, [
							["value", "number"]
						])
					case 'unescape.sql':
						param = One.param(action_param, [
							["value", "number"]
						])
					case 'unescape.one':
						param = One.param(action_param, [
							["value", "number"]
						])
					case 'starts':
						param = One.param(action_param, [
							["value", "number"]
						])
					case 'ends':
						param = One.param(action_param, [
							["value", "number"]
						])
					case 'first':
						param = One.param(action_param, [
							["value", "number"]
						])
					case 'last':
						param = One.param(action_param, [
							["value", "number"]
						])
					case 'push':
						param = One.param(action_param, [
							["value", "number"]
						])
					case 'pop':
						param = One.param(action_param, [
							["value", "number"]
						])
					case 'add':
						param = One.param(action_param, [
							["value", "number"]
						])
					case 'remove':
						param = One.param(action_param, [
							["value", "number"]
						])
					case 'shuffle':
						param = One.param(action_param, [
							["value", "number"]
						])
					case 'reverse':
						param = One.param(action_param, [
							["value", "number"]
						])
					case 'part':
						param = One.param(action_param, [
							["value", "number"]
						])
					case 'unique':
						param = One.param(action_param, [
							["value", "number"]
						])
					case 'indexes':
						param = One.param(action_param, [
							["value", "number"]
						])
					case 'values':
						param = One.param(action_param, [
							["value", "number"]
						])
					case 'map':
						param = One.param(action_param, [
							["value", "number"]
						])
					case 'filter':
						param = One.param(action_param, [
							["value", "number"]
						])
					case 'reduce':
						param = One.param(action_param, [
							["value", "number"]
						])
					case 'flat':
						param = One.param(action_param, [
							["value", "number"]
						])
					case 'associate':
						param = One.param(action_param, [
							["value", "number"]
						])
					case 'sql.open':
						param = One.param(action_param, [
							["name", "string"],
							["host", "string"],
							["user", "string"],
							["password", "string"],
							["database", "string", None]
						])
						One.Sql.open(param['name'], param['host'], param['user'], param['password'], param['database'])
					case 'sql.close':
						param = One.param(action_param, [
							["name", "string"]
						])
						One.Sql.close(param['name'])
					case 'sql.query':
						param = One.param(action_param, [
							["name", "string"],
							["query", "string"],
							["param", "list", []]
						])
						One.Sql.query(param['name'], param['query'], param['param'])
					case 'sql.list':
						data['result'] = One.Sql.list()
					case 'sql.db.open':
						param = One.param(action_param, [
							["name", "string"],
							["database", "string"]
						])
						One.Sql.Db.open(param['name'], param['database'])
					case 'sql.fetch.one' | "sql.one":
						pass
					case 'sql.fetch.all' | "sql.all":
						pass
					case 'log':
						param = One.param(action_param, [
							["value", "number"]
						])
					case 'request':
						param = One.param(action_param, [
							["url", "string"],
							["success", "list", None],
							["error", "list", None]
						])
					case 'request.get':
						param = One.param(action_param, [
							["value", "number"]
						])
					case 'request.post':
						param = One.param(action_param, [
							["value", "number"]
						])
					case 'request.put':
						param = One.param(action_param, [
							["value", "number"]
						])
					case 'request.patch':
						param = One.param(action_param, [
							["value", "number"]
						])
					case 'request.delete':
						param = One.param(action_param, [
							["value", "number"]
						])
					case 'ui.web':
						param = One.param(action_param, [
							["data", "list"]
						])
						One.Http.content(One.Ui.Web.create(param['data']))
					case 'html.encode' | 'format.html.encode':
						param = One.param(action_param, [
							["data", ["list", "params"]]
						])
						data['result'] = One.Html.encode(param['data'])
					case 'http.content':
						param = One.param(action_param, [
							["text", "any", "{}"]
						])
						One.Http.content(param['text'])
					case 'http.type':
						param = One.param(action_param, [
							["name", "string"]
						])
						One.Http.type(param['name'])
					case 'http.redirect':
						param = One.param(action_param, [
							["url", "string", "/"]
						])
						One.Http.redirect(param['url'])
					case 'echo' | '.':
						param = One.param(action_param, [
							["value", "any"],
							["end", "string", None]
						])
						One.echo(param['value'], param['end'])
					case 'error':
						param = One.param(action_param, [
							["reason", ["int", "string"], None]
						])
						action_new = One.get('action.error')
						if type(action_new) is list:
							action_new = list(action_new)
							action_new.reverse()
							action += action_new
						else:
							One.error(param['reason'], action_param)
					case 'exit' | 'X':
						param = One.param(action_param, [
							["code", "int", 0]
						]),
						One.exit(param['code'])
					case _:
						action_new = One.get('action.' + action_name)
						if type(action_new) is list:
							action_data['list'].append({
								"top": len(action),
								"result": None,
								"param": action_param,
								"data": {}
							})
							action_new = list(action_new)
							action_new.reverse()
							action += action_new
							data = action_data['list'][-1]
						del action_new
			except Exception as error:
				action.append({
					"": "error",
					"code": 1002,
					"current": action_current,
					"list": action,
					"reason": One.reason(error),
					"trace": One.trace()
				})
		result = data['result']
		del One.data['data']
		return result

	# Time

	@staticmethod
	def time():
		return time.time()

	@staticmethod
	def wait(delay: float):
		time.sleep(delay)

	# Speed

	class Speed:

		@staticmethod
		def start(tag: str = 'Start'):
			time = One.time()
			One.data['speed'] = {
				"start": time,
				"total": 0,
				"check": [
					[tag, time]
				]
			}

		@staticmethod
		def check(tag: str = None):
			time = One.time()
			if 'speed' not in One.data or len(One.data['speed']['check']) == 0:
				One.Speed.start()
			else:
				One.data['speed']['total'] += time - One.data['speed']['check'][-1][1]
			if tag == None:
				tag = 'Check ' + str(len(One.data['speed']['check']))
			One.data['speed']['check'].append([tag, time])

		@staticmethod
		def reset():
			del One.data['speed']

		@staticmethod
		def total():
			if 'speed' in One.data:
				return One.data['speed']['total']
			return 0

	# String

	@staticmethod
	def lower(text: str):
		return text.lower()

	@staticmethod
	def upper(text: str):
		return text.upper()

	@staticmethod
	def trim(text: str):
		return text.lower()

	@staticmethod
	def ltrim(text: str):
		return text.lower()

	@staticmethod
	def rtrim(text: str):
		return text.lower()

	@staticmethod
	def replace(text: str, search, replace):
		if type(search) is str and type(replace) is str:
			return text.replace(search, replace)
		if type(search) is list and type(replace) is list:
			for index in range(0, len(search)):
				text = text.replace(search[index], replace[index])
		return text

	@staticmethod
	def path(*path):
		result = ''
		separator = os.path.sep
		for path in path:
			path = path.replace('\\', separator) if separator == '/' else path.replace('/', separator)
			if result != '':
				if result != separator:
					result += separator + path
				else:
					result += path
			else:
				result = path
		return result

	@staticmethod
	def find(text: str):
		return text.lower()

	@staticmethod
	def part():
		pass

	@staticmethod
	def date(format: str = 'full', date = None):
		if format == 'full':
			return str(datetime.now())

	class Regex:

		@staticmethod
		def find(text: str):
			return text.lower()

		@staticmethod
		def replace(text: str):
			return text.lower()

	class Escape:
		
		@staticmethod
		def html(text: str, newline: bool = False):
			search = ['&', '>', '<', '\'', '"']
			replace = ['&amp;', '&gt;', '&lt;', '&#39;', '&#34;']
			if newline:
				search.append('\r\n')
				search.append('\n')
				replace.append('<br>')
				replace.append('<br>')
			return One.replace(text, search, replace)

		@staticmethod
		def json(text: str, slash: bool = False, unicode: bool = False):
			search = ['"', '\\', '\b', '\f', '\r', '\n', '\t']
			replace = ['\\"', '\\\\', '\\b', '\\f', '\\r', '\\n', '\\t']
			if slash:
				search.append('/')
				replace.append('\\/')
			return One.replace(text, search, replace)

		@staticmethod
		def backslash(text: str):
			return One.replace(text, '\\', '\\\\')

		@staticmethod
		def url(text: str):
			return urllib.parse.quote(text)

		@staticmethod
		def sql(text: str):
			return One.replace(text, ['"', '\\', '/', '\b', '\f', '\r', '\n', '\t'], ['\\"', '\\\\', '\\/', '\\b', '\\f', '\\r', '\\n', '\\t'])

	class Unescape:
		
		@staticmethod
		def html(text: str, newline: bool = False):
			search = ['&amp;', '&gt;', '&lt;', '&#39;', '&#34;']
			replace = ['&', '>', '<', '\'', '"']
			if newline:
				search.append('<br>')
				replace.append(Onde.data['settings']['run']['newline'])
			return One.replace(text, search, replace)

		@staticmethod
		def json(text: str, slash: bool = False, unicode: bool = False):
			search = ['"', '\\', '\b', '\f', '\r', '\n', '\t']
			replace = ['\\"', '\\\\', '\\b', '\\f', '\\r', '\\n', '\\t']
			if slash:
				search.append('/')
				replace.append('\\/')
			return One.replace(text, search, replace)

		@staticmethod
		def backslash(text: str):
			return One.replace(text, '\\\\', '\\')

		@staticmethod
		def url(text: str):
			return urllib.parse.unquote(text)

		@staticmethod
		def sql(text: str):
			return One.replace(text, ['\\"', '\\\\', '\\/', '\\b', '\\f', '\\r', '\\n', '\\t'], ['"', '\\', '/', '\b', '\f', '\r', '\n', '\t'])

	# Array

	@staticmethod
	def push():
		pass

	@staticmethod
	def pop():
		pass

	@staticmethod
	def reverse():
		pass

	@staticmethod
	def merge(first, second, replace: bool = False):
		for key in second:
			if key in first:
				if isinstance(first[key], dict) and isinstance(second[key], dict):
					One.merge(first[key], second[key], replace)
				elif isinstance(first[key], list) and isinstance(second[key], list):
					if replace:
						first[key] = second[key]
					else:
						first[key] += second[key]
				elif first[key] == second[key]:
					pass
				else:
					first[key] = second[key]
			else:
				first[key] = second[key]
		return first

	@staticmethod
	def shuffle(array: list):
		data = list(array)
		random.shuffle(data)
		return data

	# Type

	@staticmethod
	def type(value):
		if value == None:
			return 'none'
		kind = type(value)
		if kind is str:
			return 'string'
		elif kind is int:
			return 'int'
		elif kind is float:
			return 'float'
		elif kind is bool:
			return 'bool'
		elif kind is list:
			return 'list'
		elif kind is dict:
			return 'param'
		return None

	@staticmethod
	def list(value):
		if type(value) is not list:
			return [value]
		return list(value)

	@staticmethod
	def string(value):
		return str(value)

	@staticmethod
	def int(value):
		return int(value)

	@staticmethod
	def float(value):
		return float(value)

	@staticmethod
	def bool(value):
		return bool(value)

	@staticmethod
	def number(value):
		result = float(value)
		if result % 1 != 0:
			return result
		return int(result)

	# Math

	@staticmethod
	def sin(number: float):
		return math.sin(number)

	@staticmethod
	def cos(number: float):
		return math.cos(number)

	@staticmethod
	def tan(number: float):
		return math.tan(number)

	@staticmethod
	def asin(number: float):
		return math.asin(number)

	@staticmethod
	def acos(number: float):
		return math.acos(number)

	@staticmethod
	def atan(number: float):
		return math.atan(number)

	@staticmethod
	def sinh(number: float):
		return math.sinh(number)

	@staticmethod
	def cosh(number: float):
		return math.acosh(number)

	@staticmethod
	def tanh(number: float):
		return math.tanh(number)

	@staticmethod
	def asinh(number: float):
		return math.asinh(number)

	@staticmethod
	def acosh(number: float):
		return math.acosh(number)

	@staticmethod
	def atanh(number: float):
		return math.atanh(number)

	@staticmethod
	def round(number: float, digits: int = 0):
		result = round(number, digits)
		return result if result % 1 != 0 else int(result)

	@staticmethod
	def floor(number: float):
		return math.floor(number)

	@staticmethod
	def ceil(number: float):
		return math.ceil(number)

	@staticmethod
	def lg(number: float, base: float = None):
		return math.log(number, base) if base != None else math.log(number)

	@staticmethod
	def pow(number: float, power: float = 2):
		return pow(number, power)

	@staticmethod
	def factorial(number: int):
		return math.factorial(number)

	@staticmethod
	def abs(number: float):
		return abs(number)

	@staticmethod
	def min(*number):
		if len(number) > 0:
			if type(number[0]) is list:
				return min(number[0])
			else:
				return min(number)
		return None

	@staticmethod
	def max(*number):
		if len(number) > 0:
			if type(number[0]) is list:
				return max(number[0])
			else:
				return max(number)
		return None

	@staticmethod
	def average(*number):
		if len(number) > 0:
			sum = 0
			if type(number[0]) is list:
				number = number[0]
			for num in number:
				sum += num
			return sum / len(number)
		return None

	@staticmethod
	def hex(number: int):
		return hex(number).lstrip('0x')

	@staticmethod
	def dec(number, kind: str):
		match kind:
			case 'hex':
				return int(number, 16)
			case 'bin':
				return int(number, 2)
			case 'oct':
				return int(number, 8)
		return None

	@staticmethod
	def bin(number: int):
		return bin(number).lstrip('0b')

	@staticmethod
	def oct(number: int):
		return oct(number).lstrip('0o')

	@staticmethod
	def rad(number: float):
		return math.degrees(number)

	@staticmethod
	def deg(number: float):
		return math.radians(number)

	@staticmethod
	def random(start = 0, end = 1):
		if type(start) is int and type(end) is int and abs(start - end) > 1:
			return random.randint(start, end)
		return random.uniform(start, end)

	# Crypto

	@staticmethod
	def hash(length: int = 64, symbols: str = None):
		match symbols:
			case 'letter':
				symbols = string.ascii_letters
			case 'lower':
				symbols = string.ascii_lowercase
			case 'upper':
				symbols = string.ascii_uppercase
			case 'digit':
				symbols = string.digits
			case 'hex':
				symbols = '0123456789ABCDEF'
			case _:
				if symbols == None:
					symbols = string.ascii_letters + string.digits
		return ''.join(random.SystemRandom().choice(symbols) for _ in range(length))

	@staticmethod
	def uuid():
		return str(uuid.uuid4())

	@staticmethod
	def md5(data):
		if type(data) is str:
			data = data.encode('utf-8')
		return hashlib.md5(data).hexdigest()

	@staticmethod
	def sha1(data):
		if type(data) is str:
			data = data.encode('utf-8')
		return hashlib.sha1(data).hexdigest()

	@staticmethod
	def sha256(data):
		if type(data) is str:
			data = data.encode('utf-8')
		return hashlib.sha256(data).hexdigest()

	@staticmethod
	def sha512(data):
		if type(data) is str:
			data = data.encode('utf-8')
		return hashlib.sha512(data).hexdigest()

	@staticmethod
	def crc32(data):
		if type(data) is str:
			data = data.encode('utf-8')
		return binascii.crc32(data)

	class Base64:

		@staticmethod
		def encode(data):
			if type(data) is str:
				data = data.encode('utf-8')
			return base64.b64encode(data).decode('utf-8')

		@staticmethod
		def decode(data, byte: bool = False, zip: bool = False):
			if type(data) is str:
				data = data.encode('utf-8')
			result = base64.b64decode(data).decode('utf-8') if not byte else base64.b64decode(data)
			return One.Gzip.decode(result, byte) if zip else result

	class Gzip:

		@staticmethod
		def encode(data):
			if type(data) is str:
				data = data.encode('utf-8')
			return gzip.compress(data)

		@staticmethod
		def decode(data, byte: bool = False):
			return gzip.decompress(data).decode('utf-8') if not byte else gzip.decompress(data)

	class Rsa:

		@staticmethod
		def encode(data, publicKey):
			if type(data) is str:
				data = data.encode('utf-8')
			return rsa.encrypt(data, publicKey)

		@staticmethod
		def decode(data, privateKey, byte = False):
			return rsa.decrypt(data, privateKey).decode('utf-8') if not byte else rsa.decrypt(data, privateKey)

		@staticmethod
		def keys(length: int = 512):
			keys = rsa.newkeys(length)
			return {
				"public": keys[0],
				"private": keys[1]
			}

	class Ssl:
		# Will be available in June 2022
		pass

	class Bcrypt:
		
		@staticmethod
		def encode(data, rounds: int = 10):
			if type(data) is str:
				data = data.encode('utf-8')
			salt = bcrypt.gensalt(rounds=rounds)
			hashed = bcrypt.hashpw(data, salt)
			return {
				'salt': salt,
				'hash': hashed
			}

		@staticmethod
		def check(data, hashed):
			if type(data) is str:
				data = data.encode('utf-8')
			if type(hashed) is str:
				hashed = hashed.encode('utf-8')
			return bcrypt.checkpw(data, hashed)

	class Crypto:

		class Coin:
			# Will be available in September 2022
			pass

		class Nft:
			# Will be available in September 2022
			pass

	# File

	class File:

		@staticmethod
		def exists(path: str):
			return os.path.isfile(path)

		@staticmethod
		def create(path: str):
			open(path, 'w').write('')

		@staticmethod
		def write(path: str, content):
			if type(content) is str:
				open(path, 'w').write(content)
			else:
				open(path, 'wb').write(content)

		@staticmethod
		def read(path: str, byte: bool = False):
			result = open(path, 'rb').read()
			return result.decode('utf-8') if not byte else result

		@staticmethod
		def remove(path: str):
			os.remove(path)

		@staticmethod
		def size(path: str):
			return os.path.getsize(path)

		@staticmethod
		def copy(pathFrom: str, pathTo: str):
			return shutil.copyfile(pathFrom, pathTo)

		@staticmethod
		def move(pathFrom: str, pathTo: str):
			shutil.move(pathFrom, pathTo)

		@staticmethod
		def rename(path, name):
			shutil.move(pathFrom, os.path.join(One.File.path(path), name))

		@staticmethod
		def extension(path: str):
			return os.path.splitext(path)[1].lstrip('.')

		@staticmethod
		def name(path: str):
			return os.path.splitext(os.path.basename(path))[0]

		@staticmethod
		def filename(path: str):
			return os.path.basename(path)

		@staticmethod
		def path(path: str):
			return os.path.dirname(path)

		@staticmethod
		def base64(path: str, zip: bool = False):
			data = One.File.read(path, True)
			return One.Base64.encode(One.Gzip.encode(data)) if zip else One.Base64.encode(data)

		@staticmethod
		def crc32(path: str):
			with open(path, 'rb') as file:
				hash = 0
				while True:
					data = file.read(65536)
					if not data:
						break
					hash = zlib.crc32(data, hash)
				return "%08X" % (hash & 0xFFFFFFFF)

		@staticmethod
		def info(path: str):
			# Will be available in June 2022
			pass

	class Dir:

		@staticmethod
		def separator():
			return os.path.sep

		@staticmethod
		def current():
			return os.getcwd()

		@staticmethod
		def exists(path: str):
			return os.path.isdir(path)

		@staticmethod
		def create(path: str):
			return os.mkdir(path)

		@staticmethod
		def remove(path: str):
			shutil.rmtree(path)

		@staticmethod
		def list(path: str):
			result = []
			for name in os.listdir(path):
				result.append(name)
			return result

		@staticmethod
		def size(path: str = '.'):
			size = 0
			for root, dirs, files in os.walk(path):
				for file in files:
					path = os.path.join(root, file)
					if not os.path.islink(path):
						size += os.path.getsize(path)
			return size

		@staticmethod
		def copy(pathFrom: str, pathTo: str):
			# Will be available in June 2022
			pass

		@staticmethod
		def move(pathFrom: str, pathTo: str):
			shutil.move(pathFrom, pathTo)

		@staticmethod
		def rename(path, name):
			shutil.move(pathFrom, os.path.join(One.File.path(path), name))

		@staticmethod
		def info(path: str):
			# Will be available in June 2022
			pass

		@staticmethod
		def clear(path: str):
			if len(path) > 0:
				for name in One.Dir.list(path):
					name = os.path.join(path, name)
					if os.path.isfile(name):
						One.File.remove(name)
					elif os.path.isdir(name):
						One.Dir.remove(name)

	class Link:

		@staticmethod
		def exists(path: str):
			return os.path.islink(path)

		@staticmethod
		def create(pathFrom: str, pathTo: str):
			os.symlink(pathFrom, pathTo)

		@staticmethod
		def remove(path: str):
			if os.path.islink(path):
				os.remove(path)

		@staticmethod
		def info(path: str):
			# Will be available in June 2022
			pass

	class Volume:

		@staticmethod
		def current():
			# Will be available in June 2022
			pass

		@staticmethod
		def letter(path):
			# Will be available in June 2022
			pass

		@staticmethod
		def mount():
			# Will be available in June 2022
			pass

		@staticmethod
		def unmount():
			# Will be available in June 2022
			pass

		@staticmethod
		def size(path: str = '/'):
			return shutil.disk_usage(path)[0]

		@staticmethod
		def used(path: str = '/'):
			size = shutil.disk_usage(path)
			return size[0] - size[2]

		@staticmethod
		def free(path: str = '/'):
			return shutil.disk_usage(path)[2]

		@staticmethod
		def list():
			# Will be available in June 2022
			pass

		@staticmethod
		def info():
			# Will be available in June 2022
			pass

		@staticmethod
		def change():
			# Will be available in June 2022
			pass

	# Server

	class Server:
		
		class Http(BaseHTTPRequestHandler):
			
			server = None
			log = True

			class ForkingHTTPServer(ForkingMixIn, HTTPServer):

				def finish_request(self, request, client_address):
					request.settimeout(30)
					HTTPServer.finish_request(self, request, client_address)

			def do_HEAD(self):
				One.Server.Http.process(self, 'head')

			def do_GET(self):
				One.Server.Http.process(self, 'get')

			def do_POST(self):
				try:
					raw = self.rfile.read(int(self.headers['Content-Length'])).decode('utf-8')
					data = {}
					for pair in urllib.parse.parse_qsl(raw, keep_blank_values=True):
						data[pair[0]] = pair[1]
				except Exception as error:
					pass
				One.Server.Http.process(self, 'post', data)

			def log_message(self, format, *args):
				if One.Server.Http.log:
					if len(args) > 1:
						One.echo(self.client_address[0] + ' [' + One.date('full') + '] ' + ' '.join(args))
					elif len(args) == 1:
						One.echo(args[0])

			@staticmethod
			def process(self, method, data: dict = {}):
				try:
					One.Http.Cookie.run()
					cookie = {}
					if 'Cookie' in self.headers:
						One.Http.Cookie.load(self.headers['Cookie'])
						cookie = Http.Cookie.all()
					parts = self.path.split('?')
					path = parts[0].rstrip('/') if len(parts[0]) > 1 else '/'
					query = {}
					if len(parts) > 1:
						for part in parts[1].split('&'):
							part = part.split('=')
							query[part[0]] = One.Unescape.url(part[1]) if len(part) > 1 else True
					header = {}
					for value in self.headers.items():
						header[value[0]] = value[1]
					language = []
					if 'Accept-Language' in header:
						for part in header['Accept-Language'].split(','):
							sub = part.strip().split(';')
							language.append(sub[0].strip())
					accept = []
					if 'Accept' in header:
						for part in header['Accept'].split(','):
							sub = part.strip().split(';')
							accept.append(sub[0].strip())
					host = header['Host'] if 'Host' in header else None
					agent = header['User-Agent'] if 'User-Agent' in header else None
					encoding = header['Accept-Encoding'].lower().replace(' ', '').split(',') if 'Accept-Encoding' in header else []
					referer = header['Referer'] if 'Referer' in header else None
					gzip = 'gzip' in encoding
					One.data['request'] = {
						'host': host,
						'url': self.path,
						'route': path,
						'method': method,
						'ip': self.client_address[0],
						'port': self.client_address[1],
						'agent': agent,
						'encoding': encoding,
						'language': language,
						'accept': accept,
						'referer': referer,
						'gzip': gzip,
						'header': header,
						'query': query,
						'data': data,
						'cookie': cookie
					}
					One.data['response'] = {
						'code': 200,
						'header': {
							'content-type': 'text/plain'
						},
						'cookie': {},
						'encoding': 'utf-8',
						'content': ''
					}

					if 'server' in One.data and 'before' in One.data['server']:
						One.action(One.data['server']['before'])

					One.Server.Http.route()

					if 'server' in One.data and 'after' in One.data['server']:
						One.action(One.data['server']['after'])

					self.send_response(One.data['response']['code'])
					for name, value in One.data['response']['header'].items():
						self.send_header(name, value)
					for output in One.Http.Cookie.output():
						self.send_header("set-cookie", output)
					self.end_headers()

					if type(One.data['response']['content']) is str:
						self.wfile.write(bytes(One.data['response']['content'], One.data['response']['encoding']))
					elif type(One.data['response']['content']) is bytes:
						self.wfile.write(One.data['response']['content'])
				except Exception as error:
					One.log(One.trace())

			@staticmethod
			def run():
				try:
					One.Server.Http.log = One.get('settings.verbose', True)
					if 'server' not in One.data:
						One.data['server'] = {}
					host = One.data['server']['host'] if 'host' in One.data['server'] else '0.0.0.0'
					if 'ssl' in One.data['server'] and 'certificate' in One.data['server']['ssl']:
						One.data['server']['type'] = 'https'
						port = One.data['server']['port'] if 'port' in One.data['server'] else 443
						One.Server.Http.server = One.Server.Http.ForkingHTTPServer((host, port), One.Server.Http)
						One.Server.Http.server.socket = ssl.wrap_socket(One.Server.Http.server.socket, server_side=True, certfile=One.data['server']['ssl']['certificate'], ssl_version=ssl.PROTOCOL_TLS)
						if One.Server.Http.log:
							One.echo(f"Server up: https://{host}:{port}")
					else:
						One.data['server']['type'] = 'http'
						port = One.data['server']['port'] if 'port' in One.data['server'] else 80
						One.Server.Http.server = One.Server.Http.ForkingHTTPServer((host, port), One.Server.Http)
						if One.Server.Http.log:
							One.echo(f"Server up: http://{host}:{port}")
					One.Server.Http.server.serve_forever()
				except KeyboardInterrupt:
					pass
				One.Server.Http.server.socket.close()
				if One.get('settings.verbose', True):
					One.echo("Server down")

			@staticmethod
			def route():
				request_path = One.data['request']['route']
				request_method = One.data['request']['method']
				request_host = One.data['request']['host']
				for runner in ['api', 'web', 'stream', 'static']:
					if not (runner in One.data and 'route' in One.data[runner]):
						continue
					for route in One.data[runner]['route']:
						if type(route) is list:
							length = len(route)
							if length < 2:
								continue
							path = route[0]
							action = route[1]
							method = route[2] if length > 2 else 'get'
							zip = False
							file = None
							content = None
							kind = None
							cache = False
							host = None
						elif type(route) is dict:
							if 'url' not in route:
								continue
							path = route['url']
							action = route['action'] if 'action' in route else None
							method = route['method'] if 'method' in route else 'get'
							zip = bool(route['zip']) if 'zip' in route else False
							file = route['file'] if 'file' in route else None
							content = route['content'] if 'content' in route else None
							kind = route['type'] if 'type' in route else None
							cache = bool(route['cache']) if 'cache' in route else False
							host = route['host'] if 'host' in route else None
						else:
							continue
						if request_path != path or request_method != method or (host != None and request_host != host):
							continue
						cache = One.Cache.get(One.data['request']['path'] + ':' + One.data['request']['method']) if One.Cache.kind != None else None
						if cache != None:
							One.Http.content(cache['content'])
							One.Http.Header.set(cache['header'])
						else:
							if runner == 'api':
								One.Http.type('json')
								if action in One.data['action']:
									One.action(One.data['action'][action])
									One.Http.content(One.Json.encode({"result": One.data['response']['content']}, bool(One.get('api.pretty')) ))
								else:
									One.Http.code(404)
									One.Http.content(One.Json.encode({"error": {"code": 404, "reason": "action not found"}, "result": None}, bool(One.get('api.pretty')) ))
							elif runner == 'web':
								One.Http.type('html')
								if action in One.data['action']:
									One.action(One.data['action'][action])
								else:
									One.Http.code(404)
							else:
								if 'expire' in One.data['static']:
									One.Http.cache(int(One.data['static']['expire']))
								if content != None:
									One.Http.content(One.Base64.decode(content, True, zip))
									One.Http.type(kind)
								elif file != None:
									if One.File.exists(file):
										One.Http.content(One.File.read(file, True))
										filename = One.File.filename(file)
										One.Http.Header.set('Content-Disposition', f'attachment; filename="{filename}"')
										if kind != None:
											One.Http.type(kind)
										else:
											One.Http.type(One.File.extension(file))
									else:
										One.Http.code(404)
										return
								else:
									if action in One.data['action']:
										One.action(One.data['action'][action])
									else:
										One.Http.code(404)
										return
								if cache:
									One.Cache.set(One.data['request']['path'] + ':' + One.data['request']['method'], {
										"content": One.data['response']['content'],
										"header": One.data['response']['header']
									})
						return

				public = One.get('static.public')
				if public != None:
					path = One.path(public + request_path.replace('/../', '/'))
					if One.File.exists(path):
						One.Http.content(One.File.read(path, True))
						One.Http.type(One.File.extension(path))
						expire = One.get('static.expire')
						if expire != None:
							One.Http.cache(int(expire))
						return
				One.Http.code(404)
				action = One.get('web.default')
				if action != None:
					One.Http.type('html')
					One.action(action)

		class Ftp:
			# Will be available in June 2022
			pass

		class Pop3:
			# Will be available in June 2022
			pass

		class Imap:
			# Will be available in June 2022
			pass

		class Socket:
			# Will be available in June 2022
			pass

		class Websocket:
			# Will be available in June 2022
			pass

		class One:
			# Will be available in June 2022
			pass

		class Telegram:
			# Will be available in June 2022
			pass

		class Crypto:
			# Will be available in September 2022
			pass

	class Http:

		class Cookie:

			cookie = None

			@staticmethod
			def run():
				One.Http.Cookie.cookie = cookies.SimpleCookie()

			@staticmethod
			def load(data: dict):
				One.Http.Cookie.cookie.load(data)

			@staticmethod
			def get(name: str, default = None):
				return One.get('request.cookie.' + name, default)

			@staticmethod
			def all():
				result = {}
				for morsel in cookieRequest.values():
					result[morsel.key] = morsel.value
				return result

			@staticmethod
			def set(name: str, value, expire: int = None):
				One.Http.Cookie.cookie[name] = value
				if expire != None:
					One.Http.Cookie.cookie[name]['max-age'] = expire

			@staticmethod
			def clear(name: str):
				One.remove('request.cookie.' + name)
				One.Http.Cookie.set(name, '', -1)

			@staticmethod
			def output():
				result = []
				for morsel in One.Http.Cookie.cookie.values():
					result.append(morsel.OutputString())
				return result

		class Header:

			@staticmethod
			def get(name: str, default = None):
				return One.data['request']['header'][name] if name in One.data['request']['header'] else default

			@staticmethod
			def set(name, value = None):
				if type(name) is str:
					One.data['response']['header'][name] = f'{value}'
				elif type(name) is list:
					One.data['response']['header'] = value				

		@staticmethod
		def content(value, zip: bool = False):
			One.data['response']['content'] = value if not zip else One.Crypto.Gzip.decode(One.Crypto.Base64.decode(value, True), True)

		@staticmethod
		def code(code: int = 200):
			One.data['response']['code'] = code

		@staticmethod
		def type(name: str):
			One.data['response']['header']['content-type'] = One.get('settings.http.type.' + name, name)

		@staticmethod
		def etag(hash: str):
			One.data['response']['header']['etag'] = f'"{hash}"'

		@staticmethod
		def cache(time: int = None, private: bool = False):
			One.data['response']['header']['cache-control'] = ('public,' if not private else 'private,') + (f'max-age={time}' if time != None else '')

		@staticmethod
		def clear(value: list = ['cache']):
			One.data['response']['header']['clear-site-data'] = '"' + '","'.join(value) + '"'

		@staticmethod
		def redirect(url: str, code: int = 307):
			One.Http.Header.set('Location', url)
			if code != None:
				One.Http.code(code)


	# Request

	class Request:

		@staticmethod
		def send(url, method = 'get', query = None, data = None, header = None, cookie = None):
			# Will be available in June 2022
			try:
				result = requests.request(method.upper(), url)
				return {
					"code": result.status_code,
					"text": result.text
				}
			except Exception as error:
				return {
					"code": 0,
					"text": str(error)
				}

		@staticmethod
		def get(url, query = None, header = None, cookie = None):
			return One.Request.send(url, 'get', query, header, cookie)

		@staticmethod
		def post(url, query = None, data = None, header = None, cookie = None):
			return One.Request.send(url, 'post', query, data, header, cookie)

		@staticmethod
		def put(url, query = None, data = None, header = None, cookie = None):
			return One.Request.send(url, 'put', query, data, header, cookie)

		@staticmethod
		def patch(url, query = None, data = None, header = None, cookie = None):
			return One.Request.send(url, 'patch', query, data, header, cookie)

		@staticmethod
		def delete(url, query = None, header = None, cookie = None):
			return One.Request.send(url, 'delete', query, header, cookie)

	# Cache

	class Cache:

		kind = None

		@staticmethod
		def run():
			kind = One.get('settings.cache.type')
			if kind == 'memcache':
				One.Cache.kind = kind
				One.Cache.Memcache.run()
			elif kind == 'file':
				One.Cache.kind = kind
				One.Cache.File.run()
			elif kind == 'db':
				One.Cache.kind = kind
				One.Cache.Db.run()

		@staticmethod
		def get(name: str, default = None):
			if One.Cache.kind == 'memcache':
				return One.Cache.Memcache.get(name, default)
			elif One.Cache.kind == 'file':
				return One.Cache.File.get(name, default)
			elif One.Cache.kind == 'db':
				return One.Cache.Db.get(name, default)

		@staticmethod
		def set(name: str, value):
			if One.Cache.kind == 'memcache':
				One.Cache.Memcache.set(name, value)
			elif One.Cache.kind == 'file':
				One.Cache.File.set(name, value)
			elif One.Cache.kind == 'db':
				One.Cache.Db.set(name, value)

		@staticmethod
		def remove(name: str):
			if One.Cache.kind == 'memcache':
				One.Cache.Memcache.remove(name)
			elif One.Cache.kind == 'file':
				One.Cache.File.remove(name)
			elif One.Cache.kind == 'db':
				One.Cache.Db.remove(name)

		@staticmethod
		def info(name: str):
			if One.Cache.kind == 'memcache':
				return One.Cache.Memcache.info(name)
			elif One.Cache.kind == 'file':
				return One.Cache.File.info(name)
			elif One.Cache.kind == 'db':
				return One.Cache.Db.info(name)

		@staticmethod
		def list():
			if One.Cache.kind == 'memcache':
				return One.Cache.Memcache.list()
			elif One.Cache.kind == 'file':
				return One.Cache.File.list()
			elif One.Cache.kind == 'db':
				return One.Cache.Db.list()

		@staticmethod
		def clear():
			if One.Cache.kind == 'memcache':
				One.Cache.Memcache.clear()
			elif One.Cache.kind == 'file':
				One.Cache.File.clear()
			elif One.Cache.kind == 'db':
				One.Cache.Db.clear()

		class File:
			
			@staticmethod
			def run():
				path = One.get('settings.cache.file.path', One.path(One.Dir.current(), 'cache'))
				if not One.Dir.exists(path):
					One.Dir.create(path)

			@staticmethod
			def get(name: str, default = None):
				hash = One.md5(name)
				path = One.path(One.get('settings.cache.file.path', One.path(One.Dir.current(), 'cache')), hash)
				if One.File.exists(path):
					data = One.File.read(path, True)
					info = One.File.read(path + '.info', True)
					info = One.Json.decode(info)
					match info['type']:
						case 'string':
							data = data.decode('utf-8')
						case 'json':
							data = One.Json.decode(data)
						case 'int':
							data = int(data)
						case 'float':
							data = float(data)
						case 'bool':
							data = bool(data)
					return data
				else:
					return default

			@staticmethod
			def set(name: str, value):
				hash = One.md5(name)
				path = One.path(One.get('settings.cache.file.path', One.path(One.Dir.current(), 'cache')), hash)
				if value != None:
					kind = type(value)
					if kind is str:
						kind = 'string'	
						value = str.encode(value)
					elif kind is dict or kind is list:
						kind = 'json'
						value = str.encode(str(One.Json.encode(value, False)))
					elif kind is int:
						kind = 'int'
						value = str.encode(str(value))
					elif kind is float:
						kind = 'float'
						value = str.encode(str(value))
					elif kind is bool:
						kind = 'bool'
						value = str.encode(str(value))
					else:
						kind = 'byte'
					One.File.write(path, value)
					One.File.write(path + '.info', One.Json.encode({
						"name": name,
						"type": kind,
						"time": One.time(),
						"size": len(value)
					}, False))
				else:
					One.Cache.File.remove(name)
				pass

			@staticmethod
			def remove(name: str):
				hash = One.md5(name)
				path = One.path(One.get('settings.cache.file.path', One.path(One.Dir.current(), 'cache')), hash)
				if One.File.exists(path):
					One.File.remove(path)
					One.File.remove(path + '.info')

			@staticmethod
			def info(name: str):
				hash = One.md5(name)
				path = One.path(One.get('settings.cache.file.path', One.path(One.Dir.current(), 'cache')), hash)
				if One.File.exists(path):
					info = One.File.read(path + '.info', True)
					return One.Json.decode(info)
				return None

			@staticmethod
			def list():
				result = []
				path = One.get('settings.cache.file.path', One.path(One.Dir.current(), 'cache'))
				for name in One.Dir.list(path):
					if name.endswith('.info'):
						info = One.File.read(One.path(path, name), True)
						result.append(One.Json.decode(info))
				return result

			@staticmethod
			def clear():
				path = One.get('settings.cache.file.path', One.path(One.Dir.current(), 'cache'))
				One.Dir.clear(path)

		class Memcache:

			memcache = None

			@staticmethod
			def run():
				server = One.get('settings.cache.memcache.server', '127.0.0.1')
				port = One.get('settings.cache.memcache.port', 11211)
				One.Cache.Memcache.memcache = pymemcache.client.base.Client((server, port))

			@staticmethod
			def get(name: str, default = None):
				hash = One.md5(name)
				info = One.Cache.Memcache.memcache.get(hash + ".info")
				if info == None:
					return default
				info = One.Json.decode(info)
				data = One.Cache.Memcache.memcache.get(hash, default)
				if data != default:
					match info['type']:
						case 'string':
							data = data.decode('utf-8')
						case 'json':
							data = One.Json.decode(data)
						case 'int':
							data = int(data)
						case 'float':
							data = float(data)
						case 'bool':
							data = bool(data)
				return data

			@staticmethod
			def set(name: str, value):
				hash = One.md5(name)
				if value != None:
					kind = type(value)
					if kind is str:
						kind = 'string'	
					elif kind is dict or kind is list:
						kind = 'json'
						value = One.Json.encode(value, False)
					elif kind is int:
						kind = 'int'
					elif kind is float:
						kind = 'float'
					elif kind is bool:
						kind = 'bool'
					else:
						kind = 'byte'
					One.Cache.Memcache.memcache.set(hash + ".info", One.Json.encode({
						"name": name,
						"type": kind,
						"time": One.time(),
						"size": len(str(value))
					}, False))
					One.Cache.Memcache.memcache.set(hash, value)
					names = One.Cache.Memcache.memcache.get('names')
					if names != None:
						names = One.Json.decode(names)
					else:
						names = []
					if name not in names:
						names.append(name)
						One.Cache.Memcache.memcache.set('names', One.Json.encode(names, False))
				else:
					One.Cache.Memcache.remove(name)

			@staticmethod
			def remove(name: str):
				names = One.Cache.Memcache.memcache.get('names')
				if names != None:
					names = One.Json.decode(names)
					if name in names:
						names.remove(name)
						One.Cache.Memcache.memcache.set('names', One.Json.encode(names, False))
						hash = One.md5(name)
						One.Cache.Memcache.memcache.delete(hash + ".info")
						One.Cache.Memcache.memcache.delete(hash)

			@staticmethod
			def info(name: str):
				hash = One.md5(name)
				info = One.Cache.Memcache.memcache.get(hash + ".info")
				return One.Json.decode(info) if info != None else None

			@staticmethod
			def list():
				names = One.Cache.Memcache.memcache.get("names")
				if names != None:
					return One.Json.decode(names)
				return []

			@staticmethod
			def clear():
				for name in One.Cache.Memcache.list():
					hash = One.md5(name)
					One.Cache.Memcache.memcache.delete(hash + ".info")
					One.Cache.Memcache.memcache.delete(hash)
				One.Cache.Memcache.memcache.delete('names')

		class Db:

			db = None

			@staticmethod
			def run():
				# Will be available in June 2022
				pass

			@staticmethod
			def get(name: str, default = None):
				# Will be available in June 2022
				pass

			@staticmethod
			def set(name: str, value):
				# Will be available in June 2022
				pass

			@staticmethod
			def remove(name: str):
				# Will be available in June 2022
				pass

			@staticmethod
			def info(name: str):
				# Will be available in June 2022
				pass

			@staticmethod
			def list():
				# Will be available in June 2022
				pass

			@staticmethod
			def clear():
				# Will be available in June 2022
				pass

	# Debug

	@staticmethod
	def trace():
		return traceback.format_exc()

	@staticmethod
	def reason(error):
		return repr(error)

	# Log

	@staticmethod
	def log(message, code = None, data = None):
		# Will be available in June 2022
		One.echo(message)
		kind = ''
		match kind:
			case 'file':
				pass
			case 'system':
				pass
			case 'request':
				pass
			case 'db':
				pass
			case 'mail':
				pass

	# SQL

	class Sql:

		current = None
		db = {}

		@staticmethod
		def open(name: str, host: str, user: str, password: str, database: str = None):
			if name == None:
				name = host + user + str(database)
			try:
				db[name] = {
					'connection': connect(
						host=host,
						user=user,
						password=password,
						database=database
					),
					'database': database,
					'cursor': None
				}
				One.Sql.current = name
			except Error as error:
				One.error("Connection failed " + str(error))

		@staticmethod
		def close(name: str = None):
			if name == None:
				name = One.Sql.current
			if name in db:
				if db[name].connection != None:
					db[name].connection.close()
				del db[name]

		@staticmethod
		def list():
			return db.keys()

		@staticmethod
		def query(name: str, query: str, param: list = None):
			if name == None:
				name = One.Sql.current
			One.Sql.db[name].cursor = One.Sql.connection.cursor()
			One.Sql.db[name].cursor.execute(query, param)

		@staticmethod
		def cursor(name: str = None):
			if name == None:
				name = One.Sql.current
			return One.Sql.db[name].cursor if name in One.Sql.db else None

		@staticmethod
		def db(name: str = None):
			if name == None:
				name = One.Sql.current
			return One.Sql.db[name] if name in One.Sql.db else None

		@staticmethod
		def commit(name: str = None):
			One.Sql.db(name).connection.commit()

		@staticmethod
		def rollback(name: str = None):
			One.Sql.db(name).connection.rollback()

		@staticmethod
		def fetch(name: str = None):
			cursor = One.Sql.cursor(name)
			columns = [col[0] for col in cursor.description]
			return [dict(zip(columns, row)) for row in cursor.fetchone()][0]

		@staticmethod
		def all(name: str = None):
			cursor = One.Sql.cursor(name)
			columns = [col[0] for col in cursor.description]
			return [dict(zip(columns, row)) for row in cursor.fetchall()]

		@staticmethod
		def size(name: str = None, table = None, total: bool = False):
			if name == None:
				name = One.Sql.current
			where = f" WHERE table_schema = '{table}'" if table != None else ''
			query = f"SELECT table_schema AS 'name', SUM(data_length + index_length) AS 'size' FROM information_schema.tables{where} GROUP BY table_schema"
			One.Sql.query(name, query)
			if table == None:
				if not total:
					columns = [col[0] for col in One.Sql.db[name].cursor.description]
					return [dict(zip(columns, row)) for row in One.all(name)]
				else:
					total = 0
					for row in One.Sql.all(name):
						total = total + row[1]
					return total
			else:
				result = One.Sql.db[name].cursor.fetchall()
				if len(result):
					return result[0][1]
				else:
					return None

		@staticmethod
		def where(condition):
			if type(condition[2]) is str:
				condition[2] = f"'{condition[2]}'"
			result = f' WHERE `{condition[0]}` {condition[1]} {condition[2]}'
			return result

		class Database:

			@staticmethod
			def list(name: str = None):
				One.Sql.query(name, 'SHOW DATABASES')
				result = []
				for db in One.Sql.db(name).cursor:
					result.append(db[0])
				return result

			@staticmethod
			def create(name: str, database: str):
				One.Sql.query(name, 'CREATE DATABASE %s', [database])

			@staticmethod
			def remove(name: str, database: str):
				One.Sql.query(name, 'DROP DATABASE IF EXISTS %s', [database])

			@staticmethod
			def open(name: str, database):
				One.Sql.query(name, 'USE %s', [database])
				One.Sql.db[name].database = name

		class Table:

			@staticmethod
			def list(name: str):
				if name == None:
					name = One.Sql.current
				One.Sql.query(name, f"SHOW TABLES")
				result = []
				for db in One.Sql.db[name].cursor:
					result.append(db[0])
				return result

			@staticmethod
			def create(name: str, field):
				fields = []
				indices = []

				for key, value in field.items():
					fieldType = None
					defaultValue = ''
					length = ''
					null = ''
					default = ' DEFAULT NULL'
					unique = ''
					enum = None
					index = None

					if type(value) is str:
						fieldType = value
						if fieldType == 'ref':
							index = True

					elif type(value) is list:
						if len(value) == 0:
							continue
						if len(value) > 0:
							fieldType = value[0]
						if len(value) > 1 and value[1]:
							index = value[1]

					elif type(value) is dict:
						if 'type' not in value:
							continue
						fieldType = value['type']
						if 'default' in value:
							defaultValue = value['defaullt']
							if type(value['default']) is str:
								default = f" DEFAULT '{value['default']}'"
							else:
								default = f" DEFAULT {value['default']}"
						if 'length' in value:
							length = f"({value['length']})"
						if 'null' in value:
							null = '' if value['null'] else ' NOT NULL'
						if 'index' in value:
							index = value['index']
						if 'unique' in value:
							unique = ' UNIQUE' if value['unique'] else ''

					elif value == None:
						fieldType = key

					if type(fieldType) is list:
						enum = "'" + "','".join(fieldType) + "'"
						fieldType = 'enum'

					match fieldType:
						case 'string' | 'unique':
							if length == '':
								length = '(255)'
							if fieldType == 'unique':
								unique = ' UNIQUE'
							fields.append(f'`{key}` VARCHAR{length}{null}{unique}{default}')
						case 'int' | 'timestamp' | 'ref':
							fields.append(f'`{key}` BIGINT{length}{null}{unique}{default}')
						case 'tiny':
							fields.append(f'`{key}` TINYINT{length}{null}{unique}{default}')
						case 'bool':
							default = ' DEFAULT 1' if defaultValue else ' DEFAULT 0'
							fields.append(f'`{key}` TINYINT{length}{null}{unique}{default}')
						case 'json':
							fields.append(f'`{key}` JSON{length}{null}{unique}{default}')
						case 'text':
							fields.append(f'`{key}` TEXT{length}{null}{unique}{default}')
						case 'float' | 'price':
							fields.append(f'`{key}` DOUBLE{length}{null}{unique}{default}')
						case 'id': 
							fields.append(f'`{key}` BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY')
						case 'enum':
							fields.append(f'`{key}` ENUM ({enum})')

					if index == True:
						indices.append([key, [key], unique != ''])
					elif type(index) is list:
						indices.append(['_'.join(index), index, unique != ''])
					elif type(index) is str:
						indices.append([index, [key], unique != ''])

				fields = ','.join(fields)
				query = f"CREATE TABLE `{name}` ({fields})"
				One.Sql.query(query)
				for index in indices:
					One.Sql.Index.create(name, index[0], index[1], index[2])

			@staticmethod
			def remove(name):
				One.Sql.query(f"DROP TABLE IF EXISTS `{name}`")

			@staticmethod
			def clear(name):
				One.Sql.query(f"TRUNCATE TABLE `{name}`")


		class Column:

			@staticmethod
			def list(name: str, table: str, database: str = None):
				if name == None:
					name = One.Sql.current

			@staticmethod
			def create(name: str):
				if name == None:
					name = One.Sql.current

			@staticmethod
			def remove(name: str):
				if name == None:
					name = One.Sql.current

		class Index:

			@staticmethod
			def list(name: str, index: str):
				if name == None:
					name = One.Sql.current
				result = []
				One.Sql.query(name, 'SHOW INDEX FROM %s', [index])
				for row in One.Sql.cursor.fetchall():
					result.append(row)
				return result			

			@staticmethod
			def create(name: str, inedx: str, table: str, index: str, column = None, unique = False):
				if name == None:
					name = One.Sql.current
				columns = []
				if unique:
					unique = ' UNIQUE'
				else:
					unique = ''
				if column == None:
					column = [name]
				elif type(column) is str:
					column = [column]
				for column in column:
					columns.append('`' + column + '`')
				columns = ','.join(columns)
				One.Sql.query(f"CREATE{unique} INDEX `{name}` ON `{table}` ({columns})")

			@staticmethod
			def remove(name: str, index: str):
				One.Sql.query(name, 'DROP INDEX IF EXISTS %s', [index])

		class Row:

			@staticmethod
			def list(name: str, row, count = None, offset = 0):
				if name == None:
					name = One.Sql.current
				limit = f' LIMIT {offset},{count}' if count != None else ''
				One.Sql.query(f"SELECT * FROM `{name}`{limit}")
				columns = [col[0] for col in One.Sql.cursor.description]
				return [dict(zip(columns, row)) for row in One.Sql.cursor.fetchall()]

			@staticmethod
			def count(name: str, row, estimate: bool = False, database: str = None):
				if name == None:
					name = One.Sql.current
				if database == None:
					database = One.Sql.db
				if not estimate:
					One.Sql.query(f"SELECT COUNT(*) FROM `{name}`")
				else:
					One.Sql.query(f"SELECT `table_rows` FROM `information_schema`.`tables` WHERE `table_name`='{name}' AND `table_schema`='{database}'")
				return One.Sql.cursor.fetchone()[0]

			@staticmethod
			def create(name: str, row, value):
				if name == None:
					name = One.Sql.current
				columns = ''
				values = []
				if type(value) is list:
					for value in value:
						if type(value) is str:
							values.append("'" + value + "'")
						else:
							values.append(str(value))
				if type(value) is dict:
					columns = []
					for key, value in value.items():
						columns.append('`' + key + '`')
						if type(value) is str:
							for i, j in [('\\', '\\\\'), ('\n', '\\n'), ('\r', '\\r'), ("'", "\\'"), ('"', '\\"')]:
								value = value.replace(i, j)
							values.append("'" + value + "'")
						elif value == True:
							values.append('1')
						elif value == False:
							values.append('0')
						elif value == None:
							values.append('NULL')
						else:
							values.append(str(value))
					columns = ' (' + ','.join(columns) + ')'
				values = ','.join(values)
				query = f"INSERT INTO `{name}`{columns} VALUES ({values})"
				One.Sql.query(query)

			@staticmethod
			def update(name: str, row, value, condition):
				if name == None:
					name = One.Sql.current
				values = []
				for key, value in value.items():
					if type(value) is str:
						value = f"'{value}'"
					values.append(f'`{key}` = {value}')
				values = ','.join(values)
				where = One.Sql.where(condition)
				One.Sql.query(f"UPDATE `{name}` SET {values}{where}")

			@staticmethod
			def remove(name: str, row: str):
				if name == None:
					name = One.Sql.current

		class User:

			@staticmethod
			def list(name: str = None):
				if name == None:
					name = One.Sql.current

			@staticmethod
			def create(name: str, user):
				if name == None:
					name = One.Sql.current

			@staticmethod
			def remove(name: str, user: str):
				if name == None:
					name = One.Sql.current

		class Function:

			@staticmethod
			def list(name: str = None):
				if name == None:
					name = One.Sql.current

			@staticmethod
			def create(name: str, function):
				if name == None:
					name = One.Sql.current

			@staticmethod
			def remove(name: str, function: str):
				One.Sql.query(name, 'DROP FUNCTION IF EXISTS %s', [function])

		class View:

			@staticmethod
			def list(name: str = None):
				if name == None:
					name = One.Sql.current

			@staticmethod
			def create(name: str, view):
				if name == None:
					name = One.Sql.current

			@staticmethod
			def remove(name: str, view: str):
				if name == None:
					name = One.Sql.current

	# UI

	class Ui:

		class Web:

			@staticmethod
			def attrib(data: dict):
				result = ''
				for name, value in data.items():
					if name == 'style':
						if type(value) is dict and len(value) > 0:
							result += ' style="'
							for name, value in value.items():
								result += name + ':' + str(value) + ';'
							result += '"'
					else:
						if name == 'class' and type(value) is list and len(value) > 0:
							value = ' '.join(value)
						result += ' ' + name + '=' + ('"' + value.replace('"', '\\"') + '"' if type(value) is str else str(value))
				return result

			@staticmethod
			def create(data: list):
				result = ''
				for ui in data:
					kind = type(ui);
					if kind is list:
						if len(ui) > 0:
							ui_name = ui[0]
							ui_param = ui
							length = len(ui_param)
						else:
							continue
					elif kind is str:
						ui_name = ui
						ui_param = [ui]
					else:
						continue
					match ui_name:
						case 'action':
							action = ui_param[1]
							One.action(action)
							del action
						case 'html':
							body = ui_param[1]
							attrib = One.Ui.Web.attrib(ui_param[2]) if length > 2 else ''
							result += f'<!DOCTYPE html><html{attrib}>'
							result += One.Ui.Web.create(body)
							result += '</html>'
							del attrib
							del body
						case 'text' | 'text.inline' | 'text.block':
							text = ui_param[1]
							if type(text) is str:
								text = One.value(text)
								text = One.Escape.html(text, True)
								text = One.Html.minimark(text)
							elif type(text) is list:
								text = One.Ui.Web.create(text)
							attrib = One.Ui.Web.attrib(ui_param[2]) if length > 2 else ''
							match ui_name:
								case 'text':
									result += f'<p{attrib}>{text}</p>'
								case 'text.inline':
									result += f'<span{attrib}>{text}</span>'
								case 'text.block':
									result += f'<div{attrib}>{text}</div>'
							del text
							del attrib
						case 'text.plain':
							text = ui_param[1]
							text = One.value(text)
							text = One.Escape.html(text)
							text = One.Html.minimark(text)
							attrib = One.Ui.Web.attrib(ui_param[2]) if length > 2 else ''
							result += f'<span{attrib}>{text}</span>'
							del text
							del attrib						
						case 'newline':
							number = ui_param[1] if length > 1 else 1
							attrib = One.Ui.Web.attrib(ui_param[2]) if length > 2 else ''
							result += f'<br{attrib}>' * number
							del number
							del attrib
						case 'head':
							body = ui_param[1]
							attrib = One.Ui.Web.attrib(ui_param[2]) if length > 2 else ''
							result += f'<head{attrib}>'
							result += One.Ui.Web.create(body)
							result += '</head>'
							del body
							del attrib
						case 'title':
							title = One.Escape.html(One.value(str(ui_param[1])))
							attrib = One.Ui.Web.attrib(ui_param[2]) if length > 2 else ''
							result += f'<title{attrib}>{title}</title>'
							del title
							del attrib
						case 'body':
							body = ui_param[1]
							attrib = One.Ui.Web.attrib(ui_param[2]) if length > 2 else ''
							result += f'<body{attrib}>'
							result += One.Ui.Web.create(body)
							result += '</body>'
							del body
							del attrib
						case 'image':
							path = One.Escape.html(ui_param[1])
							attrib = One.Ui.Web.attrib(ui_param[2]) if length > 2 else ''
							result += f'<img src="{path}"{attrib}>'
							del path
							del attrib
						case 'script':
							path = ui_param[1]
							attrib = One.Ui.Web.attrib(ui_param[2]) if length > 2 else ''
							result += f'<script src="{path}"{attrib}></script>'
							del path
							del attrib
						case 'script.code':
							code = ui_param[1]
							result += f'<script>{code}</script>'
							del code
						case 'style':
							path = ui_param[1]
							attrib = One.Ui.Web.attrib(ui_param[2]) if length > 2 else ''
							result += f'<link href="{path}" rel="stylesheet"{attrib}>'
							del path
							del attrib
						case 'meta.default':
							result += '<meta charset="utf-8">'
							result += '<meta name="viewport" content="width=device-width, initial-scale=1">'
						case 'charset':
							code = ui_param[1] if len(ui_param) > 1 else 'utf-8'
							result += f'<meta charset="{code}">'
							del code
						case 'viewport':
							result += '<meta name="viewport" content="width=device-width, initial-scale=1">'
						case 'icon' | 'icon.square' | 'icon.round':
							name = ui_param[1]
							kind = ui_param[2] if len(ui_param) > 2 else 'solid'
							attrib = ui_param[3] if length > 3 else {}
							if 'class' not in attrib:
								attrib['class'] = []
							elif type(attrib['class']) is str:
								attrib['class'] = [attrib['class']]
							attrib['class'].append(f'fa-{name}')
							match kind:
								case 'solid':
									attrib['class'].append('fas')
								case 'brands' | 'brand':
									attrib['class'].append('fab')
								case 'regular':
									attrib['class'].append('far')
							if ui_name == 'icon.round':
								attrib['class'].append('rounded-circle')
							attrib = One.Ui.Web.attrib(attrib)
							result += f'<i{attrib}></i>'
							del name
							del kind
							del attrib
						case 'header':
							size = ui_param[1]
							text = ui_param[2]	
							if type(text) is str:
								text = One.Escape.html(text)
							elif type(text) is list:
								text = One.Ui.Web.create(text)
							attrib = One.Ui.Web.attrib(ui_param[3]) if length > 3 else ''
							match size:
								case 'main' | 1:
									result += f'<h1{attrib}>{text}</h1>'
								case 'large' | 2:
									result += f'<h2{attrib}>{text}</h2>'
								case 'big'| 3:
									result += f'<h3{attrib}>{text}</h3>'
								case 'small'| 4:
									result += f'<h4{attrib}>{text}</h4>'
								case 'tiny' | 5:
									 result += f'<h5{attrib}>{text}</h5>'
								case 'mini' | 6:
									result += f'<h6{attrib}>{text}</h6>'
								case _:
									result += f'<h1{attrib}>{text}</h1>'
							del size
							del text
							del attrib
						case 'tag':
							name = ui_param[1]
							body = ui_param[2] if length > 2 else []
							attrib = ui_param[3] if length > 3 else {}
							attrib = One.Ui.Web.attrib(attrib)
							result += f'<{name}{attrib}>'
							result += One.Ui.Web.create(body)
							result += f'</{name}>'
							del name
							del body
							del attrib
						case 'group':
							body = ui_param[1] if length > 1 else []
							attrib = ui_param[2] if length > 2 else {}
							if 'tap' in attrib:
								attrib['onclick'] = "location.href='" + One.Escape.html(attrib['tap']) + "'"
								del attrib['tap']
							attrib = One.Ui.Web.attrib(attrib)
							result += f'<div{attrib}>' +  One.Ui.Web.create(body) + '</div>'
							del body
							del attrib
						case 'group.input':
							body = ui_param[1] if length > 1 else []
							attrib = ui_param[2] if length > 2 else {}
							if 'class' not in attrib:
								attrib['class'] = []
							attrib['class'].append('input-group');
							attrib = One.Ui.Web.attrib(attrib)
							result += f'<div{attrib}>'
							result += One.Ui.Web.create(body)
							result += f'</div>'
							del body
							del attrib
						case 'link':
							link = One.value(ui_param[1])
							body = ui_param[2]
							if type(body) is str:
								body = One.Escape.html(body)
							elif type(body) is list:
								body = One.Ui.Web.create(body)
							attrib = ui_param[3] if length > 3 else {}
							attrib['href'] = link
							attrib = One.Ui.Web.attrib(attrib)
							result += f'<a{attrib}>{body}</a>'
							del link
							del body
							del attrib
						case 'row':
							body = ui_param[1] if length > 1 else []
							attrib = ui_param[2] if length > 2 else {}
							if 'class' not in attrib:
								attrib['class'] = []
							elif type(attrib['class']) is str:
								attrib['class'] = [attrib['class']]
							attrib['class'].append('row')
							attrib = One.Ui.Web.attrib(attrib)
							result += f'<div{attrib}>'
							result += One.Ui.Web.create(body)
							result += '</div>'
							del body
							del attrib
						case 'col':
							body = ui_param[1] if length > 1 else []
							attrib = ui_param[2] if length > 2 else {}
							if 'class' not in attrib:
								attrib['class'] = []
							elif type(attrib['class']) is str:
								attrib['class'] = [attrib['class']]
							attrib['class'].append('col')
							attrib = One.Ui.Web.attrib(attrib)
							result += f'<div{attrib}>'
							result += One.Ui.Web.create(body)
							result += '</div>'
							del body
							del attrib
						case 'data':
							name = ui_param[1]
							if 'data' in One.data and name in One.data['data']:
								result += One.Ui.Web.create(One.data['data'][name])
							del name
						case 'column':
							number = ui_param[1]
							body = ui_param[2]
							attrib = ui_param[3] if length > 3 else {}
							if 'class' not in attrib:
								attrib['class'] = []
							elif type(attrib['class']) is str:
								attrib['class'] = [attrib['class']]
							if 'style' not in attrib:
								attrib['style'] = {}
							attrib['class'].append('columns')
							attrib['style']['column-count'] = number
							attrib = One.Ui.Web.attrib(attrib)
							result += f'<div{attrib}>'
							result += One.Ui.Web.create(body)
							result += '</div>'
							del body
							del number
						case 'box':
							title = ui_param[1]
							title = One.Escape.html(title)
							image = ui_param[2]
							url = ui_param[3]
							attrib = ui_param[4] if length > 4 else {}
							if 'class' not in attrib:
								attrib['class'] = []
							if 'style' not in attrib:
								attrib['style'] = {}
							attrib['class'].append('box')
							attrib['style']['break-inside'] = 'avoid-column'
							attrib = One.Ui.Web.attrib(attrib)
							result += f'<div{attrib}><a href="{url}" class="nolink"><img class="rounded" src="{image}"><h6>{title}</h6></a></div>'
							del image
							del title
							del url
							del attrib
						case 'footer':
							text = ui_param[1]
							text = One.Escape.html(text)
							result += f'<footer>{text}</footer>'
							del text
						case 'button':
							text = ui_param[1]
							text = One.Escape.html(text)
							url = ui_param[2] if length > 2 else None
							outline = bool(ui_param[3]) if length > 3 else False
							attrib = ui_param[4] if length > 4 else {}
							if 'class' not in attrib:
								attrib['class'] = []
							attrib['class'].append("btn")
							attrib['class'].append("btn-outline-dark" if outline else "btn-dark")
							if type(url) is str:
								attrib['onclick'] = f'window.location.href=\'{url}\';'
							attrib = One.Ui.Web.attrib(attrib)
							result += f'<button{attrib}>{text}</button>'
							del text
							del outline
							del attrib
						case 'button.drop':
							text = ui_param[1]
							text = One.Escape.html(text)
							data = ui_param[2]
							outline = bool(ui_param[3]) if length > 3 else False
							attrib = ui_param[4] if length > 4 else {}
							if 'class' not in attrib:
								attrib['class'] = []
							attrib['class'].append("btn")
							attrib['class'].append("btn-outline-dark" if outline else "btn-dark")
							attrib['class'].append("dropdown-toggle")
							hash = One.hash(16)
							if 'id' not in attrib:
								attrib['id'] = hash
							else:
								hash = attrib['id']
							attrib['type'] = "button"
							attrib['data-bs-toggle'] = "dropdown"
							attrib['aria-expanded'] = "false"
							attrib = One.Ui.Web.attrib(attrib)
							items = ''
							for item in data:
								item_title = One.Escape.html(item[0])
								items += f'<li><a class="dropdown-item" href="javascript:void(0);" onclick="$(\'#{hash}\').text(\'{item_title}\');">{item_title}</a></li>'
							result += f'<div class="btn-group" role="group"><button{attrib}>{text}</button><ul class="dropdown-menu" aria-labelledby="{hash}">{items}</ul></div>'
							del text
							del data
							del outline
							del attrib							
							del hash
							del items
						case 'progress':
							pass
						case 'float':
							pass
						case 'form':
							body = ui_param[1]
							body = One.Ui.Web.create(body)
							attrib = ui_param[2] if length > 2 else {}
							attrib = One.Ui.Web.attrib(attrib)
							result += f'<form{attrib}>{body}</form>'
							del body
							del attrib
						case 'edit':
							name = ui_param[1]
							value = ui_param[2] if length > 2 else ''
							placeholder = ui_param[3] if length > 3 else ''
							kind = ui_param[4] if length > 4 else 'text'
							attrib = ui_param[5] if length > 5 else {}
							value = One.Escape.html(value)
							if 'class' not in attrib:
								attrib['class'] = []
							attrib['class'].append("form-control")
							if kind == 'text.big':
								if 'rows' not in attrib:
									attrib['rows'] = 3
								attrib = One.Ui.Web.attrib(attrib)
								result += f'<textarea{attrib}>{value}</textarea>'
							else:
								attrib['value'] = value
								attrib['type'] = kind
								attrib['placeholder'] = placeholder
								attrib['aria-label'] = placeholder
								attrib = One.Ui.Web.attrib(attrib)
								result += f'<input{attrib}>'
							del name
							del value
							del placeholder
							del kind
							del attrib
						case 'slider':
							pass
						case 'video':
							pass
						case 'menu':
							pass
						case 'select':
							pass
						case 'switch':
							pass
						case 'tab':
							pass
						case 'content':
							pass
						case 'list':
							header = ui_param[1]
							data = ui_param[2]
							attrib = ui_param[3] if length > 3 else {}
							if 'class' not in attrib:
								attrib['class'] = []
							attrib['class'].append('table')
							attrib['class'].append('table-striped')
							attrib = One.Ui.Web.attrib(attrib)
							result += f'<table{attrib}>'
							result += '<thead><tr>'
							for title in header:
								title = One.Escape.html(title)
								result += f'<th scope="col">{title}</th>'
							result += '</tr></thead>'
							result += '<tbody>'
							for row in data:
								result += '<tr>'
								width = 100.0 / len(row)
								for col in row:
									col = One.Escape.html(col, True)
									result += f'<td style="width: {width}%">{col}</td>'
								result += '</tr>'
							result += '</tbody></table>'
							del header
							del data
						case 'list.number':
							data = ui_param[1]
							attrib = ui_param[2] if length > 2 else {}
							attrib = One.Ui.Web.attrib(attrib)
							result += f'<ol{attrib}>'
							for text in data:
								text = One.Escape.html(text)
								text = One.Html.minimark(text)
								result += f'<li>{text}</li>'
							result += '</ol>'
							del data
							del attrib
						case 'tab.collapse':
							data = ui_param[1]
							result += f'<div class="accordion">'
							for item in data:
								title = item[0]
								title = One.Escape.html(title)
								body = item[1]
								body = One.Ui.Web.create(body)
								hash = One.hash(16, 'letter')
								result += f'<div class="accordion-item"><h2 class="accordion-header" id="{hash}header"><button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#{hash}" aria-expanded="false" aria-controls="{hash}">{title}</button></h2><div id="{hash}" class="accordion-collapse collapse" aria-labelledby="{hash}header"><div class="accordion-body">{body}</div></div></div>'
							result += '</div>'
							del data						
						case 'tile':
							pass
						case 'notification':
							pass
						case 'modal':
							pass
						case 'page':
							pass
						case 'spinner':
							pass
						case 'hstack':
							pass
						case 'vstack':
							pass
						case 'line.vertical':
							result += f'<div class="one-line-vertical" style="width: 100%; text-align: center;"><span></span></div>'
						case 'map.google':
							pass
						case 'map.yandex':
							if not (len(ui_param) > 1 and type(ui_param[1]) is dict):
								continue
							data = ui_param[1]
							if 'key' in data:
								key = data['key']
								del data['key']
							else:
								continue
							attrib = []
							if 'height' in data:
								attrib.append('height=' + str(data['height']))
								del data['height']
							if 'language' in data:
								attrib.append('lang=' + str(data['language']))
								del data['language']
							if 'scroll' in data:
								attrib.append('scroll=' + ('true' if bool(data['scroll']) else 'false'))
								del data['scroll']
							if len(attrib) > 0:
								attrib = '&amp;' + '&amp;'.join(attrib)
							else:
								attrib = ''
							if len(data) > 0:
								result += f'<div' + One.Ui.Web.attrib(data) + '>'
							result += f'<script type="text/javascript" charset="utf-8" async src="https://api-maps.yandex.ru/services/constructor/1.0/js/?um=constructor%3A{key}{attrib}"></script>'
							if len(data) > 0:
								result += '</div>'
							del data
							del key
							del attrib
						case 'url':
							pass
						case 'gallery':
							pass
						case 'code':
							language = ui_param[1]
							code = ui_param[2]
							attrib = ui_param[3] if length > 3 else {}
							clipboard = code.replace('\\', '\\\\').replace('\'', '\\\'').replace('"', '&quot;').replace('\r', '\\r').replace('\n', '\\n')
							attrib['ondblclick'] =f'one.clipboard(\'{clipboard}\');one.toast.show(\'Code copied to clpboard\');'
							attrib = One.Ui.Web.attrib(attrib)
							result += f'<p><pre><code class="language-{language} rounded"{attrib}>{code}</code></pre></p>'
							del language
							del code
							del attrib
						case 'plain':
							value = ui_param[1]
							result += value
							del value
						case 'navbar':
							data = ui_param[1]
							attrib = One.Ui.Web.attrib(ui_param[2]) if length > 2 else ''
							result += f'<nav class=\"navbar fixed-top\"{attrib}><div class=\"container-fluid\"><div class=\"navbar-header\">'
							result += One.Ui.Web.create(data)
							result += '</div></div></nav>'
							del data
							del attrib
						case 'breadcrumbs':
							title = ui_param[1]
							title = One.Escape.html(title)
							parent = ui_param[2] if length > 2 else None
							if parent != None:
								result += f'<h2 class="title"><a href="{parent}" class="nolink">← {title}</a></h2>'
							else:
								result += f'<h2 class="title">{title}</h2>'
							del title
							del parent
						case 'head.default':
							result += '<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><link rel="icon" type="image/x-icon" href="/static/image/favicon.ico"><script src="/static/js/bootstrap.bundle.min.js"></script><link href="/static/css/bootstrap.min.css" rel="stylesheet"><link href="/static/css/fontawesome.min.css" rel="stylesheet"><script src="/static/js/jquery.min.js"></script>'
						case 'carousel':
							data = ui_param[1]
							attrib = ui_param[2] if length > 2 else {}
							if 'id' in attrib:
								id = attrib['id']
								del attrib['id']
							else:
								id = 'carousel'
							attrib = One.Ui.Web.attrib(attrib)
							tabs = ''
							items = ''
							data = One.shuffle(data)
							for index, item in enumerate(data):
								leng = len(item)
								image = item[0]
								url = One.value(item[1]) if leng > 1 else ''
								title = item[2] if leng > 2 else ''
								description = item[3] if leng > 3 else ''
								if title != '':
									title = f'<h5>{title}</h5>'
								if description != '':
									description = f'<p>{description}</p>'
								classes = ' active' if index == 0 else ''
								if url != '':
									url = f' onclick="window.location.href=\'{url}\'"'
									classes += ' pointer'
								tabs += f'<button type="button" data-bs-target="#carousel" data-bs-slide-to="{index}" class="active" aria-current="true" aria-label="Slide {index}">'
								items += f'<div class="carousel-item{classes}"{url} data-bs-interval="9000"><img src="{image}" class="d-block w-100" alt="..."><div class="carousel-caption d-md-block">{title}{description}</div></div>'
								result += ''
							result += f'<div{attrib}><div id="{id}" class="carousel slide" data-bs-ride="carousel"><div class="carousel-indicators">{tabs}</div><div class="carousel-inner">{items}</div><button class="carousel-control-prev" type="button" data-bs-target="#carousel" data-bs-slide="prev"><span class="carousel-control-prev-icon" aria-hidden="true"></span><span class="visually-hidden">Previous</span></button><button class="carousel-control-next" type="button" data-bs-target="#carousel" data-bs-slide="next"><span class="carousel-control-next-icon" aria-hidden="true"></span><span class="visually-hidden">Next</span></button></div></div>'
							del data
							del tabs
							del items
							del attrib
							del id
						case 'top':
							start = ui_param[1]
							center = ui_param[2] if len(ui_param) > 2 else []
							end = ui_param[3] if len(ui_param) > 3 else []
							attrib = ui_param[4] if len(ui_param) > 4 else {}
							attrib = One.Ui.Web.attrib(attrib)
							result += f'<div{attrib}><div class="row g-0">'
							if len(start) > 0:
								result += '<div class="col"><div class="d-flex justify-content-start align-items-center" style="height: 100%">' + One.Ui.Web.create(start) + '</div></div>'
							if len(center) > 0:
								result += '<div class="col"	><div class="d-flex justify-content-center align-items-center" style="height: 100%">' + One.Ui.Web.create(center) + '</div></div>' 
							if len(end) > 0:
								result += '<div class="col"><div class="d-flex justify-content-end align-items-center" style="height: 100%">' + One.Ui.Web.create(end) + '</div></div>'
							result += '</div></div>'
							del start
							del center
							del end
							del attrib
						case 'panel':
							header = ui_param[1] if len(ui_param) > 1 else ''
							if type(header) is list:
								header = One.Ui.Web.create(header)
							body = ui_param[2] if len(ui_param) > 2 else ''
							if type(body) is list:
								body = One.Ui.Web.create(body)
							attrib = ui_param[3] if len(ui_param) > 3 else {}
							attrib = One.Ui.Web.attrib(attrib)
							result += f'<div class="offcanvas offcanvas-start" tabindex="-1" id="panel" aria-labelledby="panel" data-bs-scroll="false"><div class="offcanvas-header">{header}</div><div class="offcanvas-body"><div{attrib}>{body}</div></div></div>'
							del header
							del body
							del attrib
						case 'favicon':
							if type(ui_param[1]) is str:
								ui_param[1] = {
									'web': ui_param[1],
									'android': ui_param[1],
									'apple': ui_param[1]
								}
							elif type(ui_param[1]) is not dict:
								continue
							for name, value in ui_param[1].items():
								rel = 'shortcut icon'
								if type(value) is str:
									url = value
									extension = One.File.extension(url)
									mime = One.get('settings.http.type.' + extension)
								elif type(value) is dict and 'url' in value:
									url = value['url']
									if 'rel' in value:
										rel = value['rel']
									if 'type' in value:
										mime = value['type']
									else:
										extension = One.File.extension(url)
										mime = One.get('settings.http.type.' + extension)
								else:
									continue
								if mime != None:
									mime = f' type="{mime}"'
								match name:
									case 'browser' | 'web':
										result += f'<link rel="{rel}"{mime} sizes="16x16" href="{url}">'
									case 'android':
										result += f'<link rel="{rel}"{mime} sizes="192x192" href="{url}">'
									case 'apple':
										result += f'<link rel="apple-touch-icon"{mime} href="{url}">'
									case _:
										size = int(name)
										if size > 0:
											result += f'<link rel="{rel}"{mime} sizes="{size}x{size}" href="{url}">'
				return result

	# Format

	class Json:
		
		@staticmethod
		def encode(data, pretty: bool = True, indent: str = '\t'):
			try:
				if pretty:			
					return json.dumps(data, indent=indent, ensure_ascii=False)
				else:
					return json.dumps(data, indent=None, separators=(',',':'), ensure_ascii=False)
			except Exception as error:
				return None

		@staticmethod
		def decode(text):
			try:
				if type(text) is bytes:
					text = text.decode('utf-8')
				return json.loads(text)
			except Exception as error:
				if One.get('settings.verbose'):
					One.echo(One.reason(error))
				return None

	class Yaml:

		@staticmethod
		def encode(data):
			from ruamel import yaml
			return yaml.dump(data)

		@staticmethod
		def decode(text):
			if type(text) is bytes:
				text = text.decode('utf-8')
			#from ruamel import yaml
			return yaml.safe_load(text)

	class Csv:

		@staticmethod
		def encode(data: list, delimiter = ',', line = '\n'):
			buffer = io.StringIO()
			dialect = csv.Dialect
			dialect.delimiter = delimiter
			dialect.lineterminator = line
			dialect.quoting = csv.QUOTE_MINIMAL
			dialect.quotechar = '"'
			writer = csv.writer(buffer, dialect=dialect)
			for row in data:
				writer.writerow(row)
			value = buffer.getvalue().strip(line)
			buffer.seek(0)
			buffer.truncate(0)
			return value

		@staticmethod
		def decode(text, delimiter = ',', line = None):
			if type(text) is bytes:
				text = text.decode('utf-8')
			if line == None:
				line = '\n' if text.find('\r\n') < 0 else '\r\n'
			dialect = csv.Dialect
			dialect.delimiter = delimiter
			dialect.lineterminator = line
			dialect.quoting = csv.QUOTE_MINIMAL
			dialect.quotechar = '"'
			buffer = io.StringIO(text)
			reader = csv.reader(buffer, dialect=dialect)
			result = []
			for row in reader:
				for index, value in enumerate(row):
					if value == 'true':	
						row[index] = True
					elif value == 'false':
						row[index] = False
					elif value == '':
						row[index] = None
					elif value.lstrip('-').replace('.', '', 1).isdigit():
						value = float(value)
						row[index] = value if value % 1 != 0 else int(value)
				result.append(row)
			buffer.seek(0)
			buffer.truncate(0)
			return result

	class Html:

		@staticmethod
		def encode(element, pretty = True, indent = ''):
			if type(element) is list:
				length = len(element)
				if length == 0:
					return ''
				tag = element[0]
				if length > 1:
					body = element[1]
				if length > 2:
					element = element[2]
				else:
					element = {}
			else:
				if 'tag' not in element:
					return ''
				tag = element['tag']
				body = element['body'] if 'body' in element else None
			result = '<' + tag
			for name, value in element.items():
				if name in ['', 'tag', 'body']:
					continue
				if name == 'style':
					if type(value) is dict:
						result += ' style="'
						for name, value in value:
							if type(value) is not str:
								value = str(value)
							result += name + ':' + (' ' if pretty else '') +  (f'"{value}"' if type(value) is str else str(value)) + ';'
						result += '"'
				else:
					result += ' ' + name + '=' + (f'"{value}"' if type(value) is str else str(value))
			result += '>'
			if tag not in ['area', 'base', 'br', 'col', 'command', 'embed', 'hr', 'img', 'input', 'keygen', 'link', 'meta', 'param', 'source', 'track', 'wbr']:
				if type(body) is list:
					for element in body:
						result += One.Html.encode(element)
				elif type(body) is str:
					result += body
				result += '</' + tag + '>'
			return result

		@staticmethod
		def decode(text: str):
			# Will be available in June 2022
			pass

		@staticmethod
		def markdown(text: str):
			# Will be available in June 2022
			pass

		@staticmethod
		def minimark(text: str):
			return re.sub(r'(^|\s)\*(.+?)\*($|\s|[.,:;])', r'\1<strong>\2</strong>\3', text)

	@staticmethod
	def install():
		for name in One.get('about.required.python.pip', []):
			One.shell(One.get('settings.path.python') + ' -m pip install ' + name, None, True)
		One.echo('Restart script')
		One.exit()

# Required

try:
	import rsa
	import requests
	import pymemcache
	import bcrypt
	from ruamel import yaml
	from mysql.connector import connect, Error
except ModuleNotFoundError as error:
	One.echo(error)
	One.install()

# Autorun

One.autorun()