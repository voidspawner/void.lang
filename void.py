import os
import sys
import psutil
import platform
import time
import json
import math

class void:

	data = {
		'description': {
			'about': {
				'name': 'V O I D lang',
				'site': 'https://voidsp.com',
				'language': 'python',
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
					'param': [{'name': 'name', 'type': 'str', 'default': None}],
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
					'name': None,
					'group': 'expression',
					'description': 'Perform addition operation',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'-': {
					'name': None,
					'group': 'expression',
					'description': 'Perform subtraction operation',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'*': {
					'name': None,
					'group': 'expression',
					'description': 'Perform multiplication operation',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'/': {
					'name': None,
					'group': 'expression',
					'description': 'Perform division operation',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'%': {
					'name': None,
					'group': 'expression',
					'description': 'Perform modulo operation',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'~': {
					'name': None,
					'group': 'expression',
					'description': 'Elevation operator',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'!': {
					'name': None,
					'group': 'expression',
					'description': 'Perform logical negation',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'&': {
					'name': None,
					'group': 'expression',
					'description': 'Perform bitwise AND operation',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'|': {
					'name': None,
					'group': 'expression',
					'description': 'Perform bitwise OR operation',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'^': {
					'name': None,
					'group': 'expression',
					'description': 'Perform bitwise XOR operation',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'>>': {
					'name': None,
					'group': 'expression',
					'description': 'Perform right bitwise shift operation',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'<<': {
					'name': None,
					'group': 'expression',
					'description': 'Perform left bitwise shift operation',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'=': {
					'name': None,
					'group': 'expression',
					'description': 'Assign value to a variable',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'+=': {
					'name': None,
					'group': 'expression',
					'description': 'Add and assign value to a variable',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'=+': {
					'name': None,
					'group': 'expression',
					'description': 'Assign and add value to a variable',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'-=': {
					'name': None,
					'group': 'expression',
					'description': 'Subtract and assign value to a variable',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'*=': {
					'name': None,
					'group': 'expression',
					'description': 'Multiply and assign value to a variable',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'/=': {
					'name': None,
					'group': 'expression',
					'description': 'Divide and assign value to a variable',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'%=': {
					'name': None,
					'group': 'expression',
					'description': 'Modulo and assign value to a variable',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'~=': {
					'name': None,
					'group': 'expression',
					'description': 'Elevation and assign value to a variable',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'!=': {
					'name': None,
					'group': 'expression',
					'description': 'Check if values are not equal',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'&=': {
					'name': None,
					'group': 'expression',
					'description': 'Bitwise AND and assign value to a variable',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'|=': {
					'name': None,
					'group': 'expression',
					'description': 'Bitwise OR and assign value to a variable',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'^=': {
					'name': None,
					'group': 'expression',
					'description': 'Bitwise XOR and assign value to a variable',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'>>=': {
					'name': None,
					'group': 'expression',
					'description': 'Right shift and assign value to a variable',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'<<=': {
					'name': None,
					'group': 'expression',
					'description': 'Left shift and assign value to a variable',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'==': {
					'name': None,
					'group': 'expression',
					'description': 'Checks if left value is equal to right',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'>': {
					'name': None,
					'group': 'expression',
					'description': 'Checks if left value is greater than right',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'<': {
					'name': None,
					'group': 'expression',
					'description': 'Checks if left value is less than right',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'<=': {
					'name': None,
					'group': 'expression',
					'description': 'Checks if left value is less than or equal to right',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'>=': {
					'name': None,
					'group': 'expression',
					'description': 'Checks if left value is greater than or equal to right',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'not': {
					'name': None,
					'group': 'expression',
					'description': 'Logical NOT operation',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'and': {
					'name': None,
					'group': 'expression',
					'description': 'Logical AND operation',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'or': {
					'name': None,
					'group': 'expression',
					'description': 'Logical OR operation',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'xor': {
					'name': None,
					'group': 'expression',
					'description': 'Logical XOR operation',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'in': {
					'name': None,
					'group': 'expression',
					'description': 'Checks if value is in a list or name in a dictionary',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': []
				},
				'not in': {
					'name': None,
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
						{'name': 'name', 'type': 'str', 'default': None}
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
						{'name': 'name', 'type': 'str', 'default': None}
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
	}

	# value

	def get(name: str = '', default = None, data = None):
			pass

	def set(name: str, value = None, data = None):
		pass

	def remove(name: str, data = None):
		pass

	def type(data):
		pass

	def type_text(data):
		pass

	def type_int(data):
		try:
			return int(data)
		except:
			return 0

	def type_float(data):
		try:
			return float(data)
		except:
			return 0.0

	def type_number(data):
		result = void.type_float(data)
		return result if result % 1 != 0 else int(result)

	def type_bool(data):
		return data not in [0, '0', b'0', False, None, [], {}]

	def type_list(data):
		return list(data) if type(data) is list else [data]

	def type_dict(data):
		if type(data) is dict:
			return dict(data)
		if type(data) is list:
			result = {}
			for value in data:
				if type(value) is list and len(value) == 2:
					result[value[0]] = value[1]
				else:
					result[len(result)] = value
		return {'value': data}

	def type_binary(data):
		if type(data) is str:
			return data.decode()
		if type(data) is bytes:
			return data
		return void.text(data).decode()

	def n(data):
		pass

	# control

	def print(data, end: str ='\n'):
		result = None
		data_type = type(data)
		if data_type is str:
			result = data
		elif data_type in [int, float, bool, bytes]:
			result = str(data)
		elif data_type in [dict, list]:
			result = void.void_encode(data, '  ')
		print(result, end=end)

	def input(text: str = None):
		pass

	def condition():
		pass

	def loop():
		pass

	def loop_break():
		pass

	def loop_continue():
		pass

	def loop_repeat():
		pass

	def action_return():
		pass

	def action(action):
		result = None
		if type(action) is not list:
			action = [action]
		actions = void.data['description']['action']
		for action in action:
			if type(action) is not list:
				action = [action]
			if len(action) == 0:
				continue
			name = action[0]
			if name in actions:
				info = actions[name]
				params = action[1:]
				if 'param' in info:
					index = 0
					skip = False
					for param in info['param']:
						if index >= len(params):
							if 'default' in param:
								params.append(param['default'])
								index += 1
								continue
							else:
								skip = True
								break
						value = params[index]
						match param['type']:
							case 'str':
								value = str(value)
							case 'number':
								value = float(value)
								if value % 1 == 0:
									value = int(value)
							case 'int':
								value = int(value)
							case 'float':
								value = float(value)
							case 'bool':
								value = bool(value)
							case 'list':
								if type(value) is str:
									value = list(void.json_decode(value))
							case 'dict':
								if type(value) is str:
									value = dict(void.json_decode(value))
						params[index] = value
						index += 1
					if skip:
						continue
				if 'name' in info:
					method = getattr(void, info['name'])
					result = method(*params)
		return result

	def open(text: str):
		pass

	def code(text: str):
		exec(text)

	def exit(code = 0):
		if type(code) is not int:
			void.print(code)
			exit(-1)
		exit(code)

	def l(name: str, data):
		pass

	def convert(name_from: str, name_to: str, value = None):
		pass

	def export():
		pass

	def update(name: str = None):
		pass

	def test(name: str = None):
		actions = void.data['description']['action']
		if name in actions:
			actions = {name: actions[name]}
		for name in actions:
			action = actions[name]
			if 'example' not in action:
				continue
			for example in action['example']:
				if 'test' in example and not example['test']:
					continue
				code = list(example['code'])
				if 'before' in example:
					code = list(example['before']) + code
				if 'after' in example:
					code += list(example['after'])
				result = void.action(code)
				if 'round' in example:
					result = round(result, example['round'])
				if 'result' in example:
					error = False
					match example['result']:
						case 'str':
							if type(result) is not str:
								error = True
						case 'number':
							if type(result) not in [int, float]:
								error = True
						case 'bool':
							if type(result) is not bool:
								error = True
						case 'dict':
							if type(result) is not dict:
								error = True
						case 'list':
							if type(result) is not list:
								error = True
						case 'none':
							if result != None:
								error = True
						case _:
							if result != example['result']:
								error = True
					if error:
						void.exit({
							'action': name,
							'expect': example['result'],
							'found': result
							})
		void.print('ok')

	def help(name: str = None):
		result = dict(void.data['description'])
		if name != None:
			if name in result['action']:
				result['action'] = {name: result['action'][name]}
			else:
				void.print({
					'action': name,
					'error': 'not found'
					})
				return
		void.print(result)

	def void(name: str, action = None):
		pass

	# text

	def lower(text: str):
		return text.lower()

	def upper(text: str):
		return text.upper()

	def starts(text: str, subtext: str):
		return text.startswith(subtext)

	def ends(text: str, subtext: str):
		return text.endswith(subtext)

	def strip():
		pass

	def strip_start():
		pass

	def strip_end():
		pass

	def replace():
		pass

	def find(text: str, subtext: str):
		pass

	def parse(text: str, format: str):
		pass

	def similar(first: str, second: str):
		return SequenceMatcher(None, first, second).ratio()

	def part():
		pass

	def split():
		pass

	def join():
		pass

	def date(time: float, format: dict):
		pass

	def escape(text, symbol, replace = None):
		pass

	def escape_html(text: str):
		pass

	def escape_url(text: str):
		pass

	def escape_sql(text: str):
		pass

	def unescape():
		pass

	def unescape_html(text: str):
		pass

	def unescape_url(text: str):
		pass

	def unescape_sql(text: str):
		pass

	def letters(text: str):
		return void.find(text, '{letter}')

	def words(text: str):
		return void.find(text, '{word}')['count']

	def sentences(text: str):
		return void.find(text, ['{letter}.', '\n'])['count']

	def lines(text: str):
		return void.find(text, '\n')['count']

	def bytes(text: str):
		return len(text.decode())

	# list

	def merge(first, second):
		if type(first) is dict and type(second) is dict:
			result = dict(first)
			for name in second:
				if name in result:
					if (type(result[name]) is dict and type(second[name]) is dict) or (type(result[name]) is list and type(second[name]) is list):
						result[name] = void.merge(result[name], second[name])
					else:
						result[name] = second[name]
				else:
					result[name] = second[name]
			return result
		elif type(first) is list and type(second) is list:
			result = []
			for item1, item2 in zip(first, second):
				if (type(item1) is dict and type(item2) is dict) or (type(item1) is list and type(item2) is list):
					result.append(void.merge(item1, item2))
				else:
					result.append(item2)
			result.extend(first[len(result):])
			result.extend(second[len(result):])
			return result

	def push(list: list, data, position: int = None):
		pass

	def pop(list: list, position: int = None):
		pass

	def reverse(list: list):
		pass

	def shuffle(list: list):
		pass

	def map(list: list, action):
		pass

	def reduce(list: list, action):
		pass

	def names(dict: dict):
		pass

	def values(dict: dict):
		pass

	# math

	def sin(value: float):
		return math.sin(value)

	def cos(value: float):
		return math.cos(value)

	def tan(value: float):
		return math.tan(value)

	def sinh(value: float):
		return math.sinh(value)

	def cosh(value: float):
		return math.cosh(value)

	def tanh(value: float):
		return math.tanh(value)

	def asin(value: float):
		return math.asin(value)

	def acos(value: float):
		return math.acos(value)

	def atan(value: float):
		return math.atan(value)

	def asinh(value: float):
		return math.asinh(value)

	def acosh(value: float):
		return math.acosh(value)

	def atanh(value: float):
		return math.atanh(value)

	def round(value: float, dot: int = 0):
		return math.round(value, dot)

	def floor(value: float):
		return math.floor(value)

	def ceil(value: float):
		return math.ceil(value)

	def log(value: float, base: float = None):
		return math.log(value) if base == None else math.log(value, base)

	def factorial(value: float):
		return math.factorial(value)

	def fibonacci(value: int):
		if value <= 0:
			return 0
		elif value == 1:
			return 1
		a, b = 0, 1
		for _ in range(2, value + 1):
			a, b = b, a + b
		return b

	def gold():
		pass

	def abs(value: float):
		return abs(value)

	def min(value: list):
		return min(value)

	def max(value: list):
		return max(value)

	def avg(value: list):
		if len(value) == 0:
			return 0
		return void.sum(value) / float(len(value))

	def sum(value: list):
		result = 0
		for value in value:
			if type(value) in [int, float]:
				result += value
		return result

	def random(value = None, to = None):
		if value == None and to == None:
			return random.random()
		if value != None and to != None:
			if type(value) is int and type(to) is int:
				return random.randint(value, to)
			return random.uniform(value, to)
		if value == None and to != None:
			value = to
			to = None
		if value != None and to == None:
			if type(value) is int:
				return random.randint(0, value)
			return random.uniform(0, value)

	def random_seed(seed = None):
		if seed == None:
			return random.getstate()
		return random.setstate(seed)

	# time

	def t(name: str = None):
		pass

	def time(dot: int = 6):
		result = time.time()
		if dot >= 0:
			result = round(result, dot)
		else:
			result = round(result * (10 ** dot))
		return result

	def timer(action, seconds: float = 1, name: str = None):
		pass

	def timer_remove(name: str):
		pass

	def timepast(time: float = None):
		pass

	def wait(seconds: float = 1):
		wait(seconds)

	# encrypt

	def encrypt(data, key: str = None):
		pass

	def decrypt(data, key: str):
		pass

	def hash(length: str = 64, symbols = None):
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

	def base64_encode():
		pass

	def base64_decode():
		pass

	def gzip_encode():
		pass

	def gzip_decode():
		pass

	def rsa_encode():
		pass

	def rsa_decode():
		pass

	def rsa_public():
		pass

	def rsa_private():
		pass

	def ssl_encode():
		pass

	def ssl_decode():
		pass

	def ssl_check():
		pass

	def bcrypt_encode():
		pass

	def bcrypt_check():
		pass

	# file

	def file(path: str, data = None):
		pass

	def file_exists(path: str):
		pass

	def file_read(path: str, start: int = None, length: int = None):
		with open(path, 'rb') as file:
			return file.read()

	def file_read_text(path: str, encoding: str = 'utf-8'):
		with open(path, 'r', encoding=encoding) as file:
			return file.read()

	def file_read_lines(path: str, encoding: str = 'utf-8', newline: str = '\n'):
		with open(path, 'r', encoding=encoding) as file:
			return file.read().split(newline)

	def file_write(path: str, data = b''):
		if type(data) is not bytes:
			with open(path, 'w') as file:
				file.write(str(data))
		else:
			with open(path, 'wb') as file:
				file.write(data)

	def file_append(path: str, data):
		pass

	def file_remove(path: str):
		pass

	def file_move(path: str):
		pass

	def file_copy(path: str):
		pass

	def file_rename(path: str):
		pass

	def file_link(path: str):
		pass

	def file_link_exists(path: str):
		pass

	def file_info(path: str):
		pass

	def file_size(path: str):
		pass

	def file_permission(path: str):
		pass

	def file_time(path: str):
		pass

	def file_sha256(path: str):
		pass

	def file_crc32(path: str):
		pass

	def file_base64(path: str):
		pass

	def file_zip(path: str):
		pass

	def file_zip_list(path: str):
		pass

	def file_zip_exists(path: str):
		pass

	def file_zip_read(path: str):
		pass

	def file_zip_remove(path: str):
		pass

	def file_unzip(path: str):
		pass

	def file_gzip(path: str):
		pass	

	def file_ungzip(path: str):
		pass

	def file_void(path: str, key: str = None):
		pass

	def file_unvoid(path: str, key: str = None):
		pass

	# dir

	def dir_exists(path: str):
		pass

	def dir_create(path: str):
		pass

	def dir_copy(path: str):
		pass

	def dir_move(path: str):
		pass

	def dir_rename(path: str):
		pass

	def dir_remove(path: str):
		pass

	def dir_list(path: str):
		pass

	def dir_clear(path: str):
		pass

	def dir_info(path: str):
		pass

	def dir_size(path: str):
		pass

	def dir_permission(path: str):
		pass

	def dir_time(path: str):
		pass

	def dir_zip(path: str):
		pass

	def dir_void(path: str):
		pass

	# drive

	def drive_list():
		result = []
		for drive in psutil.disk_partitions():
			result.append({
				'name': drive[0],
				'path': drive[1],
				'type': drive[2]
				})
		return result

	def drive_name(path: str):
		pass

	def drive_size(path: str):
		return psutil.disk_usage(path)[0]

	def drive_used(path: str):
		return psutil.disk_usage(path)[1]

	def drive_free(path: str):
		return psutil.disk_usage(path)[2]

	def drive_info(path: str):
		pass

	def drive_mount(path: str):
		pass

	def drive_unmount(path: str):
		pass

	def drive_create(path: str):
		pass

	def drive_resize(path: str):
		pass

	def drive_format(path: str):
		pass

	def drive_remove(path: str):
		pass

	# path

	def path_drive(path: str):
		if void.os('windows'):
			part = path.split(':')
			if len(part) > 1:
				return part[0].lower()

	def path_dir(path: str):
		return os.path.dirname(path)

	def path_file(path: str):
		return os.path.basename(path)

	def path_name(path: str):
		basename = os.path.basename(path)
		dot = basename.rfind('.')
		return basename[0:dot] if dot > 0 else basename

	def path_extension(path: str):
		index = path.rfind('.')
		return path[index + 1:] if index >= 0 and len(path) > (index + 1) else ''

	def path_strip(path: str, strip: str = None):
		if strip != None:
			return path.rstrip('.' + strip)
		index = path.rfind('.')
		if index != -1:
			return path[:index]
		return path

	# format

	def void_encode(data, indent: str = '\t', level: int = 0):
		result = ''
		short = indent == None
		indent_current = indent * level if not short else ''
		match data:
			case str():
				if not short:
					result += indent_current + data + '\n'
				else:
					if len(data) > 0:
						result += (f'"{data}"' if (data.count(' ') > 1 or data[0] == '*') else data.replace(' ', '\\ ')) + ' '
					else:
						result += ' '
			case bool():
				data = 'true' if data else 'false'
				if not short:
					result += indent_current + data + '\n'
				else:
					result += data + ' '
			case int():
				if not short:
					result += indent_current + f'{data:,}'.replace(',', ' ') + '\n'
				else:
					result += f'{data}' + ' '
			case float():
				if not short:
					result += indent_current + f'{data:,}'.replace(',', ' ') + '\n'
				else:
					result += f'{data}' + ' '
			case bytes():
				if not short:
					result += indent_current + '*\n' + indent_current + indent + void.base64_encode(data) + '\n'
				else:
					result += '*' + void.base64_encode(data) + ' '
			case list():
				if not short:
					text_short = void.void_encode(data, None)
					if len(text_short) > 80:
						for value in data:
							result += void.void_encode(value, indent, level + 1).rstrip(']"') + '\n'
					else:
						result += indent_current + text_short + '\n'
				else:
					if len(data) > 0:
						result += '['
						for value in data:
							result += void.void_encode(value, None) + ' '
						result = result[:-1] + '] '
					else:
						result += '[] '
			case dict():
				if not short:
					for name in data:
						value = data[name]
						result += indent_current + name + '\n'
						result += void.void_encode(value, indent, level + 1).rstrip(']"') + '\n'
				else:
					if len(data) > 0:
						result += '['
						for name in data:
							value = data[name]
							result += void.void_encode(str(name), None) + ':' + void.void_encode(value, None) + ' '
						result = result[:-1] + '] '
					else:
						result += '[] '
			case None:
				data = 'none'
				if not short:
					result += indent_current + data + '\n'
				else:
					result += data + ' '
			case _:
				if not short:
					result += '\n'
				else:
					result += ' '
		return result[:-1]

	def void_decode(text: str):
		pass

	def json_encode(data, indent: str = '\t', separators: tuple = None):
		try:
			if separators != None:
				if indent not in ['', None]: 
					separators = (', ', ': ')
				else:
					separators = (',', ':')
			return json.dumps(data, ensure_ascii=False, indent=indent, separators=separators)
		except:
			return ''

	def json_decode(text: str):
		try:
			return json.loads(text)
		except:
			return None

	def csv_encode(data):
		pass

	def csv_decode(text: str):
		pass

	def yaml_encode(text: str):
		pass

	def yaml_decode(text: str):
		pass

	def ini_encode(text: str):
		pass

	def ini_decode(text: str):
		pass

	def html_encode(text: str):
		pass

	def html_decode(text: str):
		pass

	def html_markdown(text: str):
		pass

	def xml_encode(text: str):
		pass

	def xml_decode(text: str):
		pass

	def css_encode(text: str):
		pass

	def css_decode(text: str):
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

	# download

	def download():
		pass

	def download_info():
		pass

	def download_audio():
		pass

	def download_video():
		pass

	# cookie

	def cookie(name: str, value = None):
		pass

	def cookie_remove(name: str):
		pass

	# cloud

	def cloud():
		pass

	def cloud_file():
		pass

	def cloud_web():
		pass

	def cloud_api():
		pass

	def cloud_socket():
		pass

	def cloud_mail():
		pass	

	def cloud_proxy():
		pass

	# bot

	def bot_telegram():
		pass

	def bot_discord():
		pass

	def bot_wechat():
		pass

	# social

	def social_x():
		pass

	def social_youtube():
		pass

	def social_tiktok():
		pass

	# notification

	def notification(token: str, text: str, badge = None, image = None):
		pass

	def mail(address_from: str, address_to: str, text: str, subject: str = None, attach = None):
		pass

	def call():
		pass

	def sms():
		pass

	# sql

	def sql(query, data = None):
		pass

	# os

	def os(name: str = None):
		if name == None:
			return data['os']['type']
		return data['os']['type'] == name

	def os_version():
		pass

	def os_user():
		user = psutil.users()[0]
		return {
			'name': user.name,
			'terminal': user.terminal,
			'host': user.host,
			'pid': user.pid,
			'time': {
				'started': user.started,
				'passed': time.time() - user.started
			}
		}

	def language():
		pass

	# device

	def device():
		cpu_used = psutil.getloadavg()
		memory = psutil.virtual_memory()
		swap = psutil.swap_memory()
		network = {
			'connection': [],
			'interface': []
		}
		temperature = None
		fan = None
		battery = None
		if hasattr(psutil, 'net_connections'):
			for connection in psutil.net_connections():
				network['connection'].append({
					'socket': connection[0],
					'family': connection[1],
					'type': connection[2],
					'local': {
						'ip': connection[3][0] if len(connection[3]) > 0 else None,
						'port': connection[3][1] if len(connection[3]) > 1 else None
					},
					'remote': {
						'ip': connection[4][0] if len(connection[4]) > 0 else None,
						'port': connection[4][1] if len(connection[4]) > 1 else None
					},
					'status': connection[5],
					'pid': connection[6]
					})
		if hasattr(psutil, 'net_if_addrs'):
			interfaces = psutil.net_if_addrs()
			for name in interfaces:
				protocol = []
				for interface in interfaces[name]:
					protocol.append({
						'family': interface[0],
						'address': interface[1],
						'mask': interface[2],
						'broadcast': interface[3],
						'ptp': interface[4]
						})
				network['interface'].append({
					'name': name,
					'list': protocol
					})
		if hasattr(psutil, 'sensors_temperatures'):
			sensor = psutil.sensors_temperatures()
			if len(sensor) > 0:
				temperature = []
				for sensor in sensor:
					temperature.append({
						'name': sensor[0],
						'current': sensor[1],
						'high': sensor[2],
						'critical': sensor[3]
						})
		if hasattr(psutil, 'sensors_battery'):
			sensor = psutil.sensors_fans()
			for name in sensor:
				fan.append({
					'name': name,
					'current': sensor[name]
					})
		if hasattr(psutil, 'sensors_battery'):
			sensor = psutil.sensors_battery()
			if sensor != None:
				battery = {
					'percent': sensor[0],
					'time': sensor[1],
					'power': sensor[2]
				}
		return {
			'cpu': {
				'name': platform.processor(),
				'count': psutil.cpu_count(logical=False),
				'threads': psutil.cpu_count(logical=True),
				'frequency': psutil.cpu_freq()[0],
				'used': {
					'current': psutil.cpu_percent(0),
					'1m': cpu_used[0],
					'5m': cpu_used[1],
					'15m': cpu_used[2]
				}
			},
			'memory': {
				'size': memory[0],
				'used': memory[3],
				'free': memory[1]
			},
			'swap': {
				'size': swap[0],
				'used': swap[1],
				'free': swap[2]
			},
			'network': network,
			'time': {
				'started': psutil.boot_time(),
				'passed': time.time() - psutil.boot_time()
			},
			'sensor': {
				'temperature': temperature,
				'fan': fan,
				'battery': battery
			},
			'screen': {
				'size': '',
				'rate': '',
				'orientation': '',
				'dpi': '',
				'darkmode': '',
				'touchscreen': ''
			}
		}

	def cpu(seconds: float = 0):
		return psutil.cpu_percent(seconds)

	def fps():
		pass

	def vsync():
		pass

	def resolution():
		pass

	def orientation(name = None):
		pass

	def darkmode():
		pass

	def pixel():
		pass

	def textmode_character():
		pass

	def textmode_cursor():
		pass

	def textmode_clear():
		pass

	def flashlight():
		pass

	def location():
		pass

	def gyroscope():
		pass

	def accelerometer():
		pass

	def compass():
		pass

	def proximity():
		pass

	def brightness():
		pass

	def calendar():
		pass

	def gallery():
		pass

	def contacts():
		pass

	# clipboard

	def clipboard(value = None):
		pass

	def clipboard_remove():
		pass

	# ai

	def translate():
		pass

	def spellcheck():
		pass

	def chat():
		pass

	def image():
		pass

	def image_size():
		pass

	def image_square():
		pass

	def image_crop():
		pass

	def image_rotate():
		pass

	def image_text():
		pass

	def image_image():
		pass

	def image_grayscale():
		pass

	def image_tint():
		pass

	def image_flip_h():
		pass

	def image_flip_v():
		pass

	def image_upscale():
		pass

	def image_draw():
		pass

	def image_style():
		pass

	def image_colorize():
		pass

	def image_recognize():
		pass

	def image_face():
		pass

	def image_effect():
		pass

	def video():
		pass

	def video_crop():
		pass

	def video_text():
		pass

	def video_image():
		pass

	def video_sound():
		pass

	def video_video():
		pass

	def video_trim():
		pass

	def video_size():
		pass

	def video_upscale():
		pass

	def video_speed():
		pass

	def video_volume():
		pass

	def video_mute():
		pass

	def video_face():
		pass

	def video_effect():
		pass

	def sound():
		pass

	def sound_trim():
		pass

	def sound_speed():
		pass

	def sound_volume():
		pass

	def sound_effect():
		pass

	def music():
		pass

	def voice(text: str = None, voice: str = None):
		pass

	def voice_list():
		pass

	def voice_recognize():
		pass

	def voice_stop():
		pass

	def voice_capture():
		pass

	def motion():
		pass

	def motion_capture():
		pass

	# google

	def google_voice():
		pass

	def google_voice_list():
		pass

	def google_voice_recognize():
		pass

	def google_translate():
		pass

	# deepl

	def deepl_translate():
		pass

	# openai

	def openai_chat():
		pass

	def openai_image():
		pass

	def openai_video():
		pass

	def openai_translate():
		pass

	# deepseek

	def deepseek_chat():
		pass

	def deepseek_translate():
		pass

	# claude

	def claude_chat():
		pass

	# stablediffusion

	def stablediffusion_image(text: str, size = None):
		pass

	def stablediffusion_upscale():
		pass

	def stablediffusion_draw():
		pass

	def stablediffusion_background():
		pass

	def stablediffusion_video(text: str):
		pass

	# ollama

	def ollama_chat(text: str):
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

	def enable():
		pass

	def disable():
		pass

	def focus():
		pass

	def unfocus():
		pass

	def scale():
		pass

	def ui_text():
		pass

	def ui_image():
		pass

	def ui_video():
		pass

	def ui_sound():
		pass

	def ui_camera():
		pass

	def ui_draw():
		pass

	def ui_header():
		pass

	def ui_footer():
		pass

	def ui_wait():
		pass

	def ui_gallery():
		pass

	def ui_button():
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

	def ui_divider():
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

	def ui_menu():
		pass

	def ui_menu_context():
		pass

	def window():
		pass

	def window_list():
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

	def nofocus():
		pass

	def noresize():
		pass

	def center():
		pass

	def fullscreen():
		pass

	def maximize():
		pass

	def minimize():
		pass

	def exclusive():
		pass

	def border():
		pass

	def filedrop():
		pass

	def dialog():
		pass

	def dialog_file():
		pass

	def effect():
		pass

	def effect_remove():
		pass

	#input

	def tap():
		pass

	def key():
		pass

	def key_remove():
		pass

	def key_enable():
		pass

	def key_disable():
		pass

	def key_press():
		pass

	def keyboard():
		pass

	def mouse():
		pass

	def mouse_lock():
		pass

	def mouse_position():
		pass

	def mouse_shape():
		pass

	def gamepad():
		pass

	def gamepad_vibrate():
		pass

	# game

	def game():
		pass

	# run

	def run():
		void.t('run')
		arguments = sys.argv[1:]
		void.set('app.name', sys.argv[0])
		void.set('app.path', os.getcwd())
		void.set('app.argument', arguments)
		result = None
		if len(arguments) > 0:
			text = arguments[0]
			if text in void.data['description']['action']:
				result = void.action([arguments])
			elif void.path_extension(text) == 'py':
				text = void.file_read_text(text)
				void.code(text)
			else:
				if void.path_extension(text) in ['json', 'void']:
					action = file(text)
				else:
					action = void.json_decode(text.replace("'", '"'))
				if action != None and len(action) > 0:
					if type(action) in [str, list]:
						result = void.action(action)
					elif type(action) is dict:
						void.data = void.merge(void.data, action)
						if 'run' in void.data and type(void.data['run']) is list:
							result = void.action(void.data['run'])
		if result not in ['', None]:
			void.print(result)

if __name__ == '__main__':
	void.run()