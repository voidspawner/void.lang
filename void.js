class void {

	static data = {
		'description': {
			'about': {
				'name': 'V O I D lang',
				'site': 'https://voidsp.com',
				'language': 'javascript',
				'version': {
					'time': 0,
					'date': ''
				}
			},
			'action': {
				'get': {
					'name': 'get',
					'group': 'value',
					'description': 'Retrieve a value based on provided parameter name',
					'safe': False,
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'param': [{'name': 'name', 'type': 'str', 'default': null}],
					'example': [
						{'code': [['get', 'description.about.name']], 'result': 'V O I D lang', 'test': False}
					] 
				},
				'set': {
					'name': 'set',
					'group': 'value',
					'description': 'Assign a value to a specified parameter',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'remove': {
					'name': 'remove',
					'group': 'value',
					'description': 'Remove a specified parameter or value',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'type': {
					'name': 'type',
					'group': 'value',
					'description': 'Determine the data type of a specified parameter',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'text': {
					'name': 'type_text',
					'group': 'value',
					'description': 'Specify a parameter as a text type',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'number': {
					'name': 'type_number',
					'group': 'value',
					'description': 'Specify a parameter as a number type',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'bool': {
					'name': 'type_bool',
					'group': 'value',
					'description': 'Specify a parameter as a boolean type',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'list': {
					'name': 'type_list',
					'group': 'value',
					'description': 'Specify a parameter as a list type',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'dict': {
					'name': 'type_dict',
					'group': 'value',
					'description': 'Specify a parameter as a dictionary type',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'binary': {
					'name': 'type_binary',
					'group': 'value',
					'description': 'Specify a parameter as a binary type',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'n': {
					'name': 'n',
					'group': 'value',
					'description': 'Gets the length of the text, the number of items in a list or dictionary',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'+': {
					'name': null,
					'group': 'expression',
					'description': 'Perform addition operation',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'-': {
					'name': null,
					'group': 'expression',
					'description': 'Perform subtraction operation',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'*': {
					'name': null,
					'group': 'expression',
					'description': 'Perform multiplication operation',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'/': {
					'name': null,
					'group': 'expression',
					'description': 'Perform division operation',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'%': {
					'name': null,
					'group': 'expression',
					'description': 'Perform modulo operation',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'~': {
					'name': null,
					'group': 'expression',
					'description': 'Elevation operator',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'!': {
					'name': null,
					'group': 'expression',
					'description': 'Perform logical negation',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'&': {
					'name': null,
					'group': 'expression',
					'description': 'Perform bitwise AND operation',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'|': {
					'name': null,
					'group': 'expression',
					'description': 'Perform bitwise OR operation',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'^': {
					'name': null,
					'group': 'expression',
					'description': 'Perform bitwise XOR operation',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'>>': {
					'name': null,
					'group': 'expression',
					'description': 'Perform right bitwise shift operation',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'<<': {
					'name': null,
					'group': 'expression',
					'description': 'Perform left bitwise shift operation',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'=': {
					'name': null,
					'group': 'expression',
					'description': 'Assign value to a variable',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'+=': {
					'name': null,
					'group': 'expression',
					'description': 'Add and assign value to a variable',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'=+': {
					'name': null,
					'group': 'expression',
					'description': 'Assign and add value to a variable',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'-=': {
					'name': null,
					'group': 'expression',
					'description': 'Subtract and assign value to a variable',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'*=': {
					'name': null,
					'group': 'expression',
					'description': 'Multiply and assign value to a variable',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'/=': {
					'name': null,
					'group': 'expression',
					'description': 'Divide and assign value to a variable',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'%=': {
					'name': null,
					'group': 'expression',
					'description': 'Modulo and assign value to a variable',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'~=': {
					'name': null,
					'group': 'expression',
					'description': 'Elevation and assign value to a variable',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'!=': {
					'name': null,
					'group': 'expression',
					'description': 'Check if values are not equal',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'&=': {
					'name': null,
					'group': 'expression',
					'description': 'Bitwise AND and assign value to a variable',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'|=': {
					'name': null,
					'group': 'expression',
					'description': 'Bitwise OR and assign value to a variable',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'^=': {
					'name': null,
					'group': 'expression',
					'description': 'Bitwise XOR and assign value to a variable',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'>>=': {
					'name': null,
					'group': 'expression',
					'description': 'Right shift and assign value to a variable',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'<<=': {
					'name': null,
					'group': 'expression',
					'description': 'Left shift and assign value to a variable',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'==': {
					'name': null,
					'group': 'expression',
					'description': 'Checks if left value is equal to right',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'>': {
					'name': null,
					'group': 'expression',
					'description': 'Checks if left value is greater than right',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'<': {
					'name': null,
					'group': 'expression',
					'description': 'Checks if left value is less than right',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'<=': {
					'name': null,
					'group': 'expression',
					'description': 'Checks if left value is less than or equal to right',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'>=': {
					'name': null,
					'group': 'expression',
					'description': 'Checks if left value is greater than or equal to right',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'not': {
					'name': null,
					'group': 'expression',
					'description': 'Logical NOT operation',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'and': {
					'name': null,
					'group': 'expression',
					'description': 'Logical AND operation',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'or': {
					'name': null,
					'group': 'expression',
					'description': 'Logical OR operation',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'xor': {
					'name': null,
					'group': 'expression',
					'description': 'Logical XOR operation',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'in': {
					'name': null,
					'group': 'expression',
					'description': 'Checks if value is in a list or name in a dictionary',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'not in': {
					'name': null,
					'group': 'expression',
					'description': 'Checks if value is not in a list or name not in a dictionary',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'.': {
					'name': 'print',
					'group': 'control',
					'description': 'Output data to the console',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'..': {
					'name': 'input',
					'group': 'control',
					'description': 'Input text from the user',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'?': {
					'name': 'condition',
					'group': 'control',
					'description': 'Evaluate a conditional expression',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'o': {
					'name': 'loop',
					'group': 'control',
					'description': 'Perform a loop operation',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'x': {
					'name': 'loop_break',
					'group': 'control',
					'description': 'Exit the current loop',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'->': {
					'name': 'loop_continue',
					'group': 'control',
					'description': 'Skip to the next iteration of the loop',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'<-': {
					'name': 'loop_repeat',
					'group': 'control',
					'description': 'Repeat the current iteration of the loop',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				':': {
					'name': 'action_return',
					'group': 'control',
					'description': 'Return a result from an action',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'action': {
					'name': 'action',
					'group': 'control',
					'description': 'Initiate or call an action',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'open': {
					'name': 'open',
					'group': 'control',
					'description': 'Open a link',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'code': {
					'name': 'code',
					'group': 'control',
					'description': 'Execute a block of native code',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'X': {
					'name': 'exit',
					'group': 'control',
					'description': 'Exit the current application',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'l': {
					'name': 'l',
					'group': 'control',
					'description': 'Log data',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'convert': {
					'name': 'convert',
					'group': 'control',
					'description': 'Convert data from one format to another',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'export': {
					'name': 'export',
					'group': 'control',
					'description': 'Export code to an application or game',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'update': {
					'name': 'update',
					'group': 'control',
					'description': 'Updating the language code',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'test': {
					'name': 'test',
					'group': 'control',
					'description': 'Test one or all actions',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [
						{'name': 'name', 'type': 'str', 'default': null}
					],
					'example': [
						{'code': [['test']], 'test': False},
						{'code': [['test', 'upper']]}
					]
				},
				'help': {
					'name': 'help',
					'group': 'control',
					'description': 'Show description and use of the action',
					'safe': True,
					'param': [
						{'name': 'name', 'type': 'str', 'default': null}
					],
					'example': [
						{'code': [['help']], 'test': False},
						{'code': [['help', 'upper']], 'test': False}
					]
				},
				'void': {
					'name': 'void',
					'group': 'control',
					'description': 'Perform a void action on the hash',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'lower': {
					'name': 'lower',
					'group': 'text',
					'description': 'Convert text to lowercase',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'upper': {
					'name': 'upper',
					'group': 'text',
					'description': 'Convert text to uppercase',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'starts': {
					'name': 'starts',
					'group': 'text',
					'description': 'Check if text starts with a specific substring',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'ends': {
					'name': 'ends',
					'group': 'text',
					'description': 'Check if text ends with a specific substring',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'strip': {
					'name': 'strip',
					'group': 'text',
					'description': 'Remove leading and trailing spaces from text',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'strip.start': {
					'name': 'strip_start',
					'group': 'text',
					'description': 'Remove leading spaces from text',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True, 
					'param': [],
					'example': []
				},
				'strip.end': {
					'name': 'strip_end',
					'group': 'text',
					'description': 'Remove trailing spaces from text',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'replace': {
					'name': 'replace',
					'group': 'text',
					'description': 'Replace occurrences of a substring within text',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'find': {
					'name': 'find',
					'group': 'text',
					'description': 'Locate a substring within text',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'parse': {
					'name': 'parse',
					'group': 'text',
					'description': 'Parse text into structured data',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'similar': {
					'name': 'similar',
					'group': 'text',
					'description': 'Find similarity between texts',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'part': {
					'name': 'part',
					'group': 'text',
					'description': 'Extract a part of the text',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'split': {
					'name': 'split',
					'group': 'text',
					'description': 'Split text into parts based on a delimiter',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'join': {
					'name': 'join',
					'group': 'text',
					'description': 'Join a list of strings into a single string with a delimiter',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'date': {
					'name': 'date',
					'group': 'text',
					'description': 'Format or parse date-related information',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'escape': {
					'name': 'escape',
					'group': 'text',
					'description': 'Escape special characters in a string',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'escape.html': {
					'name': 'escape_html',
					'group': 'text',
					'description': 'Escape HTML tags and attributes in a string',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'escape.url': {
					'name': 'escape_url',
					'group': 'text',
					'description': 'Escape URL components',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'escape.sql': {
					'name': 'escape_sql',
					'group': 'text',
					'description': 'Escape SQL query components to prevent injection',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'unescape': {
					'name': 'unescape',
					'group': 'text',
					'description': 'Unescape special characters in a string',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'unescape.html': {
					'name': 'unescape_html',
					'group': 'text',
					'description': 'Unescape HTML tags and attributes in a string',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'unescape.url': {
					'name': 'unescape_url',
					'group': 'text',
					'description': 'Unescape URL components',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'unescape.sql': {
					'name': 'unescape_sql',
					'group': 'text',
					'description': 'Unescape SQL query components',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'letters': {
					'name': 'letters',
					'group': 'text',
					'description': 'Extract alphabetic characters from a string',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'words': {
					'name': 'words',
					'group': 'text',
					'description': 'Split text into individual words',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'sentences': {
					'name': 'sentences',
					'group': 'text',
					'description': 'Split text into sentences',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'lines': {
					'name': 'lines',
					'group': 'text',
					'description': 'Split text into lines',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'bytes': {
					'name': 'bytes',
					'group': 'text',
					'description': 'Convert a string into bytes',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'merge': {
					'name': 'merge',
					'group': 'list',
					'description': 'Combine multiple lists into one',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'push': {
					'name': 'push',
					'group': 'list',
					'description': 'Add an element to the end of a list',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'pop': {
					'name': 'pop',
					'group': 'list',
					'description': 'Remove and return an element from the end of a list',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'reverse': {
					'name': 'reverse',
					'group': 'list',
					'description': 'Reverse the order of elements in a list',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'shuffle': {
					'name': 'shuffle',
					'group': 'list',
					'description': 'Randomly reorder elements in a list',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'map': {
					'name': 'map',
					'group': 'list',
					'description': 'Apply a function to each element in a list',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'reduce': {
					'name': 'reduce',
					'group': 'list',
					'description': 'Apply a function cumulatively to the elements in a list',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'names': {
					'name': 'names',
					'group': 'list',
					'description': 'Retrieve all keys or attribute names from a structure',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'values': {
					'name': 'values',
					'group': 'list',
					'description': 'Retrieve all values from a structure',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'sin': {
					'name': 'sin',
					'group': 'math',
					'description': 'Sine of the value (in radians)',
					'language': ['python', 'js', 'swift', 'kotlin', 'godot', 'c++'],
					'safe': True,
					'param': [{'name': 'value', 'type': 'number'}],
					'example': [
						{'code': [['sin', 0.1]], 'result': 0.0998, 'round': 4}
					]
				},
				'cos': {
					'name': 'cos',
					'group': 'math',
					'description': 'Cosine of the value (in radians)',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [{'name': 'value', 'type': 'number'}],
					'example': [
						{'code': [['cos', 0.1]], 'result': 0.995, 'round': 3}
					]
				},
				'tan': {
					'name': 'tan',
					'group': 'math',
					'description': 'Tangent of the value (in radians)',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'sinh': {
					'name': 'sinh',
					'group': 'math',
					'description': 'Hyperbolic sine of the value',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'cosh': {
					'name': 'cosh',
					'group': 'math',
					'description': 'Hyperbolic cosine of the value',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'tanh': {
					'name': 'tanh',
					'group': 'math',
					'description': 'Hyperbolic tangent of the valu',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'asin': {
					'name': 'asin',
					'group': 'math',
					'description': 'Arc sine of the value',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'acos': {
					'name': 'acos',
					'group': 'math',
					'description': 'Arc cosine of the value',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'atan': {
					'name': 'atan',
					'group': 'math',
					'description': 'Arc tangent of the value',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'asinh': {
					'name': 'asinh',
					'group': 'math',
					'description': 'Arc hyperbolic sine of the value',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'acosh': {
					'name': 'acosh',
					'group': 'math',
					'description': 'Arc hyperbolic cosine of the value',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'atanh': {
					'name': 'atanh',
					'group': 'math',
					'description': 'Arc hyperbolic tangent of the value',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'round': {
					'name': 'round',
					'group': 'math',
					'description': 'Rounds a number to the nearest integer or to the specified number of decimal places',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'floor': {
					'name': 'floor',
					'group': 'math',
					'description': 'Largest integer less than or equal to a number',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'ceil': {
					'name': 'ceil',
					'group': 'math',
					'description': 'Smallest integer greater than or equal to a number',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'log': {
					'name': 'log',
					'group': 'math',
					'description': 'Logarithm (natural by default) of a number',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'factorial': {
					'name': 'factorial',
					'group': 'math',
					'description': 'Factorial of a given non-negative number',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'fibonacci': {
					'name': 'fibonacci',
					'group': 'math',
					'description': 'Fibonacci numbers up to a specified index',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'gold': {
					'name': 'gold',
					'group': 'math',
					'description': 'Golden ratio of a number',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'abs': {
					'name': 'abs',
					'group': 'math',
					'description': 'Absolute value of a number',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'min': {
					'name': 'min',
					'group': 'math',
					'description': 'Smallest of a list of numbers',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'max': {
					'name': 'max',
					'group': 'math',
					'description': 'Largest of a list of numbers',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'avg': {
					'name': 'avg',
					'group': 'math',
					'description': 'Average value of a list of numbers',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'sum': {
					'name': 'sum',
					'group': 'math',
					'description': 'Sum of a list of numbers',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'random': {
					'name': 'random',
					'group': 'math',
					'description': 'Generates a pseudo-random number',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'random.seed': {
					'name': 'random_seed',
					'group': 'math',
					'description': 'Sets or gets the seed for the random number generator to produce reproducible results',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				't': {
					'name': 't',
					'group': 'time',
					'description': 'Stopwatch for calculating the time spent on operations',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'time': {
					'name': 'time',
					'group': 'time',
					'description': 'Provides current time since the epoch (1970-01-01 00:00:00 UTC)',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'timer': {
					'name': 'timer',
					'group': 'time',
					'description': 'Creates a timer that can be used to trigger events at specific intervals',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'timer.remove': {
					'name': 'timer_remove',
					'group': 'time',
					'description': 'Removes previously created timer',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'timepast': {
					'name': 'timepast',
					'group': 'time',
					'description': 'Calculates time passed since a given start time',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'wait': {
					'name': 'wait',
					'group': 'time',
					'description': 'Pauses execution for a specified number of seconds',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'encrypt': {
					'name': 'encrypt',
					'group': 'crypto',
					'description': 'Encrypts data using a specified key',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'decrypt': {
					'name': 'decrypt',
					'group': 'crypto',
					'description': 'Decrypts previously encrypted data using the specified key',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'hash': {
					'name': 'hash',
					'group': 'crypto',
					'description': 'Generates a hash for the data or generates a random text',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'uuid': {
					'name': 'uuid',
					'group': 'crypto',
					'description': 'Generates a universally unique identifier',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'md5': {
					'name': 'md5',
					'group': 'crypto',
					'description': 'Generates an MD5 hash of a text',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'sha1': {
					'name': 'sha1',
					'group': 'crypto',
					'description': 'Generates an SHA-1 hash of a text',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'sha256': {
					'name': 'sha256',
					'group': 'crypto',
					'description': 'Generates an SHA-256 hash of a text',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'sha512': {
					'name': 'sha512',
					'group': 'crypto',
					'description': 'Generates an SHA-512 hash of a text',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'crc32': {
					'name': 'crc32',
					'group': 'crypto',
					'description': 'Calculates the CRC32 checksum of a text',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'base64.encode': {
					'name': 'base64_encode',
					'group': 'crypto',
					'description': 'Encodes the data into base64 format',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'base64.decode': {
					'name': 'base64_decode',
					'group': 'crypto',
					'description': 'Decodes base64 encoded data back to its original form',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'gzip.encode': {
					'name': 'gzip_encode',
					'group': 'crypto',
					'description': 'Compresses data using the GZip compression algorithm',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'gzip.decode': {
					'name': 'gzip_decode',
					'group': 'crypto',
					'description': 'Decompresses GZip compressed data',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'rsa.encode': {
					'name': 'rsa_encode',
					'group': 'crypto',
					'description': 'Encrypts data using RSA encryption with a public key',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'rsa.decode': {
					'name': 'rsa_decode',
					'group': 'crypto',
					'description': 'Decrypts data encrypted with RSA using the corresponding private key',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'rsa.public': {
					'name': 'rsa_public',
					'group': 'crypto',
					'description': 'Generates the RSA public key used for encryption',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'rsa.private': {
					'name': 'rsa_private',
					'group': 'crypto',
					'description': 'Generates the RSA private key used for decryption',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'ssl.encode': {
					'name': 'ssl_encode',
					'group': 'crypto',
					'description': 'Performs SSL encryption on data to secure communication',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'ssl.decode': {
					'name': 'ssl_decode',
					'group': 'crypto',
					'description': 'Decrypts data encrypted with SSL for secure data transfer',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'ssl.check': {
					'name': 'ssl_check',
					'group': 'crypto',
					'description': 'Verifies the validity and authenticity of an SSL certificate',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'bcrypt.encode': {
					'name': 'bcrypt_encode',
					'group': 'crypto',
					'description': 'Hashes a password using the bcrypt algorithm for secure storage',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'bcrypt.check': {
					'name': 'bcrypt_check',
					'group': 'crypto',
					'description': 'Verifies a password against a bcrypt hashed password',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'file': {
					'name': 'file',
					'group': 'file',
					'description': 'Read or write data to a file at a specified path',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'file.exists': {
					'name': 'file_exists',
					'group': 'file',
					'description': 'Checks if a specified file exists at the given path',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'file.read': {
					'name': 'file_read',
					'group': 'file',
					'description': 'Reads the contents of a specified file',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'file.read.text': {
					'name': 'file_read_text',
					'group': 'file',
					'description': 'Reads the text contents of a specified file',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'file.read.lines': {
					'name': 'file_read_lines',
					'group': 'file',
					'description': 'Reads a specified file line by line into a list',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'file.write': {
					'name': 'file_write',
					'group': 'file',
					'description': 'Writes data to a specified file, creating or replacing it',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'file.append': {
					'name': 'file_append',
					'group': 'file',
					'description': 'Appends data to the end of a specified file without replacing it',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'file.remove': {
					'name': 'file_remove',
					'group': 'file',
					'description': 'Removes a specified file from the file system',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'file.move': {
					'name': 'file_move',
					'group': 'file',
					'description': 'Moves a specified file to a new location',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'file.copy': {
					'name': 'file_copy',
					'group': 'file',
					'description': 'Copies a specified file to a new location',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'file.rename': {
					'name': 'file_rename',
					'group': 'file',
					'description': 'Renames a specified file',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'file.link': {
					'name': 'file_link',
					'group': 'file',
					'description': 'Creates a hard link to a specified file',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'file.link.exists': {
					'name': 'file_link_exists',
					'group': 'file',
					'description': 'Checks if a hard link exists at the given path',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'file.info': {
					'name': 'file_info',
					'group': 'file',
					'description': 'Retrieves information about a specified file',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'file.size': {
					'name': 'file_size',
					'group': 'file',
					'description': 'Returns the size of a specified file in bytes',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'file.permission': {
					'name': 'file_permission',
					'group': 'file',
					'description': 'Retrieves or sets permissions for a specified file',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'file.time': {
					'name': 'file_time',
					'group': 'file',
					'description': 'Gets or sets the modified timestamp for a specified file',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'file.sha256': {
					'name': 'file_sha256',
					'group': 'file',
					'description': 'Computes the SHA256 checksum of a specified file',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'file.crc32': {
					'name': 'file_crc32',
					'group': 'file',
					'description': 'Computes the CRC32 checksum for a specified file',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'file.base64': {
					'name': 'file_base64',
					'group': 'file',
					'description': 'Encodes a specified file to base64 format',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'file.zip': {
					'name': 'file_zip',
					'group': 'file',
					'description': 'Compresses a specified file into a ZIP archive',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'file.zip.list': {
					'name': 'file_zip_list',
					'group': 'file',
					'description': 'Lists the files contained within a ZIP archive',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'file.zip.exists': {
					'name': 'file_zip_exists',
					'group': 'file',
					'description': 'Checks if a specific file exists within a ZIP archive',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'file.zip.read': {
					'name': 'file_zip_read',
					'group': 'file',
					'description': 'Reads a specific file from within a ZIP archive',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'file.zip.remove': {
					'name': 'file_zip_remove',
					'group': 'file',
					'description': 'Removes a specific file from a ZIP archive',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'file.unzip': {
					'name': 'file_unzip',
					'group': 'file',
					'description': 'Extracts files from a ZIP archive into a specified directory',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'file.gzip': {
					'name': 'file_gzip',
					'group': 'file',
					'description': 'Compresses a specified file using GZip compression',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'file.ungzip': {
					'name': 'file_ungzip',
					'group': 'file',
					'description': 'Decompresses a GZip-compressed file',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'file.void': {
					'name': 'file_void',
					'group': 'file',
					'description': 'Compresses the specified file using GZip compression and places it in a Void container',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'file.unvoid': {
					'name': 'file_unvoid',
					'group': 'file',
					'description': 'Decompresses a GZip-compressed files and directories from a Void container',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'dir.exists': {
					'name': 'dir_exists',
					'group': 'file',
					'description': 'Checks if a specified directory exists',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'dir.create': {
					'name': 'dir_create',
					'group': 'file',
					'description': 'Creates a new directory at a specified path',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'dir.copy': {
					'name': 'dir_copy',
					'group': 'file',
					'description': 'Copies a specified directory and its contents to a new location',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'dir.move': {
					'name': 'dir_move',
					'group': 'file',
					'description': 'Moves a specified directory to a new location',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'dir.rename': {
					'name': 'dir_rename',
					'group': 'file',
					'description': 'Renames a specified directory',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'dir.remove': {
					'name': 'dir_remove',
					'group': 'file',
					'description': 'Removes a specified directory and its contents',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'dir.list': {
					'name': 'dir_list',
					'group': 'file',
					'description': 'Lists the contents of a specified directory',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'dir.clear': {
					'name': 'dir_clear',
					'group': 'file',
					'description': 'Clears all contents of a specified directory without deleting the directory itself',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'dir.info': {
					'name': 'dir_info',
					'group': 'file',
					'description': 'Retrieves information about a specified directory',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'dir.size': {
					'name': 'dir_size',
					'group': 'file',
					'description': 'Calculates the total size of a specified directory and its contents',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'dir.permission': {
					'name': 'dir_permission',
					'group': 'file',
					'description': 'Gets or sets the permissions of a specified directory',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'dir.time': {
					'name': 'dir_time',
					'group': 'file',
					'description': 'Gets or sets the timestamps of a specified directory',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'dir.zip': {
					'name': 'dir_zip',
					'group': 'file',
					'description': 'Compresses a specified directory into a ZIP archive',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'dir.void': {
					'name': 'dir_void',
					'group': 'file',
					'description': 'Compresses a specified directory into a Void container',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'drive.list': {
					'name': 'drive_list',
					'group': 'file',
					'description': 'Lists all available drives on the system',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'drive.name': {
					'name': 'drive_name',
					'group': 'file',
					'description': 'Gets or sets the name of a specified drive',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'drive.size': {
					'name': 'drive_size',
					'group': 'file',
					'description': 'Total size of a specified drive',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'drive.used': {
					'name': 'drive_used',
					'group': 'file',
					'description': 'Amount of used space on a specified drive',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'drive.free': {
					'name': 'drive_free',
					'group': 'file',
					'description': 'Amount of free space on a specified drive',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'drive.info': {
					'name': 'drive_info',
					'group': 'file',
					'description': 'Retrieves information about a specified drive',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'drive.mount': {
					'name': 'drive_mount',
					'group': 'file',
					'description': 'Mounts a drive to make it accessible',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'drive.unmount': {
					'name': 'drive_unmount',
					'group': 'file',
					'description': 'Unmounts a drive',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'drive.create': {
					'name': 'drive_create',
					'group': 'file',
					'description': 'Creates a new virtual drive or volume',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'drive.resize': {
					'name': 'drive_resize',
					'group': 'file',
					'description': 'Resizes an existing drive partition or volume',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'drive.format': {
					'name': 'drive_format',
					'group': 'file',
					'description': 'Formats a drive with a specified file system',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'drive.remove': {
					'name': 'drive_remove',
					'group': 'file',
					'description': 'Removes or deletes a specified drive or partition',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'path.drive': {
					'name': 'path_drive',
					'group': 'file',
					'description': 'Drive component of a specified file path',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'path.dir': {
					'name': 'path_dir',
					'group': 'file',
					'description': 'Directory portion of a specified file path',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'path.file': {
					'name': 'path_file',
					'group': 'file',
					'description': 'File portion of a specified file path',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'path.name': {
					'name': 'path_name',
					'group': 'file',
					'description': 'Name of the file without extension from a specified path',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'path.extension': {
					'name': 'path_extension',
					'group': 'file',
					'description': 'File extension from a specified file path',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'path.strip': {
					'name': 'path_strip',
					'group': 'file',
					'description': 'Removes the extension from a specified path',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'void.encode': {
					'name': 'void_encode',
					'group': 'format',
					'description': 'Encodes data into the Void format',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [
						{'name': 'data', 'type': 'any'},
						{'name': 'indent', 'type': 'str', 'default': '\t'}
					],
					'example': []
				},
				'void.decode': {
					'name': 'void_decode',
					'group': 'format',
					'description': 'Decodes data from the Void format',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'json.encode': {
					'name': 'json_encode',
					'group': 'format',
					'description': 'Encodes data into the JSON format',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'json.decode': {
					'name': 'json_decode',
					'group': 'format',
					'description': 'Decodes data from the JSON format',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'csv.encode': {
					'name': 'csv_encode',
					'group': 'format',
					'description': 'Encodes data into the CSV format',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'csv.decode': {
					'name': 'csv_decode',
					'group': 'format',
					'description': 'Decodes data from the CSV format',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'yaml.encode': {
					'name': 'yaml_encode',
					'group': 'format',
					'description': 'Encodes data into the YAML format',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'yaml.decode': {
					'name': 'yaml_decode',
					'group': 'format',
					'description': 'Decodes data from the YAML format',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'ini.encode': {
					'name': 'ini_encode',
					'group': 'format',
					'description': 'Encodes data into the INI format',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'ini.decode': {
					'name': 'ini_decode',
					'group': 'format',
					'description': 'Decodes data from the INI format',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'html.encode': {
					'name': 'html_encode',
					'group': 'format',
					'description': 'Encodes data into the HTML format',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'html.decode': {
					'name': 'html_decode',
					'group': 'format',
					'description': 'Decodes data from the HTML format',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'html.markdown': {
					'name': 'html_markdown',
					'group': 'format',
					'description': 'Encodes Markdown-formatted text into the HTML format',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'xml.encode': {
					'name': 'xml_encode',
					'group': 'format',
					'description': 'Encodes data into the XML format',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'xml.decode': {
					'name': 'xml_decode',
					'group': 'format',
					'description': 'Decodes data from the XML format',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'css.encode': {
					'name': 'css_encode',
					'group': 'format',
					'description': 'Encodes data into the CSS format',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'css.decode': {
					'name': 'css_decode',
					'group': 'format',
					'description': 'Decodes data from the CSS format',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'request': {
					'name': 'request',
					'group': 'request',
					'description': 'Sends an HTTP (GET by default) request to a specified URL',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'request.post': {
					'name': 'request_post',
					'group': 'request',
					'description': 'Sends an HTTP POST request to a specified URL',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'request.put': {
					'name': 'request_put',
					'group': 'request',
					'description': 'Sends an HTTP PUT request to a specified URL',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'request.delete': {
					'name': 'request_delete',
					'group': 'request',
					'description': 'Sends an HTTP DELETE request to a specified URL',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'request.head': {
					'name': 'request_head',
					'group': 'request',
					'description': 'Sends an HTTP HEAD request to a specified URL',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'download': {
					'name': 'download',
					'group': 'download',
					'description': 'Downloads content from a specified URL',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'download.info': {
					'name': 'download_info',
					'group': 'download',
					'description': 'Retrieves information about a content available for download',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'download.audio': {
					'name': 'download_audio',
					'group': 'download',
					'description': 'Downloads audio from a specified URL',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'download.video': {
					'name': 'download_video',
					'group': 'download',
					'description': 'Downloads video from a specified URL',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'cookie': {
					'name': 'cookie',
					'group': 'cookie',
					'description': 'Gets or sets a specified cookie',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'cookie.remove': {
					'name': 'cookie_remove',
					'group': 'cookie',
					'description': 'Removes a specified cookie from the client\'s storage',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'cloud': {
					'name': 'cloud',
					'group': 'cloud',
					'description': 'Runs cloud storage or services for data management',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'cloud.file': {
					'name': 'cloud_file',
					'group': 'cloud',
					'description': 'Runs cloud storage',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'cloud.web': {
					'name': 'cloud_web',
					'group': 'cloud',
					'description': 'Runs WEB service',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'cloud.api': {
					'name': 'cloud_api',
					'group': 'cloud',
					'description': 'Runs API service',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'cloud.socket': {
					'name': 'cloud_socket',
					'group': 'cloud',
					'description': 'Runs Socket service',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'cloud.mail': {
					'name': 'cloud_mail',
					'group': 'cloud',
					'description': 'Runs Mail service',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'cloud.proxy': {
					'name': 'cloud_proxy',
					'group': 'cloud',
					'description': 'Runs Proxy service',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'bot.telegram': {
					'name': 'bot_telegram',
					'group': 'bot',
					'description': 'Interacting with the Telegram bot API',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'bot.discord': {
					'name': 'bot_discord',
					'group': 'bot',
					'description': 'Interacting with the Discord bot API',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'bot.wechat': {
					'name': 'bot_wechat',
					'group': 'bot',
					'description': 'Interacting with the WeChat bot API',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'social.x': {
					'name': 'social_x',
					'group': 'social',
					'description': 'Interacting with the X API',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'social.youtube': {
					'name': 'social_youtube',
					'group': 'social',
					'description': 'Interacting with the YouTube API',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'social.tiktok': {
					'name': 'social_tiktok',
					'group': 'social',
					'description': 'Interacting with the TikTok API',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'notification': {
					'name': 'notification',
					'group': 'notification',
					'description': 'Send notification',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'mail': {
					'name': 'mail',
					'group': 'notification',
					'description': 'Send mail',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'call': {
					'name': 'call',
					'group': 'notification',
					'description': 'Initiate a voice or video call to a specified recipient',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'sms': {
					'name': 'sms',
					'group': 'notification',
					'description': 'Send a text message (SMS) to a specified recipient',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'sql': {
					'name': 'sql',
					'group': 'sql',
					'description': 'Execute SQL query',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'os': {
					'name': 'os',
					'group': 'os',
					'description': 'Gets or checks the operating system type',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'os.version': {
					'name': 'os_version',
					'group': 'os',
					'description': 'Current version of the operating system',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'os.user': {
					'name': 'os_user',
					'group': 'os',
					'description': 'Information about the current user logged into the operating system',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'language': {
					'name': 'language',
					'group': 'os',
					'description': 'System language',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'device': {
					'name': 'device',
					'group': 'device',
					'description': 'Information related to the hardware device',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'cpu': {
					'name': 'cpu',
					'group': 'device',
					'description': 'Information about the CPU, including its usage and specifications',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'fps': {
					'name': 'fps',
					'group': 'device',
					'description': 'Frames per second for video or graphical rendering',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'vsync': {
					'name': 'vsync',
					'group': 'device',
					'description': 'Vertical sync settings to reduce screen tearing during rendering',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'resolution': {
					'name': 'resolution',
					'group': 'device',
					'description': 'Screen resolution',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'orientation': {
					'name': 'orientation',
					'group': 'device',
					'description': 'Orientation of a device\'s display (landscape or portrait)',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'darkmode': {
					'name': 'darkmode',
					'group': 'device',
					'description': 'Dark mode setting for user interfaces',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'pixel': {
					'name': 'pixel',
					'group': 'device',
					'description': 'Color of the pixel displayed on the screen',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'textmode.character': {
					'name': 'textmode_character',
					'group': 'device',
					'description': 'Symbol on the screen in text mode',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'textmode.cursor': {
					'name': 'textmode_cursor',
					'group': 'device',
					'description': 'Cursor position on the screen in text mode',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'textmode.clear': {
					'name': 'textmode_clear',
					'group': 'device',
					'description': 'Clears the screen in text mode',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'flashlight': {
					'name': 'flashlight',
					'group': 'device',
					'description': 'Turns on or off the device\'s flashlight',
					'language': ['swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'location': {
					'name': 'location',
					'group': 'device',
					'description': 'Retrieves the current geographic location using GPS or network triangulation',
					'language': ['js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'gyroscope': {
					'name': 'gyroscope',
					'group': 'device',
					'description': 'Provides access to the gyroscope sensor for motion detection',
					'language': ['js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'accelerometer': {
					'name': 'accelerometer',
					'group': 'device',
					'description': 'Provides access to the accelerometer sensor to detect acceleration forces',
					'language': ['js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'compass': {
					'name': 'compass',
					'group': 'device',
					'description': 'Accesses the magnetic compass sensor to determine orientation relative to the Earth\'s magnetic field',
					'language': ['js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'proximity': {
					'name': 'proximity',
					'group': 'device',
					'description': 'Detects the proximity of objects in relation to the device\'s proximity sensor',
					'language': ['swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'brightness': {
					'name': 'brightness',
					'group': 'device',
					'description': 'Manages the screen brightness level of the device',
					'language': ['swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'calendar': {
					'name': 'calendar',
					'group': 'device',
					'description': 'Calendar events on a device',
					'language': ['swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'gallery': {
					'name': 'gallery',
					'group': 'device',
					'description': 'Photo and video library on a device',
					'language': ['swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'contacts': {
					'name': 'contacts',
					'group': 'device',
					'description': 'Contact list on a device',
					'language': ['swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'clipboard': {
					'name': 'clipboard',
					'group': 'clipboard',
					'description': 'Storing or retrieving clipboard temporary data',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'clipboard.remove': {
					'name': 'clipboard_remove',
					'group': 'clipboard',
					'description': 'Clears the clipboard content',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': []
				},
				'translate': {
					'name': 'translate',
					'group': 'ai',
					'description': 'Converts text from one language to another',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'spellcheck': {
					'name': 'spellcheck',
					'group': 'ai',
					'description': 'Spell check in different languages',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []				
				},
				'chat': {
					'name': 'chat',
					'group': 'ai',
					'description': 'AI conversation and interaction through text',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'image': {
					'name': 'image',
					'group': 'ai',
					'description': 'Create an image',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'image.size': {
					'name': 'image_size',
					'group': 'ai',
					'description': 'Adjusts the dimensions of an image',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'image.square': {
					'name': 'image_square',
					'group': 'ai',
					'description': 'Crops an image to a square aspect ratio',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'image.crop': {
					'name': 'image_crop',
					'group': 'ai',
					'description': 'Cuts a portion of the image according to specified dimensions',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'image.rotate': {
					'name': 'image_rotate',
					'group': 'ai',
					'description': 'Rotates an image by a specified number of degrees',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'image.text': {
					'name': 'image_text',
					'group': 'ai',
					'description': 'Adds text to an image at specified positions',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'image.image': {
					'name': 'image_image',
					'group': 'ai',
					'description': 'Adds an image onto another',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'image.grayscale': {
					'name': 'image_grayscale',
					'group': 'ai',
					'description': 'Converts an image to grayscale',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'image.tint': {
					'name': 'image_tint',
					'group': 'ai',
					'description': 'Applies a color tint to an image',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'image.flip.h': {
					'name': 'image_flip_h',
					'group': 'ai',
					'description': 'Flips an image horizontally',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'image.flip.v': {
					'name': 'image_flip_v',
					'group': 'ai',
					'description': 'Flips an image vertically',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'image.upscale': {
					'name': 'image_upscale',
					'group': 'ai',
					'description': 'Increases the resolution of an image',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'image.draw': {
					'name': 'image_draw',
					'group': 'ai',
					'description': 'Allows draw, clear or replace objects on an image',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'image.style': {
					'name': 'image_style',
					'group': 'ai',
					'description': 'Applies stylistic effects to an image',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'image.colorize': {
					'name': 'image_colorize',
					'group': 'ai',
					'description': 'Adds color to a grayscale image',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'image.recognize': {
					'name': 'image_recognize',
					'group': 'ai',
					'description': 'Identifies objects or text within an image',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'image.face': {
					'name': 'image_face',
					'group': 'ai',
					'description': 'Detects and processes faces within an image',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'image.effect': {
					'name': 'image_effect',
					'group': 'ai',
					'description': 'Applies special effects to an image',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'video': {
					'name': 'video',
					'group': 'ai',
					'description': 'Create a video',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'video.crop': {
					'name': 'video_crop',
					'group': 'ai',
					'description': 'Cuts a portion of the video according to specified dimensions',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'video.text': {
					'name': 'video_text',
					'group': 'ai',
					'description': 'Adds text to a video at specified positions',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'video.image': {
					'name': 'video_image',
					'group': 'ai',
					'description': 'Adds an image to a video',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'video.sound': {
					'name': 'video_sound',
					'group': 'ai',
					'description': 'Adds audio track to a video',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'video.video': {
					'name': 'video_video',
					'group': 'ai',
					'description': 'Adds another video clip to a video',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'video.trim': {
					'name': 'video_trim',
					'group': 'ai',
					'description': 'Trims the video to a specified length',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'video.size': {
					'name': 'video_size',
					'group': 'ai',
					'description': 'Adjusts the dimensions of a video',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'video.upscale': {
					'name': 'video_upscale',
					'group': 'ai',
					'description': 'Increases the resolution of a video',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'video.speed': {
					'name': 'video_speed',
					'group': 'ai',
					'description': 'Adjusts the playback speed of a video',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'video.volume': {
					'name': 'video_volume',
					'group': 'ai',
					'description': 'Adjusts the volume of the video\'s audio track',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'video.mute': {
					'name': 'video_mute',
					'group': 'ai',
					'description': 'Removes sound from a video',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'video.face': {
					'name': 'video_face',
					'group': 'ai',
					'description': 'Detects and processes faces within a video',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'video.effect': {
					'name': 'video_effect',
					'group': 'ai',
					'description': 'Applies special effects to a video',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'sound': {
					'name': 'sound',
					'group': 'ai',
					'description': 'Create audio track',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'sound.trim': {
					'name': 'sound_trim',
					'group': 'ai',
					'description': 'Trims the audio track to a specified length',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'sound.speed': {
					'name': 'sound_speed',
					'group': 'ai',
					'description': 'Adjusts the playback speed of audio',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'sound.volume': {
					'name': 'sound_volume',
					'group': 'ai',
					'description': 'Adjusts the volume of an audio track',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'sound.effect': {
					'name': 'sound_effect',
					'group': 'ai',
					'description': 'Applies special effects to an audio track',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'music': {
					'name': 'music',
					'group': 'ai',
					'description': 'Generates music',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'voice': {
					'name': 'voice',
					'group': 'ai',
					'description': 'Text voicing with different voices',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'voice.list': {
					'name': 'voice_list',
					'group': 'ai',
					'description': 'List of available voices',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'voice.recognize': {
					'name': 'voice_recognize',
					'group': 'ai',
					'description': 'Convert voice to text',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'voice.stop': {
					'name': 'voice_stop',
					'group': 'ai',
					'description': 'Stop dictation of the text',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'voice.capture': {
					'name': 'voice_capture',
					'group': 'ai',
					'description': 'Create a specific voice',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'motion': {
					'name': 'motion',
					'group': 'ai',
					'description': 'Processes motion-based data',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'motion.capture': {
					'name': 'motion_capture',
					'group': 'ai',
					'description': 'Records or analyzes motion data in real-time',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'google.voice': {
					'name': 'google_voice',
					'group': 'ai',
					'description': 'Utilizes Google\'s voice recognition services',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'google.voice.list': {
					'name': 'google_voice_list',
					'group': 'ai',
					'description': 'Lists available voice options via Google services',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'google.voice.recognize': {
					'name': 'google_voice_recognize',
					'group': 'ai',
					'description': 'Recognizes speech using Google technology',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'google.translate': {
					'name': 'google_translate',
					'group': 'ai',
					'description': 'Utilizes Google\'s translation services',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'deepl.translate': {
					'name': 'deepl_translate',
					'group': 'ai',
					'description': 'Utilizes DeepL\'s translation services',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'openai.chat': {
					'name': 'openai_chat',
					'group': 'ai',
					'description': 'Conversation using OpenAI\'s chat models',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'openai.image': {
					'name': 'openai_image',
					'group': 'ai',
					'description': 'Generates or processes images using OpenAI\'s models',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'openai.video': {
					'name': 'openai_video',
					'group': 'ai',
					'description': 'Generates or processes videos using OpenAI\'s models',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'openai.translate': {
					'name': 'openai_translate',
					'group': 'ai',
					'description': 'Utilizes OpenAI\'s services for text translation',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'deepseek.chat': {
					'name': 'deepseek_chat',
					'group': 'ai',
					'description': 'Conversation using DeepSeek\'s chat models',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'deepseek.translate': {
					'name': 'deepseek_translate',
					'group': 'ai',
					'description': 'Utilizes DeepSeek\'s services for text translation',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'claude.chat': {
					'name': 'claude_chat',
					'group': 'ai',
					'description': 'Conversation using Claude\'s chat models',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'stablediffusion.image': {
					'name': 'stablediffusion_image',
					'group': 'ai',
					'description': 'Generates artistic images using Stable Diffusion models',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'stablediffusion.upscale': {
					'name': 'stablediffusion_upscale',
					'group': 'ai',
					'description': 'Enhances image resolution using Stable Diffusion models',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'stablediffusion.draw': {
					'name': 'stablediffusion_draw',
					'group': 'ai',
					'description': 'Creating and replacing objects in an image using Stable Diffusion models',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'stablediffusion.background': {
					'name': 'stablediffusion_background',
					'group': 'ai',
					'description': 'Background removal using Stable Diffusion models',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'stablediffusion.video': {
					'name': 'stablediffusion_video',
					'group': 'ai',
					'description': 'Creates videos using Stable Diffusion\'s models',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'ollama.chat': {
					'name': 'ollama_chat',
					'group': 'ai',
					'description': 'Conversation using Ollama\'s chat models',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'ui': {
					'name': 'ui',
					'group': 'ui',
					'description': 'Creating a basic element of user interface',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'bg': {
					'name': 'bg',
					'group': 'ui',
					'description': 'Sets or updates the background properties, such as color or image',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'show': {
					'name': 'show',
					'group': 'ui',
					'description': 'Displays a UI element to make it visible',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'hide': {
					'name': 'hide',
					'group': 'ui',
					'description': 'Hides a UI element to make it invisible',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'enable': {
					'name': 'enable',
					'group': 'ui',
					'description': 'Enables a UI element, making it interactive and functional',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'disable': {
					'name': 'disable',
					'group': 'ui',
					'description': 'Disables a UI element, preventing interaction or use',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'focus': {
					'name': 'focus',
					'group': 'ui',
					'description': 'Sets focus on a specific UI element, making it active or highlighted',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'unfocus': {
					'name': 'unfocus',
					'group': 'ui',
					'description': 'Removes focus from a UI element',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'scale': {
					'name': 'scale',
					'group': 'ui',
					'description': 'Adjusts the size of a UI element by scaling it up or down',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'ui.text': {
					'name': 'ui_text',
					'group': 'ui',
					'description': 'Displays or manages text within the user interface',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'ui.image': {
					'name': 'ui_image',
					'group': 'ui',
					'description': 'Displays or manages images within the user interface',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'ui.video': {
					'name': 'ui_video',
					'group': 'ui',
					'description': 'Handles video playback or displays video content in the UI',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'ui.sound': {
					'name': 'ui_sound',
					'group': 'ui',
					'description': 'Manages sound playback or controls audio settings in the UI',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'ui.camera': {
					'name': 'ui_camera',
					'group': 'ui',
					'description': 'Handles camera input or streams video from a camera in the UI',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'ui.draw': {
					'name': 'ui_draw',
					'group': 'ui',
					'description': 'Enables drawing within the user interface',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'ui.header': {
					'name': 'ui_header',
					'group': 'ui',
					'description': 'Defines or manages the header section of the user interface',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'ui.footer': {
					'name': 'ui_footer',
					'group': 'ui',
					'description': 'Defines or manages the footer section of the user interface',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'ui.wait': {
					'name': 'ui_wait',
					'group': 'ui',
					'description': 'Displays a waiting indicator within the UI',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'ui.gallery': {
					'name': 'ui_gallery',
					'group': 'ui',
					'description': 'Manages or displays a collection of images or media items',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'ui.button': {
					'name': 'ui_button',
					'group': 'ui',
					'description': 'Defines or manages buttons in the UI for user interaction',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'ui.select': {
					'name': 'ui_select',
					'group': 'ui',
					'description': 'Creates or manages a selection interface, such as a dropdown menu',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'ui.switch': {
					'name': 'ui_switch',
					'group': 'ui',
					'description': 'Implements a toggle switch for binary choices in the UI',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'ui.progress': {
					'name': 'ui_progress',
					'group': 'ui',
					'description': 'Displays a progress bar or status indicator',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'ui.slider': {
					'name': 'ui_slider',
					'group': 'ui',
					'description': 'Implements a sliding control for adjusting values along a range',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'ui.edit': {
					'name': 'ui_edit',
					'group': 'ui',
					'description': 'Enables text editing or manages editable fields in the UI',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'ui.divider': {
					'name': 'ui_divider',
					'group': 'ui',
					'description': 'Inserts a visual divider or separating line within the UI layout',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'ui.split.h': {
					'name': 'ui_split_h',
					'group': 'ui',
					'description': 'Splits a UI container horizontally to create multiple sections',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'ui.split.v': {
					'name': 'ui_split_v',
					'group': 'ui',
					'description': 'Splits a UI container vertically to create multiple sections',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'ui.list': {
					'name': 'ui_list',
					'group': 'ui',
					'description': 'Displays a list of items for selection or viewing',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'ui.tile': {
					'name': 'ui_tile',
					'group': 'ui',
					'description': 'Arranges content in a tiled format for visual organization',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'ui.color': {
					'name': 'ui_color',
					'group': 'ui',
					'description': 'Color selection or manages color properties in the UI',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'ui.date': {
					'name': 'ui_date',
					'group': 'ui',
					'description': 'Date selection or displays date information',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'ui.menu': {
					'name': 'ui_menu',
					'group': 'ui',
					'description': 'Creates or manages menu options for navigation or actions',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'ui.menu.context': {
					'name': 'ui_menu_context',
					'group': 'ui',
					'description': 'Defines a context menu for right-click actions or additional options',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'window': {
					'name': 'window',
					'group': 'ui',
					'description': 'Creates or manages window',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'window.list': {
					'name': 'window_list',
					'group': 'ui',
					'description': 'List of windows',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'title': {
					'name': 'title',
					'group': 'ui',
					'description': 'Sets or updates the title of a window or UI element',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'icon': {
					'name': 'icon',
					'group': 'ui',
					'description': 'Defines or changes an icon associated with a window or UI element',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'size': {
					'name': 'size',
					'group': 'ui',
					'description': 'Adjusts the dimensions or size of a window or UI element',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'size.max': {
					'name': 'size_max',
					'group': 'ui',
					'description': 'Sets the maximum size constraints for a window or UI element',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'size.min': {
					'name': 'size_min',
					'group': 'ui',
					'description': 'Sets the minimum size constraints for a window or UI element',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'position': {
					'name': 'position',
					'group': 'ui',
					'description': 'Adjusts the position or placement of a window or UI element',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'direction': {
					'name': 'direction',
					'group': 'ui',
					'description': 'Text writing direction for the selected language',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'attention': {
					'name': 'attention',
					'group': 'ui',
					'description': 'Highlights a window or UI element',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'top': {
					'name': 'top',
					'group': 'ui',
					'description': 'Brings a window or UI element to the top layer or foreground',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'nofocus': {
					'name': 'nofocus',
					'group': 'ui',
					'description': 'Prevents a UI element from receiving focus or interaction',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'noresize': {
					'name': 'noresize',
					'group': 'ui',
					'description': 'Locks the size of a window or UI element, preventing resizing',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'center': {
					'name': 'center',
					'group': 'ui',
					'description': 'Centers a window or UI element within its parent container or screen',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'fullscreen': {
					'name': 'fullscreen',
					'group': 'ui',
					'description': 'Switches a window or UI element to fullscreen mode',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'maximize': {
					'name': 'maximize',
					'group': 'ui',
					'description': 'Minimizes a window to the taskbar or dock',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'minimize': {
					'name': 'minimize',
					'group': 'ui',
					'description': '',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'exclusive': {
					'name': 'exclusive',
					'group': 'ui',
					'description': 'Enables exclusive mode restricting other operations',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'border': {
					'name': 'border',
					'group': 'ui',
					'description': 'Border properties or visibility for a UI element',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'filedrop': {
					'name': 'filedrop',
					'group': 'ui',
					'description': 'File drag-and-drop capabilities within the application UI',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'dialog': {
					'name': 'dialog',
					'group': 'ui',
					'description': 'Dialog box for user prompts or options',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'dialog.file': {
					'name': 'dialog_file',
					'group': 'ui',
					'description': 'Opens a file selection dialog',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'effect': {
					'name': 'effect',
					'group': 'ui',
					'description': 'Applies visual or audio effect to a UI element',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'effect.remove': {
					'name': 'effect_remove',
					'group': 'ui',
					'description': 'Removes applied effect from a UI element',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'tap': {
					'name': 'tap',
					'group': 'input',
					'description': 'Simulates a tap gesture',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'key': {
					'name': 'key',
					'group': 'input',
					'description': 'Key binding',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'key.remove': {
					'name': 'key_remove',
					'group': 'input',
					'description': 'Removes a key binding',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'key.enable': {
					'name': 'key_enable',
					'group': 'input',
					'description': 'Enables key binding',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'key.disable': {
					'name': 'key_disable',
					'group': 'input',
					'description': 'Disable key binding',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'key.press': {
					'name': 'key_press',
					'group': 'input',
					'description': 'Simulates a key press event',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'keyboard': {
					'name': 'keyboard',
					'group': 'input',
					'description': 'Keyboard information',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'mouse': {
					'name': 'mouse',
					'group': 'input',
					'description': 'Mouse information',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'mouse.lock': {
					'name': 'mouse_lock',
					'group': 'input',
					'description': 'Locks the mouse cursor to prevent it from leaving a designated area',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'mouse.position': {
					'name': 'mouse_position',
					'group': 'input',
					'description': 'Retrieves or sets the current position of the mouse cursor',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'mouse.shape': {
					'name': 'mouse_shape',
					'group': 'input',
					'description': 'Change the shape of the mouse cursor',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'gamepad': {
					'name': 'gamepad',
					'group': 'input',
					'description': 'Gamepad information',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'gamepad.vibrate': {
					'name': 'gamepad_vibrate',
					'group': 'input',
					'description': 'Gamepad vibration',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'game': {
					'name': 'game',
					'group': 'game',
					'description': 'Create a custom game',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				}
			}
		},
		'app': {
			'path': '',
			'name': '',
			'argument': []
		},
		'device': {},
		'os': {},
		'cloud': {},
		'log': {},
		'db': {},
		'ai': {},
		'run': [],
		'action': {
			'version': [
				['.', '{description.about}']
			],
			'help': [],
			'update': [],
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
				}
			}
		},
		'text': {}
	};

	static get(name = '', defaultValue = null, data = this.data) {
	}

	static set(name, value = null, data = null) {
	}

	static remove(name, data = null) {
	}

	static type(data) {
	}

	static type_text(data) {
	}

	static type_int(data) {
	}

	static type_float(data) {
	}

	static type_number(data) {
	}

	static type_bool(data) {
	}

	static type_list(data) {
	}

	static type_dict(data) {
	}

	static type_binary(data) {
	}

	static n(data) {
	}

	// control

	static print(data, end ='\n') {
	}

	static input(text = '') {
	}

	static condition() {
	}

	static loop() {
	}

	static loop_break() {
	}

	static loop_continue() {
	}

	static loop_repeat() {
	}

	static action_return() {
	}

	static action(action) {
	}

	static open(text) {
	}

	static code(text) {
	}

	static exit(code = 0) {
	}

	static l(name, data) {
	}

	static convert(name_from, name_to, value = null) {
	}

	static export() {
	}

	static update(name = null) {
	}

	static test(name = null) {
	}

	static help(name = null) {
	}

	static void(name, action = null) {
	}

	// text

	static lower(text) {
	}

	static upper(text) {
	}

	static starts(text, subtext) {
	}

	static ends(text, subtext) {
	}

	static strip() {
	}

	static strip_start() {
	}

	static strip_end() {
	}

	static replace() {
	}

	static find(text, subtext) {
	}

	static parse(text, format) {
	}

	static similar(first, second) {
	}

	static part() {
	}

	static split() {
	}

	static join() {
	}

	static date(time, format) {
	}

	static escape(text, symbol, replace = null) {
	}

	static escape_html(text) {
	}

	static escape_url(text) {
	}

	static escape_sql(text) {
	}

	static unescape() {
	}

	static unescape_html(text) {
	}

	static unescape_url(text) {
	}

	static unescape_sql(text) {
	}

	static letters(text) {
	}

	static words(text) {
	}

	static sentences(text) {
	}

	static lines(text) {
	}

	static bytes(text) {
	}

	// list

	static merge(first, second) {
	}

	static push(list, data, position = null) {
	}

	static pop(list, position = null) {
	}

	static reverse(list) {
	}

	static shuffle(list) {
	}

	static map(list, action) {
	}

	static reduce(list, action) {
	}

	static names(dict) {
	}

	static values(dict) {
	}

	// math

	static sin(value) {
		return Math.sin(value)
	}

	static cos(value) {
		return Math.cos(value)
	}

	static tan(value) {
		return Math.tan(value)
	}

	static sinh(value) {
		return Math.sinh(value)
	}

	static cosh(value) {
		return Math.cosh(value)
	}

	static tanh(value) {
		return Math.tanh(value)
	}

	static asin(value) {
		return Math.asin(value)
	}

	static acos(value) {
		return Math.acos(value)
	}

	static atan(value) {
		return Math.atan(value)
	}

	static asinh(value) {
		return Math.asinh(value)
	}

	static acosh(value) {
		return Math.acosh(value)
	}

	static atanh(value) {
		return Math.atanh(value)
	}

	static round(value, dot = 0) {
	}

	static floor(value) {
		return Math.floor(value)
	}

	static ceil(value) {
		return Math.ceil(value)
	}

	static log(value, base = null) {
	}

	static factorial(value) {
	}

	static fibonacci(value) {
	}

	static gold() {
	}

	static abs(value) {
		return Math.abs(value)
	}

	static min(value) {
		return Math.min(value)
	}

	static max(value) {
		return Math.max(value)
	}

	static avg(value) {
	}

	static sum(value) {
	}

	static random(value = null, to = null) {
	}

	static random_seed(seed = null) {
	}

	// time

	static t(name = '') {
	}

	static time(dot = 6) {
	}

	static timer(action, seconds = 1, name = '') {
	}

	static timer_remove(name) {
	}

	static timepast(time = 0) {
	}

	static wait(seconds = 1) {
	}

	// encrypt

	static encrypt(data, key = '') {
	}

	static decrypt(data, key) {
	}

	static hash(length = 64, symbols = null) {
	}

	static uuid() {
	}

	static md5() {
	}

	static sha1() {
	}

	static sha256() {
	}

	static sha512() {
	}

	static crc32() {
	}

	static base64_encode() {
	}

	static base64_decode() {
	}

	static gzip_encode() {
	}

	static gzip_decode() {
	}

	static rsa_encode() {
	}

	static rsa_decode() {
	}

	static rsa_public() {
	}

	static rsa_private() {
	}

	static ssl_encode() {
	}

	static ssl_decode() {
	}

	static ssl_check() {
	}

	static bcrypt_encode() {
	}

	static bcrypt_check() {
	}

	// file

	static file(path, data = null) {
	}

	static file_exists(path) {
	}

	static file_read(path, start = 0, length = 0) {
	}

	static file_read_text(path, encoding = 'utf-8') {
	}

	static file_read_lines(path, encoding = 'utf-8', newline = '\n') {
	}

	static file_write(path, data = '') {
	}

	static file_append(path, data) {
	}

	static file_remove(path) {
	}

	static file_move(path) {
	}

	static file_copy(path) {
	}

	static file_rename(path) {
	}

	static file_link(path) {
	}

	static file_link_exists(path) {
	}

	static file_info(path) {
	}

	static file_size(path) {
	}

	static file_permission(path) {
	}

	static file_time(path) {
	}

	static file_sha256(path) {
	}

	static file_crc32(path) {
	}

	static file_base64(path) {
	}

	static file_zip(path) {
	}

	static file_zip_list(path) {
	}

	static file_zip_exists(path) {
	}

	static file_zip_read(path) {
	}

	static file_zip_remove(path) {
	}

	static file_unzip(path) {
	}

	static file_gzip(path) {
	}	

	static file_ungzip(path) {
	}

	static file_void(path, key = '') {
	}

	static file_unvoid(path, key = '') {
	}

	// dir

	static dir_exists(path) {
	}

	static dir_create(path) {
	}

	static dir_copy(path) {
	}

	static dir_move(path) {
	}

	static dir_rename(path) {
	}

	static dir_remove(path) {
	}

	static dir_list(path) {
	}

	static dir_clear(path) {
	}

	static dir_info(path) {
	}

	static dir_size(path) {
	}

	static dir_permission(path) {
	}

	static dir_time(path) {
	}

	static dir_zip(path) {
	}

	static dir_void(path) {
	}

	// drive

	static drive_list() {
	}

	static drive_name(path) {
	}

	static drive_size(path) {
	}

	static drive_used(path) {
	}

	static drive_free(path) {
	}

	static drive_info(path) {
	}

	static drive_mount(path) {
	}

	static drive_unmount(path) {
	}

	static drive_create(path) {
	}

	static drive_resize(path) {
	}

	static drive_format(path) {
	}

	static drive_remove(path) {
	}

	// path

	static path_drive(path) {
	}

	static path_dir(path) {
	}

	static path_file(path) {
	}

	static path_name(path) {
	}

	static path_extension(path) {
	}

	static path_strip(path, strip = null) {
	}

	// format

	static void_encode(data, indent = '\t', level = 0) {
	}

	static void_decode(text) {
	}

	static json_encode(data, indent = '\t', separators = null) {
	}

	static json_decode(text) {
	}

	static csv_encode(data) {
	}

	static csv_decode(text) {
	}

	static yaml_encode(text) {
	}

	static yaml_decode(text) {
	}

	static ini_encode(text) {
	}

	static ini_decode(text) {
	}

	static html_encode(text) {
	}

	static html_decode(text) {
	}

	static html_markdown(text) {
	}

	static xml_encode(text) {
	}

	static xml_decode(text) {
	}

	static css_encode(text) {
	}

	static css_decode(text) {
	}

	// request

	static request() {
	}

	static request_post() {
	}

	static request_put() {
	}

	static request_delete() {
	}

	static request_head() {
	}

	// download

	static download() {
	}

	static download_info() {
	}

	static download_audio() {
	}

	static download_video() {
	}

	// cookie

	static cookie(name, value = null) {
	}

	static cookie_remove(name) {
	}

	// cloud

	static cloud() {
	}

	static cloud_file() {
	}

	static cloud_web() {
	}

	static cloud_api() {
	}

	static cloud_socket() {
	}

	static cloud_mail() {
	}	

	static cloud_proxy() {
	}

	// bot

	static bot_telegram() {
	}

	static bot_discord() {
	}

	static bot_wechat() {
	}

	// social

	static social_x() {
	}

	static social_youtube() {
	}

	static social_tiktok() {
	}

	// notification

	static notification(token, text, badge = null, image = null) {
	}

	static mail(address_from, address_to, text, subject = null, attach = null) {
	}

	static call() {
	}

	static sms() {
	}

	// sql

	static sql(query, data = null) {
	}

	// os

	static os(name = null) {
	}

	static os_version() {
	}

	static os_user() {
	}

	static language() {
	}

	// device

	static device() {
	}

	static cpu(seconds = 0) {
	}

	static fps() {
	}

	static vsync() {
	}

	static resolution() {
	}

	static orientation(name = null) {
	}

	static darkmode() {
	}

	static pixel() {
	}

	static textmode_character() {
	}

	static textmode_cursor() {
	}

	static textmode_clear() {
	}

	static flashlight() {
	}

	static location() {
	}

	static gyroscope() {
	}

	static accelerometer() {
	}

	static compass() {
	}

	static proximity() {
	}

	static brightness() {
	}

	static calendar() {
	}

	static gallery() {
	}

	static contacts() {
	}

	// clipboard

	static clipboard(value = null) {
	}

	static clipboard_remove() {
	}

	// ai

	static translate() {
	}

	static spellcheck() {
	}

	static chat() {
	}

	static image() {
	}

	static image_size() {
	}

	static image_square() {
	}

	static image_crop() {
	}

	static image_rotate() {
	}

	static image_text() {
	}

	static image_image() {
	}

	static image_grayscale() {
	}

	static image_tint() {
	}

	static image_flip_h() {
	}

	static image_flip_v() {
	}

	static image_upscale() {
	}

	static image_draw() {
	}

	static image_style() {
	}

	static image_colorize() {
	}

	static image_recognize() {
	}

	static image_face() {
	}

	static image_effect() {
	}

	static video() {
	}

	static video_crop() {
	}

	static video_text() {
	}

	static video_image() {
	}

	static video_sound() {
	}

	static video_video() {
	}

	static video_trim() {
	}

	static video_size() {
	}

	static video_upscale() {
	}

	static video_speed() {
	}

	static video_volume() {
	}

	static video_mute() {
	}

	static video_face() {
	}

	static video_effect() {
	}

	static sound() {
	}

	static sound_trim() {
	}

	static sound_speed() {
	}

	static sound_volume() {
	}

	static sound_effect() {
	}

	static music() {
	}

	static voice(text = null, voice = null) {
	}

	static voice_list() {
	}

	static voice_recognize() {
	}

	static voice_stop() {
	}

	static voice_capture() {
	}

	static motion() {
	}

	static motion_capture() {
	}

	// google

	static google_voice() {
	}

	static google_voice_list() {
	}

	static google_voice_recognize() {
	}

	static google_translate() {
	}

	// deepl

	static deepl_translate() {
	}

	// openai

	static openai_chat() {
	}

	static openai_image() {
	}

	static openai_video() {
	}

	static openai_translate() {
	}

	// deepseek

	static deepseek_chat() {
	}

	static deepseek_translate() {
	}

	// claude

	static claude_chat() {
	}

	// stablediffusion

	static stablediffusion_image(text, size = null) {
	}

	static stablediffusion_upscale() {
	}

	static stablediffusion_draw() {
	}

	static stablediffusion_background() {
	}

	static stablediffusion_video(text) {
	}

	// ollama

	static ollama_chat(text) {
	}

	// ui

	static ui() {
	}

	static bg() {
	}

	static show() {
	}

	static hide() {
	}

	static enable() {
	}

	static disable() {
	}

	static focus() {
	}

	static unfocus() {
	}

	static scale() {
	}

	static ui_text() {
	}

	static ui_image() {
	}

	static ui_video() {
	}

	static ui_sound() {
	}

	static ui_camera() {
	}

	static ui_draw() {
	}

	static ui_header() {
	}

	static ui_footer() {
	}

	static ui_wait() {
	}

	static ui_gallery() {
	}

	static ui_button() {
	}

	static ui_select() {
	}

	static ui_switch() {
	}

	static ui_progress() {
	}

	static ui_slider() {
	}

	static ui_edit() {
	}

	static ui_divider() {
	}

	static ui_split_h() {
	}

	static ui_split_v() {
	}

	static ui_list() {
	}

	static ui_tile() {
	}

	static ui_color() {
	}

	static ui_date() {
	}

	static ui_menu() {
	}

	static ui_menu_context() {
	}

	static window() {
	}

	static window_list() {
	}

	static title() {
	}

	static icon() {
	}

	static size() {
	}

	static size_max() {
	}

	static size_min() {
	}

	static position() {
	}

	static direction() {
	}

	static attention() {
	}

	static top() {
	}

	static nofocus() {
	}

	static noresize() {
	}

	static center() {
	}

	static fullscreen() {
	}

	static maximize() {
	}

	static minimize() {
	}

	static exclusive() {
	}

	static border() {
	}

	static filedrop() {
	}

	static dialog() {
	}

	static dialog_file() {
	}

	static effect() {
	}

	static effect_remove() {
	}

	// input

	static tap() {
	}

	static key() {
	}

	static key_remove() {
	}

	static key_enable() {
	}

	static key_disable() {
	}

	static key_press() {
	}

	static keyboard() {
	}

	static mouse() {
	}

	static mouse_lock() {
	}

	static mouse_position() {
	}

	static mouse_shape() {
	}

	static gamepad() {
	}

	static gamepad_vibrate() {
	}

	// game

	static game() {
	}

	// run

	static run() {
		void.t('run');
	}
}