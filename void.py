import time
import importlib
import traceback

class void:

	module = {}
	result = [None]
	data = {
		'about': {
			'name': 'V O I D lang',
			'site': 'https://voidsp.com',
			'version': 1,
			'time': 1725022891
		},
		'debug': {
			'time': False
		},
		'env': {
			'name': 'python',
			'version': {
				'full': '',
				'short': ''
			},
			'path': {
				'python': 'python.exe'
			},
			'arg': {},
			'script': {
				'file': '',
				'path': '',
				'arg': []
			},
			'os': {
				'type': '',
				'name': '',
				'version': ''
			},
			"newline": '',
			"separator": '',
			"required": {
				'version': '3.10',
				'import': [
					'io',
					'sys',
					'os',
					'platform',
					'json',
					'math',
					'hashlib',
					'base64',
					're',
					'binascii',
					'random',
					'string',
					'shutil',
					'urllib.parse',
					'uuid',
					'datetime',
					['subprocess'],
					['cryptography'],
					['gzip'],
					['zlib'],
					['csv'],
					['ssl'],
					['socketserver'],
					['http.cookies'],
					['requests'],
					['rsa'],
					['bcrypt'],
					['ruamel.yaml'],
					['pymemcache'],
					['mysql.connector']
				]
			}
		},
		'stat': {
			'time': {
				'run': {
					'start': 0,
					'end': 0,
					'total': 0
				},
				'import': {
					'total': 0,
					'module': {}
				}
			}
		},
		'db': {},
		'data': {},
		'run': [],
		'web': {},
		'api': {},
		'http': {
			'code': {
				100: "Continue",
				101: "Switching protocols",
				102: "Processing",
				103: "Early Hints",
				200: "OK",
				201: "Created",
				202: "Accepted",
				203: "Non-Authoritative Information",
				204: "No Content",
				205: "Reset Content",
				206: "Partial Content",
				207: "Multi-Status",
				208: "Already Reported",
				226: "IM Used",
				300: "Multiple Choices",
				301: "Moved Permanently",
				302: "Found (Previously \"Moved Temporarily\")",
				303: "See Other",
				304: "Not Modified",
				305: "Use Proxy",
				306: "Switch Proxy",
				307: "Temporary Redirect",
				308: "Permanent Redirect",
				400: "Bad Request",
				401: "Unauthorized",
				402: "Payment Required",
				403: "Forbidden",
				404: "Not Found",
				405: "Method Not Allowed",
				406: "Not Acceptable",
				407: "Proxy Authentication Required",
				408: "Request Timeout",
				409: "Conflict",
				410: "Gone",
				411: "Length Required",
				412: "Precondition Failed",
				413: "Payload Too Large",
				414: "URI Too Long",
				415: "Unsupported Media Type",
				416: "Range Not Satisfiable",
				417: "Expectation Failed",
				418: "I'm a Teapot",
				421: "Misdirected Request",
				422: "Unprocessable Entity",
				423: "Locked",
				424: "Failed Dependency",
				425: "Too Early",
				426: "Upgrade Required",
				428: "Precondition Required",
				429: "Too Many Requests",
				431: "Request Header Fields Too Large",
				451: "Unavailable For Legal Reasons",
				500: "Internal Server Error",
				501: "Not Implemented",
				502: "Bad Gateway",
				503: "Service Unavailable",
				504: "Gateway Timeout",
				505: "HTTP Version Not Supported",
				506: "Variant Also Negotiates",
				507: "Insufficient Storage",
				508: "Loop Detected",
				510: "Not Extended",
				511: "Network Authentication Required"
			},
			'type': {
				'html': 'text/html',
				'htm': 'text/html',
				'xml': 'application/xml',
				'text': 'text/plain',
				'txt': 'text/plain',
				'void': 'text/void',
				'void binary': 'application/octet-stream',
				'css': 'text/css',
				'js': 'text/javascript',
				'mjs': 'text/javascript',
				'csv': 'text/csv',
				'ttf': 'font/ttf',
				'otf': 'font/otf',
				'sfnt': 'font/sfnt',
				'woff': 'font/woff',
				'woff2': 'font/woff2',
				'eot': 'application/vnd.ms-fontobject',
				'svg': 'image/svg+xml',
				'webp': 'image/webp',
				'gif': 'image/gif',
				'jpeg': 'image/jpeg',
				'jpg': 'image/jpeg',
				'png': 'image/png',
				'tiff': 'image/tiff',
				'tif': 'image/tiff',
				'avif': 'image/avif',
				'apng': 'image/apng',
				'ico': 'image/x-icon',
				'icon': 'image/vnd.microsoft.icon',
				'djvu': 'image/vnd.djvu',
				'bin': 'application/octet-stream',
				'ogg': 'application/ogg',
				'pdf': 'application/pdf',
				'xhtml': 'application/xhtml+xml',
				'json': 'application/json',
				'jsonld': 'application/ld+json',
				'zip': 'application/zip',
				'gz': 'application/gzip',
				'7z': 'application/x-7z-compressed',
				'tar': 'application/x-tar',
				'arc': 'application/x-freearc',
				'rar': 'application/vnd.rar',
				'bz': 'application/x-bzip',
				'bz2': 'application/x-bzip2',
				'mpa': 'audio/mpeg',
				'mp2': 'audio/mpeg',
				'mp3': 'audio/mpeg',
				'wma': 'audio/x-ms-wma',
				'wav': 'audio/x-wav',
				'oga': 'audio/ogg',
				'weba': 'audio/webm',
				'cda': 'application/x-cdf',
				'aac': 'audio/aac',
				'ac3': 'audio/ac3',
				'mid': 'audio/midi',
				'midi': 'audio/x-midi',
				'mpeg': 'video/mpeg',
				'mpg': 'video/mpeg',
				'mpv': 'video/mpeg',
				'mp4': 'video/mp4',
				'webm': 'video/webm',
				'ogv': 'video/ogg',
				'qt': 'video/quicktime',
				'mov': 'ideo/quicktime',
				'm4v': 'video/x-m4v',
				'wmv': 'video/x-ms-wmv',
				'avi': 'video/x-msvideo',
				'mkv': 'application/x-matroska',
				'mjpeg': 'multipart/x-mixed-replace',
				'ts': 'video/mp2t',
				'multipart': 'multipart/form-data',
				'multipart form': 'application/x-www-form-urlencoded',
				'multipart mixed': 'multipart/mixed',
				'multipart alternative': 'multipart/alternative',
				'xls': 'application/vnd.ms-excel',
				'xlsx': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
				'abw': 'application/x-abiword',
				'azw': 'application/vnd.amazon.ebook',
				'sh': 'application/x-sh',
				'csh': 'application/x-csh',
				'doc': 'application/msword',
				'docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
				'ppt': 'application/vnd.ms-powerpoint',
				'pptx': 'application/vnd.openxmlformats-officedocument.presentationml.presentation',
				'rtf': 'application/rtf',
				'epub': 'application/epub+zip',
				'ics': 'text/calendar',
				'mpkg': 'application/vnd.apple.installer+xml',
				'odp': 'application/vnd.oasis.opendocument.presentation',
				'ods': 'application/vnd.oasis.opendocument.spreadsheet',
				'odt': 'application/vnd.oasis.opendocument.text',
				'ogx': 'application/ogg',
				'php': 'application/x-httpd-php',
				'py': 'applycation/x-python-code',
				'jar': 'application/java-archive',
				'java': 'application/java',
				'swift': 'application/swift'
			},
			'port': 80,
			'server': '0.0.0.0',
			'compress': {
				'enable': False,
				'min': 1_000,
				'type': [
					'text/html',
					'application/xml',
					'text/plain',
					'text/void',
					'text/css',
					'text/javascript',
					'text/csv'
				]
			},
			'secured': {
				'port': 443,
				'certificate': '',
				'key': ''
			}
		},
		'socket': {},
		'mail': {},
		'cloud': {},
		'balancer': {},
		'cli': {},
		'game': {},
		'app': {},
		'ui': {},
		'run': [],
		'const': {
			'pi': 3.14159265358979323846264338327950288419716939937510,
			'e': 2.71828182845904523536028747135266249775724709369995,
			'2pi': 6.283185307179586476925286766559,
			'pi/2': 1.5707963267948966192313216916398,
			'pi/3': 1.0471975511965977461542144610932,
			'2pi/3': 2.0943951023931954923084289221863,
			'f': 1.61803398874989484820458683436563811772030917980576,
			'g': 9.80665,
			'stars': 200_000_000_000_000_000_000_000,
			'hash': {
				'up': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
				'low': 'abcdefghijklmnopqrstuvwxyz',
				'number': '0123456789',
				'symbol': '!@#$%^&*()[]<>.,:;-+=_~',
				'friendly': 'ABCDEFGHJKLNPRSTVWXZ'
			},
			'number': {
				'byte': {
					'multiply': 1024,
					'short': ['B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB', 'RB', 'QB'],
					'long': ['byte', 'kilobyte', 'megabyte', 'gigabyte', 'terabyte', 'petabyte', 'exabyte', 'zettabyte', 'yottabyte', 'ronnabyte', 'quettabyte']
				},
				'thousands': {
					'multiply': 1_000,
					'short': ['K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y', 'R', 'Q'],
					'long': ['kilo', 'mega', 'giga', 'tera', 'peta', 'exa', 'zetta', 'yotta', 'ronna', 'quetta']
				},
				'fractional': {
					'multiply': 0.001,
					'short': ['m', 'µ', 'n', 'p', 'f', 'a', 'z', 'y', 'r', 'q'],
					'long': ['milli', 'micro', 'nano', 'pico', 'femto', 'atto', 'zepto', 'yocto', 'ronto', 'quecto']
				}
			}
		},
		'text': {
			"void": {
				"volume": ["🔇", "🔈", "🔉", "🔊"],
			}
		},
		'action': {
			'run': [
				['action.open', 'run.json'],
				[' ?', ['file.exists', 'run.json'], [
					['json.read', 'run.json'],
					'action'
				]]
			],
			'export': [],
			'test': [],
			'format': {
				'ini': {
					'encode': [],
					'decode': []
				},
				'xml': {
					'encode': [],
					'decode': []
				},
				'html': {
					'encode': [],
					'decode': []
				},
				'css': {
					'encode': [],
					'decode': []
				},
				'jpg': {
					'read': [],
					'write': [],
					'encode': [],
					'decode': []
				},
				'png': {
					'read': [],
					'write': [],
					'encode': [],
					'decode': []
				},
				'sitemap': {
					'encode': [],
					'decode': []
				},
				'robots': {
					'encode': [],
					'decode': []
				}
			},
			'file': {
				'backup': []
			},
			'convert': [],
			'game': [],
			'menu': [],
			'vn': {},
			'social': {

			},
			'tech': {

			}
		}
	}

	# run

	def run():
		try:
			a/0
			void.t('run.start')
			void.importer()
			file = void.module['os'].path.realpath(__file__)
			void.set({
				'env': {
					'version': {
						'full': void.module['sys'].version,
						'short': void.module['sys'].version.split(' ')[0]
					},
					'script': {
						'file': void.path_file(file),
						'path': void.path_dir(file),
						'arg': void.module['sys'].argv
					},
					'os': {
						'type': void.module['platform'].system().lower(),
						'version': void.module['platform'].release(),
						'name': void.module['platform'].system() + ' ' + void.module['platform'].release()
					},
					'newline': void.module['os'].linesep,
					'separator': void.module['os'].path.sep,
					'language': {
						'full': '',
						'short': ''
					},
					'timezone': ''
				}
			})
			if void.version(void.get('env.version.short')) < void.version(void.get('env.required.version')):
				void.xx(f'required Python {void.get('env.required.version')}')
			void.action('run')
			void.t('run.end')
			void.t('run.total', 'run.start', 'run.end')
			if (void.get('debug.time')):
				void.print(void.get('stat.time'))
		except Exception:
			trace = traceback.format_exc()
			print(trace)

	# helper

	def importer(module = None, try_count: int = 0):
		if module == None:
			module = void.get('env.required.import')
		elif type(module) is not list:
			module = [module]
		reimport = []
		imported = False
		stat = void.get('stat.time.import.module')
		for name in module:
			if type(name) is not str or name in stat:
				continue
			part = name.split('.')
			index = part[-1]
			void.t()
			try:
				void.module[index] = importlib.import_module(name)
				imported = True
				void.t('import.module.' + index, '')
			except ModuleNotFoundError as error:
				void.shell(void.get('env.path.python') + ' -m pip install ' + name, None, True)
				reimport.append(name)
		if len(reimport) > 0:
			if try_count == 0:
				void.importer(reimport, try_count + 1)
			else:
				void.xx('can\'t import module', reimport)
		if imported:
			void.t('import.total', 'import.module', None, '')

	def update(module = None):
		if module == None:
			module = void.data['env']['required']['import']
		elif type(module) is not list:
			module = [module]
		builtin = list(void.module['sys'].builtin_module_names) + list(void.module['sys'].stdlib_module_names)
		for name in ['pip'] + module:
			if type(name) is list and len(name) > 0:
				name = name[0]
			if type(name) is not str:
				continue
			base = name.split('.')[0]
			if base not in builtin:
				void.print(f'update {name}:')
				void.shell(void.data['env']['path']['python'] + ' -m pip install --upgrade ' + name, None, True)

	def version(version: str):
		result = []
		for number in version.split('.'):
			result.append(number.zfill(10))
		return tuple(result)

	def merge(data_to: dict, data_from: dict):
		for index_from in data_from:
			value = data_from[index_from]
			if type(value) is dict and index_from in data_to and type(data_to[index_from]) is dict:
				void.merge(data_to[index_from], value)
			else:
				data_to[index_from] = value

	# value

	def get(name, default = None, data: dict = None):
		if type(name) is str:
			if name == '':
				return void.result[0]
			name = name.split('.')[::-1]
		elif type(name) is not list:
			return default
		subname = name.pop()
		if type(data) is not dict:
			data = void.data
		if subname in data:
			if len(name) != 0:
				if type(data[subname]) is not dict:
					return default
				return void.get(name, default, data[subname])
			else:
				return data[subname]
		else:
			return default

	def set(name, data = True):
		if type(name) is str:
			name = name.split('.')[::-1]
		elif type(name) is dict:
			void.merge(void.data, name)
			return
		elif type(name) is not list:
			return
		subdata = void.data
		subname = name.pop()
		while len(name) > 0:
			if subname not in subdata or type(subdata[subname]) is not dict:
				subdata[subname] = {}
			subdata = subdata[subname]
			subname = name.pop()
		subdata[subname] = data

	def remove(name):
		if type(name) is str:
			name = name.split('.')
		elif type(name) is not list:
			return
		name = name[::-1]
		subdata = void.data
		subname = name.pop()
		while len(name) > 0:
			if subname not in subdata or type(subdata[subname]) is not dict:
				return
			subdata = subdata[subname]
			subname = name.pop()
		if subname in subdata:
			del subdata[subname]

	def get_data(data, index, default = None):
		if type(data) is list:
			result = data[index] if len(data) > index else default
		else:
			result = data[index] if index in data else default
		if type(result) is str:
			if len(result) > 1 and result[0] == '{' and result[-1] == '}':
				result = void.get(result[1:-1])
		return result

	def get_int(data, index, default = 0):
		result = void.get_data(data, index)
		return int(result) if result != None else default

	def get_float(data, index, default = 0.0):
		result = void.get_data(data, index)
		return float(result) if result != None else default

	def get_bool(data, index, default = False):
		result = void.get_data(data, index)
		return bool(result) if result != None else default

	def get_str(data, index, default = ''):
		result = void.get_data(data, index)
		return str(result) if result != None else default

	def get_list(data, index, default = []):
		result = void.get_data(data, index)
		return list(result) if result != None else default

	def get_dict(data, index, default = {}):
		result = void.get_data(data, index)
		return dict(result) if result != None else default

	def type(value):
		if value == None:
			return 'null'
		value_type = type(value)
		if value_type is str:
			return 'text'
		if value_type in [int, float]:
			return 'number'
		if value_type is list:
			return 'list'
		if value_type is dict:
			return 'dict'
		if value_type is bool:
			return 'bool'
		return 'byte'

	def bool(value):
		pass

	def number():
		pass

	def int(value):
		pass

	def float(value):
		pass

	def text(value):
		pass

	def list(value):
		pass

	# expression

	def expression(value):
		pass
	
	# control

	def action(actions):
		if type(actions) is not list:
			actions = [actions]
		result = void.result
		actions = actions[::-1]
		while len(actions) > 0:
			action = actions.pop()
			if type(action) is list:
				name = action[0] if len(action) > 0 else ''
			else:
				name = str(action)
				action = [name]
			match name:
				
				# value

				case 'get':
					result[0] = void.get(void.get_data(action, 1))
				case 'set':
					void.set(void.get_data(action, 1), void.get_data(action, 2))
				case 'remove':
					void.remove(void.get_data(action, 1))
				case 'type':
					result[0] = void.type(void.get_data(action, 1))
				case 'bool':
					void.bool()
				case 'number':
					void.number()
				case 'int':
					void.int()
				case 'float':
					void.float()
				case 'text':
					void.text()
				case 'list':
					void.list()
				case 'alias':
					void.alias()
				
				# expression
				
				case '+':
					result = result and get_data(action, 1)
				case '-':
					result = result and get_data(action, 1)
				case '*':
					result = result and get_data(action, 1)
				case '/':
					result = result and get_data(action, 1)
				case '//':
					result = result and get_data(action, 1)
				case '%':
					result = result and get_data(action, 1)
				case '**':
					result = result and get_data(action, 1)
				case '!':
					result = result and get_data(action, 1)
				case '&':
					result = result and get_data(action, 1)
				case '|':
					result = result and get_data(action, 1)
				case '^':
					result = result and get_data(action, 1)
				case '>>':
					result = result and get_data(action, 1)
				case '<<':
					result = result and get_data(action, 1)
				case '+=':
					result = result and get_data(action, 1)
				case '-=':
					result = result and get_data(action, 1)
				case '*=':
					result = result and get_data(action, 1)
				case '/=':
					result = result and get_data(action, 1)
				case '//=':
					result = result and get_data(action, 1)
				case '%=':
					result = result and get_data(action, 1)
				case '**=':
					result = result and get_data(action, 1)
				case '!=':
					result = result and get_data(action, 1)
				case '&=':
					result = result and get_data(action, 1)
				case '|=':
					result = result and get_data(action, 1)
				case '^=':
					result = result and get_data(action, 1)
				case '>>=':
					result = result and get_data(action, 1)
				case '<<=':
					result = result and get_data(action, 1)
				case 'and':
					result = result and get_data(action, 1)
				case 'or':
					result = result and get_data(action, 1)
				case 'xor':
					result = result and get_data(action, 1)
				case 'not':
					result = result and get_data(action, 1)
				case 'in':
					result = result and get_data(action, 1)
				case 'not in':
					result = result and get_data(action, 1)
				case 'is':
					result = result and get_data(action, 1)
				case 'not is':
					result = result and get_data(action, 1)
				
				# control

				case '?':
					void._if()
				case '??':
					void._match()
				case 'o':
					void.loop()
				case 'x':
					void.x()
				case '>>>':
					void._continue()
				case '<<<':
					void._repeat()
				case '_':
					void._()
				case '.':
					void.print(void.get_data(action, 1), void.get_str(action, 2, None))
				case '..':
					void.print(void.get_data(action, 1), '')
				case 'action':
					actions.extend(void.action_run(void.get_data(action, 1)))
				case 'action.open':
					actions.extend(void.action_open(void.get_str(action, 1)))
				case 'X':
					void.X(void.get_data(action, 1, 0))
				case 'xx':
					void.xx(void.get_data(action, 1, 1), void.get_str(action, 2))
				case 'open':
					void.open()
				case 'shell':
					void.shell()
				case 'shell.open':
					void.shell_open()
				case 'code':
					void.code(void.get_str(action, 1))
				case 'code.python':
					void.code_python(void.get_str(action, 1))
				case 'i':
					void.log_info()
				case 'w':
					void.log_warning()
				case 'e':
					void.log_error()
				case 'd':
					void.log_debug()
				case 't':
					void.t()
				case 'update':
					void.update()

				# text

				case 'lower':
					void.lower()
				case 'upper':
					void.upper()
				case 'starts':
					void.starts()
				case 'ends':
					void.ends()
				case 'strip':
					void.strip()
				case 'strip.begin':
					void.strip_begin()
				case 'strip.end':
					void.strip_end()
				case 'replace':
					void.replace()
				case 'find':
					void.find()
				case 'similar':
					void.similar()
				case 'part':
					void.part()
				case 'split':
					void.split()
				case 'join':
					void.join()
				case 'regex':
					void.regex()
				case 'regex.replace':
					void.regex_replace()
				case 'escape':
					void.escape()
				case 'escape.html':
					void.escape_html()
				case 'escape.sql':
					void.escape_sql()
				case 'escape.url':
					void.escape_url()
				case 'escape.json':
					void.escape_json()
				case 'escape.void':
					void.escape_void()
				case 'unescape':
					void.unescape()
				case 'unescape.html':
					void.unescape_html()
				case 'unescape.sql':
					void.unescape_sql()
				case 'unescape.url':
					void.unescape_url()
				case 'unescape.json':
					void.unescape_json()
				case 'unescape.void':
					void.unescape_void()
				case 'num':
					void.num()
				case 'pad':
					void.pad()
				case 'date':
					void.date()
				case 'letters':
					void.letters()
				case 'words':
					void.words()
				case 'sentences':
					void.sentences()
				case 'lines':
					void.lines()

				# list

				case 'push':
					void.push()
				case 'pop':
					void.pop()
				case 'reverse':
					void.reverse()
				case 'shuffle':
					void.shuffle()
				case 'map':
					void.map()
				case 'reduce':
					void.reduce()
				case 'names':
					void.names()
				case 'values':
					void.values()
				case 'clear':
					void.clear()

				# math

				case 'sin':
					void.sin()
				case 'cos':
					void.cos()
				case 'tan':
					void.tan()
				case 'sinh':
					void.sinh()
				case 'cosh':
					void.cosh()
				case 'tanh':
					void.tanh()
				case 'asin':
					void.asin()
				case 'acos':
					void.acos()
				case 'atan':
					void.atan()
				case 'asinh':
					void.asinh()
				case 'acosh':
					void.acosh()
				case 'atanh':
					void.atanh()
				case 'round':
					void.round()
				case 'floor':
					void.floor()
				case 'ceil':
					void.ceil()
				case 'log':
					void.log()
				case 'pow':
					void.pow()
				case 'fac':
					void.factorial()
				case 'fib':
					void.fibonacci()
				case 'abs':
					void.abs()
				case 'min':
					void.min()
				case 'max':
					void.max()
				case 'avg':
					void.avg()
				case 'sum':
					void.sum()
				case 'hex':
					void.hex()
				case 'bin':
					void.bin()
				case 'dec':
					void.dec()
				case 'rad':
					void.rad()
				case 'deg':
					void.deg()
				case 'random':
					void.random()
				case 'random.reseed':
					void.random_reseed()
				case 'random.seed':
					void.random_seed()

				# time

				case 'time':
					void.time()
				case 'time.ms':
					void.time_ms()
				case 'time.s':
					void.time_s()
				case 'timer':
					void.timer()
				case 'timer.remove':
					void.timer_remove()
				case 'timepast':
					void.timepast()
				case 'wait':
					void.wait()

				# crypto

				case 'encrypt':
					result[0] = void.encrypt(void.get_data(action, 1), void.get_str(action, 2, None), void.get_str(action, 3), void.get_str(action, 4, 'utf-8'))
				case 'decrypt':
					result[0] = void.decrypt(void.get_data(action, 1), void.get_str(action, 2), void.get_str(action, 3, 'utf-8'))
				case 'hash':
					void.hash()
				case 'uuid':
					void.uuid()
				case 'md5':
					void.md5()
				case 'sha1':
					void.sha1()
				case 'sha256':
					void.sha256()
				case 'sha512':
					void.sha512()
				case 'crc32':
					void.crc32()
				case 'base64':
					void.base64()
				case 'base64.decode':
					void.base64_decode()
				case 'gzip':
					result = void.gzip(void.get_data(action, 1, 0))
				case 'gzip.decode':
					result = void.gzip_decode(void.get_data(action, 1, 0))
				case 'rsa':
					void.rsa()
				case 'rsa.decode':
					void.rsa_decode()
				case 'rsa.key.public':
					void.rsa_key_public()
				case 'rsa.key.private':
					void.rsa_key_private()
				case 'ssl':
					void.ssl()
				case 'ssl.decode':
					void.ssl_decode()
				case 'ssl.check':
					void.ssl_check()
				case 'bcrypt':
					void.bcrypt()
				case 'bcrypt.check':
					void.bcrypt_check()

				# format

				case 'void':
					void.void()
				case 'void.decode':
					void.void_decode()
				case 'void.read':
					void.void_read()
				case 'void.write':
					void.void_write()
				case 'json':
					void.json()
				case 'json.decode':
					void.json_decode()
				case 'json.read':
					result = void.file_read(void.get_str(action, 1), 'json')
				case 'json.write':
					void.file_write(void.get_str(action, 1), void.get_data(action, 2), 'json')
				case 'yaml':
					void.yaml()
				case 'yaml.decode':
					void.yaml_decode()
				case 'csv':
					void.csv()
				case 'csv.decode':
					void.csv_decode()

				# file

				case 'file.exists':
					void.file_exists()
				case 'file.write':
					void.file_write()
				case 'file.read':
					void.file_read()
				case 'file.remove':
					void.file_remove()
				case 'file.move':
					void.file_move()
				case 'file.copy':
					void.file_copy()
				case 'file.rename':
					void.file_rename()
				case 'file.info':
					void.file_info()
				case 'file.size':
					void.file_size()
				case 'file.permissions':
					void.file_permissions()
				case 'file.readonly':
					void.file_readonly()
				case 'file.hidden':
					void.file_hidden()
				case 'file.modified':
					void.file_modified()
				case 'file.sha256':
					void.file_sha256()
				case 'file.crc32':
					void.file_crc32()
				case 'file.base64':
					void.file_base64()
				case 'file.zip':
					void.file_zip()
				case 'file.zip.list':
					void.file_zip_list()
				case 'file.zip.exists':
					void.file_zip_exists()
				case 'file.zip.read':
					void.file_zip_read()
				case 'file.zip.remove':
					void.file_zip_remove()
				case 'file.unzip':
					void.file_unzip()
				case 'file.gzip':
					void.file_gzip()
				case 'file.ungzip':
					void.file_ungzip()
				case 'file.link':
					void.file_link()
				case 'file.link.exists':
					void.file_link_exists()
				case 'file.backup':
					void.file_backup()
				case 'dir.exists':
					void.dir_exists()
				case 'dir.create':
					void.dir_create()
				case 'dir.copy':
					void.dir_copy()
				case 'dir.move':
					void.dir_move()
				case 'dir.rename':
					void.dir_rename()
				case 'dir.remove':
					void.dir_remove()
				case 'dir.list':
					void.dir_list()
				case 'dir.clear':
					void.dir_clear()
				case 'dir.info':
					void.dir_info()
				case 'dir.size':
					void.dir_size()
				case 'dir.permissions':
					void.dir_permissions()
				case 'dir.readonly':
					void.dir_readonly()
				case 'dir.hidden':
					void.dir_hidden()
				case 'dir.modified':
					void.dir_modified()
				case 'dir.zip':
					void.dir_zip()
				case 'drive.list':
					void.drive_list()
				case 'drive.name':
					void.drive_name()
				case 'drive.size':
					void.drive_size()
				case 'drive.used':
					void.drive_used()
				case 'drive.free':
					void.drive_free()
				case 'drive.mount':
					void.drive_mount()
				case 'drive.unmount':
					void.drive_unmount()
				case 'path.drive':
					void.path_drive()
				case 'path.dir':
					void.path_dir()
				case 'path.file':
					void.path_file()
				case 'path.name':
					void.path_name()
				case 'path.extension':
					void.path_extension()
				case 'path.extension.strip':
					void.path_extension_strip()

				# cloud

				case 'cloud.file':
					void.cloud_file()
				case 'cloud.web':
					void.cloud_web()
				case 'cloud.api':
					void.cloud_api()
				case 'cloud.socket':
					void.cloud_socket()
				case 'cloud.websocket':
					void.cloud_websocket()
				case 'cloud.mail':
					void.cloud_mail()
				case 'cloud.game':
					void.cloud_game()
				case 'cloud.social':
					void.cloud_social()
				case 'cloud.coin':
					void.cloud_coin()

				# bot

				case 'bot.telegram':
					void.bot_telegram()
				case 'bot.wechat':
					void.bot_wechat()
				case 'bot.x':
					void.bot_x()
				case 'bot.youtube':
					void.bot_youtube()
				case 'bot.tiktok':
					void.bot_tiktok()
				case 'bot.steam':
					void.bot_steam()

				# request

				case 'request':
					void.request()
				case 'request.post':
					void.request_post()
				case 'request.put':
					void.request_put()
				case 'request.delete':
					void.request_delete()
				case 'request.head':
					void.request_head()

				# cookie

				case 'cookie':
					void.cookie()
				case 'cookie.remove':
					void.cookie_remove()

				# sql

				case 'sql':
					void.sql()
				case 'sql.connect':
					void.sql_connect()
				case 'sql.disconnet':
					void.sql_disconnet()
				case 'sql.user':
					void.sql_user()
				case 'sql.user.list':
					void.sql_user_list()
				case 'sql.user.remove':
					void.sql_user_remove()
				case 'sql.db':
					void.sql_db()
				case 'sql.db.list':
					void.sql_db_list()
				case 'sql.db.remove':
					void.sql_db_remove()
				case 'sql.db.size':
					void.sql_db_size()
				case 'sql.table':
					void.sql_table()
				case 'sql.table.list':
					void.sql_table_list()
				case 'sql.table.remove':
					void.sql_table_remove()
				case 'sql.field':
					void.sql_field()
				case 'sql.field.list':
					void.sql_field_list()
				case 'sql.field.remove':
					void.sql_field_remove()
				case 'sql.index':
					void.sql_index()
				case 'sql.index.list':
					void.sql_index_list()
				case 'sql.index.remove':
					void.sql_index_remove()
				case 'sql.function':
					void.sql_function()
				case 'sql.function.list':
					void.sql_function_list()
				case 'sql.function.remove':
					void.sql_function_remove()
				case 'sql.view':
					void.sql_view()
				case 'sql.view.list':
					void.sql_view_list()
				case 'sql.view.remove':
					void.sql_view_remove()
				case 'sql.get':
					void.sql_get()
				case 'sql.all':
					void.sql_all()
				case 'sql.cursor':
					void.sql_cursor()
				case 'sql.transaction':
					void.sql_transaction()
				case 'sql.commit':
					void.sql_commit()
				case 'sql.rollback':
					void.sql_rollback()

				# os

				case 'os.name':
					void.os_name()
				case 'os.version':
					void.os_version()
				case 'os.username':
					void.os_username()
				case 'os.desktop':
					void.os_desktop()
				case 'os.mobile':
					void.os_mobile()
				case 'os.web':
					void.os_web()
				case 'os.windows':
					void.os_windows()
				case 'os.macos':
					void.os_macos()
				case 'os.ios':
					void.os_ios()
				case 'os.ipados':
					void.os_ipados()
				case 'os.watchos':
					void.os_watchos()
				case 'os.tvos':
					void.os_tvos()
				case 'os.android':
					void.os_android()
				case 'os.linux':
					void.os_linux()

				# device

				case 'cpu.name':
					void.cpu_name()
				case 'cpu.cores':
					void.cpu_cores()
				case 'memory.size':
					void.memory_size()
				case 'memory.free':
					void.memory_free()
				case 'memory.used':
					void.memory_used()
				case 'memory.available':
					void.memory_available()

				# gps

				case 'gps':
					void.gps()
				
				# sensor

				case 'speed':
					void.speed()
				case 'tilt':
					void.tilt()
				case 'compass':
					void.compass()
				case 'motion':
					void.motion()

				# photo

				case 'camera':
					void.camera()
				case 'gallery':
					void.gallery()

				# contacts

				case 'contacts':
					void.contacts()

				# calendar

				case 'calendar':
					void.calendar()

				# flashlight

				case 'flashlight':
					void.flashlight()

				# health

				case 'health':
					void.health()
				# microphone

				case 'mic':
					void.mic()

				# notification

				case 'notification':
					void.notification()
				case 'notification.token':
					void.notification_token()
				case 'notification.send':
					void.notification_send()

				# key

				case 'key':
					void.key()
				case 'key.remove':
					void.key_remove()
				case 'key.press':
					void.key_press()
				case 'key.enable':
					void.key_enable()
				case 'key.disable':
					void.key_disable()

				# keyboard

				case 'keyboard':
					void.keyboard()
				case 'keyboard.height':
					void.keyboard_height()

				# mouse

				case 'mouse':
					void.mouse()
				case 'mouse.lock':
					void.mouse_lock()
				case 'mouse.position':
					void.mouse_position()
				case 'mouse.capture':
					void.mouse_capture()
				case 'mouse.confine':
					void.mouse_confine()
				case 'mouse.shape':
					void.mouse_shape()

				# gamepad

				case 'gamepad.axis':
					void.gamepad_axis()
				case 'gamepad.vibrate':
					void.gamepad_vibrate()

				# clipboard

				case 'clipboard':
					void.clipboard()
				case 'clipboard.clear':
					void.clipboard_clear()

				# say

				case 'say':
					void.say()
				case 'say.list':
					void.say_list()
				case 'say.stop':
					void.say_stop()
				case 'say.pause':
					void.say_pause()

				# convert

				case 'convert':
					void.convert()

				# image

				case 'image':
					void.image()
				case 'image.read':
					void.image_read()
				case 'image.write':
					void.image_write()
				case 'image.size':
					void.image_size()
				case 'image.crop':
					void.image_crop()
				case 'image.square':
					void.image_square()
				case 'image.rotate':
					void.image_rotate()
				case 'image.flip.h':
					void.image_flip_h()
				case 'image.flip.v':
					void.image_flip_v()
				case 'image.tint':
					void.image_tint()
				case 'image.gray':
					void.image_gray()
				case 'image.text':
					void.image_text()
				case 'image.image':
					void.image_image()
				case 'image.draw':
					void.image_draw()
				
				# video

				case 'video':
					void.video()
				case 'video.read':
					void.video_read()
				case 'video.write':
					void.video_write()
				case 'video.size':
					void.video_size()
				case 'video.rotate':
					void.video_rotate()
				case 'video.flip.h':
					void.video_flip_h()
				case 'video.flip.v':
					void.video_flip_v()
				case 'video.clip':
					void.video_clip()
				case 'video.speed':
					void.video_speed()
				case 'video.reverse':
					void.video_reverse()
				case 'video.text':
					void.video_text()
				case 'video.image':
					void.video_image()
				case 'video.sound':
					void.video_sound()
				case 'video.video':
					void.video_video()

				# model

				case 'model':
					void.model()
				case 'model.read':
					void.model_read()
				case 'model.write':
					void.model_write()
				case 'model.animate':
					void.model_animate()
				case 'model.texture':
					void.model_texture()

				# sound

				case 'sound':
					void.sound()
				case 'sound.read':
					void.sound_read()
				case 'sound.write':
					void.sound_write()
				case 'sound.list':
					void.sound_list()
				case 'sound.remove':
					void.sound_remove()
				case 'sound.volume':
					void.sound_volume()
				case 'sound.speed':
					void.sound_speed()
				case 'sound.clip':
					void.sound_clip()
				case 'sound.sound':
					void.sound_sound()

				# music

				case 'music':
					void.music()
				case 'music.stop':
					void.music_stop()
				case 'music.pause':
					void.music_pause()
				case 'music.volume':
					void.music_volume()

				# volume

				case 'volume':
					void.volume()

				# screen

				case 'screen.count':
					void.screen_count()
				case 'screen.list':
					void.screen_list()
				case 'screen.info':
					void.screen_info()
				case 'size':
					void.size()
				case 'orientation':
					void.orientation()
				case 'landscape':
					void.landscape()
				case 'portrait':
					void.portrait()
				case 'rate':
					void.rate()
				case 'pixel':
					void.pixel()
				case 'symbol':
					void.symbol(void.get_int(action, 1), void.get_int(action, 2), void.get_str(action, 3), void.get_str(action, 4))
				case 'dpi':
					void.dpi()
				case 'dark':
					void.dark()
				case 'touchscreen':
					void.touchscreen()

				# ui

				case 'ui':
					void.ui()
				case 'bg':
					void.bg()
				case 'show':
					void.show()
				case 'hide':
					void.hide()
				case 'visible':
					void.visible()
				case 'enable':
					void.enable()
				case 'disable':
					void.disable()
				case 'enabled':
					void.enabled()
				case 'focus':
					void.focus()
				case 'scale':
					void.scale()
				case 'ui.text':
					void.ui_text()
				case 'ui.image':
					void.ui_image()
				case 'ui.button':
					void.ui_button()
				case 'ui.divider':
					void.ui_divider()
				case 'ui.video':
					void.ui_video()
				case 'ui.select':
					void.ui_select()
				case 'ui.switch':
					void.ui_switch()
				case 'ui.progress':
					void.ui_progress()
				case 'ui.slider':
					void.ui_slider()
				case 'ui.edit':
					void.ui_edit()
				case 'ui.split.h':
					void.ui_split_h()
				case 'ui.split.v':
					void.ui_split_v()
				case 'ui.list':
					void.ui_list()
				case 'ui.tile':
					void.ui_tile()
				case 'ui.color':
					void.ui_color()
				case 'ui.date':
					void.ui_date()
				case 'ui.drop':
					void.ui_drop()
				case 'ui.menu':
					void.ui_menu()
				case 'ui.menu.context':
					void.ui_menu_context()
				case 'ui.window':
					void.ui_window()
				case 'ui_debug':
					void.ui_debug()
				case 'ui_fps':
					void.ui_fps()

				# window

				case 'window.list':
					void.window_list()
				case 'window.info':
					void.window_info()
				case 'title':
					void.title()
				case 'icon':
					void.icon()
				case 'size':
					void.size()
				case 'size.max':
					void.size_max()
				case 'size.min':
					void.size_min()
				case 'position':
					void.position()
				case 'direction':
					void.direction()
				case 'attention':
					void.attention()
				case 'top':
					void.top()
				case 'foreground':
					void.foreground()
				case 'unfocusable':
					void.unfocusable()
				case 'unresizable':
					void.unresizable()
				case 'center':
					void.center()
				case 'fullscreen':
					void.fullscreen()
				case 'drop':
					void.drop()
				case 'border':
					void.border()
				case 'maximized':
					void.maximized()
				case 'minimized':
					void.minimized()
				case 'exclusive':
					void.exclusive()
				case 'vsync':
					void.vsync()
				case 'fps':
					void.fps()

				# dialog

				case 'dialog.file':
					void.dialog_file()
				case 'dialog.color':
					void.dialog_color()
				case 'dialog.date':
					void.dialog_date()
				case 'dialog.select':
					void.dialog_select()

				# effect

				case 'effect':
					void.effect()
				case 'effect.list':
					void.effect_list()
				case 'effect.clear':
					void.effect_clear()
				case 'effect.remove':
					void.effect_remove()

				# game

				case 'game':
					void.game()
				case 'menu':
					void.menu()

				# vn

				case 'vn':
					void.vn()
				case 'vn.clear':
					void.vn_clear()
				case 'vn.say':
					void.vn_say()
				case 'vn.skip':
					void.vn_skip()
				case 'vn.route':
					void.vn_route()
				case 'vn.route.remove':
					void.vn_route_remove()
				case 'vn.route.check':
					void.vn_route_check()
				case 'vn.route.select':
					void.vn_route_select()
				case 'vn.route.repeat':
					void.vn_route_repeat()
				case 'vn.route.skip':
					void.vn_route_skip()
				case 'vn.character':
					void.vn_character()
				case 'vn.come':
					void.vn_come()
				case 'vn.leave':
					void.vn_leave()
				case 'vn.change':
					void.vn_change()
				case 'vn.env':
					void.vn_env()
				case 'vn.env.change':
					void.vn_env_change()

				# 2d

				case '2d':
					void._2d()
				case '2d.bg':
					void._2d_bg()
				case '2d.map':
					void._2d_map()
				case '2d.character':
					void._2d_character()
				case '2d.object':
					void._2d_object()
				case '2d.npc':
					void._2d_npc()
				case '2d.enemy':
					void._2d_enemy()
				case '2d.shoot':
					void._2d_shoot()
				case '2d.jump':
					void._2d_jump()
				case '2d.drop':
					void._2d_drop()
				case '2d.look':
					void._2d_look()
				case '2d.inventory':
					void._2d_inventory()
				case '2d.hud':
					void._2d_hud()
				case '2d.sound':
					void._2d_sound()
				case '2d.light':
					void._2d_light()
				case '2d.camera':
					void._2d_camera()

				# 3d

				case '3d':
					void._3d()
				case '3d.bg':
					void._3d_bg()
				case '3d.map':
					void._3d_map()
				case '3d.character':
					void._3d_character()
				case '3d.object':
					void._3d_object()
				case '3d.npc':
					void._3d_npc()
				case '3d.enemy':
					void._3d_enemy()
				case '3d.shoot':
					void._3d_shoot()
				case '3d.jump':
					void._3d_jump()
				case '3d.drop':
					void._3d_drop()
				case '3d.look':
					void._3d_look()
				case '3d.hud':
					void._3d_hud()
				case '3d.inventory':
					void._3d_inventory()
				case '3d.sound':
					void._3d_sound()
				case '3d.light':
					void._3d_light()
				case '3d.camera':
					void._3d_camera()

				# ai

				case 'ai.text':
					void.ai_text()
				case 'ai.image':
					void.ai_image()
				case 'ai.video':
					void.ai_video()
				case 'ai.music':
					void.ai_music()
				case 'ai.sound':
					void.ai_sound()
				case 'ai.say':
					void.ai_say()
				case 'ai.2d':
					void.ai_2d()
				case 'ai.3d':
					void.ai_3d()
				case 'ai.character':
					void.ai_character()
				case 'ai.clean':
					void.ai_clean()
				case 'ai.resize':
					void.ai_resize()
				case 'ai.color':
					void.ai_color()
				case 'ai.style':
					void.ai_style()
				case 'ai.translate':
					void.ai_translate()
				case 'ai.recognize.text':
					void.ai_recognize_text()
				case 'ai.recognize.image':
					void.ai_recognize_image()
				case 'ai.recognize.video':
					void.ai_recognize_video()
				case 'ai.recognize.motion':
					void.ai_recognize_motion()
				case 'ai.capture.voice':
					void.ai_capture_voice()
				case 'ai.capture.face':
					void.ai_capture_face()
				case 'ai.capture.motion':
					void.ai_capture_motion()

				# social

				case 'social.auth':
					void.social_auth()
				case 'social.auth.signin':
					void.social_auth_signin()
				case 'social.auth.signup':
					void.social_auth_signup()
				case 'social.auth.signout':
					void.social_auth_signout()
				case 'social.auth.restore':
					void.social_auth_restore()
				case 'social.auth.restore.code':
					void.social_auth_restore_code()
				case 'social':
					void.social()
				case 'social.send':
					void.social_send()
				case 'social.profile':
					void.social_profile()
				case 'social.buy':
					void.social_buy()

				case _:
					if name in void.data['action']:
						actions.extend(void.action_run(void.data['action'][name]))
		return result

	def action_open(path: str):
		if void.file_exists(path):
			result = void.file_read(path)
			if type(result) is not list:
				return [] 
			return (result if type(result) is list else list(result))[::-1]
		return []

	def action_run(action):
		return (action if type(action) is list else [action])[::-1]

	def _if():
		pass

	def _match():
		pass

	def loop():
		pass

	def _break():
		pass

	def _continue():
		pass

	def repeat():
		pass

	def _return():
		pass

	def print(data = '', end: str = None):
		if type(data) in [list, dict]:
			data = void.json(data)
		print(data, end=end if end != None else '\n')

	def X(code: int = 0):
		exit(code)

	def xx(*args):
		code = 1
		for index in range(0, len(args)):
			value = args[index]
			if index == 0 and type(value) is int:
				code = value
			elif value != None:
				if 'json' in void.module:
					void.print(value)
				else:
					print(value)
		exit(code)

	def open():
		pass

	def shell(command: str, input: str = None, verbose: bool = False, charset: str = 'utf-8'):
		void.importer('subprocess')
		if verbose:
			result = {
				'code': void.module['subprocess'].call(command, shell=True),
				'error': '',
				'text': ''
			}
		else:
			if input == None:
				input = ''
			pipe = void.module['subprocess'].PIPE
			result = void.module['subprocess'].run(command, shell=True, stdout=pipe, stderr=pipe, input=input.encode(charset))
			try:
				result = {
					"code": result.returncode,
					"error": result.stderr.decode(charset),
					"text": result.stdout.decode(charset)
				}
			except:
				result = {
					"code": result.returncode,
					"error": result.stderr,
					"text": result.stdout
				}				
		return result

	def shell_open():
		pass

	def code(code: str):
		exec(code)

	def code_python(code: str):
		exec(code)

	def log_info():
		pass

	def log_warning():
		pass

	def log_error():
		pass

	def log_debug():
		pass

	def t(name: str = '', start: str = None, end: str = None, remove: str = None):
		if end == None and start == None:
			result = time.time()
		else:
			if end != None:
				result = void.get('stat.time.' + end, 0) - void.get('stat.time.' + start, 0)
			else:
				value = void.get('stat.time.' + start, 0)
				if type(value) in [float, int]:
					current = time.time()
					result = current - value if current > value else 0
				elif type(value) is list:
					result = void.sum(value)
				elif type(value) is dict:
					result = 0
					for index in value:
						result += value[index]
		void.set('stat.time.' + name, round(result, 4))
		if remove != None:
			void.remove('stat.time.' + remove)

	def export():
		pass

	# text

	def lower():
		pass

	def upper():
		pass

	def starts():
		pass

	def ends():
		pass

	def strip():
		pass

	def strip_begin():
		pass

	def strip_end():
		pass

	def replace():
		pass

	def find():
		pass

	def similar(first: str, second: str):
		return SequenceMatcher(None, first, second).ratio()

	def part():
		pass

	def split():
		pass

	def join():
		pass

	def regex():
		pass

	def regex_replace():
		pass

	def escape():
		pass

	def escape_html():
		pass

	def escape_sql():
		pass

	def escape_url():
		pass

	def escape_json():
		pass

	def escape_void():
		pass

	def unescape():
		pass

	def unescape_html():
		pass

	def unescape_sql():
		pass

	def unescape_url():
		pass

	def unescape_json():
		pass

	def unescape_void():
		pass

	def num():
		pass

	def pad():
		pass

	def date():
		pass

	# list

	def push():
		pass

	def pop():
		pass

	def reverse():
		pass

	def shuffle():
		pass

	def map():
		pass

	def reduce():
		pass

	def names():
		pass

	def values():
		pass

	def clear():
		pass

	# math

	def sin():
		pass

	def cos():
		pass

	def tan():
		pass

	def sinh():
		pass

	def cosh():
		pass

	def tanh():
		pass

	def asin():
		pass

	def acos():
		pass

	def atan():
		pass

	def asinh():
		pass

	def acosh():
		pass

	def atanh():
		pass

	def round():
		pass

	def floor():
		pass

	def ceil():
		pass

	def log():
		pass

	def pow():
		pass

	def factorial():
		pass

	def fibonacci():
		pass

	def abs():
		pass

	def min():
		pass

	def max():
		pass

	def avg():
		pass

	def sum(value: list):
		result = 0
		for value in value:
			if type(value) in [int, float]:
				result += value
		return result

	def hex():
		pass

	def bin():
		pass

	def dec():
		pass

	def rad():
		pass

	def deg():
		pass

	def random():
		pass

	def random_reseed():
		pass

	def random_seed():
		pass

	# time

	def time():
		pass

	def time_ms():
		pass

	def time_s():
		pass

	def timer():
		pass

	def timer_remove():
		pass

	def timepast():
		pass

	def wait():
		pass

	# crypto

	def encrypt(data, key: str = None, secret: str = '', charset: str = 'utf-8'):
		void.importer('cryptography.fernet')
		if key == None: 
			key = void.module['fernet'].Fernet.generate_key() + secret.encode(charset)
			return {
				'key': key.decode(charset),
				'data': void.module['fernet'].Fernet(key).encrypt(data.encode(charset)).decode(charset)
			}
		else:
			return void.module['fernet'].Fernet(key.encode(charset)).encrypt(data.encode(charset)).decode(charset)

	def decrypt(data, key: str, charset: str = 'utf-8'):
		void.importer('cryptography.fernet')
		result = void.module['fernet'].Fernet(key.encode(charset)).decrypt(data.encode(charset)).decode(charset)
		return result

	def hash():
		pass

	def uuid():
		pass

	def md5():
		pass

	def sha1():
		pass

	def sha256():
		pass

	def sha512():
		pass

	def crc32():
		pass

	def base64(data, charset: str = 'utf-8'):
		if type(data) is str:
			data = data.encode(charset)
		return void.module['base64'].b64encode(data).decode(charset)

	def base64_decode(data, byte: bool = False, charset: str = 'utf-8'):
		if type(data) is str:
			data = data.encode(charset)
		return void.module['base64'].b64decode(data).decode(charset) if not byte else void.module['base64'].b64decode(data)

	def gzip(data, charset: str = 'utf-8'):
		if type(data) is str:
			data = data.encode(charset)
		return gz.compress(data)

	def gzip_decode(data, charset: str = 'utf-8'):
		return gz.decompress(data).decode(charset) if charset != None else gz.decompress(data)

	def rsa():
		pass

	def rsa_decode():
		pass

	def rsa_key_public():
		pass

	def rsa_key_private():
		pass

	def ssl():
		pass

	def ssl_decode():
		pass

	def ssl_check():
		pass

	def bcrypt():
		pass

	def bcrypt_check():
		pass

	# format

	def void():
		pass

	def void_decode():
		pass

	def void_read():
		pass

	def void_write():
		pass

	def json(data, indent='\t', separators:list=[', ',': ']):
		try:
			return void.module['json'].dumps(data, indent=indent, separators=tuple(separators),  ensure_ascii=False)
		except:
			pass

	def json_decode(data: str):
		try:
			return void.module['json'].loads(data)
		except:
			pass

	def json_read():
		pass

	def json_write():
		pass

	def yaml():
		pass

	def yaml_decode():
		pass

	def csv():
		pass

	def csv_decode():
		pass

	def ini():
		pass

	def ini_decode():
		pass

	def html():
		pass

	def html_decode():
		pass

	def xml():
		pass

	def xml_decode():
		pass

	def css():
		pass

	def css_decode():
		pass

	def robots():
		pass

	def sitemap():
		pass

	# file

	def file_exists(path: str):
		return void.module['os'].path.isfile(path)

	def file_write(path: str, data, format = 'auto', append: bool = False):
		if format == 'auto':
			format = void.path_extension(path).lower()
		match format:
			case 'gzip':
				return void.gzip_decode(void.file_read(path, 'binary'))
			case 'zip':
				return void.file_zip_read(path)
			case 'json':
				return void.json_decode(void.file_read(path, 'text'))
			case 'yaml':
				void.encode('yaml', path)
			case 'ini':
				void.encode('ini', path)
			case 'xml':
				void.encode('xml', path)
			case 'html' | 'htm':
				void.encode('html', path)
			case 'text' | 'txt':
				file = open(path, 'w' if not append else 'a', encoding='utf-8')
				data = file.write(data)
				file.close()
			case _:
				file = open(path, "wb" if not append else 'ab')
				data = file.write(data)
				file.close()

	def file_read(path: str, format = 'auto', seek: int = 0, count: int = 0):
		if format == 'auto':
			format = void.path_extension(path).lower()
		match format:
			case 'gzip':
				return void.gzip_decode(void.file_read(path, 'binary'))
			case 'zip':
				return void.file_zip_read(path)
			case 'json':
				data = void.file_read(path, 'text')
				return void.json_decode(data) if data != None else None
			case 'yaml':
				return void.decode('yaml', path)
			case 'ini':
				return void.decode('ini', path)
			case 'xml':
				return void.decode('xml', path)
			case 'html' | 'htm':
				return void.decode('html', path)
			case 'text' | 'txt':
				if not void.file_exists(path):
					return
				file = open(path, "r", encoding='utf-8')
				if seek != 0:
					file.seek(seek, 0 if seek > 0 else 2)
				data = file.read()
				file.close()
			case _:
				if not void.file_exists(path):
					return
				file = open(path, "rb")
				if seek != 0:
					file.seek(seek, 0 if seek > 0 else 2)
				data = file.read()
				file.close()
		return data

	def file_remove():
		pass

	def file_move():
		pass

	def file_copy():
		pass

	def file_rename():
		pass

	def file_info():
		pass

	def file_size():
		pass

	def file_permissions():
		pass

	def file_readonly():
		pass

	def file_hidden():
		pass

	def file_modified():
		pass

	def file_sha256():
		pass

	def file_crc32():
		pass

	def file_base64():
		pass

	def file_zip():
		pass

	def file_zip_list():
		pass

	def file_zip_exists():
		pass

	def file_zip_read():
		pass

	def file_zip_remove():
		pass

	def file_unzip():
		pass

	def file_gzip(path: str):
		with open(path, 'rb') as file_in:
			with void.module['gzip'].open(path + '.gz', 'wb') as file_out:
				void.module['shutil'].copyfileobj(file_in, file_out)

	def file_ungzip(path: str):
		with void.module['gzip'].open(path + '.gz', 'wb') as file_in:
			with open(path, 'wb') as file_out:
				void.module['shutil'].copyfileobj(file_in, file_out)

	def file_link():
		pass

	def file_link_exists():
		pass

	def dir_exists():
		pass

	def dir_create():
		pass

	def dir_copy():
		pass

	def dir_move():
		pass

	def dir_rename():
		pass

	def dir_remove():
		pass

	def dir_list():
		pass

	def dir_clear():
		pass

	def dir_info():
		pass

	def dir_size():
		pass

	def dir_permissions():
		pass

	def dir_readonly():
		pass

	def dir_hidden():
		pass

	def dir_modified():
		pass

	def dir_zip():
		pass

	def drive_list():
		pass

	def drive_name():
		pass

	def drive_size():
		pass

	def drive_used():
		pass

	def drive_free():
		pass

	def drive_mount():
		pass

	def drive_unmount():
		pass

	def path_drive(path: str):
		if os('windows'):
			part = path.split(':')
			if len(part) > 1:
				return part[0].lower()

	def path_dir(path: str):
		return void.module['os'].path.dirname(path)

	def path_file(path: str):
		return void.module['os'].path.basename(path)

	def path_name(path: str):
		pass

	def path_extension(path: str):
		index = path.rfind('.')
		return path[index + 1:] if index >= 0 and len(path) > (index + 1) else ''	

	def path_extension_strip(path: str):
		index = path.rfind('.')
		return path[0:index] if index >= 0 else path

	# cloud

	def cloud_file():
		pass

	def cloud_web():
		pass

	def cloud_api():
		pass

	def cloud_socket():
		pass

	def cloud_websocket():
		pass

	def cloud_mail():
		pass

	def cloud_game():
		pass

	def cloud_social():
		pass

	def cloud_coin():
		pass

	# bot

	def bot_telegram():
		pass

	def bot_wechat():
		pass

	def bot_x():
		pass

	def bot_youtube():
		pass

	def bot_tiktok():
		pass

	def bot_steam():
		pass

	# request

	def request():
		pass

	def request_post():
		pass

	def request_put():
		pass

	def request_delete():
		pass

	def request_head():
		pass

	# cookie

	def cookie():
		pass

	def cookie_remove():
		pass

	# sql

	def sql():
		pass

	def sql_connect():
		pass

	def sql_disconnet():
		pass

	def sql_user():
		pass

	def sql_user_list():
		pass

	def sql_user_remove():
		pass

	def sql_db():
		pass

	def sql_db_list():
		pass

	def sql_db_remove():
		pass

	def sql_db_size():
		pass

	def sql_table():
		pass

	def sql_table_list():
		pass

	def sql_table_remove():
		pass

	def sql_field():
		pass

	def sql_field_list():
		pass

	def sql_field_remove():
		pass

	def sql_index():
		pass

	def sql_index_list():
		pass

	def sql_index_remove():
		pass

	def sql_function():
		pass

	def sql_function_list():
		pass

	def sql_function_remove():
		pass

	def sql_view():
		pass

	def sql_view_list():
		pass

	def sql_view_remove():
		pass

	def sql_get():
		pass

	def sql_all():
		pass

	def sql_cursor():
		pass

	def sql_transaction():
		pass

	def sql_commit():
		pass

	def sql_rollback():
		pass

	# os

	def os(name: str = None):
		os = void.data['env']['os']['type']
		if name != None:
			return name == os
		return os

	def os_name():
		return void.data['env']['os']['name']

	def os_version():
		return void.data['env']['os']['version']

	def os_username():
		pass

	def os_desktop():
		pass

	def os_mobile():
		pass

	def os_web():
		pass

	def os_windows():
		pass

	def os_macos():
		pass

	def os_ios():
		pass

	def os_ipados():
		pass

	def os_watchos():
		pass

	def os_tvos():
		pass

	def os_android():
		pass

	def os_linux():
		pass

	# device

	def cpu_name():
		pass

	def cpu_cores():
		pass

	def memory_size():
		pass

	def memory_free():
		pass

	def memory_used():
		pass

	def memory_available():
		pass

	# gps

	def gps():
		pass

	# sensor

	def speed():
		pass

	def tilt():
		pass

	def compass():
		pass

	def motion():
		pass

	# photo

	def camera():
		pass

	def gallery():
		pass

	# contacts

	def contacts():
		pass

	# calendar

	def calendar():
		pass

	# flashlight

	def flashlight():
		pass

	# health

	def health():
		pass

	# microphone

	def mic():
		pass

	# notification

	def notification():
		pass

	def notification_token():
		pass

	def notification_send():
		pass

	# key

	def key():
		pass

	def key_remove():
		pass

	def key_press():
		pass

	def key_enable():
		pass

	def key_disable():
		pass

	# keyboard

	def keyboard():
		pass

	def keyboard_height():
		pass

	# mouse

	def mouse():
		pass

	def mouse_lock():
		pass

	def mouse_position():
		pass

	def mouse_capture():
		pass

	def mouse_confine():
		pass

	def mouse_shape():
		pass

	# gamepad

	def gamepad_axis():
		pass

	def gamepad_vibrate():
		pass

	# clipboard

	def clipboard():
		pass

	def clipboard_clear():
		pass

	# say

	def say():
		pass

	def say_list():
		pass

	def say_stop():
		pass

	def say_pause():
		pass

	# convert

	def convert():
		pass

	# image

	def image():
		pass

	def image_read():
		pass

	def image_write():
		pass

	def image_size():
		pass

	def image_crop():
		pass

	def image_square():
		pass

	def image_rotate():
		pass

	def image_flip_h():
		pass

	def image_flip_v():
		pass

	def image_tint():
		pass

	def image_gray():
		pass

	def image_text():
		pass

	def image_image():
		pass

	def image_draw():
		pass

	# video

	def video():
		pass

	def video_read():
		pass

	def video_write():
		pass

	def video_size():
		pass

	def video_rotate():
		pass

	def video_flip_h():
		pass

	def video_flip_v():
		pass

	def video_clip():
		pass

	def video_speed():
		pass

	def video_reverse():
		pass

	def video_text():
		pass

	def video_image():
		pass

	def video_sound():
		pass

	def video_video():
		pass

	# model

	def model():
		pass

	def model_read():
		pass

	def model_write():
		pass

	def model_animate():
		pass

	def model_texture():
		pass

	# sound

	def sound():
		pass

	def sound_read():
		pass

	def sound_write():
		pass

	def sound_list():
		pass

	def sound_remove():
		pass

	def sound_volume():
		pass

	def sound_speed():
		pass

	def sound_clip():
		pass

	def sound_sound():
		pass

	# music

	def music():
		pass

	def music_stop():
		pass

	def music_pause():
		pass

	def music_volume():
		pass

	# volume

	def volume():
		pass

	# screen

	def screen_count():
		pass

	def screen_list():
		pass

	def screen_info():
		pass

	def size():
		pass

	def orientation():
		pass

	def landscape():
		pass

	def portrait():
		pass

	def rate():
		pass

	def pixel():
		pass

	def symbol(x: int, y: int, text: str, color: str = None):
		print("\033[{0};{1}H{2}".format(x, y, text))

	def dpi():
		pass

	def dark():
		pass

	def touchscreen():
		pass

	# ui

	def ui():
		pass

	def bg():
		pass

	def show():
		pass

	def hide():
		pass

	def visible():
		pass

	def enable():
		pass

	def disable():
		pass

	def enabled():
		pass

	def focus():
		pass

	def scale():
		pass

	def ui_text():
		pass

	def ui_image():
		pass

	def ui_button():
		pass

	def ui_divider():
		pass

	def ui_video():
		pass

	def ui_select():
		pass

	def ui_switch():
		pass

	def ui_progress():
		pass

	def ui_slider():
		pass

	def ui_edit():
		pass

	def ui_split_h():
		pass

	def ui_split_v():
		pass

	def ui_list():
		pass

	def ui_tile():
		pass

	def ui_color():
		pass

	def ui_date():
		pass

	def ui_drop():
		pass

	def ui_menu():
		pass

	def ui_menu_context():
		pass

	def ui_window():
		pass

	# window

	def window_list():
		pass

	def window_info():
		pass

	def title():
		pass

	def icon():
		pass

	def size():
		pass

	def size_max():
		pass

	def size_min():
		pass

	def position():
		pass

	def direction():
		pass

	def attention():
		pass

	def top():
		pass

	def foreground():
		pass

	def unfocusable():
		pass

	def unresizable():
		pass

	def center():
		pass

	def fullscreen():
		pass

	def drop():
		pass

	def border():
		pass

	def maximized():
		pass

	def minimized():
		pass

	def exclusive():
		pass

	def vsync():
		pass

	def fps():
		pass

	# dialog

	def dialog_file():
		pass

	def dialog_color():
		pass

	def dialog_date():
		pass

	def dialog_select():
		pass

	def effect():
		pass

	# effect

	def effect_list():
		pass

	def effect_clear():
		pass

	def effect_remove():
		pass

	# vn

	def vn():
		pass

	def vn_clear():
		pass

	def vn_say():
		pass

	def vn_skip():
		pass

	def vn_route():
		pass

	def vn_route_remove():
		pass

	def vn_route_check():
		pass

	def vn_route_select():
		pass

	def vn_route_repeat():
		pass

	def vn_route_skip():
		pass

	def vn_character():
		pass

	def vn_come():
		pass

	def vn_leave():
		pass

	def vn_change():
		pass

	def vn_env():
		pass

	def vn_env_change():
		pass

	# 2d

	def _2d():
		pass

	def _2d_bg():
		pass

	def _2d_map():
		pass

	def _2d_character():
		pass

	def _2d_object():
		pass

	def _2d_npc():
		pass

	def _2d_enemy():
		pass

	def _2d_shoot():
		pass

	def _2d_jump():
		pass

	def _2d_drop():
		pass

	def _2d_look():
		pass

	def _2d_inventory():
		pass

	def _2d_hud():
		pass

	def _2d_sound():
		pass

	def _2d_light():
		pass

	def _2d_camera():
		pass

	# 3d

	def _3d():
		pass

	def _3d_bg():
		pass

	def _3d_map():
		pass

	def _3d_character():
		pass

	def _3d_object():
		pass

	def _3d_npc():
		pass

	def _3d_enemy():
		pass

	def _3d_shoot():
		pass

	def _3d_jump():
		pass

	def _3d_drop():
		pass

	def _3d_look():
		pass

	def _3d_hud():
		pass

	def _3d_inventory():
		pass

	def _3d_sound():
		pass

	def _3d_light():
		pass

	def _3d_camera():
		pass

	# ai

	def ai_text():
		pass

	def ai_image():
		pass

	def ai_video():
		pass

	def ai_music():
		pass

	def ai_sound():
		pass

	def ai_say():
		pass

	def ai_2d():
		pass

	def ai_3d():
		pass

	def ai_character():
		pass

	def ai_clean():
		pass

	def ai_resize():
		pass

	def ai_color():
		pass

	def ai_style():
		pass

	def ai_translate():
		pass

	def ai_recognize_text():
		pass

	def ai_recognize_image():
		pass

	def ai_recognize_video():
		pass

	def ai_recognize_motion():
		pass

	def ai_capture_voice():
		pass

	def ai_capture_face():
		pass

	def ai_capture_motion():
		pass

if __name__ == "__main__":
	void.run()
