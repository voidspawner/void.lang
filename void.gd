# ＶＯＩＤ lang

extends Node2D

var data = {
	"settings": {
		"print": "window",
		"size": {
			"original": null
		},
		"debug": false,
		"info": false,
		"menu": false,
		"os": {
			"name": null,
			"type": "windows",
			"path": {},
			"language": {
				"short": "en",
				"long": "en-EN"
			},
			"processor": {},
			"argument": {}
		},
		'app': {
			'timer': {},
			'action': [],
			'var': {},
			'file': []
		},
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
			'limit': {
				'count': 100,
				'wait': 0.1,
				'size': 10_000_000,
				'fragment': 100_000
			},
			'port': 80,
			'compress': {
				'enable': false,
				'min': 1000,
				'type': [
					'text/html',
					'application/xml',
					'text/plain',
					'text/void',
					'text/css',
					'text/javascript',
					'text/csv',
					'application/x-sh',
					'application/x-csh',
					'application/x-httpd-php',
					'applycation/x-python-code',
					'application/swift'
				]
			}
		},
		'https': {
			'port': 443,
			'certificate': '',
			'key': ''
		}
	},
	"ui": [],
	"key": {
		"bind": {},
		"disable": []
	},
	"alias": {},
	"apps": [],
	"run": [],
	"action": {
		"void": {
			"auth": {
				"signin": [],
				"signout": [],
				"signup": [],
				"restore": {
					"code": [],
					"password": []
				}
			},
			"pay": {},
			"ai": {
				"image": [],
				"video": []
			},
			"upload": []
		},
		"format": {
			"void": {
				"encode": [],
				"decode": []
			},
			"csv": {
				"encode": [],
				"decode": []
			},
			"ini": {
				"encode": [],
				"decode": []
			},
			"yaml": {
				"encode": [],
				"decode": []
			}
		}
	},
	"text": {
		"void": {
			"volume": ["🔇", "🔈", "🔉", "🔊"],
			"hash": {
				'upper': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
				'lower': 'abcdefghijklmnopqrstuvwxyz',
				'number': '0123456789',
				'symbol': '!@#$%^&*()[]<>.,:;-+=_~'
			},
			"number": {
				"byte": {
					"multiply": 1024,
					"short": ["B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB"],
					"long": ["byte", "kilobyte", "megabyte", "gigabyte", "terabyte", "petabyte", "exabyte", "zettabyte", "yottabyte"]
				},
				"thousands": {
					"multiply": 1000,
					"short": ["K", "M", "G", "T", "P", "E", "Z", "Y"],
					"long": ["kilo", "mega", "giga", "tera", "peta", "exa", "zetta", "yotta"]
				},
				"fractional": ["milli", "micro", "nano", "pico", "femto", "atto", "zepto", "yocto"]
			}
		}
	},
	"timer": {},
	"vn": {
		"show": false,
		"image": {},
		"text": {},
		"button": {},
		"character": {},
		"route": {
			"selected": [],
			"current": null,
			"list": []
		}
	}
}

var vars = {
	'uuid': preload('res://script/uuid.gd'),
	'random': RandomNumberGenerator.new(),
	'cursor': {
		'arrow': DisplayServer.CursorShape.CURSOR_ARROW,
		'ibeam': DisplayServer.CursorShape.CURSOR_IBEAM,
		'hand': DisplayServer.CursorShape.CURSOR_POINTING_HAND,
		'cross': DisplayServer.CursorShape.CURSOR_CROSS,
		'wait': DisplayServer.CursorShape.CURSOR_WAIT,
		'busy': DisplayServer.CursorShape.CURSOR_BUSY,
		'drag': DisplayServer.CursorShape.CURSOR_DRAG,
		'drop': DisplayServer.CursorShape.CURSOR_CAN_DROP,
		'forbidden': DisplayServer.CursorShape.CURSOR_FORBIDDEN,
		'vsize': DisplayServer.CursorShape.CURSOR_VSIZE,
		'hsize': DisplayServer.CursorShape.CURSOR_HSIZE,
		'bdiagsize': DisplayServer.CursorShape.CURSOR_BDIAGSIZE,
		'fdiagsize': DisplayServer.CursorShape.CURSOR_FDIAGSIZE,
		'move': DisplayServer.CursorShape.CURSOR_MOVE,
		'vsplit': DisplayServer.CursorShape.CURSOR_VSPLIT,
		'hsplit': DisplayServer.CursorShape.CURSOR_HSPLIT,
		'help': DisplayServer.CursorShape.CURSOR_HELP,
		'max': DisplayServer.CursorShape.CURSOR_MAX
	},
	'file dialog': {
		'file': DisplayServer.FileDialogMode.FILE_DIALOG_MODE_OPEN_FILE,
		'files': DisplayServer.FileDialogMode.FILE_DIALOG_MODE_OPEN_FILES,
		'dir': DisplayServer.FileDialogMode.FILE_DIALOG_MODE_OPEN_DIR,
		'any': DisplayServer.FileDialogMode.FILE_DIALOG_MODE_OPEN_ANY,
		'save': DisplayServer.FileDialogMode.FILE_DIALOG_MODE_SAVE_FILE
	},
	'orientation': {
		'landscape': DisplayServer.ScreenOrientation.SCREEN_LANDSCAPE,
		'portrait': DisplayServer.ScreenOrientation.SCREEN_PORTRAIT,
		'landscape reverse': DisplayServer.ScreenOrientation.SCREEN_REVERSE_LANDSCAPE,
		'portrait reverse': DisplayServer.ScreenOrientation.SCREEN_REVERSE_PORTRAIT,
		'landscape sensor': DisplayServer.ScreenOrientation.SCREEN_SENSOR_LANDSCAPE,
		'portrait sensor': DisplayServer.ScreenOrientation.SCREEN_SENSOR_PORTRAIT,
		'sensor': DisplayServer.ScreenOrientation.SCREEN_SENSOR
	},
	'feature': {
		'menu': DisplayServer.Feature.FEATURE_GLOBAL_MENU,
		'subwindows': DisplayServer.Feature.FEATURE_SUBWINDOWS,
		'touchscreen': DisplayServer.Feature.FEATURE_TOUCHSCREEN,
		'mouse': DisplayServer.Feature.FEATURE_MOUSE,
		'mouse warp': DisplayServer.Feature.FEATURE_MOUSE_WARP,
		'clipboard': DisplayServer.Feature.FEATURE_CLIPBOARD,
		'virtual keyboard': DisplayServer.Feature.FEATURE_VIRTUAL_KEYBOARD,
		'cursor shape': DisplayServer.Feature.FEATURE_CURSOR_SHAPE,
		'cursor shape custom': DisplayServer.Feature.FEATURE_CUSTOM_CURSOR_SHAPE,
		'dialog': DisplayServer.Feature.FEATURE_NATIVE_DIALOG,
		'ime': DisplayServer.Feature.FEATURE_IME,
		'window transparency': DisplayServer.Feature.FEATURE_WINDOW_TRANSPARENCY,
		'hidpi': DisplayServer.Feature.FEATURE_HIDPI,
		'icon': DisplayServer.Feature.FEATURE_ICON,
		'icon native': DisplayServer.Feature.FEATURE_NATIVE_ICON,
		'orientation': DisplayServer.Feature.FEATURE_ORIENTATION,
		'swap buffers': DisplayServer.Feature.FEATURE_SWAP_BUFFERS,
		'clipboard primary': DisplayServer.Feature.FEATURE_CLIPBOARD_PRIMARY,
		'text to speech': DisplayServer.Feature.FEATURE_TEXT_TO_SPEECH,
		'extend to title': DisplayServer.Feature.FEATURE_EXTEND_TO_TITLE,
		'screen capture': DisplayServer.Feature.FEATURE_SCREEN_CAPTURE
	},
	'mouse mode': {
		'visible': DisplayServer.MouseMode.MOUSE_MODE_VISIBLE,
		'hidden': DisplayServer.MouseMode.MOUSE_MODE_HIDDEN,
		'captured': DisplayServer.MouseMode.MOUSE_MODE_CAPTURED,
		'confined': DisplayServer.MouseMode.MOUSE_MODE_CONFINED,
		'confined hidden': DisplayServer.MouseMode.MOUSE_MODE_CONFINED_HIDDEN
	},
	'cloud': {
		'server': null,
		'client': {}
	},
	'key': {
		'esc': 'Escape',
		'[': 'BracketLeft',
		']': 'BracketRight',
		'lkm': 'LMB',
		'rkm': 'RMB',
		'skm': 'MMB'
	},
	'effect': {},
	'wait': {}
}

func _ready():
	prepare()
	test()
	start()

func _process(delta):
	# Server
	if vars['cloud']['server'] != null:
		server_process()
	# Effect
	if vars['effect'].size() > 0:
		for name in vars['effect']:
			var effect = vars['effect'][name]
			if effect['skip']:
				vars['effect'].erase(name)
				continue
			match effect['type']:
				'ticker':
					var time = timestamp()
					if time - effect['last'] >= effect['speed']:
						var index = effect['index']
						effect['node'].text += effect['text'][index]
						index += 1
						if index >= effect['size']:
							vars['effect'].erase(name)
						else:
							effect['last'] = time
							effect['index'] = index
	# Timer
	var timers = data['timer'] 
	if len(timers) > 0:
		var time = timestamp()
		for name in timers:
			var timer = timers[name]
			if timer['end'] <= time:
				action(timer['action'])
				if not timer['repeat']:
					data['timer'].erase(name)
				else:
					timer['end'] += timer['duration']
	# Debug
	if data['settings']['info']:
		p(debug_info())

func _physics_process(delta):
	pass

func _input(event):
	if event is InputEventKey and event.is_pressed():
		var code = event.as_text_physical_keycode()
		#var label = event.as_text_key_label()
		if code in data['key']['bind'] and code not in data['key']['disable']:
			action(data['key']['bind'][code])
	if event is InputEventMouseButton and event.is_pressed():
		var code = null
		match event.button_index:
			1: code = 'LMB'
			2: code = 'RMB'
			3: code = 'MMB'
			4: code = 'Scroll Up'
			5: code = 'Scroll Down'
		if code != null and code in data['key']['bind'] and code not in data['key']['disable']:
			action(data['key']['bind'][code])

func _notification(what):
	if what == NOTIFICATION_APPLICATION_FOCUS_OUT:
		pass

func _button_pressed(button: Button):
	var ui = ui(button.name)
	action(ui['action'])

# Prepare

func prepare():
	self.prepare_arguments()
	self.prepare_data()
	self.prepare_data_app()
	self.prepare_path()
	self.prepare_ui()
	self.random_change()

func prepare_arguments():
	var arguments = {}
	var name = null
	var value = null
	var index = 0
	for argument in OS.get_cmdline_args():
		if argument[0] == '-':
			if name != null:
				arguments[name] = true
			name = argument.lstrip("-")
		else:
			if name != null:
				arguments[name] = argument
			else:
				arguments[index] = argument
				index += 1
			name = null
	self.data['settings']['os']['argument'] = arguments

func prepare_data():
	self.data['settings']['os']['name'] = OS.get_name()
	self.data['settings']['os']['version'] = OS.get_version()
	self.data['settings']['os']['model'] = OS.get_model_name()
	self.data['settings']['os']['distribution'] = OS.get_distribution_name()
	self.data['settings']['os']['path']['data'] = OS.get_data_dir()
	self.data['settings']['os']['path']['user'] = OS.get_user_data_dir()
	self.data['settings']['os']['path']['cache'] = OS.get_cache_dir()
	self.data['settings']['os']['path']['config'] = OS.get_config_dir()
	self.data['settings']['os']['path']['execute'] = path_dir(OS.get_executable_path())
	self.data['settings']['os']['path']['current'] = self.data['settings']['os']['path']['execute']
	self.data['settings']['os']['language']['short'] = OS.get_locale_language()
	self.data['settings']['os']['language']['long'] = OS.get_locale().replace("_", "-")
	self.data['settings']['os']['processor']['name'] = OS.get_processor_name()
	self.data['settings']['os']['processor']['count'] = OS.get_processor_count()
	self.data['settings']['os']['debug'] = OS.is_debug_build()

func prepare_data_app():
	var data = null
	if 0 in self.data['settings']['os']['argument'] and path_extension(self.data['settings']['os']['argument'][0]).to_lower() == 'json' and file_exists(self.data['settings']['os']['argument'][0]):
		data = json_read(self.data['settings']['os']['argument'][0])
	elif file_exists(self.data['settings']['os']['path']['execute'] + '/run.json'):
		data = json_read(self.data['settings']['os']['path']['execute'] + '/run.json')
	if data != null:
		self.data = self.merge(self.data, data)

func prepare_path():
	data['settings']['app']['names'] = dir_filename_recursive(self.data['settings']['os']['path']['execute'])

func prepare_ui():
	vars['content'] = get_node("/root/main/content")
	vars['size_original'] = window_size()
	get_node('/root/main/debug').size = vars['size_original']
	get_node("/root").connect("size_changed", window_resize)
	window_resize()

func test():
	var time = timestamp()
	for i in range(100):
		var image: Image = get_viewport().get_texture().get_image()
	print((timestamp() - time) / 1000.0)
	pass

func start():
	self.action(data['run'])

func end():
	pass

# Helper

func props(instance):
	for property in instance.get_property_list():
		print(property)
	for method in instance.get_method_list():
		print(method)

func font_load(name):
	match name:
		'mono':
			return load("res://font/mono.ttf")
		_:
			var font = FontFile.new()
			font.data = file_read(name, true)
			return font

func alignment(name):
	match name:
		'left':
			return HorizontalAlignment.HORIZONTAL_ALIGNMENT_LEFT
		'right':
			return HorizontalAlignment.HORIZONTAL_ALIGNMENT_RIGHT
		'center':
			return HorizontalAlignment.HORIZONTAL_ALIGNMENT_CENTER
		'fill':
			return HorizontalAlignment.HORIZONTAL_ALIGNMENT_FILL
		_:
			return HorizontalAlignment.HORIZONTAL_ALIGNMENT_LEFT

# Data

func data_get():
	pass

func data_set():
	pass

func data_remove():
	pass

func alias(data):
	for name in data:
		self.data['alias'][name] = data[name]

func alias_remove(name):
	data['alias'] = null

# Control

func action(list):
	var action_list = list.duplicate(true)
	var action_name = null
	var alias = data['alias']
	if typeof(action_list) != TYPE_ARRAY:
		action_list = [action_list]
	var index = 0
	for action in action_list:
		if typeof(action) == TYPE_ARRAY:
			action_name = action[0]
		else:
			action_name = str(action)
			action = [action_name]
		if action_name in alias:
			action_name = alias[action_name]
		match action_name:
			'.': p(param(action, 1))
			'x': pass
			'X': self.exit(param_int(action, 1), param_str(action, 1))
			'event.process': pass
			'event.resize': pass
			'event.rotate': pass
			'event.keyboard': pass
			'event.mouse': pass
			'event.gamepad': pass
			'event.focus': pass
			'event.unfocus': pass
			'event.idle': pass
			'event.active': pass
			'event.drop': pass
			'action': action(param_array(action, 1))
			'action.new': data['action'][param_str(action, 1)] = param_array(action, 2)
			'action.pause': action_pause(param_str(action, 1), action_list.slice(index + 1));return
			'action.continue': action_continue(param_str(action, 1))
			'music': music_play(param_file(action, 1))
			'music.stop': music_stop()
			'sound': sound_play(param_file(action, 1))
			'sound.stop': sound_stop()
			'volume.up': volume_up(param_percent(action, 1, 0.1))
			'volume.down': volume_down(param_percent(action, 1, 0.1))
			'mute': mute(param_bool(action, 1))
			'timer': timer(param_float(action, 1), param_array(action, 2), param_str(action, 3, null), param_bool(action, 4, false), param_bool(action, 5, false))
			'bg': ui_background(param_file(action, 1))
			'size': window_size(Vector2i(param_int(action, 1, 0), param_int(action, 2, 0)))
			'size.max': window_size_max(Vector2i(param_int(action, 1, 0), param_int(action, 2, 0)))
			'size.min': window_size_min(Vector2i(param_int(action, 1, 0), param_int(action, 2, 0)))
			'size.lock': window_unresizable(param_bool(action, 1, true))
			'position': window_position(Vector2i(param_int(action, 1), param_int(action, 2)))
			'fullscreen': window_fullscreen(param_bool(action, 1, null))
			'noborder': window_borderless(param_bool(action, 1, true))
			'center': window_center()
			'title': window_title(param_str(action, 1))
			'icon': window_icon(param_file(action, 1))
			'file.gzip': file_gzip(param_str(action, 1))
			'file.ungzip': file_ungzip(param_str(action, 1))
			'alias': self.alias(param_dict(action, 1))
			'vn': vn(param(action, 1))
			'vn.show': vn(true)
			'vn.hide': vn(false)
			'vn.say': vn_say(param_str(action, 1), param_str(action, 2, null));return action_pause('vn.say', action_list, index)
			'vn.skip': vn_skip()
			'vn.next': vn_skip(true)
			'vn.route': vn_route(param_array(action, 1));return action_pause('vn.route', action_list, index)
			'vn.repeat': vn_route_repeat()
			'vn.continue': vn_route_continue()
			'vn.check': vn_route_check_all(param_array(action, 1));return action_pause('vn.check', action_list, index)
			'vn.remove': vn_route_remove(param_str(action, 1))
			'vn.current': vn_route_current(param_str(action, 1))
			'vn.select': vn_route_select(param_str(action, 1))
			'vn.reset': vn_reset()
			'vn.char': pass
			'vn.come': pass
			'vn.leave': pass
			'show': ui_show(param_str(action, 1))
			'hide': ui_hide(param_str(action, 1))
			'enable': ui_enable(param_str(action, 1))
			'disable': ui_disable(param_str(action, 1))
			'remove': ui_remove(param_str(action, 1))
			'ui.remove': ui_remove(param_str(action, 1))
			'text': ui_add('text', param_dict(action, 1))
			'image': ui_add('image', param_dict(action, 1))
			'button': ui_add('button', param_dict(action, 1))
			'menu': ui_menu(param_dict(action, 1, null))
			'menu.show': ui_menu(true)
			'menu.hide': ui_menu(false)
			'key': key_bind(param_str(action, 1), param_array(action, 2))
			'key.remove': key_remove(param_str(action, 1))
			'key.disable': key_disable(param_str(action, 1))
			'key.enable': key_enable(param_str(action, 1))
			'app': pass
			'cli': pass
			'http': server_http(param_dict(action, 1))
			'https': pass
			'socket': pass
			'cloud': pass
			'game': game(param_array(action, 1, null))
			'debug': debug(param_bool(action, 1, null))
			'open': open(param_str(action, 1))
			'wait': wait(param_float(action, 1))
			'say': say(param_str(action, 1), param_str(action, 2), param_int(action, 3, 50), param_float(action, 4, 1.0), param_float(action, 5, 1.0))
			'say.stop': say_stop()
			'say.pause': say_pause()
			'say.resume': say_resume()
			'say.voices': p(say_voices())
			'say.file': say(file_read(param_file(action, 1)), param_str(action, 2), param_int(action, 3, 50), param_float(action, 4, 1.0), param_float(action, 5, 1.0))
			_:
				pass
		index += 1

func action_pause(name: String, list: Array, index: int = -1):
	vars['wait'][name] = list if index < 0 else list.slice(index + 1)

func action_continue(name: String):
	if name in vars['wait']:
		var list = vars['wait'][name]
		vars['wait'].erase(name)
		action(list)

func action_clear(name: String):
	vars['wait'].erase(name)

func param(params, index = 0, default = null):
	var type = typeof(index) 
	if (type == TYPE_STRING and index in params) or (type == TYPE_INT and index <= params.size() - 1):
		return params[index]
	return default

func param_str(params, index = 0, default = ''):
	var type = typeof(index) 
	if (type == TYPE_STRING and index in params) or (type == TYPE_INT and index <= params.size() - 1):
		return str(params[index])
	return default

func param_int(params, index = 0, default = 0):
	var type = typeof(index) 
	if (type == TYPE_STRING and index in params) or (type == TYPE_INT and index <= params.size() - 1):
		return int(params[index])
	return default

func param_float(params, index = 0, default = 0.0):
	var type = typeof(index) 
	if (type == TYPE_STRING and index in params) or (type == TYPE_INT and index <= params.size() - 1):
		return float(params[index])
	return default

func param_bool(params, index = 0, default = false):
	var type = typeof(index) 
	if (type == TYPE_STRING and index in params) or (type == TYPE_INT and index <= params.size() - 1):
		return bool(params[index])
	return default

func param_array(params, index = 0, default = []):
	var type = typeof(index) 
	if (type == TYPE_STRING and index in params) or (type == TYPE_INT and index <= params.size() - 1):
		if typeof(params[index]) == TYPE_ARRAY:
			return params[index]
		else:
			return [params[index]]
	return default

func param_dict(params, index = 0, default = {}):
	var type = typeof(index) 
	if (type == TYPE_STRING and index in params) or (type == TYPE_INT and index <= params.size() - 1):
		if typeof(params[index]) == TYPE_DICTIONARY:
			return params[index]
	return default

func param_file(params, index = 0, default = ''):
	var type = typeof(index) 
	if (type == TYPE_STRING and index in params) or (type == TYPE_INT and index <= params.size() - 1):
		var path = params[index]
		if file_exists(path):
			return path
		if path in data['settings']['app']['names']:
			return data['settings']['app']['names'][path]
	return default

func param_percent(params, index = 0, default = 0):
	var type = typeof(index) 
	if (type == TYPE_STRING and index in params) or (type == TYPE_INT and index <= params.size() - 1):
		var value = params[index]
		if typeof(value) == TYPE_STRING and '%' in value:
			return float(value.replace('%', '')) / 100.0
		return float(value)
	return default

func param_color(params, index = 0, default = Color(1, 1, 1, 1)):
	var type = typeof(index) 
	if (type == TYPE_STRING and index in params) or (type == TYPE_INT and index <= params.size() - 1):
		var value = params[index]
		match typeof(value):
			TYPE_STRING:
				return Color.from_string(value, default)
			TYPE_INT:
				if value > 255:
					value = 255
				elif value < 0:
					value = 0
				value = int(value / 255)
				return Color(value, value, value, 1)
			TYPE_FLOAT:
				if value > 1:
					value = 1
				elif value < 0:
					value = 0
				return Color(value, value, value, 1)
	return default
	
func check():
	pass

func loop():
	pass

func shell(command: String, arguments: Array = [], hidden: bool = true, process: bool = false):
	if not process:
		var lines = []
		var code = null
		if os_windows():
			code = OS.execute('cmd.exe', ['/C', command] + arguments, lines, true, not hidden)
		return {
			'code': code,
			'text': '\n'.join(lines)
		}
	return {
		'pid': OS.create_process(OS.get_executable_path(), [command] + arguments, not hidden)
	}

func open(uri: String):
	OS.shell_open(uri)

func exit(code: int = 0, message: String = ''):
	if message != '':
		print(message)
	if os_windows():
		printraw(OS.get_executable_path().get_base_dir().replace('/', '\\') + '>')
	get_tree().quit(code)

func error(name: String, code = 1, message: String = '', data = null):
	print(name + (' :: ' + message if message != '' else ''))
	if data != null:
		p(data)
	exit(code)

func warning(name: String, message: String = ''):
	p(name + (' :: ' + message if message != '' else ''))

func ok(name: String, message: String = ''):
	p(name + (' :: ' + message if message != '' else ''))

func p(data = '', newline: bool = true):
	var text = null
	if data is Array or data is Dictionary:
		text = self.json_encode(data, true)
	else:
		text = str(data) if data != null else ''
	match self.data['settings']['print']:
		'cli':
			if newline:
				print(text)
			else:
				printraw(text)			
		'window':
			get_node("/root/main/debug").text = text

# Debug

func debug(state = null):
	data['settings']['info'] = not data['settings']['info'] if state == null else bool(state)
	if not data['settings']['info']:
		p('')

func d(name: String, data = null):
	if debug():
		if typeof(data) in [TYPE_STRING, TYPE_INT, TYPE_FLOAT, TYPE_BOOL]:
			p(name + ' :: ' + str(data))
		else:
			p(name + ' :: ')
			if data != null:
				p(data)
	
func debug_info():
	var memory = self.memory()
	return \
		"FPS " + str(self.fps()) + "\n" + \
		"MEM " + self.number(memory['total'], 'byte') + "\n" + \
		"USE " + self.number(memory['used'], 'byte') + "\n" + \
		"FRE " + self.number(memory['free'], 'byte') + "\n" + \
		"PRC " + self.data['settings']['os']['processor']['name'] + "\n" + \
		"COR " + str(self.data['settings']['os']['processor']['count']) + "\n" + \
		"OSN " + self.data['settings']['os']['name'] + "\n" + \
		"OSV " + self.data['settings']['os']['version'] + "\n" + \
		"LNG " + self.data['settings']['os']['language']['long']

# Time

func timestamp():
	return Time.get_unix_time_from_system()

func timepast():
	return Time.get_ticks_usec() / 1000000.0

func wait(seconds: float):
	OS.delay_msec(seconds * 1000)
	# await get_tree().create_timer(seconds).timeout

func timer(seconds: float, action, name = null, repeat: bool = false, immediate: bool = false):
	if name == null:
		name = uuid()
	var start = self.timestamp()
	data['timer'][name] = {
		'start': start,
		'end': start + (seconds if not immediate else 0),
		'duration': seconds,
		'repeat': repeat,
		'action': action
	}

func timer_remove(name = null):
	if name == null:
		data['timer'] = {}
	else:
		data['timer'].erase(name)
		for name_child in data['timer'].keys():
			if name_child.begins_with(name + '_'):
				data['timer'].erase(name_child)

# Math

func dec_hex(value):
	return "%X" % value

# String

func number(number, unit = null, group: String = ' ', fraction: String = '.'):
	var result = number
	var numbers = data['text']['void']['number']
	if unit in numbers:
		numbers = numbers[unit]
		var value = numbers['short']
		var index = 0
		while result > 1024:
			result = result / 1024.0
			index += 1
		if index < value.size():
			return str(round(result)) + group + value[index]
	return result

func datetime(timestamp = null, separator = null):
	if timestamp == null:
		timestamp = self.timestamp()
	var time: Dictionary = Time.get_datetime_dict_from_unix_time(timestamp)
	if separator == null:
		return "%d/%02d/%02d %02d:%02d" % [time.year, time.month, time.day, time.hour, time.minute]
	return "%d%s%02d%s%02d%s%02d%s%02d" % [time.year, separator, time.month, separator, time.day, separator, time.hour, separator, time.minute]

func path_dir(path: String):
	return path.rstrip('/').get_base_dir()

func path_name(path: String):
	return path.get_basename().split('/')[-1]

func path_extension(path: String):
	return path.get_extension()

func path_basename(path: String):
	return path.get_file()

func path_extension_strip(path: String):
	return path.get_basename()

func path_volume(path: String):
	pass

# Array

func merge(data1, data2):
	var result = data1.duplicate(true)
	if data1 is Array:
		if data2 is Array:
			result += data2
		else:
			result.append(data2)
	elif data1 is Dictionary:
		if data2 is Dictionary:
			for name in data2:
				if name in data1 and data1[name] is Dictionary and data2[name] is Dictionary:
					result[name] = merge(result[name], data2[name])
				else:
					result[name] = data2[name]
	return result

# JSON

func json_encode(data, indent = false):
	if indent == false:
		indent = ""
	elif indent == true:
		indent = "\t"
	else:
		indent = str(indent)
	var json = JSON.new()
	return json.stringify(data, indent)

func json_decode(text: String):
	var json = JSON.new()
	var error = json.parse(text)
	if error == OK:
		return json.data
	else:
		self.warning('json', json.get_error_message() + " - " + str(json.get_error_line()))
	return null

func json_read(path: String):
	var text = self.file_read(path)
	if typeof(text) == TYPE_STRING:
		return self.json_decode(text)
	return null

func json_write(path: String, data, indent = true):
	self.file_write(path, self.json_encode(data, indent))

# File

func file_exists(path: String):
	return FileAccess.file_exists(path)

func file_write(path: String, text):
	var file = FileAccess.open(path, FileAccess.WRITE)
	if typeof(text) == TYPE_PACKED_BYTE_ARRAY:
		file.store_buffer(text)
	else:
		file.store_string(str(text))
	file.close()

func file_read(path: String, bytes: bool = false):
	if file_exists(path):
		var file = FileAccess.open(path, FileAccess.READ)
		var text = file.get_as_text() if not bytes else file.get_buffer(file.get_length())
		file.close()
		return text
	return null

func file_remove(path: String, trash: bool = true):
	if self.file_exists(path):
		if trash:
			return OS.move_to_trash(path)
		else:
			return DirAccess.remove_absolute(path)

func file_move(from: String, to: String):
	var dir = DirAccess.open(path_dir(from))
	return dir.rename(from, to)

func file_copy(from: String, to: String):
	var dir = DirAccess.open(path_dir(from))
	return dir.copy(from, to)

func file_rename(path: String, name: String):
	var dir_path = path_dir(path)
	var dir = DirAccess.open(dir_path)
	var newname = dir_path + '/' + name
	return dir.rename(path, newname) if dir != null else null

func file_size(path: String) -> int:
	if file_exists(path):
		var file = FileAccess.open(path, FileAccess.READ)
		var size = file.get_length()
		file.close()
		return size
	return 0

func file_info(path: String):
	if file_exists(path):
		return {
			'path': path, 
			'dir': path_dir(path),
			'file': path_basename(path),
			'name': path_name(path),
			'extension': path_extension(path),
			'size': file_size(path),
			'modified': file_time_modified(path),
			'readonly': file_readonly(path),
			'hidden': file_hidden(path),
			'permissions': file_permissions(path)
		}

func file_permissions(path: String, permissions: int = -1):
	if file_exists(path):
		if permissions == -1:
			return FileAccess.get_unix_permissions(path)
		else:
			return FileAccess.set_unix_permissions(path, permissions)

func file_readonly(path: String, flag = null):
	if file_exists(path):
		if flag == null:
			return FileAccess.get_read_only_attribute(path)
		else:
			return FileAccess.set_read_only_attribute(path, bool(flag))

func file_hidden(path: String, flag = null):
	if file_exists(path):
		if flag == null:
			return FileAccess.get_hidden_attribute(path)
		else:
			return FileAccess.set_hidden_attribute(path, bool(flag))

func file_time_modified(path: String):
	if file_exists(path):
		return FileAccess.get_modified_time(path)

func file_sha256(path: String):
	return FileAccess.get_sha256(path)

func file_zip(path: String, zip_path: String = ''):
	var data = file_read(path, true)
	if data == null:
		return
	var zip_file = path_extension_strip(path) + '.zip' if zip_path == '' else zip_path
	var writer = ZIPPacker.new()
	var error = writer.open(zip_file, ZIPPacker.APPEND_CREATE if zip_path == '' else ZIPPacker.APPEND_ADDINZIP)
	if error != OK:
		return error
	writer.start_file(path_basename(path))
	writer.write_file(data)
	writer.close_file()
	writer.close()

func file_zip_list(path: String) -> Array:
	if not file_exists(path):
		return []
	var reader = ZIPReader.new()
	var error = reader.open(path)
	if error != OK:
		return []
	var result = reader.get_files()
	reader.close()
	return result

func file_zip_exists(path: String, filename: String) -> bool:
	if not file_exists(path):
		return false
	var reader = ZIPReader.new()
	var error = reader.open(path)
	if error != OK:
		return false
	var exists = reader.file_exists(filename)
	reader.close()
	return exists

func file_zip_read(path: String, filename: String, data: bool = false):
	if not file_exists(path):
		return
	var reader = ZIPReader.new()
	var error = reader.open(path)
	if error != OK:
		return null
	var result = null
	if reader.file_exists(filename):
		result = reader.read_file(filename)
		if not data:
			result = result.get_string_from_utf8()
	reader.close()
	return result

func file_unzip(path: String, filename: String = ''):
	var reader = ZIPReader.new()
	var error = reader.open(path)
	if error != OK:
		return error
	var dir = path_dir(path)
	if filename != '':
		if reader.file_exists(filename):
			file_write(dir + '/' + filename, reader.read_file(filename))
	else:
		for file in reader.get_files():
			file_write(dir + '/' + file, reader.read_file(file))
	reader.close()

func file_gzip(path: String):
	if file_exists(path):
		var data = FileAccess.get_file_as_bytes(path)
		var gzip = StreamPeerGZIP.new()
		gzip.start_compression()
		gzip.put_data(data)
		gzip.finish()
		data = gzip.get_data(gzip.get_available_bytes())[1]
		var file = FileAccess.open(path + '.gz', FileAccess.WRITE)
		file.store_buffer(data)
		file.close()

func file_ungzip(path: String):
	if file_exists(path):
		var data = FileAccess.get_file_as_bytes(path)
		var gzip = StreamPeerGZIP.new()
		gzip.start_decompression()
		gzip.put_data(data)
		gzip.finish()
		data = gzip.get_data(gzip.get_available_bytes())[1]
		path = path.rstrip('.gz') 
		var file = FileAccess.open(path, FileAccess.WRITE)
		file.store_buffer(data)
		file.close()

# Link

func link_create(path: String, source: String, name: String = '', image = null):
	pass

func link_exists(path: String):
	return FileAccess.file_exists(path)

# Dir

func dir_exists(path: String):
	return DirAccess.open(path) != null

func dir_create(path: String):
	return DirAccess.make_dir_recursive_absolute(path)

func dir_copy(from: String, to: String):
	var dirname = path_basename(from)
	var to_dirname = to + '/' + dirname
	dir_create(to_dirname)
	for name in dir_list(from):
		if file_exists(from + '/' + name):
			file_copy(from + '/' + name, to_dirname + '/' + name)
		elif dir_exists(from + '/' + name):
			dir_copy(from + '/' + name, to_dirname)

func dir_move(from: String, to: String):
	var dir = DirAccess.open(from)
	return dir.rename(from, to) if dir != null else null

func dir_rename(path: String, name: String):
	var dir = DirAccess.open(path)
	var newname = path_dir(path) + '/' + name
	return dir.rename(path, newname) if dir != null else null

func dir_remove(path: String, trash: bool = true):
	if trash:
		return OS.move_to_trash(path)
	return DirAccess.remove_absolute(path)

func dir_list(path: String):
	var result = []
	var dir = DirAccess.open(path)
	dir.include_hidden = true
	if dir:
		dir.list_dir_begin()
		var file = dir.get_next()
		while file != '':
			result.append(file)
			file = dir.get_next()
	return result

func dir_clear(path: String):
	for name in dir_list(path):
		dir_remove(path + '/' + name)

func dir_info(path: String):
	var result = {
		'path': path,
		'list': {
			'files': 0,
			'dirs': 0,
			'size': 0
		},
		'total': {
			'files': 0,
			'dirs': 0,
			'size': 0
		},
		'modified': dir_modified(path),
		'readonly': dir_readonly(path),
		'hidden': dir_hidden(path),
		'premissions': dir_permissions(path)
	}
	if dir_exists(path):
		for subpath in dir_list(path):
			if file_exists(path + '/' + subpath):
				result['list']['files'] += 1
				result['list']['size'] += file_size(path + '/' + subpath)
			elif dir_exists(path + '/' + subpath):
				result['list']['dirs'] += 1
		var info = dir_size_recursive(path)
		result['total']['files'] = info['files']
		result['total']['dirs'] = info['dirs']
		result['total']['size'] = info['size']
	return result

func dir_size(path: String, recursive: bool = true) -> int:
	var result = 0
	if dir_exists(path):
		if recursive:
			result = dir_size_recursive(path)['size']
		else:
			for subpath in dir_list(path):
				result += file_size(path + '/' + subpath)
	return result

func dir_size_recursive(path: String) -> Dictionary:
	var result = {
		'files': 0,
		'dirs': 0,
		'size': 0
	}
	if dir_exists(path):
		for subpath in dir_list(path):
			if file_exists(path + '/' + subpath):
				result['files'] += 1
				result['size'] += file_size(path + '/' + subpath)
			elif dir_exists(path + '/' + subpath):
				result['dirs'] += 1
				var info = dir_size_recursive(path + '/' + subpath)
				result['files'] += info['files']
				result['dirs'] += info['dirs']
				result['size'] += info['size']
	return result

func dir_filename_recursive(path: String) -> Dictionary:
	var result = {}
	if dir_exists(path):
		for subpath in dir_list(path):
			if file_exists(path + '/' + subpath):
				result[path_name(path + '/' + subpath)] = path + '/' + subpath
			elif dir_exists(path + '/' + subpath):
				var names = dir_filename_recursive(path + '/' + subpath)
				for name in names:
					result[name] = names[name]
	return result
	
func dir_permissions(path: String, permissions: int = -1):
	if dir_exists(path):
		if permissions == -1:
			return FileAccess.get_unix_permissions(path)
		else:
			return FileAccess.set_unix_permissions(path, permissions)

func dir_readonly(path: String, flag = null):
	if dir_exists(path):
		if flag == null:
			return FileAccess.get_read_only_attribute(path)
		else:
			return FileAccess.set_read_only_attribute(path, bool(flag))

func dir_hidden(path: String, flag = null):
	if dir_exists(path):
		if flag == null:
			return FileAccess.get_hidden_attribute(path)
		else:
			return FileAccess.set_hidden_attribute(path, bool(flag))

func dir_modified(path: String):
	if dir_exists(path):
		return FileAccess.get_modified_time(path)

func dir_zip(path):
	if dir_exists(path):
		var zip_file = path_basename(path) + '.zip'
		var writer = null
		for subpath in dir_list(path):
			var filepath = path + '/' + subpath
			var filename = path_basename(filepath)
			if file_exists(filepath):
				var data = file_read(filepath, true)
				if data == null:
					continue
				if writer == null:
					writer = ZIPPacker.new()
					var error = writer.open(zip_file)
					if error != OK:
						return error
				writer.start_file(filename)
				writer.write_file(data)
				writer.close_file()
		if writer != null:
			writer.close()

# Drive

func drive_name(path: String):
	var dir = DirAccess.open(path)
	return dir.get_drive_name(dir.get_current_drive()) if dir != null else null

func drive_count() -> int:
	return DirAccess.get_drive_count()

func drive_mount():
	pass

func drive_unmount():
	pass

func drive_size():
	pass

func drive_free(path: String) -> int:
	var dir = DirAccess.open(path)
	return dir.get_space_left() if dir != null else 0

# Sound

func sound_play(name: String):
	var sound = get_tree().get_root().get_node("main/sound")
	sound.stream = asset(name)
	sound.play()

func sound_stop():
	var sound = get_tree().get_root().get_node("main/sound")
	sound.stop()

func sound_volume(volume = null, bus: String = 'Master'):
	if volume != null:
		AudioServer.set_bus_volume_db(AudioServer.get_bus_index(bus), float(volume))
	else:
		return AudioServer.get_bus_volume_db(AudioServer.get_bus_index(bus))

func sound_mute(mute: bool = true, bus: String = 'Master'):
	AudioServer.set_bus_mute(AudioServer.get_bus_index(bus), mute)

# Music

func music_play(path = null, repeat: bool = true):
	var music = get_tree().get_root().get_node("main/music")
	if typeof(path) == TYPE_STRING:
		music.stream = asset(path)
		if music.stream == null:
			return
		if repeat:
			var length = music.stream.get_length()
			timer(length, [
				['music', path, true]
			], 'music', true)
		else:
			timer_remove('music')
	music.play()

func music_stop():
	var music = get_tree().get_root().get_node("main/music")
	music.stop()
	timer_remove('music')

func music_resume(position: float = 0):
	var music = get_tree().get_root().get_node("main/music")
	music.play(position)

func music_playing():
	var music = get_tree().get_root().get_node("main/music")
	return music.playing

func music_volume(volume = null):
	var music = get_tree().get_root().get_node("main/music")
	if volume != null:
		music.set_volume_db(float(volume))
	else:
		return music.volume_db

# Volume

func volume(volume: float):
	AudioServer.set_bus_volume_db(AudioServer.get_bus_index('Master'), volume)

func volume_get():
	return AudioServer.get_bus_volume_db(AudioServer.get_bus_index('Master'))
	
func volume_up(increment: float = 0.1):
	var volume = volume_get()
	volume += increment * 20
	mute(false)
	if volume > 0:
		volume = 0
	self.volume(volume)
	
func volume_down(decrement: float = 0.1):
	var volume = volume_get()
	volume -= decrement * 20
	if volume <= -20:
		volume = -20
		mute(true)
	self.volume(volume)

func mute(state = null):
	if state == null:
		state = not AudioServer.is_bus_mute(AudioServer.get_bus_index('Master'))
	AudioServer.set_bus_mute(AudioServer.get_bus_index('Master'), bool(state))

# Image

func image_to_texture(image: Image) -> ImageTexture:
	return ImageTexture.create_from_image(image)

func image_crop(image: Image, rect: Rect2i) -> Image:
	var size = image.get_size()
	image.blit_rect(image, rect, Vector2i.ZERO)
	image.crop(rect.size.x, rect.size.y)
	return image

func image_resize(image: Image, size: Vector2i) -> Image:
	image.resize(size.x, size.y, Image.INTERPOLATE_CUBIC)
	return image

func image_square(image: Image, size: Vector2i = Vector2i.ZERO) -> Image:
	var image_size = image.get_size()
	var length = image_size.x if image_size.x <= image_size.y else image_size.y
	var rect = Rect2i((image_size.x - length) / 2, (image_size.y - length) / 2, length, length)
	image.blit_rect(image, rect, Vector2i.ZERO)
	image.crop(length, length)
	image.resize(size.x, size.y, Image.INTERPOLATE_CUBIC)
	return image

func image_jpeg(image: Image, quality: float = 0.9) -> PackedByteArray:
	return image.save_jpg_to_buffer(quality)

func image_png(image: Image) -> PackedByteArray:
	return image.save_png_to_buffer()

func image_webp(image: Image, quality: float = 1.0) -> PackedByteArray:
	var lossy = quality == 1
	return image.save_webp_to_buffer(lossy, quality)

func image(data: PackedByteArray, format = 'webp') -> Image:
	var image = Image.new()
	if format == 'webp':
		image.load_webp_from_buffer(data)
	elif format in ['jpeg', 'jpg']:
		image.load_jpg_from_buffer(data)
	elif format == 'png':
		image.load_png_from_buffer(data)
	elif format == 'bmp':
		image.load_bmp_from_buffer(data)
	return image

# Asset

func asset(path: String):
	var result = null
	if path.begins_with("res://"):
		result = load(path)
	elif file_exists(path):
		var bytes = FileAccess.get_file_as_bytes(path)
		match path_extension(path).to_lower():
			'wav':
				result = AudioStreamWAV.new()
				result.data = bytes
			'ogg':
				result = AudioStreamOggVorbis.new()
				result.data = bytes
			'mp3':
				result = AudioStreamMP3.new()
				result.data = bytes
			'webp', 'jpg', 'jpeg', 'png', 'bmp':
				var image = Image.new()
				image.load(path)
				result = ImageTexture.new()
				result.set_image(image)
			_:
				result = load(path)
	return result

# Color

func color_tint(node, red: float, green: float, blue: float, alpha: float = 1):
	node.modulate = Color(red, green, blue, alpha)

func color_average(image):
	if typeof(image) == TYPE_STRING:
		image = self.asset(image)
	var data: PackedByteArray = image.get_image().get_data()
	var size = data.size()
	var r = 0
	var g = 0
	var b = 0
	for i in range(0, size):
		var pixel = data[i]
		if (i + 1) % 3 == 0:
			b += pixel
		elif (i + 1) % 3 == 2:
			g += pixel
		else:
			r += pixel
	r = 4 * (float(r) / (size / 3)) / 255
	g = 4 * (float(g) / (size / 3)) / 255
	b = 4 * (float(b) / (size / 3)) / 255
	return Color(r, g, b, 1)

# Video

# Screenshot

func screenshot(path: String = '') -> Image:
	var image: Image = get_viewport().get_texture().get_image()
	if path != '':
		var extension = self.path_extension(path).to_lower()
		if extension == 'png':
			image.save_png(path)
		elif extension in ['jpg', 'jpeg']:
			image.save_jpg(path)
		elif extension == 'webp':
			image.save_webp(path)
	return image

# Request

func request():
	pass

# Server

func server(port: int = 80, address: String = '*'):
	server_stop()
	vars['cloud']['server'] = TCPServer.new()
	vars['cloud']['param'] = {
		'port': port,
		'address': address
	}
	var result = vars['cloud']['server'].listen(port, address)
	if not result:
		ok('server.start', address + ': ' + str(port))
	else:
		error('server.start', 500, '', result)

func server_listening() -> bool:
	var server = vars['cloud']['server']
	return server != null and server.is_listening()

func server_stop():
	var server = vars['cloud']['server']
	if server != null:
		server.stop()
		vars['cloud']['server'] = null
		vars['cloud']['param'] = null
		vars['cloud']['request'] = null
		vars['cloud']['response'] = null

func server_process():
	var server = vars['cloud']['server']
	var clients = vars['cloud']['client']
	if server != null and server.is_connection_available():
		var time = Time.get_ticks_msec()
		var stream = server.take_connection()
		stream.set_no_delay(true)
		var uuid = uuid()
		var ip = stream.get_connected_host()
		var client = {
			'stream': stream,
			'time': time
		}
		clients[uuid] = client
		server_connect(client)
		d('server.connect', ip)

	for key in clients.keys():
		var client = clients[key]
		var status = client['stream'].get_status()
		if status == StreamPeerTCP.Status.STATUS_CONNECTED:
			pass
		if status == StreamPeerTCP.Status.STATUS_ERROR:
			error('server.connect', 500, '', client)
			clients.erase(key)
		elif status == StreamPeerTCP.Status.STATUS_NONE:
			d('server.disconnect')
			clients.erase(key)

func server_connect(client):
	var stream = client['stream']
	var server_param = vars['cloud']['param']
	var bytes = stream.get_available_bytes()
	var text = stream.get_utf8_string(bytes)
	if len(text) == 0:
		stream.disconnect_from_host()
		return
	var header = {}
	var name = null
	var value = null
	var method = ''
	var route = null
	var scheme = null
	var version = null
	for letter in text:
		if letter == '\r':
			continue
		if route == null:
			if letter == ' ':
				route = ''
			else:
				method += letter.to_lower()
		elif scheme == null:
			if letter == ' ':
				scheme = ''
			else:
				route += letter
		elif version == null:
			if letter == '/':
				version = ''
			else:
				scheme += letter.to_lower()
		elif name == null:
			if letter == '\n':
				name = ''
				version = float(version)
			else:
				version += letter
		elif letter == '\n':
			if name == '':
				break
			header[name] = value.strip_edges() if value != null else ''
			name = ''
			value = null
		elif letter == ':' and value == null:
			value = ''
		elif value == null:
			name += letter.to_lower()
		else:
			value += letter
	route = str(route)
	var parts = route.split('?')
	var path = parts[0]
	var param = {}
	if len(parts) > 1:
		for part in parts[1].split('&'):
			parts = part.split('=')
			name = str(parts[0])
			value = true
			if len(parts) > 1:
				value = str(parts[1])
				if value == 'true':
					value = true
				elif value == 'false':
					value = false
				elif value == 'null':
					value = null
				elif value.is_valid_int():
					value = int(value)
				elif value.is_valid_float():
					value = float(value)
			if name in param:
				if typeof(param[name]) != TYPE_ARRAY:
					param[name] = [param[name], value]
				else:
					param[name].append(value)
			else:
				param[name] = value
	var request = {
		'host': stream.get_connected_host(),
		'port': stream.get_connected_port(),
		'local': stream.get_local_port(),
		'method': method,
		'scheme': scheme,
		'version': version,
		'route': route,
		'path': path,
		'param': param,
		'data': null,
		'header': header,
		'length': bytes,
		'text': text.substr(0, 1000),
		'agent': header['user-agent'] if 'user-agent' in header else '',
		'referer': header['referer'] if 'referer' in header else '',
		'encoding': [],
		'format': [],
		'language': {
			'main': '',
			'dialect': '',
			'list': []
		}
	}
	text = ''
	if 'accept-encoding' in header:
		var encoding = []
		for encoding_name in header['accept-encoding'].split(','):
			encoding.append(encoding_name.strip_edges().to_lower())
		request['encoding'] = encoding
	if 'accept' in header:
		var format = []
		for format_type in header['accept'].split(','):
			format.append(format_type.split(';')[0].strip_edges().to_lower())
		request['format'] = format
	if 'accept-language' in header:
		var language_list = []
		var main = null
		var dialect = null
		for language in header['accept-language'].split(','):
			language = language.split(';')[0].strip_edges().to_lower()
			if len(language) == 2 and main == null:
				main = language
			elif len(language) == 5 and dialect == null:
				dialect = language
			language_list.append(language)
		request['language'] = {
			'main': main if main != null else 'en',
			'dialect': dialect if dialect != null else 'en-us',
			'list': language_list
		}
	client['request'] = request
	client['response'] = {
		'code': 200,
		'connection': 'close',
		'server': 'V O I D cloud',
		'site': 'https://voidsp.com',
		'text': '',
		'header': {},
		'cookie': {}
	}
	var response = client['response']
	
	if 'path' in server_param and server_param['path'] != null:
		var path_file = server_param['path'] + '/' + path
		if file_exists(path_file):
			var data = file_read(path_file, true)
			client['response']['code'] = 200
			client['response']['type'] = path_extension(path_file).to_lower()
			client['response']['text'] = data
			client['response']['length'] = len(data)
		else:
			client['response']['code'] = 404
	else:
		response['type'] = 'text'
		response['encode'] = 'utf-8'
		response['language'] = 'en'

	var code = response['code']
	var codes = data['settings']['http']['code']
	var code_description = (' ' + codes[code]) if code in codes else ''
	
	var content_types = data['settings']['http']['type']
	var content_type = response['type'] if 'type' in response else 'text'
	if content_type in content_types:
		content_type = content_types[content_type]

	var encode = ';charset=' + response['encode'].to_upper() if 'encode' in response else ''

	text = response['text']
	var length = len(text) if 'length' not in response else response['length']
	
	var response_list = [
		'HTTP/1.1 ' + str(code) + code_description,
		'Server: ' + str(response['server']),
		'Site: ' + str(response['site']),
		'Connection: ' + response['connection'],
		'Content-Length: ' + str(length),
		'Content-Type: ' + content_type + encode,
		]

	if 'language' in response:
		response_list.append('Content-Language: ' + response['language'])

	var compress = data['settings']['http']['compress']
	if compress['enable'] and len(text) > compress['min'] and content_type in compress['type']:
		if 'gzip' in request['encoding']:
			text = gzip_encode(text, false)
			response_list.append('Content-Encoding: gzip')
		elif 'deflate' in request['encoding']:
			text = gzip_encode(text, true)
			response_list.append('Content-Encoding: deflate')

	header = response['header']
	for header_name in header:
		response_list.append(str(header_name) + ': ' + str(header[header_name]))

	response_list += ['Stopwatch: ' + str(Time.get_ticks_msec() - client['time']), '', '']

	if typeof(text) == TYPE_STRING:
		text = ('\n'.join(response_list) + '\n\n' + text).to_utf8_buffer()
	else:
		text = '\n'.join(response_list).to_utf8_buffer() + text

	d('server.request', client['request'])
	d('server.response', client['response'])

	stream.put_data(text)
	stream.disconnect_from_host()

func server_http(params = null):
	var params_checked = {
		'port': param_int(params, 'port', 80),
		'address': param_str(params, 'address', '*'),
		'path': param_str(params, 'path')
	}
	server(params_checked['port'], params_checked['address'])
	vars['cloud']['param'] = params_checked
	
# Random

func random_change():
	vars['random'].randomize()

func random_seed(seed = null):
	if seed == null:
		return vars['random'].seed
	vars['random'].seed = hash(seed if typeof(seed) == TYPE_INT else hash(str(seed)))
	vars['random'].state = 0

func random(to = 1.0, from = 0.0):
	if to is int:
		return vars['random'].randi_range(from, to)
	return vars['random'].randf_range(from, to)

# Crypto

## HASH

func hash(length: int = 64, symbols = null):
	var result = ""
	var symbols_line = ""
	if typeof(symbols) == TYPE_STRING:
		symbols_line = symbols
	else:
		for name in symbols if typeof(symbols) == TYPE_ARRAY else ["lower", "upper", "number"]:
			symbols_line += self.data['text']['void']['hash'][name]
	var symbols_length = symbols_line.length() - 1
	for index in range(0, length):
		result += symbols_line[random(0, symbols_length)]
	return result

func hash_number(text: String):
	return hash(text)

## RSA

func rsa_encode(data, key_data: String = '', domain: String = 'domain.com', company: String = 'Company'):
	var crypto = Crypto.new()
	var key = CryptoKey.new()
	var cert = X509Certificate.new()
	if key_data == '':
		key = crypto.generate_rsa(4096)
	else:
		key.load_from_string(key_data)
	if typeof(data) != TYPE_PACKED_BYTE_ARRAY:
		data = str(data).to_utf8_buffer()
	return {
		'key': key.save_to_string(),
		'data': crypto.encrypt(key, data),
		'signature': crypto.sign(HashingContext.HASH_SHA256, data.get_string_from_utf8().sha256_buffer(), key),
		'certificate': crypto.generate_self_signed_certificate(key, "CN=" + domain + ",O=" + company).save_to_string()
	}

func rsa_decode(data, key_data: String, data_type: bool = false):
	var crypto = Crypto.new()
	var key = CryptoKey.new()
	key.load_from_string(key_data)
	var decrypted = crypto.decrypt(key, data)
	return decrypted if data_type else decrypted.get_string_from_utf8()

func rsa_check(data, key_data: String, signature: String):
	var crypto = Crypto.new()
	var key = CryptoKey.new()
	key.load_from_string(key_data)
	var sha256 = data.sha256_buffer() if typeof(data) == TYPE_STRING else data.get_string_from_utf8().sha256_buffer()
	return crypto.verify(HashingContext.HASH_SHA256, sha256, signature.to_utf8_buffer(), key)

## MD5

func md5(text: String):
	return text.md5_text()

## UUID

func uuid():
	return vars['uuid'].v4()

## SHA1

func sha1(text: String):
	return text.sha1_text()

## SHA 256

func sha256(text: String):
	return text.sha256_text()

## SHA 512

func sha512(text: String):
	if (os_windows()):
		var name = 'hash'
		var cmd = 'echo|set /p="' + text + '" > %TMP%\\' + name + '|certutil -hashfile %TMP%\\' + name + ' SHA512|findstr /v "hash" & del %TMP%\\' + name
		var result = shell(cmd)
		return result['text'] if result['code'] == 0 else null

## CRC32

func crc32(text):
	var table = [
	0x00000000, 0x77073096, 0xEE0E612C, 0x990951BA, 0x076DC419, 0x706AF48F,
	0xE963A535, 0x9E6495A3, 0x0EDB8832, 0x79DCB8A4, 0xE0D5E91E, 0x97D2D988,
	0x09B64C2B, 0x7EB17CBD, 0xE7B82D07, 0x90BF1D91, 0x1DB71064, 0x6AB020F2,
	0xF3B97148, 0x84BE41DE, 0x1ADAD47D, 0x6DDDE4EB, 0xF4D4B551, 0x83D385C7,
	0x136C9856, 0x646BA8C0, 0xFD62F97A, 0x8A65C9EC, 0x14015C4F, 0x63066CD9,
	0xFA0F3D63, 0x8D080DF5, 0x3B6E20C8, 0x4C69105E, 0xD56041E4, 0xA2677172,
	0x3C03E4D1, 0x4B04D447, 0xD20D85FD, 0xA50AB56B, 0x35B5A8FA, 0x42B2986C,
	0xDBBBC9D6, 0xACBCF940, 0x32D86CE3, 0x45DF5C75, 0xDCD60DCF, 0xABD13D59,
	0x26D930AC, 0x51DE003A, 0xC8D75180, 0xBFD06116, 0x21B4F4B5, 0x56B3C423,
	0xCFBA9599, 0xB8BDA50F, 0x2802B89E, 0x5F058808, 0xC60CD9B2, 0xB10BE924,
	0x2F6F7C87, 0x58684C11, 0xC1611DAB, 0xB6662D3D, 0x76DC4190, 0x01DB7106,
	0x98D220BC, 0xEFD5102A, 0x71B18589, 0x06B6B51F, 0x9FBFE4A5, 0xE8B8D433,
	0x7807C9A2, 0x0F00F934, 0x9609A88E, 0xE10E9818, 0x7F6A0DBB, 0x086D3D2D,
	0x91646C97, 0xE6635C01, 0x6B6B51F4, 0x1C6C6162, 0x856530D8, 0xF262004E,
	0x6C0695ED, 0x1B01A57B, 0x8208F4C1, 0xF50FC457, 0x65B0D9C6, 0x12B7E950,
	0x8BBEB8EA, 0xFCB9887C, 0x62DD1DDF, 0x15DA2D49, 0x8CD37CF3, 0xFBD44C65,
	0x4DB26158, 0x3AB551CE, 0xA3BC0074, 0xD4BB30E2, 0x4ADFA541, 0x3DD895D7,
	0xA4D1C46D, 0xD3D6F4FB, 0x4369E96A, 0x346ED9FC, 0xAD678846, 0xDA60B8D0,
	0x44042D73, 0x33031DE5, 0xAA0A4C5F, 0xDD0D7CC9, 0x5005713C, 0x270241AA,
	0xBE0B1010, 0xC90C2086, 0x5768B525, 0x206F85B3, 0xB966D409, 0xCE61E49F,
	0x5EDEF90E, 0x29D9C998, 0xB0D09822, 0xC7D7A8B4, 0x59B33D17, 0x2EB40D81,
	0xB7BD5C3B, 0xC0BA6CAD, 0xEDB88320, 0x9ABFB3B6, 0x03B6E20C, 0x74B1D29A,
	0xEAD54739, 0x9DD277AF, 0x04DB2615, 0x73DC1683, 0xE3630B12, 0x94643B84,
	0x0D6D6A3E, 0x7A6A5AA8, 0xE40ECF0B, 0x9309FF9D, 0x0A00AE27, 0x7D079EB1,
	0xF00F9344, 0x8708A3D2, 0x1E01F268, 0x6906C2FE, 0xF762575D, 0x806567CB,
	0x196C3671, 0x6E6B06E7, 0xFED41B76, 0x89D32BE0, 0x10DA7A5A, 0x67DD4ACC,
	0xF9B9DF6F, 0x8EBEEFF9, 0x17B7BE43, 0x60B08ED5, 0xD6D6A3E8, 0xA1D1937E,
	0x38D8C2C4, 0x4FDFF252, 0xD1BB67F1, 0xA6BC5767, 0x3FB506DD, 0x48B2364B,
	0xD80D2BDA, 0xAF0A1B4C, 0x36034AF6, 0x41047A60, 0xDF60EFC3, 0xA867DF55,
	0x316E8EEF, 0x4669BE79, 0xCB61B38C, 0xBC66831A, 0x256FD2A0, 0x5268E236,
	0xCC0C7795, 0xBB0B4703, 0x220216B9, 0x5505262F, 0xC5BA3BBE, 0xB2BD0B28,
	0x2BB45A92, 0x5CB36A04, 0xC2D7FFA7, 0xB5D0CF31, 0x2CD99E8B, 0x5BDEAE1D,
	0x9B64C2B0, 0xEC63F226, 0x756AA39C, 0x026D930A, 0x9C0906A9, 0xEB0E363F,
	0x72076785, 0x05005713, 0x95BF4A82, 0xE2B87A14, 0x7BB12BAE, 0x0CB61B38,
	0x92D28E9B, 0xE5D5BE0D, 0x7CDCEFB7, 0x0BDBDF21, 0x86D3D2D4, 0xF1D4E242,
	0x68DDB3F8, 0x1FDA836E, 0x81BE16CD, 0xF6B9265B, 0x6FB077E1, 0x18B74777,
	0x88085AE6, 0xFF0F6A70, 0x66063BCA, 0x11010B5C, 0x8F659EFF, 0xF862AE69,
	0x616BFFD3, 0x166CCF45, 0xA00AE278, 0xD70DD2EE, 0x4E048354, 0x3903B3C2,
	0xA7672661, 0xD06016F7, 0x4969474D, 0x3E6E77DB, 0xAED16A4A, 0xD9D65ADC,
	0x40DF0B66, 0x37D83BF0, 0xA9BCAE53, 0xDEBB9EC5, 0x47B2CF7F, 0x30B5FFE9,
	0xBDBDF21C, 0xCABAC28A, 0x53B39330, 0x24B4A3A6, 0xBAD03605, 0xCDD70693,
	0x54DE5729, 0x23D967BF, 0xB3667A2E, 0xC4614AB8, 0x5D681B02, 0x2A6F2B94,
	0xB40BBE37, 0xC30C8EA1, 0x5A05DF1B, 0x2D02EF8D]
	var crc = 0 ^ (-1)
	text = text.to_utf8_buffer()
	for i in range(len(text)):
		crc = ((crc >> 8) & 0x00FFFFFF) ^ table[(crc ^ text[i]) & 0xFF]
	crc = crc ^ (-1)
	# Signed to unsigned
	if (crc < 0):
		crc += 4294967296
	return crc

## Gzip

func gzip_encode(text: String, deflate: bool = true):
	var gzip = StreamPeerGZIP.new()
	gzip.start_compression(deflate)
	gzip.put_data(text.to_utf8_buffer())
	gzip.finish()
	return gzip.get_data(gzip.get_available_bytes())[1]

func gzip_decode(data, deflate: bool = true):
	var gzip = StreamPeerGZIP.new()
	gzip.start_decompression(deflate)
	gzip.put_data(data)
	gzip.finish()
	return gzip.get_utf8_string(gzip.get_available_bytes())

## Base64
func base64_encode(text):
	if typeof(text) == TYPE_PACKED_BYTE_ARRAY:
		return Marshalls.raw_to_base64(text)
	return Marshalls.utf8_to_base64(text)

func base64_decode(text):
	return Marshalls.base64_to_utf8(text)

# OS

func os_windows() -> bool:
	return data['settings']['os']['type'] == 'windows'

func os_linux() -> bool:
	return data['settings']['os']['type'] == 'linux'

func os_mac() -> bool:
	return data['settings']['os']['type'] == 'mac'

func os_android() -> bool:
	return data['settings']['os']['type'] == 'android'

func os_ios() -> bool:
	return data['settings']['os']['type'] == 'ios'

func os_mobile() -> bool:
	return data['settings']['os']['type'] in ['android', 'ios']

func os_web() -> bool:
	return data['settings']['os']['type'] == 'web'
 
# DB

# Performance

func fps():
	return Engine.get_frames_per_second()

# Memory

static func memory():
	var data = OS.get_memory_info()
	return {
		"total": data["physical"],
		"free": data["free"],
		"used": OS.get_static_memory_usage(),
		"available": data["available"],
		"stack": data["stack"]
	}

# Window

func window_fullscreen(state = null):
	if state == null:
		state = DisplayServer.window_get_mode() == DisplayServer.WINDOW_MODE_WINDOWED
	DisplayServer.window_set_mode(DisplayServer.WINDOW_MODE_FULLSCREEN if bool(state) else DisplayServer.WINDOW_MODE_WINDOWED)

func window_size(size = null):
	if size == null:
		return get_tree().get_root().get_window().size
	else:
		get_tree().get_root().get_window().size = size

func window_size_max(size = null):
	if size == null:
		return get_tree().get_root().get_window().max_size
	else:
		get_tree().get_root().get_window().max_size = size

func window_size_min(size = null):
	if size == null:
		return get_tree().get_root().get_window().min_size
	else:
		get_tree().get_root().get_window().min_size = size

func window_position(position = null):
	if position == null:
		return get_tree().get_root().get_window().position
	else:
		get_tree().get_root().get_window().position = position

func window_position_initial(position: String):
	var window = get_tree().get_root().get_window()
	match position.to_lower():
		'absolute': window.initial_position = Window.WindowInitialPosition.WINDOW_INITIAL_POSITION_ABSOLUTE
		'primary': window.initial_position = Window.WindowInitialPosition.WINDOW_INITIAL_POSITION_CENTER_PRIMARY_SCREEN
		'main': window.initial_position = Window.WindowInitialPosition.WINDOW_INITIAL_POSITION_CENTER_MAIN_WINDOW_SCREEN
		'other': window.initial_position = Window.WindowInitialPosition.WINDOW_INITIAL_POSITION_CENTER_OTHER_SCREEN
		'mouse': window.initial_position = Window.WindowInitialPosition.WINDOW_INITIAL_POSITION_CENTER_SCREEN_WITH_MOUSE_FOCUS
		'keyboard': window.initial_position = Window.WindowInitialPosition.WINDOW_INITIAL_POSITION_CENTER_SCREEN_WITH_KEYBOARD_FOCUS

func window_direction(direction: String):
	var window = get_tree().get_root().get_window()
	match direction.to_lower():
		'parent': window.initial_position = Window.LayoutDirection.LAYOUT_DIRECTION_INHERITED
		'locale': window.initial_position = Window.LayoutDirection.LAYOUT_DIRECTION_LOCALE
		'left': window.initial_position = Window.LayoutDirection.LAYOUT_DIRECTION_LTR
		'right': window.initial_position = Window.LayoutDirection.LAYOUT_DIRECTION_RTL

func window_title(title: String):
	DisplayServer.window_set_title(title)

func window_icon(path: String):
	var extension = path_extension(path).to_lower()
	if extension in ['png', 'jpg', 'jpeg', 'webp', 'bmp']:
		var image_data = image(file_read(path, true), extension)
		DisplayServer.set_icon(image_data)
	elif extension in ['ico', 'icns']:
		DisplayServer.set_native_icon(extension)

func windows_ontop(state: bool = false):
	get_tree().get_root().get_window().always_on_top = state

func window_borderless(state: bool = false):
	get_tree().get_root().get_window().borderless = state

func window_show():
	get_tree().get_root().get_window().show()

func window_hide():
	get_tree().get_root().get_window().hide()

func window_attention():
	get_tree().get_root().get_window().request_attention()

func window_foreground():
	get_tree().get_root().get_window().move_to_foreground()

func window_center():
	get_tree().get_root().get_window().move_to_center()

func window_focus():
	get_tree().get_root().get_window().grab_focus()

func window_focus_has() -> bool:
	return get_tree().get_root().get_window().has_focus()

func window_visible(state: bool = true):
	get_tree().get_root().get_window().set_visible(state)

func window_unfocusable(state: bool):
	get_tree().get_root().get_window().unfocusable = state

func window_unresizable(state: bool):
	get_tree().get_root().get_window().unresizable = state

func window_scale(mode: String = 'canvas', aspect: String = 'keep', stretch: String = 'fractional'):
	var window = get_tree().get_root().get_window()
	match mode.to_lower():
		'disabled':
			window.set_content_scale_mode(Window.ContentScaleMode.CONTENT_SCALE_MODE_DISABLED)
		'canvas':
			window.set_content_scale_mode(Window.ContentScaleMode.CONTENT_SCALE_MODE_CANVAS_ITEMS)
		'viewport':
			window.set_content_scale_mode(Window.ContentScaleMode.CONTENT_SCALE_MODE_VIEWPORT)
	match aspect.to_lower():
		'keep':
			window.set_content_scale_aspect(Window.ContentScaleAspect.CONTENT_SCALE_ASPECT_KEEP)
		'ignore':
			window.set_content_scale_aspect(Window.ContentScaleAspect.CONTENT_SCALE_ASPECT_IGNORE)
		'width':
			window.set_content_scale_aspect(Window.ContentScaleAspect.CONTENT_SCALE_ASPECT_KEEP_WIDTH)
		'height':
			window.set_content_scale_aspect(Window.ContentScaleAspect.CONTENT_SCALE_ASPECT_KEEP_HEIGHT)
		'expand':
			window.set_content_scale_aspect(Window.ContentScaleAspect.CONTENT_SCALE_ASPECT_EXPAND)
	match stretch.to_lower():
		'fractional':
			window.set_content_scale_stretch(Window.ContentScaleStretch.CONTENT_SCALE_STRETCH_FRACTIONAL)
		'integer':
			window.set_content_scale_stretch(Window.ContentScaleStretch.CONTENT_SCALE_STRETCH_INTEGER)

func window_mode(mode: String = ''):
	var window = get_tree().get_root().get_window()
	if mode == '':
		match window.get_mode():
			Window.Mode.MODE_WINDOWED: return 'windowed'
			Window.Mode.MODE_MINIMIZED: return 'minimized'
			Window.Mode.MODE_MAXIMIZED: return 'maximized'
			Window.Mode.MODE_FULLSCREEN: return 'fullscreen'
			Window.Mode.MODE_EXCLUSIVE_FULLSCREEN: return 'exclusive'
	else:
		match mode.to_lower():
			'windowed': window.set_mode(Window.Mode.MODE_WINDOWED)
			'minimized': window.set_mode(Window.Mode.MODE_MINIMIZED)
			'maximized': window.set_mode(Window.Mode.MODE_MAXIMIZED)
			'fullscreen': window.set_mode(Window.Mode.MODE_FULLSCREEN)
			'exclusive': window.set_mode(Window.Mode.MODE_EXCLUSIVE_FULLSCREEN)

func window_exclusive(state: bool = true):
	get_tree().get_root().get_window().set_exclusive(state)

func window_vsync(state: bool = true):
	DisplayServer.window_set_vsync_mode(DisplayServer.VSyncMode.VSYNC_ENABLED if state else DisplayServer.VSyncMode.VSYNC_DISABLED)

func window_fps(fps: int):
	Engine.max_fps = fps

func window_list():
	return DisplayServer.get_window_list()

func window_screen(screen: int, window: int = 0):
	DisplayServer.window_set_current_screen(screen, window)

func window_screen_count() -> int:
	return DisplayServer.get_screen_count()

func window_screen_primary():
	return DisplayServer.get_primary_screen()

func window_screen_current(window: int = 0):
	DisplayServer.window_get_current_screen(window)

func window_cutouts():
	return DisplayServer.get_display_cutouts()

func window_safearea():
	return DisplayServer.get_display_safe_area()

func window_dpi(screen: int = -1):
	return DisplayServer.screen_get_dpi(screen)

func window_orienatation(screen: int = -1):
	return DisplayServer.screen_get_orientation(screen)

func window_darkmode() -> bool:
	return DisplayServer.is_dark_mode()

func window_darkmode_supported() -> bool:
	return DisplayServer.is_dark_mode_supported()

func window_tuchscreen_supported() -> bool:
	return DisplayServer.is_touchscreen_available()

func window_dropfiles(window: int = 0):
	DisplayServer.window_set_drop_files_callback(window_dropfiles_callback, window)

func window_dropfiles_callback(files: Array):
	print(files)
	pass

func window_resize():
	var size = window_size()
	var scale = float(size.x) / float(vars['size_original'].x)
	var debug = get_node("/root/main/debug")
	var font_size = int(60 * scale)
	if font_size > 60:
		font_size = 60
	elif font_size < 20:
		font_size = 20
	get_node("/root/main/bg").size = size
	debug.size = size
	debug.set("theme_override_font_sizes/font_size",  font_size)
	for ui in data['ui']:
		ui_redraw(ui)

# Screen

func screen_name() -> String:
	return DisplayServer.get_name()

func screen_always(state: bool = true):
	DisplayServer.screen_set_keep_on(state)

func screen_always_has() -> bool:
	return DisplayServer.screen_is_kept_on()

func screen_pixel(x: int, y: int):
	return DisplayServer.screen_get_pixel(Vector2i(x, y))

func screen_refresh_rate(screen: int = -1):
	return DisplayServer.screen_get_refresh_rate(screen)

func screen_orientation(orientation: String, screen: int = -1):
	orientation = orientation.to_lower()
	if orientation in vars['orientation']:
		DisplayServer.screen_set_orientation(vars['orientation'][orientation], screen)

func screen_orientation_current(screen: int = -1) -> String:
	var current = DisplayServer.screen_get_orientation(screen)
	for orientation in vars['orientation']:
		if vars['orientation'][orientation] == current:
			return orientation
	return ''

func screen_feature(feature: String = '') -> bool:
	feature = feature.to_lower()
	if feature in vars['feature']:
		return DisplayServer.has_feature(vars['feature'][feature])
	return false

# Clipboard

func clipboard(data = null, primary: bool = false):
	if data == null:
		if DisplayServer.clipboard_has_image():
			return DisplayServer.clipboard_get_image()
		if not primary:
			return DisplayServer.clipboard_get()
		return DisplayServer.clipboard_get_primary()
	if not primary:
		DisplayServer.clipboard_set(str(data))
	else:
		DisplayServer.clipboard_set_primary(str(data))

func clipboard_type():
	if DisplayServer.clipboard_has_image():
		return 'image'
	if DisplayServer.clipboard_has():
		return 'text'
	return null

# Cursor

func cursor_set(shape: String, image = null, point = null):
	shape = shape.to_lower()
	if shape in vars['cursor']:
		if image == null:
			DisplayServer.cursor_set_shape(vars['cursor'][shape])
		else:
			DisplayServer.cursor_set_custom_image(image, vars['cursor'][shape], point)

func cursor_get():
	var shape = DisplayServer.cursor_get_shape()
	for name in vars['cursor']:
		if vars['cursor'][name] == shape:
			return name

# Dialog

func dialog(title: String, description: String, buttons: Array):
	return DisplayServer.dialog_show(title, description, buttons, dialog_callback)

func dialog_text(title: String, description: String, value: String = ''):
	return DisplayServer.dialog_input_text(title, description, value, dialog_callback)

func dialog_file(title: String, dir: String, filename: String, mode: String):
	mode = mode.to_lower()
	var mode_value = vars['file dialog'][mode] if mode in vars['file dialog'] else DisplayServer.FileDialogMode.FILE_DIALOG_MODE_OPEN_FILE 
	return DisplayServer.file_dialog_show(title, dir, filename, true, mode_value, [], dialog_callback)

func dialog_callback():
	pass

# Text to Speech

func say(text: String, voice: String = '', volume: int = 50, pitch: float = 1.0, rate: float = 1.0, interrupt: bool = true):
	if voice == '':
		var voices = say_voices()
		if len(voices) == 0:
			return
		voice = voices[0]['id']
	DisplayServer.tts_speak(text, voice, volume, pitch, rate, 0, interrupt)

func say_voices(language: String = '') -> Array:
	if language == '':
		return DisplayServer.tts_get_voices()
	language = language.to_lower()
	return DisplayServer.tts_get_voices_for_language(language)

func say_stop():
	DisplayServer.tts_stop()

func say_pause():
	DisplayServer.tts_pause()
	
func say_resume():
	DisplayServer.tts_resume()

func say_pause_is() -> bool:
	return DisplayServer.tts_is_paused()

func say_speak_is() -> bool:
	return DisplayServer.tts_is_speaking()

# Input

## Keyboard

func key_bind(key: String, action: Array = []):
	var name = key.to_lower()
	if name in vars['key']:
		key = vars['key'][name]
	data['key']['bind'][key] = action

func key_disable(key: String):
	var name = key.to_lower()
	if name in vars['key']:
		key = vars['key'][name]
	data['key']['disable'].append(key)

func key_enable(key: String):
	var name = key.to_lower()
	if name in vars['key']:
		key = vars['key'][name]
	data['key']['disable'].erase(key)

func key_remove(key: String):
	data['key'].erase(key)

func ime_selection() -> Vector2i:
	return DisplayServer.ime_get_selection()

func ime_text() -> String:
	return DisplayServer.ime_get_text()

func keyboard_screen() -> int:
	return DisplayServer.get_keyboard_focus_screen()

func keyboard_layout() -> int:
	return DisplayServer.keyboard_get_current_layout()

func keyboard_layout_count() -> int:
	return DisplayServer.keyboard_get_layout_count()

func keyboard_layout_language(index: int) -> String:
	return DisplayServer.keyboard_get_layout_language(index)

func keyboard_layout_name(index: int) -> String:
	return DisplayServer.keyboard_get_layout_name(index)

func keyboard_layout_current_set(index: int):
	DisplayServer.keyboard_set_current_layout(index)

func keyboard_virtual_height() -> int:
	return DisplayServer.virtual_keyboard_get_height()

func keyboard_virtual_show(text: String = '', position:Rect2 = Rect2(0, 0, 0, 0), type: DisplayServer.VirtualKeyboardType = 0, max_length: int = -1, cursor_start: int = -1, cursor_end: int = -1):
	DisplayServer.virtual_keyboard_show(text, position, type, max_length, cursor_start, cursor_end)

func keyboard_virtual_hide():
	DisplayServer.virtual_keyboard_hide()

## Mouse

func mouse_show(show: bool = true):
	Input.set_mouse_mode(Input.MOUSE_MODE_VISIBLE if show else Input.MOUSE_MODE_HIDDEN)

func mouse_lock(lock: bool = true):
	Input.set_mouse_mode(Input.MOUSE_MODE_CAPTURED if lock else Input.MOUSE_MODE_CONFINED)

func mouse_position_set(x: int, y: int):
	DisplayServer.warp_mouse(Vector2i(x, y))

func mouse_position_get() -> Vector2i:
	return DisplayServer.mouse_get_position()

func mouse_mode_get() -> String:
	var mode = DisplayServer.mouse_get_mode()
	for name in vars['mouse mode']:
		if vars['mouse mode'][name] == mode:
			return name
	return ''

func mouse_mode_set(mode: String):
	mode = mode.to_lower()
	if mode in vars['mouse mode']:
		DisplayServer.mouse_set_mode(vars['mouse mode'][mode])

func mouse_button():
	var state = DisplayServer.mouse_get_button_state()
	return {
		'left': state & MouseButtonMask.MOUSE_BUTTON_MASK_LEFT > 0,
		'right': state & MouseButtonMask.MOUSE_BUTTON_MASK_RIGHT > 0,
		'middle': state & MouseButtonMask.MOUSE_BUTTON_MASK_MIDDLE > 0,
		'extra 1': state & MouseButtonMask.MOUSE_BUTTON_MASK_MB_XBUTTON1 > 0,
		'extra 2': state & MouseButtonMask.MOUSE_BUTTON_MASK_MB_XBUTTON2 > 0
	}

## Gamepad

# Effect

func effect_add(effect: Dictionary):
	var time = timestamp()
	match effect['type']:
		'ticker':
			var size = effect['text'].length()
			if size > 0:
				effect.merge({
					'start': time,
					'last': 0,
					'index': 0,
					'size': size
				})
			else:
				return
		_:
			return
	effect['skip'] = false
	vars['effect'][effect['name']] = effect

func effect_remove(name: String):
	vars['effect'].erase(name)

# Game

func game(data = null):
	if data == null:
		action(self.data['game'])
	elif typeof(data) == TYPE_ARRAY:
		self.data['game'] = data

## Visual Novel

func vn(data):
	if data == null:
		self.data['vn']['show'] = not self.data['vn']['show']
		if self.data['vn']['show']:
			ui_show('vn')
		else:
			ui_hide('vn')
	elif typeof(data) != TYPE_DICTIONARY:
		self.data['vn']['show'] = bool(data)
		if self.data['vn']['show']:
			ui_show('vn')
		else:
			ui_hide('vn')
	else:
		var image = param_dict(data, 'image')
		var text = param_dict(data, 'text')
		var button = param_dict(data, 'button')
		var character = param_dict(data, 'character')
		image['name'] = 'vn.image'
		image['hide'] = true
		text['name'] = 'vn.text'
		text['speed'] = param_float(text, 'speed', 0.01)
		text['multiline'] = true
		text['hide'] = true
		ui_add('image', image)
		ui_add('text', text)
		self.data['vn'] = {
			'show': false,
			'text': text,
			'image': image,
			'button': button,
			'character': character,
			'route': {
				'selected': ["Route 2"],
				'list': [],
				'current': null
			}
		}

func vn_say(text: String, character = null):
	var node = vars['content'].get_node('vn_text')
	var vn = data['vn']
	if character != null and character in vn['character']:
		node.set('theme_override_colors/default_color', vn['character'][character]['text']['color'])
	else:
		node.set('theme_override_colors/default_color', vn['text']['color'])
	node.text = ''
	effect_add({
		'name': 'vn.say',
		'type': 'ticker',
		'text': text,
		'speed': vn['text']['speed'],
		'node': node
	})
	vn(true)

func vn_skip(next: bool = false):
	if not data['vn']['show']:
		return
	var name = 'vn.say'
	var end = false 
	if name in vars['effect']:
		var effect = vars['effect'][name]
		effect['node'].text = effect['text']
		vars['effect'].erase(name)
	else:
		end = true
	if next or end:
		vars['content'].get_node('vn_text').text = ''
		action_continue('vn.say')

func vn_route(routes: Array):
	var vn = data['vn']
	var vn_route = vn['route']
	vn_route['current'] = null
	vn_route['list'] = routes
	var count = routes.size()
	var x = vn['text']['position'][0]
	var y_start = float(vn['text']['position'][1].replace('%', ''))
	var y_factor = float(vn['text']['height'].replace('%', '')) / count
	var height = str(0.7 * y_factor) + '%'
	var index = 0
	for route in routes:
		var button = vn['button'].duplicate()
		var text = route[0]
		var y = y_start + index * y_factor
		button['name'] = 'vn_route_' + str(index)
		button['text'] = text
		button['position'] = [x, str(y) + '%']
		button['height'] = height
		button['action'] = [['vn.current', text]] + route[1] + [['vn.continue']]
		button['alignment'] = 'left'
		var action = [["button", button]]
		if index == count - 1:
			action.append(['ui.enable', 'vn'])
		self.action([
			['timer', index * 0.3 + 0.1, action, 'vn_route_' + str(index)]
		])
		index += 1
	ui_disable('vn')
	vn(true)

func vn_route_remove(name: String = ''):
	var vn_route = data['vn']['route']
	var list = vn_route['list']
	if name == '':
		name = vn_route['current']
	for index in range(list.size()):
		if list[index][0] == str(name):
			list.remove_at(index)
			return

func vn_route_check(name, action_found: Array, action_notfound: Array = []):
	var select = name
	if typeof(select) != TYPE_ARRAY:
		select = [select]
	var vn_route = data['vn']['route'] 
	var selected = vn_route['selected']
	var count = 0
	for select_name in select:
		if select_name in selected:
			count += 1
	if count == select.size():
		action(action_found + [["vn.continue", "vn.check"]])
	elif action_notfound.size() > 0:
		action(action_notfound + [["vn.continue", "vn.check"]])

func vn_route_check_all(routes: Array):
	var selected = data['vn']['route']['selected']
	for route in routes:
		var name = route[0]
		var action = route[1]
		if name in selected:
			action(action + [['action.continue', 'vn.check']])
			return
	action_continue('vn.check')

func vn_route_current(name: String):
	data['vn']['route']['current'] = name
	ui_remove('vn_route')
	timer_remove('vn_route')

func vn_route_select(name: String):
	if name != '' and name not in data['vn']['route']['selected']:
		data['vn']['route']['selected'].append(name)

func vn_route_repeat():
	if data['vn']['route']['list'].size() > 0:
		vn_route(data['vn']['route']['list'])

func vn_route_continue():
	if data['vn']['route']['current'] != null:
		vn_route_select(data['vn']['route']['current'])
		data['vn']['route']['current'] = null
		action_continue('vn.route')

func vn_char(char: Dictionary):
	pass

func vn_come(char: String, effect = null):
	pass

func vn_leave(char: String, effect = null):
	pass

func vn_reset():
	action_clear('vn.say')
	action_clear('vn.check')
	action_clear('vn.route')
	ui_hide('vn')
	var vn = data['vn']
	vn['show'] = false
	vn['route'] = {
		'list': [],
		'selected': [],
		'current': null
	}
	ui_remove('vn_route')
	timer_remove('vn_route')
	vars['content'].get_node('vn_text').text = ''

## 2D

func d2_move(name: String, delta: float):
	var node = get_node('/root/main/content/' + name)
	

## 3D

# Effect

# UI

func ui(name: String):
	for ui in data['ui']:
		if ui['name'] == name:
			return ui

func ui_redraw(ui: Dictionary):
	var node = vars['content'].get_node(ui['name'])
	if node == null:
		return
	var size = get_tree().get_root().get_window().size
	var center = [false, false, 0, 0]
	var width = 0
	var height = 0
	for name in ui:
		var value = ui[name]
		match name:
			'position':
				var x = value[0]
				var y = value[1]
				if typeof(x) == TYPE_STRING:
					if x != 'center':
						x = ceil(size.x * float(x.rstrip('%')) / 100.0)
					else:
						x = 0
						center[0] = true
				elif x == null:
					x = size.x
				if x < 0:
					x = size.x + x
				if typeof(y) == TYPE_STRING:
					if y != 'center':
						y = ceil(size.y * float(y.rstrip('%')) / 100.0)
					else:
						y = 0
						center[1] = true
				elif y == null:
					y = size.y
				if y < 0:
					y = size.y + y
				node.position = Vector2i(x, y)
			'scale':
				node.scale = Vector2i(value[0], value[1])
			'size':
				width = value[0]
				height = value[1]
				if width == null:
					width = size.x
				elif typeof(width) == TYPE_STRING:
					width = ceil(size.x * float(width.rstrip('%')) / 100.0)
				if width < 0:
					width = size.x + width
				if height == null:
					height = size.y
				elif typeof(height) == TYPE_STRING:
					height = ceil(size.y * float(height.rstrip('%')) / 100.0)
				if height < 0:
					height = size.y + height
				node.size = Vector2i(width, height)
	if center[0]:
		node.position.x = int((size.x - width) / 2)
	if center[1]:
		node.position.y = int((size.y - height) / 2)

func ui_remove(name: String):
	var node = vars['content'].get_node(name)
	if node != null:
		node.queue_free()
	var index = 0
	var name_child = name + '_'
	for ui in data['ui'].duplicate():
		var ui_name = ui['name']
		if ui_name.begins_with(name_child):
			ui_remove(ui_name)
		elif ui_name == name:
			data['ui'].remove_at(index)
		index += 1

func ui_add(type: String, data: Dictionary):
	var node = null
	var ui = {
		'name': param_str(data, 'name', uuid()).replace('.', '_'),
		'opacity': param_percent(data, 'opacity', 1)
	}
	ui['size'] = [param(data, 'width'), param(data, 'height')]
	if 'position' not in data:
		var x = param_int(data, 'x', null)
		var y = param_int(data, 'y', null)
		ui['position'] = [x, y]
	else:
		ui['position'] = data['position']
	match type:
		'text':
			ui.merge({
				'name': param_str(data, 'name', uuid()),
				'text': param_str(data, 'text'),
				'multiline': param_bool(data, 'multiline', false),
				'font size': param_int(data, 'size', 80),
				'font name': param_file(data, 'font', data['font'] if 'font' in data else 'mono'),
				'font color': param_color(data, 'color'),
				'alignment': param_str(data, 'alignment', 'left')
			})
			var font = font_load(ui['font name'])
			var size = ui['font size']
			var alignment = self.alignment(ui['alignment'])
			if ui['multiline']:
				node = RichTextLabel.new()
				node.push_paragraph(alignment)
				node.push_font_size(size)
				node.set('theme_override_colors/default_color', ui['font color'])
				node.set('theme_override_fonts/normal_font', font)
				node.set('theme_override_font_sizes/normal_font_size', size)
				node.set('theme_override_font_sizes/bold_font_size', size)
				node.set('theme_override_font_sizes/italics_font_size', size)
				node.set('theme_override_font_sizes/bold_italics_font_size', size)
				node.set('theme_override_font_sizes/mono_font_size', size)
				node.set('theme_override_constants/outline_size', 0)
				node.text = ui['text']
			else:
				var settings = LabelSettings.new()
				settings.font = font
				settings.font_size = ui['font size']
				settings.font_color = ui['font color']
				node = Label.new()
				node.label_settings = settings
				node.text = ui['text']
				node.horizontal_alignment = alignment
		'image':
			ui['path'] = param_file(data, 'path')
			var image = Image.new()
			image.load(ui['path'])
			node = TextureRect.new()
			node.texture = image_to_texture(image)
			node.stretch_mode = TextureRect.StretchMode.STRETCH_KEEP_ASPECT_COVERED
			node.expand_mode = TextureRect.ExpandMode.EXPAND_IGNORE_SIZE
		'button':
			node = Button.new()
			node.pressed.connect(self._button_pressed.bind(node))
			var border = param_dict(data, 'border')
			ui.merge({
				'name': param_str(data, 'name', uuid()),
				'text': param_str(data, 'text'),
				'action': param_array(data, 'action'),
				'font size': param_int(data, 'size', 40),
				'font name': param_file(data, 'font', data['font'] if 'font' in data else 'mono'),
				'font color': param_color(data, 'color'),
				'font color hover': param_color(data, 'font color hover', 'white'),
				'font color hover pressed': param_color(data, 'font color hover pressed', 'white'),
				'font color focus': param_color(data, 'font color focus', 'white'),
				'font color pressed': param_color(data, 'font color pressed', 'white'),
				'alignment': param_str(data, 'alignment', 'center'),
				'outline size': param_float(data, 'outline size', 0),
				'outline color': param_color(data, 'outline color'),
				'bg': param_color(data, 'bg', Color(0.5, 0.5, 0.5, 0.5)),
				'border width': param_int(border, 'width', 0),
				'border color': param_str(border, 'color', 'white'),
				'corner': param_int(data, 'corner')
			})
			node.set('theme_override_fonts/font', font_load(ui['font name']))
			node.set('theme_override_font_sizes/font_size', ui['font size'])
			node.set('theme_override_colors/font_color', ui['font color'])
			node.set('theme_override_colors/font_hover_color', ui['font color hover'])
			node.set('theme_override_colors/font_hover_pressed_color', ui['font color hover pressed'])
			node.set('theme_override_colors/font_focus_color', ui['font color focus'])
			node.set('theme_override_colors/font_pressed_color', ui['font color pressed'])
			node.set('theme_override_constants/outline_size', ui['outline size'])
			node.set('theme_override_colors/font_outline_color', ui['outline color'])
			var style = StyleBoxFlat.new()
			style.corner_radius_bottom_left = ui['corner']
			style.corner_radius_bottom_right = ui['corner']
			style.corner_radius_top_left = ui['corner']
			style.corner_radius_top_right = ui['corner']
			style.border_color = ui['border color']
			style.border_width_bottom = ui['border width']
			style.border_width_left = ui['border width']
			style.border_width_right = ui['border width']
			style.border_width_top = ui['border width']
			style.bg_color = ui['bg']
			node.set('theme_override_styles/normal', style)
			node.set('theme_override_styles/hover', style)
			node.set('theme_override_styles/pressed', style)
			node.set('theme_override_styles/focus', style)
			node.text = ui['text']
			node.alignment = self.alignment(ui['alignment'])
		'list':
			pass
		'tile':
			pass
		'switch':
			pass
		'slider':
			pass
		'progress':
			pass
		'3d':
			pass
		'2d':
			pass
		'video':
			pass
		'edit':
			pass
	if node != null:
		if param_bool(data, 'hide', false):
			node.hide()
		self.data['ui'].append(ui)
		node.name = ui['name']
		node.modulate.a = ui['opacity']
		vars['content'].add_child(node)
		ui_redraw(ui)

func ui_show(name: String):
	for node in vars['content'].get_children():
		if node.name == name or node.name.begins_with(name + '_'):
			node.show()

func ui_hide(name: String):
	for node in vars['content'].get_children():
		if node.name == name or node.name.begins_with(name + '_'):
			node.hide()

func ui_enable(name: String = ''):
	var node = vars['content'].get_node(name) if name != '' else vars['content']
	if node != null:
		node.set_process_input(true)
		node.set_input_pickable(true)

func ui_disable(name: String):
	var node = vars['content'].get_node(name)
	if node != null:
		node.set_process_input(false)
		node.set_input_pickable(false)

func ui_background(path = null):
	var bg: TextureRect = get_tree().get_root().get_node("main/bg")
	bg.texture = asset(path) if path != null else ImageTexture.new()

func ui_menu(data):
	if typeof(data) != TYPE_DICTIONARY:
		if typeof(data) == TYPE_BOOL:
			self.data['settings']['menu'] = data
		else:
			self.data['settings']['menu'] = not self.data['settings']['menu']
		if self.data['settings']['menu']:
			ui_show('menu')
		else:
			ui_hide('menu')
		return
	ui_remove('menu')
	var title = param_str(data, 'title')
	var size = param_int(data, 'size', 80)
	var color = param_str(data, 'color')
	var font = param_str(data, 'font', 'mono')
	var button_data = param_dict(data, 'button')
	var button_action = param_array(data, 'action')
	var button_size = param_int(button_data, 'size', 40)
	var button_font = param_str(button_data, 'font', font)
	var button_color = param_str(button_data, 'color', color)
	var button_bg = param_str(button_data, 'bg', '22222255')
	var button_corner = param_int(button_data, 'corner', 4)
	var button_width = param(button_data, 'width', '80%')
	var button_list = param_array(button_data, 'list')
	var border = param_dict(button_data, 'border')
	ui_add('text', {
		'name': 'menu.title',
		'text': title,
		'alignment': 'center',
		'position': [0, "10%"],
		'size': 80,
		'width': "100%",
		'height': 50,
		'color': color,
		'font': font,
		'action': button_action
	})
	var index = 0
	var button_top = 0.3
	var button_count = button_list.size()
	if button_count > 0:
		var button_height = 0
		var button_space = 0
		if button_count > 1:
			var button_space_factor = 0.18
			var button_height_total = 1 - button_top * 2
			button_space = (button_height_total * button_space_factor) / (button_count - 1)
			button_height = button_height_total / button_count
		else:
			button_height = button_top * 0.6
		for button in button_list:
			if typeof(button) != TYPE_ARRAY or button.size() < 2:
				continue
			var y = 'center' if button_count == 1 else str((button_top + index * (button_height + button_space)) * 100) + '%'
			var ui = { 
				'name': 'menu.button' + str(index),
				'text': button[0],
				'action': button[1],
				'font': button_font,
				'color': button_color,
				'bg': button_bg,
				'size': button_size,
				'corner': button_corner,
				'height': str(button_height * 100) + '%',
				'width': button_width,
				'position': ['center', y],
				'border': border
			}
			ui_add('button', ui)
			index += 1
	self.data['settings']['menu'] = true
