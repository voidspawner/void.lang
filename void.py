import os
import sys
import psutil
import platform
import time
import json
import math
import string
import random
import hashlib
import base64

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
					'safe': True,
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'param': [
						{'name': 'name', 'type': 'text', 'default': None}
					],
					'example': [
						{'code': [['get', 'description.about.name']], 'result': 'V O I D lang'}
					] 
				},
				'set': {
					'name': 'set',
					'group': 'value',
					'description': 'Assign a value to a specified parameter',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [
							['set', 'some.value', 1],
							['get', 'some.value'],
						], 'result': 1},						
						{'code': [
							['set', 'some.text', ':)'],
							['get', 'some.text'],
						], 'result': ':)'}
					]
				},
				'remove': {
					'name': 'remove',
					'group': 'value',
					'description': 'Remove a specified parameter or value',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [
							['set', 'some.value', 1],
							['remove', 'some.value'],
							['get', 'some.value']
						], 'result': None}
					]
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
					'example': [
						{'code': [['text', 123]], 'result': '123'},
						{'code': [['text', 'title', {
							'length': 10,
							'align': 'center'
						}]], 'result': '  title   '},
						{'code': [['text', 100000.1, {
							'before': '∞',
							'after': ' monthly',
							'group': ',',
							'fraction': '.',
							'dot': 3
						}]], 'result': '∞100,000.100 monthly'},
						{'code': [['text', 100000, 'price']], 'result': '∞100 000'}
					]
				},
				'number': {
					'name': 'type_number',
					'group': 'value',
					'description': 'Specify a parameter as a number type',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['number', '123']], 'result': 123},
						{'code': [['number', 45.67]], 'result': 45.67}
					]
				},
				'bool': {
					'name': 'type_bool',
					'group': 'value',
					'description': 'Specify a parameter as a boolean type',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['bool', 1]], 'result': True},
						{'code': [['bool', 'false']], 'result': False},
						{'code': [['bool', None]], 'result': False},
						{'code': [['bool', 'none']], 'result': False}
					]
				},
				'list': {
					'name': 'type_list',
					'group': 'value',
					'description': 'Specify a parameter as a list type',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['list', 123]], 'result': [123]},
						{'code': [['list', 'a']], 'result': ['a']},
						{'code': [['list', [123, 'a']]], 'result': [123, 'a']}
					]
				},
				'dict': {
					'name': 'type_dict',
					'group': 'value',
					'description': 'Specify a parameter as a dictionary type',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['dict', [['key', 'value']]]], 'result': {'key': 'value'}},
						{'code': [['dict', [['a', 1], ['b', 2]]]], 'result': {'a': 1, 'b': 2}},
						{'code': [['dict', {'a': 1}]], 'result': {'a': 1}}
					]
				},
				'binary': {
					'name': 'type_binary',
					'group': 'value',
					'description': 'Specify a parameter as a binary type',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['binary', 'a']], 'result': b'a'},
						{'code': [['binary', 1]], 'result': b'1'}
					]
				},
				'n': {
					'name': 'n',
					'group': 'value',
					'description': 'Gets the length of the text, the number of items in a list or dictionary',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['n', 'text']], 'result': 4},
						{'code': [['n', [1, 2, 'a']]], 'result': 3},
						{'code': [['n', {'a': 1, 'b': 2}]], 'result': 2},
						{'code': [['n', 123]], 'result': 0}
					]
				},
				'+': {
					'name': None,
					'group': 'expression',
					'description': 'Perform addition operation',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['+', 2, 3]], 'result': 5},
						{'code': [['+', 'a', 'b']], 'result': 'ab'},
						{'code': [['+', ['a'], ['b']]], 'result': ['a', 'b']},
						{'code': [['+', {'a': 1, 'b': {'c': 3}}, {'c': 5}]], 'result': {'a': 1, 'b': {'c': 5}}},
					]
				},
				'-': {
					'name': None,
					'group': 'expression',
					'description': 'Perform subtraction operation',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['-', 5, 2]], 'result': 3},
						{'code': [['-', 10]], 'result': -10}
					]
				},
				'*': {
					'name': None,
					'group': 'expression',
					'description': 'Perform multiplication operation',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['*', 3, 4]], 'result': 12},
						{'code': [['*', 'a', 3]], 'result': 'aaa'}
					]
				},
				'/': {
					'name': None,
					'group': 'expression',
					'description': 'Perform division operation',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['/', 10, 2]], 'result': 5},
						{'code': [['/', 7, 2]], 'result': 3.5}
					]
				},
				'%': {
					'name': None,
					'group': 'expression',
					'description': 'Perform modulo operation',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['%', 10, 3]], 'result': 1},
						{'code': [['%', 15, 4]], 'result': 3}
					]
				},
				'~': {
					'name': None,
					'group': 'expression',
					'description': 'Elevation operator',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['~', 2, 3]], 'result': 8},
						{'code': [['~', 10, 0]], 'result': 1},
						{'code': [['~', 4, 0.5]], 'result': 2}
					]
				},
				'!': {
					'name': None,
					'group': 'expression',
					'description': 'Perform logical negation',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['!', True]], 'result': False},
						{'code': [['!', False]], 'result': True}
					]
				},
				'&': {
					'name': None,
					'group': 'expression',
					'description': 'Perform bitwise AND operation',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['&', 5, 3]], 'result': 1},
						{'code': [['&', 12, 7]], 'result': 4}
					]
				},
				'|': {
					'name': None,
					'group': 'expression',
					'description': 'Perform bitwise OR operation',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['|', 5, 3]], 'result': 7},
						{'code': [['|', 12, 7]], 'result': 15}
					]
				},
				'^': {
					'name': None,
					'group': 'expression',
					'description': 'Perform bitwise XOR operation',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['^', 5, 3]], 'result': 6},
						{'code': [['^', 12, 7]], 'result': 11}
					]
				},
				'>>': {
					'name': None,
					'group': 'expression',
					'description': 'Perform right bitwise shift operation',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['>>', 16, 2]], 'result': 4},
						{'code': [['>>', 255, 4]], 'result': 15}
					]
				},
				'<<': {
					'name': None,
					'group': 'expression',
					'description': 'Perform left bitwise shift operation',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['<<', 4, 2]], 'result': 16},
						{'code': [['<<', 7, 3]], 'result': 56}
					]
				},
				'=': {
					'name': None,
					'group': 'expression',
					'description': 'Assign value to a variable',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['=', 'x', 10]], 'result': 10},
						{'code': [['=', 'name', 'John']], 'result': 'John'}
					]
				},
				'+=': {
					'name': None,
					'group': 'expression',
					'description': 'Add and assign value to a variable',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['=', 'x', 5], ['+=', 'x', 3]], 'result': 8},
						{'code': [['=', 's', 'a'], ['+=', 's', 'b']], 'result': 'ab'}
					]
				},
				'=+': {
					'name': None,
					'group': 'expression',
					'description': 'Assign and add value to a variable',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['=+', 'x', 5, 3]], 'result': 8},
						{'code': [['=+', 's', 'a', 'b']], 'result': 'ab'}
					]
				},
				'-=': {
					'name': None,
					'group': 'expression',
					'description': 'Subtract and assign value to a variable',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['=', 'x', 10], ['-=', 'x', 4]], 'result': 6},
						{'code': [['=', 'y', 7.5], ['-=', 'y', 2.5]], 'result': 5.0}
					]
				},
				'*=': {
					'name': None,
					'group': 'expression',
					'description': 'Multiply and assign value to a variable',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['=', 'x', 3], ['*=', 'x', 4]], 'result': 12},
						{'code': [['=', 's', 'a'], ['*=', 's', 3]], 'result': 'aaa'}
					]
				},
				'/=': {
					'name': None,
					'group': 'expression',
					'description': 'Divide and assign value to a variable',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['=', 'x', 10], ['/=', 'x', 2]], 'result': 5},
						{'code': [['=', 'y', 7], ['/=', 'y', 2]], 'result': 3.5}
					]
				},
				'%=': {
					'name': None,
					'group': 'expression',
					'description': 'Modulo and assign value to a variable',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['=', 'x', 10], ['%=', 'x', 3]], 'result': 1},
						{'code': [['=', 'y', 15], ['%=', 'y', 4]], 'result': 3}
					]
				},
				'~=': {
					'name': None,
					'group': 'expression',
					'description': 'Elevation and assign value to a variable',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['=', 'x', 2], ['~=', 'x', 3]], 'result': 8},
						{'code': [['=', 'y', 5], ['~=', 'y', 0]], 'result': 1}
					]
				},
				'!=': {
					'name': None,
					'group': 'expression',
					'description': 'Check if values are not equal',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['!=', 5, 3]], 'result': True},
						{'code': [['!=', 'a', 'a']], 'result': False}
					]
				},
				'&=': {
					'name': None,
					'group': 'expression',
					'description': 'Bitwise AND and assign value to a variable',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['=', 'x', 5], ['&=', 'x', 3]], 'result': 1},
						{'code': [['=', 'y', 12], ['&=', 'y', 7]], 'result': 4}
					]
				},
				'|=': {
					'name': None,
					'group': 'expression',
					'description': 'Bitwise OR and assign value to a variable',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['=', 'x', 5], ['|=', 'x', 3]], 'result': 7},
						{'code': [['=', 'y', 12], ['|=', 'y', 7]], 'result': 15}
					]
				},
				'^=': {
					'name': None,
					'group': 'expression',
					'description': 'Bitwise XOR and assign value to a variable',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['=', 'x', 5], ['^=', 'x', 3]], 'result': 6},
						{'code': [['=', 'y', 12], ['^=', 'y', 7]], 'result': 11}
					]
				},
				'>>=': {
					'name': None,
					'group': 'expression',
					'description': 'Right shift and assign value to a variable',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['=', 'x', 16], ['>>=', 'x', 2]], 'result': 4},
						{'code': [['=', 'y', 255], ['>>=', 'y', 4]], 'result': 15}
					]
				},
				'<<=': {
					'name': None,
					'group': 'expression',
					'description': 'Left shift and assign value to a variable',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['=', 'x', 4], ['<<=', 'x', 2]], 'result': 16},
						{'code': [['=', 'y', 7], ['<<=', 'y', 3]], 'result': 56}
					]
				},
				'==': {
					'name': None,
					'group': 'expression',
					'description': 'Checks if left value is equal to right',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['==', 5, 5]], 'result': True},
						{'code': [['==', 'a', 'b']], 'result': False}
					]
				},
				'>': {
					'name': None,
					'group': 'expression',
					'description': 'Checks if left value is greater than right',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['>', 5, 3]], 'result': True},
						{'code': [['>', 2, 4]], 'result': False}
					]
				},
				'<': {
					'name': None,
					'group': 'expression',
					'description': 'Checks if left value is less than right',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['<', 3, 5]], 'result': True},
						{'code': [['<', 4, 2]], 'result': False}
					]
				},
				'<=': {
					'name': None,
					'group': 'expression',
					'description': 'Checks if left value is less than or equal to right',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['<=', 3, 5]], 'result': True},
						{'code': [['<=', 5, 5]], 'result': True},
						{'code': [['<=', 6, 5]], 'result': False}
					]
				},
				'>=': {
					'name': None,
					'group': 'expression',
					'description': 'Checks if left value is greater than or equal to right',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['>=', 5, 3]], 'result': True},
						{'code': [['>=', 5, 5]], 'result': True},
						{'code': [['>=', 4, 5]], 'result': False}
					]
				},
				'not': {
					'name': None,
					'group': 'expression',
					'description': 'Logical NOT operation',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['not', True]], 'result': False},
						{'code': [['not', False]], 'result': True}
					]
				},
				'and': {
					'name': None,
					'group': 'expression',
					'description': 'Logical AND operation',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['and', True, False]], 'result': False},
						{'code': [['and', True, True]], 'result': True}
					]
				},
				'or': {
					'name': None,
					'group': 'expression',
					'description': 'Logical OR operation',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['or', True, False]], 'result': True},
						{'code': [['or', False, False]], 'result': False}
					]
				},
				'xor': {
					'name': None,
					'group': 'expression',
					'description': 'Logical XOR operation',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['xor', True, False]], 'result': True},
						{'code': [['xor', True, True]], 'result': False}
					]
				},
				'in': {
					'name': None,
					'group': 'expression',
					'description': 'Checks if value is in a list or name in a dictionary',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['in', 'a', ['a', 'b', 'c']]], 'result': True},
						{'code': [['in', 'x', {'x': 1}]], 'result': True},
						{'code': [['in', 'd', ['a', 'b', 'c']]], 'result': False}
					]
				},
				'not in': {
					'name': None,
					'group': 'expression',
					'description': 'Checks if value is not in a list or name not in a dictionary',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['not in', 'd', ['a', 'b', 'c']]], 'result': True},
						{'code': [['not in', 'y', {'x': 1}]], 'result': True},
						{'code': [['not in', 'a', ['a', 'b', 'c']]], 'result': False}
					]
				},
				'.': {
					'name': 'print',
					'group': 'control',
					'description': 'Output data to the console',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['.', 'Hello']], 'result': 'Hello'},
						{'code': [['.', 42]], 'result': 42}
					]
				},
				'..': {
					'name': 'input',
					'group': 'control',
					'description': 'Input text from the user',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['..', 'Enter name:']], 'test': False},
						{'code': [['..']], 'test': False}
					]
				},
				'?': {
					'name': 'condition',
					'group': 'control',
					'description': 'Evaluate a conditional expression',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['?', ['>', 5, 3], 'yes', 'no']], 'result': 'yes'},
						{'code': [['?', ['==', 2, 3], 'equal', 'not equal']], 'result': 'not equal'}
					]
				},
				'o': {
					'name': 'loop',
					'group': 'control',
					'description': 'Perform a loop operation',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['o', ['<', 'i', 3], [['.', 'i'], ['=', 'i', ['+', 'i', 1]]]]], 'test': False},
						{'code': [['o', ['<', 'i', 5], [['.', ['*', 'i', 2]], ['=', 'i', ['+', 'i', 1]]]]], 'test': False}
					]
				},
				'x': {
					'name': 'loop_break',
					'group': 'control',
					'description': 'Exit the current loop',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['o', True, [['.', 'looping'], ['?', ['==', 'i', 3], [['x']], []]]]], 'test': False}
					]
				},
				'->': {
					'name': 'loop_continue',
					'group': 'control',
					'description': 'Skip to the next iteration of the loop',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['o', ['<', 'i', 5], [['?', ['==', 'i', 2], [['->']], [['.', 'i']]]]]], 'test': False}
					]
				},
				'<-': {
					'name': 'loop_repeat',
					'group': 'control',
					'description': 'Repeat the current iteration of the loop',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['o', ['<', 'i', 3], [['?', ['==', 'i', 1], [['<-']], [['.', 'i']]]]]], 'test': False}
					]
				},
				'X': {
					'name': 'action_return',
					'group': 'control',
					'description': 'Return a result from an action',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['action', [1, ['+', 1], 'X']]], 'result': 2},
						{'code': [['action', [1, ['+', 1], ['X', '{}']]]], 'result': None}
					]
				},
				'action': {
					'name': 'action',
					'group': 'control',
					'description': 'Initiate or call an action',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['action', 'greet', [], [['.', 'Hello!']]], ['greet']], 'test': False},
						{'code': [['action', 'add', ['a', 'b'], [[':', ['+', 'a', 'b']]]], ['add', 2, 3]], 'result': 5}
					]
				},
				'open': {
					'name': 'open',
					'group': 'control',
					'description': 'Open a link',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['open', 'https://example.com']], 'test': False},
						{'code': [['open', 'file.txt']], 'test': False}
					]
				},
				'code': {
					'name': 'code',
					'group': 'control',
					'description': 'Execute a block of native code',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['code', 'python', 'print("Hello from Python")']], 'test': False},
						{'code': [['code', 'js', 'console.log("Hello from JS")']], 'test': False}
					]
				},
				'xx': {
					'name': 'exit',
					'group': 'control',
					'description': 'Exit the current application',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['xx']], 'test': False},
						{'code': [['xx', 500]], 'test': False},
						{'code': [['xx', 'something went wrong']], 'test': False}
					]
				},
				'l': {
					'name': 'l',
					'group': 'control',
					'description': 'Log data',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['l', 'Debug info']], 'test': False},
						{'code': [['l', ['+', 'x=', 'x']]], 'test': False}
					]
				},
				'convert': {
					'name': 'convert',
					'group': 'control',
					'description': 'Convert data from one format to another',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['convert', 'json', {'x': 10}]], 'result': '{"x": 10}'},
						{'code': [['convert', 'yaml', {'x': 10}]], 'result': 'x: 10\n'}
					]
				},
				'spawner': {
					'name': 'spawner',
					'group': 'control',
					'description': 'Export code to an application, game or operation system',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['spawner', 'game.json']], 'test': False},
						{'code': [['spawner', 'game.json', './game']], 'test': False},
						{'code': [['spawner', {
							'source': './app.json',
							'path': './app',
							'zip': True,
							'platform': 'windows'
							}]], 'test': False},
						{'code': [['spawner', 'os.86', 'f:']], 'test': False},
						{'code': [['spawner', 'os.64', 'f:']], 'test': False},
						{'code': [['spawner', 'os.80286', 'f:']], 'test': False},
						{'code': [['spawner', 'os.atari', '/mnt/flash']], 'test': False}
					]
				},
				'update': {
					'name': 'update',
					'group': 'control',
					'description': 'Updating the language code',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['update']], 'test': False}
					]
				},
				'test': {
					'name': 'test',
					'group': 'control',
					'description': 'Test one or all actions',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [
						{'name': 'name', 'type': 'text', 'default': None},
						{'name': 'group', 'type': 'text', 'default': None}
					],
					'example': [
						{'code': [['test']], 'test': False},
						{'code': [['test', 'upper']], 'test': False},
						{'code': [['test', 'group', 'math']], 'test': False}
					]
				},
				'help': {
					'name': 'help',
					'group': 'control',
					'description': 'Show description and use of the action',
					'safe': True,
					'param': [
						{'name': 'name', 'type': 'text', 'default': None}
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
					'param': [
						{'name': 'hash', 'type': 'text', 'default': None},
						{'name': 'data', 'type': 'any', 'default': None}
					],
					'example': [
						{'code': [['void', 'hash']], 'test': False},
						{'code': [['void', 'hash', {'text': 'comment'}]], 'test': False},
						{'code': [['void', 'hash', 'camera.on']], 'test': False}
					]
				},
				'lower': {
					'name': 'lower',
					'group': 'text',
					'description': 'Convert text to lowercase',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['lower', 'TeXt']], 'result': 'text'}
					]
				},
				'upper': {
					'name': 'upper',
					'group': 'text',
					'description': 'Convert text to uppercase',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['upper', 'text']], 'result': 'TEXT'},
						{'code': [['upper', 'text and text', 'title']], 'result': 'Text And Text'},
						{'code': [['upper', 'text and text', 'sentence']], 'result': 'Text and text'}
					]
				},
				'starts': {
					'name': 'starts',
					'group': 'text',
					'description': 'Check if text starts with a specific substring',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['starts', 'hello world', 'hell']], 'result': True},
						{'code': [['starts', 'hello world', 'world']], 'result': False}
					]
				},
				'ends': {
					'name': 'ends',
					'group': 'text',
					'description': 'Check if text ends with a specific substring',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['ends', 'hello world', 'world']], 'result': True},
						{'code': [['ends', 'hello world', 'hello']], 'result': False}
					]
				},
				'strip': {
					'name': 'strip',
					'group': 'text',
					'description': 'Remove leading and trailing spaces from text',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['strip', '  hello  ']], 'result': 'hello'},
						{'code': [['strip', '\ttext\n']], 'result': 'text'}
					]
				},
				'strip.start': {
					'name': 'strip_start',
					'group': 'text',
					'description': 'Remove leading spaces from text',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True, 
					'param': [],
					'example': [
						{'code': [['strip.start', '  hello  ']], 'result': 'hello  '},
						{'code': [['strip.start', '\ttext\n']], 'result': 'text\n'}
					]
				},
				'strip.end': {
					'name': 'strip_end',
					'group': 'text',
					'description': 'Remove trailing spaces from text',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['strip.end', '  hello  ']], 'result': '  hello'},
						{'code': [['strip.end', '\ttext\n']], 'result': '\ttext'}
					]
				},
				'replace': {
					'name': 'replace',
					'group': 'text',
					'description': 'Replace occurrences of a substring within text',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['replace', 'hello world', 'world', 'there']], 'result': 'hello there'},
						{'code': [['replace', 'aabbcc', 'b', 'x']], 'result': 'aaxxcc'}
					]
				},
				'find': {
					'name': 'find',
					'group': 'text',
					'description': 'Locate a substring within text',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['find', 'hello world', 'world']], 'result': 6},
						{'code': [['find', 'abcabc', 'b']], 'result': 1}
					]
				},
				'parse': {
					'name': 'parse',
					'group': 'text',
					'description': 'Parse text into structured data',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['parse', 'json', '{"x": 5}']], 'result': {'x': 5}},
						{'code': [['parse', 'number', '42']], 'result': 42}
					]
				},
				'similar': {
					'name': 'similar',
					'group': 'text',
					'description': 'Find similarity between texts',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['similar', 'hello', 'hallo']], 'result': 0.8, 'round': 1},
						{'code': [['similar', 'cat', 'dog']], 'result': 0.0, 'round': 1}
					]
				},
				'part': {
					'name': 'part',
					'group': 'text',
					'description': 'Extract a part of the text',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['part', 'hello world', 0, 5]], 'result': 'hello'},
						{'code': [['part', 'abcdef', 2, 4]], 'result': 'cd'}
					]
				},
				'split': {
					'name': 'split',
					'group': 'text',
					'description': 'Split text into parts based on a delimiter',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['split', 'a,b,c', ',']], 'result': ['a', 'b', 'c']},
						{'code': [['split', 'one two three', ' ']], 'result': ['one', 'two', 'three']}
					]
				},
				'join': {
					'name': 'join',
					'group': 'text',
					'description': 'Join a list of strings into a single string with a delimiter',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['join', ['a', 'b', 'c'], ',']], 'result': 'a,b,c'},
						{'code': [['join', ['2023', '12', '31'], '-']], 'result': '2023-12-31'}
					]
				},
				'date': {
					'name': 'date',
					'group': 'text',
					'description': 'Format or parse date-related information',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['date', '{year}-{month}-{day} {hour}:{minute}:{second}.{millisecond}', 1744095313.123]], 'result': '2025-04-08 06:55:13.123'},
						{'code': [['date', '{month short}', 1744095313]], 'result': '4'},
						{'code': [['date', '2025-04-08 06:55:13.123', '{year}-{month}-{day} {hour}:{minute}:{second}.{millisecond}']], 'result': 1744095313.123}
					]
				},
				'escape': {
					'name': 'escape',
					'group': 'text',
					'description': 'Escape special characters in a string',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['escape', 'Line\nBreak']], 'result': 'Line\\nBreak'},
						{'code': [['escape', 'Quote\'Here']], 'result': 'Quote\\\'Here'}
					]
				},
				'escape.html': {
					'name': 'escape_html',
					'group': 'text',
					'description': 'Escape HTML tags and attributes in a string',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['escape.html', '<div>Test</div>']], 'result': '&lt;div&gt;Test&lt;/div&gt;'},
						{'code': [['escape.html', '\'Quote\'']], 'result': '&quot;Quote&quot;'}
					]
				},
				'escape.url': {
					'name': 'escape_url',
					'group': 'text',
					'description': 'Escape URL components',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['escape.url', 'hello world']], 'result': 'hello%20world'},
						{'code': [['escape.url', 'a/b?c=d']], 'result': 'a%2Fb%3Fc%3Dd'}
					]
				},
				'escape.sql': {
					'name': 'escape_sql',
					'group': 'text',
					'description': 'Escape SQL query components to prevent injection',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['escape.sql', 'O\'Reilly']], 'result': 'O\'Reilly'},
						{'code': [['escape.sql', 'x\' OR 1=1 --']], 'result': 'x\\\' OR 1=1 --'}
					]
				},
				'unescape': {
					'name': 'unescape',
					'group': 'text',
					'description': 'Unescape special characters in a string',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['unescape', 'Line\\nBreak']], 'result': 'Line\nBreak'},
						{'code': [['unescape', 'Quote\\\'Here']], 'result': 'Quote\'Here'}
					]
				},
				'unescape.html': {
					'name': 'unescape_html',
					'group': 'text',
					'description': 'Unescape HTML tags and attributes in a string',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['unescape.html', '&lt;div&gt;Test&lt;/div&gt;']], 'result': '<div>Test</div>'},
						{'code': [['unescape.html', '&quot;Quote&quot;']], 'result': '\'Quote\''}
					]
				},
				'unescape.url': {
					'name': 'unescape_url',
					'group': 'text',
					'description': 'Unescape URL components',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['unescape.url', 'hello%20world']], 'result': 'hello world'},
						{'code': [['unescape.url', 'a%2Fb%3Fc%3Dd']], 'result': 'a/b?c=d'}
					]
				},
				'unescape.sql': {
					'name': 'unescape_sql',
					'group': 'text',
					'description': 'Unescape SQL query components',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['unescape.sql', 'O''Reilly']], 'result': 'O\'Reilly'},
						{'code': [['unescape.sql', 'x\\\' OR 1=1 --']], 'result': 'x\' OR 1=1 --'}
					]
				},
				'words': {
					'name': 'words',
					'group': 'text',
					'description': 'Split text into individual words',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'vapp': True,
					'param': [],
					'example': [
						{'code': [['words', 'Hello world! How are you?']], 'result': ['Hello', 'world', 'How', 'are', 'you']},
						{'code': [['words', 'one,two,three', ',']], 'result': ['one', 'two', 'three']}
					]
				},
				'sentences': {
					'name': 'sentences',
					'group': 'text',
					'description': 'Split text into sentences',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'vapp': True,
					'param': [],
					'example': [
						{'code': [['sentences', 'First sentence. Second one! Third?']], 'result': ['First sentence', 'Second one', 'Third']},
						{'code': [['sentences', 'Line 1.Line 2']], 'result': ['Line 1', 'Line 2']}
					]
				},
				'lines': {
					'name': 'lines',
					'group': 'text',
					'description': 'Split text into lines',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'vapp': True,
					'param': [],
					'example': [
						{'code': [['lines', 'line1\nline2\nline3']], 'result': ['line1', 'line2', 'line3']},
						{'code': [['lines', 'a\r\nb\r\nc']], 'result': ['a', 'b', 'c']}
					]
				},
				'bytes': {
					'name': 'bytes',
					'group': 'text',
					'description': 'Convert a string into bytes',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'vapp': True,
					'param': [],
					'example': [
						{'code': [['bytes', 'hello', 'utf-8']], 'result': [104, 101, 108, 108, 111]},
						{'code': [['bytes', 'test']], 'result': [116, 101, 115, 116]}
					]
				},
				'merge': {
					'name': 'merge',
					'group': 'list',
					'description': 'Combine multiple lists into one',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['merge', [1, 2], [3, 4]]], 'result': [1, 2, 3, 4]},
						{'code': [['merge', ['a'], ['b', 'c']]], 'result': ['a', 'b', 'c']}
					]
				},
				'push': {
					'name': 'push',
					'group': 'list',
					'description': 'Add an element to the end of a list',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['push', [1, 2], 3]], 'result': [1, 2, 3]},
						{'code': [['push', [], 'new']], 'result': ['new']}
					]
				},
				'pop': {
					'name': 'pop',
					'group': 'list',
					'description': 'Remove and return an element from the end of a list',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['pop', [1, 2, 3]]], 'result': 3},
						{'code': [['pop', ['a']]], 'result': 'a'}
					]
				},
				'reverse': {
					'name': 'reverse',
					'group': 'list',
					'description': 'Reverse the order of elements in a list',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['reverse', [1, 2, 3]]], 'result': [3, 2, 1]},
						{'code': [['reverse', ['a', 'b']]], 'result': ['b', 'a']}
					]
				},
				'shuffle': {
					'name': 'shuffle',
					'group': 'list',
					'description': 'Randomly reorder elements in a list',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['shuffle', [1, 2, 3, 4]]], 'test': False},
						{'code': [['shuffle', ['a', 'b', 'c']]], 'test': False}
					]
				},
				'map': {
					'name': 'map',
					'group': 'list',
					'description': 'Apply a function to each element in a list',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['map', [1, 2, 3], ['*', 'item', 2]]], 'result': [2, 4, 6]},
						{'code': [['map', ['a', 'b'], ['upper', 'item']]], 'result': ['A', 'B']}
					]
				},
				'reduce': {
					'name': 'reduce',
					'group': 'list',
					'description': 'Apply a function cumulatively to the elements in a list',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['reduce', [1, 2, 3, 4], ['+', 'acc', 'item'], 0]], 'result': 10},
						{'code': [['reduce', [2, 3, 4], ['*', 'acc', 'item'], 1]], 'result': 24}
					]
				},
				'names': {
					'name': 'names',
					'group': 'list',
					'description': 'Retrieve all keys or attribute names from a structure',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['names', {'x': 1, 'y': 2}]], 'result': ['x', 'y']},
						{'code': [['names', ['a', 'b', 'c']]], 'result': ['0', '1', '2']}
					]
				},
				'values': {
					'name': 'values',
					'group': 'list',
					'description': 'Retrieve all values from a structure',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['values', {'x': 1, 'y': 2}]], 'result': [1, 2]},
						{'code': [['values', ['a', 'b', 'c']]], 'result': ['a', 'b', 'c']}
					]
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
					'example': [
						{'code': [['tan', 0.1]], 'result': 0.1, 'round': 3}
					]
				},
				'sinh': {
					'name': 'sinh',
					'group': 'math',
					'description': 'Hyperbolic sine of the value',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['sinh', 0.1]], 'result': 0.1, 'round': 3}
					]
				},
				'cosh': {
					'name': 'cosh',
					'group': 'math',
					'description': 'Hyperbolic cosine of the value',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['cosh', 0.1]], 'result': 1.005, 'round': 3}
					]
				},
				'tanh': {
					'name': 'tanh',
					'group': 'math',
					'description': 'Hyperbolic tangent of the valu',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['tanh', 0.1]], 'result': 0.1, 'round': 3}
					]
				},
				'asin': {
					'name': 'asin',
					'group': 'math',
					'description': 'Arc sine of the value',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['asin', 0.1]], 'result': 0.1, 'round': 3}
					]
				},
				'acos': {
					'name': 'acos',
					'group': 'math',
					'description': 'Arc cosine of the value',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['acos', 0.1]], 'result': 1.471, 'round': 3}
					]
				},
				'atan': {
					'name': 'atan',
					'group': 'math',
					'description': 'Arc tangent of the value',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['atan', 0.1]], 'result': 0.1, 'round': 3}
					]
				},
				'asinh': {
					'name': 'asinh',
					'group': 'math',
					'description': 'Arc hyperbolic sine of the value',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['asinh', 0.1]], 'result': 0.1, 'round': 3}
					]
				},
				'acosh': {
					'name': 'acosh',
					'group': 'math',
					'description': 'Arc hyperbolic cosine of the value',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['acosh', 2]], 'result': 1.317, 'round': 3}
					]
				},
				'atanh': {
					'name': 'atanh',
					'group': 'math',
					'description': 'Arc hyperbolic tangent of the value',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['atanh', 0.1]], 'result': 0.1, 'round': 3}
					]
				},
				'round': {
					'name': 'round',
					'group': 'math',
					'description': 'Rounds a number to the nearest integer or to the specified number of decimal places',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['round', 0.1]], 'result': 0},
						{'code': [['round', 0.7]], 'result': 1},
						{'code': [['round', -0.7]], 'result': -1},
						{'code': [['round', 0.123, 2]], 'result': 0.12}
					]
				},
				'floor': {
					'name': 'floor',
					'group': 'math',
					'description': 'Largest integer less than or equal to a number',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['floor', 0.1]], 'result': 0},
						{'code': [['floor', 0.1]], 'result': 0},
						{'code': [['floor', 0.7]], 'result': 0},
						{'code': [['floor', -0.7]], 'result': -1}
					]
				},
				'ceil': {
					'name': 'ceil',
					'group': 'math',
					'description': 'Smallest integer greater than or equal to a number',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['ceil', 0.1]], 'result': 1},
						{'code': [['ceil', 0.7]], 'result': 1},
						{'code': [['ceil', -0.7]], 'result': 0}
					]
				},
				'log': {
					'name': 'log',
					'group': 'math',
					'description': 'Logarithm (natural by default) of a number',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['log', 0.1]], 'result': -2.303, 'round': 3},
						{'code': [['log', 0.1, 2]], 'result': -3.322, 'round': 3},
						{'code': [['log', 0.1, 10]], 'result': -1, 'round': 3}
					]
				},
				'factorial': {
					'name': 'factorial',
					'group': 'math',
					'description': 'Factorial of a given non-negative number',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['factorial', 5]], 'result': 120},
						{'code': [['factorial', 0]], 'result': 1}
					]
				},
				'fibonacci': {
					'name': 'fibonacci',
					'group': 'math',
					'description': 'Fibonacci numbers up to a specified index',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [
						{'name': 'number', 'type': 'number', 'default': 10},
						{'name': 'multiply', 'type': 'number', 'default': 1},
						{'name': 'shift', 'type': 'number', 'default': 0}
					],
					'example': [
						{'code': [['fibonacci', 5]], 'result': [0, 1, 1, 2, 3]},
						{'code': [['fibonacci', 7]], 'result': [0, 1, 1, 2, 3, 5, 8]},
						{'code': [['fibonacci', 5, 3, 1]], 'result': [1, 4, 4, 7, 10]},
					]
				},
				'golden': {
					'name': 'golden',
					'group': 'math',
					'description': 'Golden ratio of a number',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['golden', 10]], 'result': {'short': 3.820, 'long': 6.180, 'total': 10}, 'round': 3},
						{'code': [['golden', 10, 'short']], 'result': {'short': 10, 'long': 16.18, 'total': 26.18}, 'round': 3},
						{'code': [['golden', 10, 'long']], 'result': {'short': 6.18, 'long': 10, 'total': 16.18}, 'round': 3},
					]
				},
				'abs': {
					'name': 'abs',
					'group': 'math',
					'description': 'Absolute value of a number',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['abs', -5]], 'result': 5},
						{'code': [['abs', 3.14]], 'result': 3.14}
					]
				},
				'min': {
					'name': 'min',
					'group': 'math',
					'description': 'Smallest of a list of numbers',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['min', [5, 3, 8, 1]]], 'result': 1},
						{'code': [['min', [-2, -5, 0]]], 'result': -5}
					]
				},
				'max': {
					'name': 'max',
					'group': 'math',
					'description': 'Largest of a list of numbers',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['max', [5, 3, 8, 1]]], 'result': 8},
						{'code': [['max', [-2, -5, 0]]], 'result': 0}
					]
				},
				'avg': {
					'name': 'avg',
					'group': 'math',
					'description': 'Average value of a list of numbers',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['avg', [1, 2, 3, 4, 5]]], 'result': 3},
						{'code': [['avg', [10, 20]]], 'result': 15}
					]
				},
				'sum': {
					'name': 'sum',
					'group': 'math',
					'description': 'Sum of a list of numbers',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['sum', [1, 2, 3, 4, 5]]], 'result': 15},
						{'code': [['sum', [10, 20, 30]]], 'result': 60}
					]
				},
				'random': {
					'name': 'random',
					'group': 'math',
					'description': 'Generates a pseudo-random number',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['random']], 'result': 'number', 'range': [0, 1]},
						{'code': [['random', 10]], 'result': 'number', 'range': [0, 10]},
						{'code': [['random', 10, 20]], 'result': 'number', 'range': [10, 20]},
					]
				},
				'random.seed': {
					'name': 'random_seed',
					'group': 'math',
					'description': 'Sets or gets the seed for the random number generator to produce reproducible results',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [
						{'name': 'seed', 'type': 'text', 'default': None}
					],
					'example': [
						{'code': [
							['random.seed', 'uniqueseed'],
							['random.seed']
						], 'result': 'uniqueseed'}
					]
				},
				'random.reseed': {
					'name': 'random_reseed',
					'group': 'math',
					'description': 'Sets a new random seed for the random number generator',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [
							['random.reseed'],
							['random.seed']
						], 'result': 'text', 'range': 64}
					]
				},
				't': {
					'name': 't',
					'group': 'time',
					'description': 'Stopwatch for calculating the time spent on operations',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['t', 'start']], 'result': None},
						{'code': [['t', 'stop']], 'result': 1.234, 'round': 3}
					]
				},
				'time': {
					'name': 'time',
					'group': 'time',
					'description': 'Provides current time since the epoch (1970-01-01 00:00:00 UTC)',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['time']], 'result': 1678901234}
					]
				},
				'timer': {
					'name': 'timer',
					'group': 'time',
					'description': 'Creates a timer that can be used to trigger events at specific intervals',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['timer', 'start', 5]], 'result': 'timer_id_1'}
					]
				},
				'timer.remove': {
					'name': 'timer_remove',
					'group': 'time',
					'description': 'Removes previously created timer',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['timer.remove', 'timer_id_1']], 'result': True}
					]
				},
				'timepast': {
					'name': 'timepast',
					'group': 'time',
					'description': 'Calculates time passed since a given start time',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['timepast', 1678901200]], 'result': 34}
					]
				},
				'wait': {
					'name': 'wait',
					'group': 'time',
					'description': 'Pauses execution for a specified number of seconds',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['wait', 1.5]], 'result': None}
					]
				},
				'encrypt': {
					'name': 'encrypt',
					'group': 'crypto',
					'description': 'Encrypts data using a specified key',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['encrypt', 'secret', 'mykey']], 'result': 'aGVsbG8='}
					]
				},
				'decrypt': {
					'name': 'decrypt',
					'group': 'crypto',
					'description': 'Decrypts previously encrypted data using the specified key',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['decrypt', 'aGVsbG8=', 'mykey']], 'result': 'secret'}
					]
				},
				'hash': {
					'name': 'hash',
					'group': 'crypto',
					'description': 'Generates a hash for the data or generates a random text',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['hash', 'hello']], 'result': '2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824'}
					]
				},
				'uuid': {
					'name': 'uuid',
					'group': 'crypto',
					'description': 'Generates a universally unique identifier',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['uuid']], 'result': '550e8400-e29b-41d4-a716-446655440000'}
					]
				},
				'md5': {
					'name': 'md5',
					'group': 'crypto',
					'description': 'Generates an MD5 hash of a text',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['md5', 'hello']], 'result': '5d41402abc4b2a76b9719d911017c592'}
					]
				},
				'sha1': {
					'name': 'sha1',
					'group': 'crypto',
					'description': 'Generates an SHA-1 hash of a text',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['sha1', 'hello']], 'result': 'aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d'}
					]
				},
				'sha256': {
					'name': 'sha256',
					'group': 'crypto',
					'description': 'Generates an SHA-256 hash of a text',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['sha256', 'hello']], 'result': '2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824'}
					]
				},
				'sha512': {
					'name': 'sha512',
					'group': 'crypto',
					'description': 'Generates an SHA-512 hash of a text',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['sha512', 'hello']], 'result': '9b71d224bd62f3785d96d46ad3ea3d73319bfbc2890caadae2dff72519673ca72323c3d99ba5c11d7c7acc6e14b8c5da0c4663475c2e5c3adef46f73bcdec043'}
					]
				},
				'crc32': {
					'name': 'crc32',
					'group': 'crypto',
					'description': 'Calculates the CRC32 checksum of a text',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['crc32', 'hello']], 'result': 907060870}
					]
				},
				'base64.encode': {
					'name': 'base64_encode',
					'group': 'crypto',
					'description': 'Encodes the data into base64 format',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['base64.encode', 'hello']], 'result': 'aGVsbG8='}
					]
				},
				'base64.decode': {
					'name': 'base64_decode',
					'group': 'crypto',
					'description': 'Decodes base64 encoded data back to its original form',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['base64.decode', 'aGVsbG8=']], 'result': 'hello'}
					]
				},
				'gzip.encode': {
					'name': 'gzip_encode',
					'group': 'crypto',
					'description': 'Compresses data using the GZip compression algorithm',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['gzip.encode', 'hello']], 'result': 'H4sIAAAAAAAA/8tIzcnJVyjPL8pJAQCFEUoNCwAAAA=='}
					]
				},
				'gzip.decode': {
					'name': 'gzip_decode',
					'group': 'crypto',
					'description': 'Decompresses GZip compressed data',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['gzip.decode', 'H4sIAAAAAAAA/8tIzcnJVyjPL8pJAQCFEUoNCwAAAA==']], 'result': 'hello'}
					]
				},
				'rsa.encode': {
					'name': 'rsa_encode',
					'group': 'crypto',
					'description': 'Encrypts data using RSA encryption with a public key',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['rsa.encode', 'secret', 'public_key']], 'result': 'encrypted_data'}
					]
				},
				'rsa.decode': {
					'name': 'rsa_decode',
					'group': 'crypto',
					'description': 'Decrypts data encrypted with RSA using the corresponding private key',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['rsa.decode', 'encrypted_data', 'private_key']], 'result': 'secret'}
					]
				},
				'rsa.public': {
					'name': 'rsa_public',
					'group': 'crypto',
					'description': 'Generates the RSA public key used for encryption',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['rsa.public']], 'result': 'public_key'}
					]
				},
				'rsa.private': {
					'name': 'rsa_private',
					'group': 'crypto',
					'description': 'Generates the RSA private key used for decryption',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['rsa.private']], 'result': 'private_key'}
					]
				},
				'ssl.encode': {
					'name': 'ssl_encode',
					'group': 'crypto',
					'description': 'Performs SSL encryption on data to secure communication',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['ssl.encode', 'data']], 'result': 'encrypted_ssl_data'}
					]
				},
				'ssl.decode': {
					'name': 'ssl_decode',
					'group': 'crypto',
					'description': 'Decrypts data encrypted with SSL for secure data transfer',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['ssl.decode', 'encrypted_ssl_data']], 'result': 'data'}
					]
				},
				'ssl.check': {
					'name': 'ssl_check',
					'group': 'crypto',
					'description': 'Verifies the validity and authenticity of an SSL certificate',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['ssl.check', 'certificate']], 'result': True}
					]
				},
				'bcrypt.encode': {
					'name': 'bcrypt_encode',
					'group': 'crypto',
					'description': 'Hashes a password using the bcrypt algorithm for secure storage',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['bcrypt.encode', 'password']], 'result': '$2a$12$saltpasswordhash'}
					]
				},
				'bcrypt.check': {
					'name': 'bcrypt_check',
					'group': 'crypto',
					'description': 'Verifies a password against a bcrypt hashed password',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['bcrypt.check', 'password', '$2a$12$saltpasswordhash']], 'result': True}
					]
				},
				'file': {
					'name': 'file',
					'group': 'file',
					'description': 'Read or write data to a file at a specified path',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['file', 'read', 'test.txt']], 'result': 'file contents'},
						{'code': [['file', 'write', 'test.txt', 'new content']], 'result': True}
					]
				},
				'file.exists': {
					'name': 'file_exists',
					'group': 'file',
					'description': 'Checks if a specified file exists at the given path',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['file.exists', 'test.txt']], 'result': True}
					]
				},
				'file.read': {
					'name': 'file_read',
					'group': 'file',
					'description': 'Reads the contents of a specified file',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['file.read', 'test.txt']], 'result': 'file contents'}
					]
				},
				'file.read.text': {
					'name': 'file_read_text',
					'group': 'file',
					'description': 'Reads the text contents of a specified file',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['file.read.text', 'test.txt']], 'result': 'text content'}
					]
				},
				'file.read.lines': {
					'name': 'file_read_lines',
					'group': 'file',
					'description': 'Reads a specified file line by line into a list',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['file.read.lines', 'test.txt']], 'result': ['line1', 'line2', 'line3']}
					]
				},
				'file.write': {
					'name': 'file_write',
					'group': 'file',
					'description': 'Writes data to a specified file, creating or replacing it',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['file.write', 'test.txt', 'new content']], 'result': True}
					]
				},
				'file.append': {
					'name': 'file_append',
					'group': 'file',
					'description': 'Appends data to the end of a specified file without replacing it',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['file.append', 'test.txt', 'appended content']], 'result': True}
					]
				},
				'file.remove': {
					'name': 'file_remove',
					'group': 'file',
					'description': 'Removes a specified file from the file system',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['file.remove', 'test.txt']], 'result': True}
					]
				},
				'file.move': {
					'name': 'file_move',
					'group': 'file',
					'description': 'Moves a specified file to a new location',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['file.move', 'old.txt', 'new.txt']], 'result': True}
					]
				},
				'file.copy': {
					'name': 'file_copy',
					'group': 'file',
					'description': 'Copies a specified file to a new location',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['file.copy', 'source.txt', 'dest.txt']], 'result': True}
					]
				},
				'file.rename': {
					'name': 'file_rename',
					'group': 'file',
					'description': 'Renames a specified file',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['file.rename', 'old.txt', 'new.txt']], 'result': True}
					]
				},
				'file.link': {
					'name': 'file_link',
					'group': 'file',
					'description': 'Creates a hard link to a specified file',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['file.link', 'source.txt', 'link.txt']], 'result': True}
					]
				},
				'file.link.exists': {
					'name': 'file_link_exists',
					'group': 'file',
					'description': 'Checks if a hard link exists at the given path',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['file.link.exists', 'link.txt']], 'result': True}
					]
				},
				'file.info': {
					'name': 'file_info',
					'group': 'file',
					'description': 'Retrieves information about a specified file',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['file.info', 'test.txt']], 'result': {'size': 1024, 'modified': 1678901234}}
					]
				},
				'file.size': {
					'name': 'file_size',
					'group': 'file',
					'description': 'Returns the size of a specified file in bytes',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['file.size', 'test.txt']], 'result': 1024}
					]
				},
				'file.permission': {
					'name': 'file_permission',
					'group': 'file',
					'description': 'Retrieves or sets permissions for a specified file',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['file.permission', 'test.txt', 'rw-r--r--']], 'result': True}
					]
				},
				'file.time': {
					'name': 'file_time',
					'group': 'file',
					'description': 'Gets or sets the modified timestamp for a specified file',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['file.time', 'test.txt']], 'result': 1678901234}
					]
				},
				'file.sha256': {
					'name': 'file_sha256',
					'group': 'file',
					'description': 'Computes the SHA256 checksum of a specified file',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['file.sha256', 'test.txt']], 'result': '2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824'}
					]
				},
				'file.crc32': {
					'name': 'file_crc32',
					'group': 'file',
					'description': 'Computes the CRC32 checksum for a specified file',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['file.crc32', 'test.txt']], 'result': 907060870}
					]
				},
				'file.base64': {
					'name': 'file_base64',
					'group': 'file',
					'description': 'Encodes a specified file to base64 format',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['file.base64', 'test.txt']], 'result': 'aGVsbG8='}
					]
				},
				'file.zip': {
					'name': 'file_zip',
					'group': 'file',
					'description': 'Compresses a specified file into a ZIP archive',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['file.zip', 'test.txt', 'archive.zip']], 'result': True}
					]
				},
				'file.zip.list': {
					'name': 'file_zip_list',
					'group': 'file',
					'description': 'Lists the files contained within a ZIP archive',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['file.zip.list', 'archive.zip']], 'result': ['test.txt']}
					]
				},
				'file.zip.exists': {
					'name': 'file_zip_exists',
					'group': 'file',
					'description': 'Checks if a specific file exists within a ZIP archive',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['file.zip.exists', 'archive.zip', 'test.txt']], 'result': True}
					]
				},
				'file.zip.read': {
					'name': 'file_zip_read',
					'group': 'file',
					'description': 'Reads a specific file from within a ZIP archive',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['file.zip.read', 'archive.zip', 'test.txt']], 'result': 'file contents'}
					]
				},
				'file.zip.remove': {
					'name': 'file_zip_remove',
					'group': 'file',
					'description': 'Removes a specific file from a ZIP archive',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['file.zip.remove', 'archive.zip', 'test.txt']]}
					]
				},
				'file.unzip': {
					'name': 'file_unzip',
					'group': 'file',
					'description': 'Extracts files from a ZIP archive into a specified directory',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['file.unzip', 'archive.zip', 'destination']]}
					]
				},
				'file.gzip': {
					'name': 'file_gzip',
					'group': 'file',
					'description': 'Compresses a specified file using GZip compression',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['file.gzip', 'test.txt', 'test.txt.gz']]}
					]
				},
				'file.ungzip': {
					'name': 'file_ungzip',
					'group': 'file',
					'description': 'Decompresses a GZip-compressed file',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['file.ungzip', 'test.txt.gz', 'test.txt']], 'result': True}
					]
				},
				'file.void': {
					'name': 'file_void',
					'group': 'file',
					'description': 'Compresses the specified file using GZip compression and places it in a Void container',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['file.void', 'test.txt', 'test.void']], 'result': True}
					]
				},
				'file.unvoid': {
					'name': 'file_unvoid',
					'group': 'file',
					'description': 'Decompresses a GZip-compressed files and directories from a Void container',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['file.unvoid', 'test.void', 'output']], 'result': True}
					]
				},
				'dir.exists': {
					'name': 'dir_exists',
					'group': 'file',
					'description': 'Checks if a specified directory exists',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['dir.exists', 'folder']], 'result': True},
						{'code': [['dir.exists', 'nonexistent']], 'result': False}
					]
				},
				'dir.create': {
					'name': 'dir_create',
					'group': 'file',
					'description': 'Creates a new directory at a specified path',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['dir.create', 'new_folder']], 'test': False},
						{'code': [['dir.create', 'path/to/folder']], 'test': False}
					]
				},
				'dir.copy': {
					'name': 'dir_copy',
					'group': 'file',
					'description': 'Copies a specified directory and its contents to a new location',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['dir.copy', 'source', 'destination']], 'test': False},
						{'code': [['dir.copy', 'backup', 'archive/backup']], 'test': False}
					]
				},
				'dir.move': {
					'name': 'dir_move',
					'group': 'file',
					'description': 'Moves a specified directory to a new location',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['dir.move', 'old', 'new']], 'test': False},
						{'code': [['dir.move', 'temp', 'perm']], 'test': False}
					]
				},
				'dir.rename': {
					'name': 'dir_rename',
					'group': 'file',
					'description': 'Renames a specified directory',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['dir.rename', 'old_name', 'new_name']], 'test': False},
						{'code': [['dir.rename', 'temp', 'final']], 'test': False}
					]
				},
				'dir.remove': {
					'name': 'dir_remove',
					'group': 'file',
					'description': 'Removes a specified directory and its contents',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['dir.remove', 'temp']], 'test': False},
						{'code': [['dir.remove', 'old_backup']], 'test': False}
					]
				},
				'dir.list': {
					'name': 'dir_list',
					'group': 'file',
					'description': 'Lists the contents of a specified directory',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['dir.list', 'folder']], 'result': ['file1.txt', 'file2.txt', 'subfolder']},
						{'code': [['dir.list', 'project/src']], 'result': ['main.py', 'utils.py']}
					]
				},
				'dir.clear': {
					'name': 'dir_clear',
					'group': 'file',
					'description': 'Clears all contents of a specified directory without deleting the directory itself',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['dir.clear', 'temp']], 'test': False},
						{'code': [['dir.clear', 'cache']], 'test': False}
					]
				},
				'dir.info': {
					'name': 'dir_info',
					'group': 'file',
					'description': 'Retrieves information about a specified directory',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['dir.info', 'folder']], 'result': {'size': 1024, 'files': 10, 'modified': 1672531200}, 'test': False},
						{'code': [['dir.info', 'project']], 'result': {'size': 2048, 'files': 15, 'modified': 1672531200}, 'test': False}
					]
				},
				'dir.size': {
					'name': 'dir_size',
					'group': 'file',
					'description': 'Calculates the total size of a specified directory and its contents',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['dir.size', 'data']], 'result': 1048576},
						{'code': [['dir.size', 'downloads']], 'result': 5242880}
					]
				},
				'dir.permission': {
					'name': 'dir_permission',
					'group': 'file',
					'description': 'Gets or sets the permissions of a specified directory',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['dir.permission', 'scripts', '755']], 'test': False},
						{'code': [['dir.permission', 'uploads', '775']], 'test': False}
					]
				},
				'dir.time': {
					'name': 'dir_time',
					'group': 'file',
					'description': 'Gets or sets the timestamps of a specified directory',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['dir.time', 'logs']], 'result': 1672531200, 'test': False},
						{'code': [['dir.time', 'backups', 'created']], 'result': 1672531200, 'test': False}
					]
				},
				'dir.zip': {
					'name': 'dir_zip',
					'group': 'file',
					'description': 'Compresses a specified directory into a ZIP archive',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['dir.zip', 'archive.zip', 'folder']], 'test': False},
						{'code': [['dir.zip', 'backup.zip', 'data']], 'test': False}
					]
				},
				'dir.void': {
					'name': 'dir_void',
					'group': 'file',
					'description': 'Compresses a specified directory into a Void container',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['dir.void', 'data']], 'result': 'data.void', 'test': False},
						{'code': [['dir.void', 'project', 'backup.void']], 'test': False}
					]
				},
				'drive.list': {
					'name': 'drive_list',
					'group': 'file',
					'description': 'Lists all available drives on the system',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['drive.list']], 'result': ['C:', 'D:', 'E:'], 'test': False},
						{'code': [['drive.list', 'removable']], 'result': ['D:', 'E:'], 'test': False}
					]
				},
				'drive.name': {
					'name': 'drive_name',
					'group': 'file',
					'description': 'Gets or sets the name of a specified drive',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['drive.name', 'C:']], 'result': 'System'},
						{'code': [['drive.name', 'D:', 'Data']], 'test': False}
					]
				},
				'drive.size': {
					'name': 'drive_size',
					'group': 'file',
					'description': 'Total size of a specified drive',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['drive.size', 'C:']], 'result': 256000000000},
						{'code': [['drive.size', 'D:']], 'result': 1000000000000}
					]
				},
				'drive.used': {
					'name': 'drive_used',
					'group': 'file',
					'description': 'Amount of used space on a specified drive',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['drive.used', 'C:']], 'result': 128000000000},
						{'code': [['drive.used', 'D:']], 'result': 500000000000}
					]
				},
				'drive.free': {
					'name': 'drive_free',
					'group': 'file',
					'description': 'Amount of free space on a specified drive',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['drive.free', 'C:']], 'result': 128000000000},
						{'code': [['drive.free', 'D:']], 'result': 500000000000}
					]
				},
				'drive.info': {
					'name': 'drive_info',
					'group': 'file',
					'description': 'Retrieves information about a specified drive',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['drive.info', 'C:']], 'result': {'size': 256000000000, 'free': 128000000000, 'type': 'SSD'}, 'test': False},
						{'code': [['drive.info', 'D:']], 'result': {'size': 1000000000000, 'free': 500000000000, 'type': 'HDD'}, 'test': False}
					]
				},
				'drive.mount': {
					'name': 'drive_mount',
					'group': 'file',
					'description': 'Mounts a drive to make it accessible',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['drive.mount', '/dev/sdb1', 'D:']], 'test': False},
						{'code': [['drive.mount', 'image.iso', 'E:']], 'test': False}
					]
				},
				'drive.unmount': {
					'name': 'drive_unmount',
					'group': 'file',
					'description': 'Unmounts a drive',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['drive.unmount', 'D:']], 'test': False},
						{'code': [['drive.unmount', 'E:']], 'test': False}
					]
				},
				'drive.create': {
					'name': 'drive_create',
					'group': 'file',
					'description': 'Creates a new virtual drive or volume',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['drive.create', 'virtual', 1000000000]], 'test': False},
						{'code': [['drive.create', 'ramdisk', 4000000000, 'RAM']], 'test': False}
					]
				},
				'drive.resize': {
					'name': 'drive_resize',
					'group': 'file',
					'description': 'Resizes an existing drive partition or volume',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['drive.resize', 'virtual', 2000000000]], 'test': False},
						{'code': [['drive.resize', 'D:', 1500000000000]], 'test': False}
					]
				},
				'drive.format': {
					'name': 'drive_format',
					'group': 'file',
					'description': 'Formats a drive with a specified file system',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['drive.format', 'D:', 'NTFS']], 'test': False},
						{'code': [['drive.format', 'E:', 'FAT32']], 'test': False}
					]
				},
				'drive.remove': {
					'name': 'drive_remove',
					'group': 'file',
					'description': 'Removes or deletes a specified drive or partition',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['drive.remove', 'virtual']], 'test': False},
						{'code': [['drive.remove', 'ramdisk']], 'test': False}
					]
				},
				'path.drive': {
					'name': 'path_drive',
					'group': 'file',
					'description': 'Drive component of a specified file path',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['path.drive', 'C:/Windows/System32']], 'result': 'C:'},
						{'code': [['path.drive', '/mnt/data/file.txt']], 'result': ''}
					]
				},
				'path.dir': {
					'name': 'path_dir',
					'group': 'file',
					'description': 'Directory portion of a specified file path',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['path.dir', 'C:/Windows/System32/kernel32.dll']], 'result': 'C:/Windows/System32'},
						{'code': [['path.dir', '/home/user/docs/file.txt']], 'result': '/home/user/docs'}
					]
				},
				'path.file': {
					'name': 'path_file',
					'group': 'file',
					'description': 'File portion of a specified file path',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['path.file', 'C:/Windows/System32/kernel32.dll']], 'result': 'kernel32.dll'},
						{'code': [['path.file', '/home/user/docs/report.pdf']], 'result': 'report.pdf'}
					]
				},
				'path.name': {
					'name': 'path_name',
					'group': 'file',
					'description': 'Name of the file without extension from a specified path',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['path.name', 'document.txt']], 'result': 'document'},
						{'code': [['path.name', '/path/to/file.name.ext']], 'result': 'file.name'}
					]
				},
				'path.extension': {
					'name': 'path_extension',
					'group': 'file',
					'description': 'File extension from a specified file path',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['path.extension', 'image.png']], 'result': '.png'},
						{'code': [['path.extension', 'archive.tar.gz']], 'result': '.gz'}
					]
				},
				'path.strip': {
					'name': 'path_strip',
					'group': 'file',
					'description': 'Removes the extension from a specified path',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['path.strip', 'file.txt']], 'result': 'file'},
						{'code': [['path.strip', '/path/to/document.pdf']], 'result': '/path/to/document'}
					]
				},
				'void.encode': {
					'name': 'void_encode',
					'group': 'format',
					'description': 'Encodes data into the Void format',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [
						{'name': 'data', 'type': 'any'},
						{'name': 'indent', 'type': 'text', 'default': '\t'}
					],
					'example': [
						{'code': [['void.encode', {'key': 'value'}]], 'result': '{\n\t\'key\': \'value\'\n}'},
						{'code': [['void.encode', [1, 2, 3], '  ']], 'result': '[\n  1,\n  2,\n  3\n]'}
					]
				},
				'void.decode': {
					'name': 'void_decode',
					'group': 'format',
					'description': 'Decodes data from the Void format',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['void.decode', '{\'key\':\'value\'}']], 'result': {'key': 'value'}},
						{'code': [['void.decode', '[1,2,3]']], 'result': [1, 2, 3]}
					]
				},
				'json.encode': {
					'name': 'json_encode',
					'group': 'format',
					'description': 'Encodes data into the JSON format',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['json.encode', {'name': 'John', 'age': 30}]], 'result': '{\'name\':\'John\',\'age\':30}'},
						{'code': [['json.encode', [True, False]]], 'result': '[true,false]'}
					]
				},
				'json.decode': {
					'name': 'json_decode',
					'group': 'format',
					'description': 'Decodes data from the JSON format',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['json.decode', '{\'x\':5,\'y\':10}']], 'result': {'x': 5, 'y': 10}},
						{'code': [['json.decode', '[\'a\',\'b\']']], 'result': ['a', 'b']}
					]
				},
				'csv.encode': {
					'name': 'csv_encode',
					'group': 'format',
					'description': 'Encodes data into the CSV format',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['csv.encode', [['Name', 'Age'], ['John', 30], ['Alice', 25]]]], 'result': 'Name,Age\nJohn,30\nAlice,25'},
						{'code': [['csv.encode', {'a': [1,2], 'b': [3,4]}]], 'result': 'a,b\n1,3\n2,4'}
					]
				},
				'csv.decode': {
					'name': 'csv_decode',
					'group': 'format',
					'description': 'Decodes data from the CSV format',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['csv.decode', 'a,b,c\n1,2,3']], 'result': [{'a':'1','b':'2','c':'3'}]},
						{'code': [['csv.decode', 'x;y\n4;5', ';']], 'result': [{'x':'4','y':'5'}]}
					]
				},
				'yaml.encode': {
					'name': 'yaml_encode',
					'group': 'format',
					'description': 'Encodes data into the YAML format',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['yaml.encode', {'name': 'John', 'skills': ['Python', 'JS']}]], 'result': 'name: John\nskills:\n  - Python\n  - JS'},
						{'code': [['yaml.encode', [1, 2, 3]]], 'result': '- 1\n- 2\n- 3'}
					]
				},
				'yaml.decode': {
					'name': 'yaml_decode',
					'group': 'format',
					'description': 'Decodes data from the YAML format',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['yaml.decode', 'key: value']], 'result': {'key': 'value'}},
						{'code': [['yaml.decode', '- 1\n- 2']], 'result': [1, 2]}
					]
				},
				'ini.encode': {
					'name': 'format.ini.encode',
					'group': 'format',
					'description': 'Encodes data into the INI format',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'vapp': True,
					'param': [],
					'example': [
						{'code': [['ini.encode', {'section': {'key': 'value'}}]], 'result': '[section]\nkey=value'},
						{'code': [['ini.encode', {'user': {'name': 'John'}, 'db': {'port': 3306}}]], 'result': '[user]\nname=John\n\n[db]\nport=3306'}
					]
				},
				'ini.decode': {
					'name': 'format.ini.decode',
					'group': 'format',
					'description': 'Decodes data from the INI format',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'vapp': True,
					'param': [],
					'example': [
						{'code': [['ini.decode', '[section]\nkey=value']], 'result': {'section': {'key': 'value'}}},
						{'code': [['ini.decode', '[user]\nname=John']], 'result': {'user': {'name': 'John'}}}
					]
				},
				'html.encode': {
					'name': 'format.html.encode',
					'group': 'format',
					'description': 'Encodes data into the HTML format',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'vapp': True,
					'param': [],
					'example': [
						{'code': [['html.encode', {'div': {'class': 'main', 'content': 'Hello'}}]], 'result': '<div class=\'main\'>Hello</div>'},
						{'code': [['html.encode', {'p': 'Paragraph'}]], 'result': '<p>Paragraph</p>'}
					]
				},
				'html.decode': {
					'name': 'format.html.decode',
					'group': 'format',
					'description': 'Decodes data from the HTML format',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'vapp': True,
					'param': [],
					'example': [
						{'code': [['html.decode', '<div>content</div>']], 'result': {'div': 'content'}},
						{'code': [['html.decode', '<a href=\'#\'>link</a>']], 'result': {'a': {'@href': '#', '#text': 'link'}}}
					]
				},
				'html.markdown': {
					'name': 'format.html.markdown',
					'group': 'format',
					'description': 'Encodes Markdown-formatted text into the HTML format',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'vapp': True,
					'param': [],
					'example': [
						{'code': [['html.markdown', '# Heading']], 'result': '<h1>Heading</h1>'},
						{'code': [['html.markdown', '**bold**']], 'result': '<p><strong>bold</strong></p>'}
					]
				},
				'xml.encode': {
					'name': 'format.xml.encode',
					'group': 'format',
					'description': 'Encodes data into the XML format',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'vapp': True,
					'param': [],
					'example': [
						{'code': [['xml.encode', {'root': {'item': ['a', 'b']}}]], 'result': '<root><item>a</item><item>b</item></root>'},
						{'code': [['xml.encode', {'person': {'@id': 1, 'name': 'John'}}]], 'result': '<person id=\'1\'><name>John</name></person>'}
					]
				},
				'xml.decode': {
					'name': 'format.xml.decode',
					'group': 'format',
					'description': 'Decodes data from the XML format',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'vapp': True,
					'param': [],
					'example': [
						{'code': [['xml.decode', '<root><x>1</x></root>']], 'result': {'root': {'x': '1'}}},
						{'code': [['xml.decode', '<person id=\'1\'><name>John</name></person>']], 'result': {'person': {'@id': '1', 'name': 'John'}}}
					]
				},
				'css.encode': {
					'name': 'format.css.encode',
					'group': 'format',
					'description': 'Encodes data into the CSS format',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'vapp': True,
					'param': [],
					'example': [
						{'code': [['css.encode', {'body': {'color': 'red'}}]], 'result': 'body { color: red; }'},
						{'code': [['css.encode', {'.class': {'margin': '10px'}}]], 'result': '.class { margin: 10px; }'}
					]
				},
				'css.decode': {
					'name': 'format.css.decode',
					'group': 'format',
					'description': 'Decodes data from the CSS format',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'vapp': True,
					'param': [],
					'example': [
						{'code': [['css.decode', 'body { color: red; }']], 'result': {'body': {'color': 'red'}}},
						{'code': [['css.decode', '.class { margin: 10px; }']], 'result': {'.class': {'margin': '10px'}}}
					]
				},
				'request': {
					'name': 'request',
					'group': 'request',
					'description': 'Sends an HTTP (GET by default) request to a specified URL',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['request', 'https://api.example.com/data']], 'test': False},
						{'code': [['request', 'https://example.com', {'headers': {'Accept': 'application/json'}}]], 'test': False}
					]
				},
				'request.post': {
					'name': 'request_post',
					'group': 'request',
					'description': 'Sends an HTTP POST request to a specified URL',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['request.post', 'https://api.example.com', {'data': {'key': 'value'}}]], 'test': False},
						{'code': [['request.post', 'https://example.com/login', {'form': {'user': 'admin'}}]], 'test': False}
					]
				},
				'request.put': {
					'name': 'request_put',
					'group': 'request',
					'description': 'Sends an HTTP PUT request to a specified URL',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['request.put', 'https://api.example.com/update', {'json': {'id': 1}}]], 'test': False},
						{'code': [['request.put', 'https://example.com/resource', {'data': 'content'}]], 'test': False}
					]
				},
				'request.delete': {
					'name': 'request_delete',
					'group': 'request',
					'description': 'Sends an HTTP DELETE request to a specified URL',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['request.delete', 'https://api.example.com/item/1']], 'test': False},
						{'code': [['request.delete', 'https://example.com/resource']], 'test': False}
					]
				},
				'request.head': {
					'name': 'request_head',
					'group': 'request',
					'description': 'Sends an HTTP HEAD request to a specified URL',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['request.head', 'https://example.com']], 'test': False},
						{'code': [['request.head', 'https://api.example.com/status']], 'test': False}
					]
				},
				'download': {
					'name': 'download.file',
					'group': 'download',
					'description': 'Downloads content from a specified URL',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'vapp': True,
					'param': [],
					'example': [
						{'code': [['download', 'https://example.com/file.txt', 'local.txt']], 'test': False},
						{'code': [['download', 'https://example.com/image.jpg']], 'test': False}
					]
				},
				'download.info': {
					'name': 'download.info',
					'group': 'download',
					'description': 'Retrieves information about a content available for download',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'vapp': True,
					'param': [],
					'example': [
						{'code': [['download.info', 'https://example.com/file.zip']], 'result': {'size': 1024, 'type': 'application/zip'}, 'test': False},
						{'code': [['download.info', 'https://example.com/video.mp4']], 'result': {'size': 5242880, 'type': 'video/mp4'}, 'test': False}
					]
				},
				'download.audio': {
					'name': 'download.audio',
					'group': 'download',
					'description': 'Downloads audio from a specified URL',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'vapp': True,
					'param': [],
					'example': [
						{'code': [['download.audio', 'https://example.com/sound.mp3']], 'test': False},
						{'code': [['download.audio', 'https://example.com/voice.ogg', 'output.ogg']], 'test': False}
					]
				},
				'download.video': {
					'name': 'download.video',
					'group': 'download',
					'description': 'Downloads video from a specified URL',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'vapp': True,
					'param': [],
					'example': [
						{'code': [['download.video', 'https://example.com/clip.mp4']], 'test': False},
						{'code': [['download.video', 'https://example.com/movie.mkv', 'film.mkv']], 'test': False}
					]
				},
				'cookie': {
					'name': 'cookie',
					'group': 'cookie',
					'description': 'Gets or sets a specified cookie',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['cookie', 'session', 'abc123']], 'test': False},
						{'code': [['cookie', 'user']], 'result': 'john_doe', 'test': False}
					]
				},
				'cookie.remove': {
					'name': 'cookie_remove',
					'group': 'cookie',
					'description': 'Removes a specified cookie from the client\'s storage',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['cookie.remove', 'session']], 'test': False},
						{'code': [['cookie.remove', 'temp']], 'test': False}
					]
				},
				'cloud': {
					'name': 'cloud',
					'group': 'cloud',
					'description': 'Runs cloud storage or services for data management',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['cloud', 'start']], 'test': False},
						{'code': [['cloud', 'status']], 'result': 'running', 'test': False}
					]
				},
				'cloud.file': {
					'name': 'cloud_file',
					'group': 'cloud',
					'description': 'Runs cloud storage',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['cloud.file', 'upload', 'data.txt']], 'test': False},
						{'code': [['cloud.file', 'list']], 'result': ['file1.txt', 'file2.txt'], 'test': False}
					]
				},
				'cloud.web': {
					'name': 'cloud_web',
					'group': 'cloud',
					'description': 'Runs WEB service',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['cloud.web', 'start', 8080]], 'test': False},
						{'code': [['cloud.web', 'stop']], 'test': False}
					]
				},
				'cloud.api': {
					'name': 'cloud_api',
					'group': 'cloud',
					'description': 'Runs API service',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['cloud.api', 'deploy', 'api.json']], 'test': False},
						{'code': [['cloud.api', 'list']], 'result': ['api1', 'api2'], 'test': False}
					]
				},
				'cloud.socket': {
					'name': 'cloud_socket',
					'group': 'cloud',
					'description': 'Runs Socket service',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['cloud.socket', 'start', 3000]], 'test': False},
						{'code': [['cloud.socket', 'send', 'message']], 'test': False}
					]
				},
				'cloud.mail': {
					'name': 'cloud_mail',
					'group': 'cloud',
					'description': 'Runs Mail service',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['cloud.mail', 'send', 'user@example.com', 'Hello']], 'test': False},
						{'code': [['cloud.mail', 'setup', 'smtp.example.com']], 'test': False}
					]
				},
				'cloud.proxy': {
					'name': 'cloud_proxy',
					'group': 'cloud',
					'description': 'Runs Proxy service',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['cloud.proxy', 'start', 8888]], 'test': False},
						{'code': [['cloud.proxy', 'stop']], 'test': False}
					]
				},
				'social': {
					'name': 'social',
					'group': 'social',
					'description': 'Interacting with social API',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['social', 'tiktok', 'upload', 'clip.mp4']], 'test': False},
						{'code': [['social', 'telegram', 'send', '@name', 'Text']], 'test': False},
						{'code': [['social', 'telegram', 'bot', 'bot_action']], 'test': False}
					]
				},
				'notification': {
					'name': 'notification',
					'group': 'notification',
					'description': 'Send notification',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['notification', 'New message']], 'test': False},
						{'code': [['notification', 'Alert', {'sound': True}]], 'test': False}
					]
				},
				'mail': {
					'name': 'mail',
					'group': 'notification',
					'description': 'Send mail',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['mail', 'user@example.com', 'Subject', 'Body']], 'test': False},
						{'code': [['mail', 'test@example.com', 'Hello', 'Content', {'cc': 'copy@example.com'}]], 'test': False}
					]
				},
				'call': {
					'name': 'call',
					'group': 'notification',
					'description': 'Initiate a voice or video call to a specified recipient',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['call', '+1234567890']], 'test': False},
						{'code': [['call', 'user@domain.com', 'video']], 'test': False}
					]
				},
				'sms': {
					'name': 'sms',
					'group': 'notification',
					'description': 'Send a text message (SMS) to a specified recipient',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['sms', '+1234567890', 'Hello']], 'test': False},
						{'code': [['sms', '+0987654321', 'Your code: 1234']], 'test': False}
					]
				},
				'sql': {
					'name': 'sql',
					'group': 'sql',
					'description': 'Execute SQL query',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['sql', 'SELECT * FROM user']], 'result': [], 'test': False},
						{'code': [['sql', 'INSERT INTO log VALUES ({1},{2})', ['date', 'message']]], 'test': False},
						{'code': [['sql', 'set', 'user', [1, 'name', 'mylogin', 'mypassword']]], 'test': False},
						{'code': [['sql', 'set', 'user', 1, {'name': 'newname'}]], 'test': False},
						{'code': [['sql', 'get', 'user']], 'test': False},
						{'code': [['sql', 'get', 'user', 1]], 'test': False},
						{'code': [['sql', 'remove', 'user', 1]], 'test': False}
					]
				},
				'os': {
					'name': 'os',
					'group': 'os',
					'description': 'Gets or checks the operating system type',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['os']], 'result': 'windows', 'test': False},
						{'code': [['os', 'check', 'linux']], 'result': False, 'test': False}
					]
				},
				'os.version': {
					'name': 'os_version',
					'group': 'os',
					'description': 'Current version of the operating system',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['os.version']], 'result': '10.0.19042', 'test': False},
						{'code': [['os.version', 'build']], 'result': '19042', 'test': False}
					]
				},
				'os.user': {
					'name': 'os_user',
					'group': 'os',
					'description': 'Information about the current user logged into the operating system',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['os.user']], 'result': {'name': 'admin', 'home': '/home/admin'}, 'test': False},
						{'code': [['os.user', 'name']], 'result': 'admin', 'test': False}
					]
				},
				'language': {
					'name': 'language',
					'group': 'os',
					'description': 'System language',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['language']], 'result': 'en-US'},
						{'code': [['language', 'set', 'ru-RU']], 'test': False}
					]
				},
				'device': {
					'name': 'device',
					'group': 'device',
					'description': 'Information related to the hardware device',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['device']], 'result': {'model': 'iPhone12,1', 'manufacturer': 'Apple'}, 'test': False},
						{'code': [['device', 'id']], 'result': 'A12B3C4D', 'test': False}
					]
				},
				'cpu': {
					'name': 'cpu',
					'group': 'device',
					'description': 'Information about the CPU, including its usage and specifications',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['cpu']], 'result': {'cores': 8, 'usage': 34.5}, 'test': False},
						{'code': [['cpu', 'temperature']], 'result': 65.2, 'test': False}
					]
				},
				'fps': {
					'name': 'fps',
					'group': 'device',
					'description': 'Frames per second for video or graphical rendering',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['fps']], 'result': 60, 'test': False},
						{'code': [['fps', 'set', 30]], 'test': False}
					]
				},
				'vsync': {
					'name': 'vsync',
					'group': 'device',
					'description': 'Vertical sync settings to reduce screen tearing during rendering',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['vsync']], 'result': True, 'test': False},
						{'code': [['vsync', 'set', False]], 'test': False}
					]
				},
				'resolution': {
					'name': 'resolution',
					'group': 'device',
					'description': 'Screen resolution',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['resolution']], 'result': [1920, 1080], 'test': False},
						{'code': [['resolution', 'set', 1280, 720]], 'test': False}
					]
				},
				'orientation': {
					'name': 'orientation',
					'group': 'device',
					'description': 'Orientation of a device\'s display (landscape or portrait)',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['orientation']], 'result': 'landscape', 'test': False},
						{'code': [['orientation', 'set', 'portrait']], 'test': False}
					]
				},
				'darkmode': {
					'name': 'darkmode',
					'group': 'device',
					'description': 'Dark mode setting for user interfaces',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['darkmode']], 'result': True, 'test': False},
						{'code': [['darkmode', 'set', False]], 'test': False}
					]
				},
				'pixel': {
					'name': 'pixel',
					'group': 'device',
					'description': 'Color of the pixel displayed on the screen',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['pixel', 100, 200]], 'result': [255, 0, 0], 'test': False},
						{'code': [['pixel', 'set', 150, 300, [0, 255, 0]]], 'test': False}
					]
				},
				'textmode.character': {
					'name': 'textmode_character',
					'group': 'device',
					'description': 'Symbol on the screen in text mode',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['textmode.character', 10, 5]], 'result': 'A', 'test': False},
						{'code': [['textmode.character', 'set', 12, 7, 'B']], 'test': False}
					]
				},
				'textmode.cursor': {
					'name': 'textmode_cursor',
					'group': 'device',
					'description': 'Cursor position on the screen in text mode',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['textmode.cursor']], 'result': [5, 10], 'test': False},
						{'code': [['textmode.cursor', 'set', 0, 0]], 'test': False}
					]
				},
				'textmode.clear': {
					'name': 'textmode_clear',
					'group': 'device',
					'description': 'Clears the screen in text mode',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['textmode.clear']], 'test': False},
						{'code': [['textmode.clear', 'green']], 'test': False}
					]
				},
				'flashlight': {
					'name': 'flashlight',
					'group': 'device',
					'description': 'Turns on or off the device\'s flashlight',
					'language': ['swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['flashlight', 'on']], 'test': False},
						{'code': [['flashlight', 'off']], 'test': False}
					]
				},
				'location': {
					'name': 'location',
					'group': 'device',
					'description': 'Retrieves the current geographic location using GPS or network triangulation',
					'language': ['js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['location']], 'result': {'lat': 55.7558, 'lon': 37.6173}, 'test': False},
						{'code': [['location', 'accuracy', 10]], 'test': False}
					]
				},
				'gyroscope': {
					'name': 'gyroscope',
					'group': 'device',
					'description': 'Provides access to the gyroscope sensor for motion detection',
					'language': ['js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['gyroscope']], 'result': {'x': 0.1, 'y': -0.2, 'z': 0.05}, 'test': False},
						{'code': [['gyroscope', 'frequency', 10]], 'test': False}
					]
				},
				'accelerometer': {
					'name': 'accelerometer',
					'group': 'device',
					'description': 'Provides access to the accelerometer sensor to detect acceleration forces',
					'language': ['js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['accelerometer']], 'result': {'x': 0.0, 'y': 0.0, 'z': 9.8}, 'test': False},
						{'code': [['accelerometer', 'calibrate']], 'test': False}
					]
				},
				'compass': {
					'name': 'compass',
					'group': 'device',
					'description': 'Accesses the magnetic compass sensor to determine orientation relative to the Earth\'s magnetic field',
					'language': ['js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['compass']], 'result': 180.5, 'test': False},
						{'code': [['compass', 'calibrate']], 'test': False}
					]
				},
				'proximity': {
					'name': 'proximity',
					'group': 'device',
					'description': 'Detects the proximity of objects in relation to the device\'s proximity sensor',
					'language': ['swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['proximity']], 'result': 5.2, 'test': False},
						{'code': [['proximity', 'threshold', 10]], 'test': False}
					]
				},
				'brightness': {
					'name': 'brightness',
					'group': 'device',
					'description': 'Manages the screen brightness level of the device',
					'language': ['swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['brightness']], 'result': 80, 'test': False},
						{'code': [['brightness', 'set', 50]], 'test': False}
					]
				},
				'calendar': {
					'name': 'calendar',
					'group': 'device',
					'description': 'Calendar events on a device',
					'language': ['swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['calendar', 'events']], 'result': [], 'test': False},
						{'code': [['calendar', 'add', 'Meeting', '2023-12-01 14:00']], 'test': False}
					]
				},
				'gallery': {
					'name': 'gallery',
					'group': 'device',
					'description': 'Photo and video library on a device',
					'language': ['swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['gallery', 'photos']], 'result': ['photo1.jpg', 'photo2.jpg'], 'test': False},
						{'code': [['gallery', 'save', 'new.jpg']], 'test': False}
					]
				},
				'contacts': {
					'name': 'contacts',
					'group': 'device',
					'description': 'Contact list on a device',
					'language': ['swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['contacts']], 'result': [{'name': 'John', 'phone': '+1234567890'}], 'test': False},
						{'code': [['contacts', 'add', 'Alice', '+0987654321']], 'test': False}
					]
				},
				'clipboard': {
					'name': 'clipboard',
					'group': 'clipboard',
					'description': 'Storing or retrieving clipboard temporary data',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['clipboard']], 'result': 'copied text', 'test': False},
						{'code': [['clipboard', 'set', 'new text']], 'test': False}
					]
				},
				'clipboard.remove': {
					'name': 'clipboard_remove',
					'group': 'clipboard',
					'description': 'Clears the clipboard content',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': False,
					'param': [],
					'example': [
						{'code': [['clipboard.remove']], 'test': False}
					]
				},
				'translate': {
					'name': 'translate',
					'group': 'ai',
					'description': 'Converts text from one language to another',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['translate', 'Hello', 'en', 'es']], 'result': 'Hola'}
					]
				},
				'spellcheck': {
					'name': 'spellcheck',
					'group': 'ai',
					'description': 'Spell check in different languages',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['spellcheck', 'Helo world']], 'result': ['Hello', 'world']}
					]
				},
				'chat': {
					'name': 'chat',
					'group': 'ai',
					'description': 'AI conversation and interaction through text',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['chat', 'What\'s the weather today?']], 'result': 'The weather is sunny and warm.'}
					]
				},
				'image': {
					'name': 'image',
					'group': 'ai',
					'description': 'Create an image',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['image', 'A sunset over mountains']], 'result': 'image.png'}
					]
				},
				'image.size': {
					'name': 'image_size',
					'group': 'ai',
					'description': 'Adjusts the dimensions of an image',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['image.size', 'image.png', 800, 600]], 'result': 'image_resized.png'}
					]
				},
				'image.square': {
					'name': 'image_square',
					'group': 'ai',
					'description': 'Crops an image to a square aspect ratio',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['image.square', 'image.png']], 'result': 'image_square.png'}
					]
				},
				'image.crop': {
					'name': 'image_crop',
					'group': 'ai',
					'description': 'Cuts a portion of the image according to specified dimensions',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['image.crop', 'image.png', 100, 100, 400, 400]], 'result': 'image_cropped.png'}
					]
				},
				'image.rotate': {
					'name': 'image_rotate',
					'group': 'ai',
					'description': 'Rotates an image by a specified number of degrees',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['image.rotate', 'image.png', 90]], 'result': 'image_rotated.png'}
					]
				},
				'image.text': {
					'name': 'image_text',
					'group': 'ai',
					'description': 'Adds text to an image at specified positions',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['image.text', 'image.png', 'Hello', 50, 50, '#FFFFFF']], 'result': 'image_with_text.png'}
					]
				},
				'image.image': {
					'name': 'image_image',
					'group': 'ai',
					'description': 'Adds an image onto another',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['image.image', 'image1.png', 'image2.png', 100, 100]], 'result': 'combined_image.png'}
					]
				},
				'image.grayscale': {
					'name': 'image_grayscale',
					'group': 'ai',
					'description': 'Converts an image to grayscale',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['image.grayscale', 'image.png']], 'result': 'image_grayscale.png'}
					]
				},
				'image.tint': {
					'name': 'image_tint',
					'group': 'ai',
					'description': 'Applies a color tint to an image',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['image.tint', 'image.png', '#FF0000']], 'result': 'image_tinted.png'}
					]
				},
				'image.flip.h': {
					'name': 'image_flip_h',
					'group': 'ai',
					'description': 'Flips an image horizontally',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['image.flip.h', 'image.png']], 'result': 'image_flipped_h.png'}
					]
				},
				'image.flip.v': {
					'name': 'image_flip_v',
					'group': 'ai',
					'description': 'Flips an image vertically',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['image.flip.v', 'image.png']], 'result': 'image_flipped_v.png'}
					]
				},
				'image.upscale': {
					'name': 'image_upscale',
					'group': 'ai',
					'description': 'Increases the resolution of an image',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['image.upscale', 'image.png', 2]], 'result': 'image_upscaled.png'}
					]
				},
				'image.draw': {
					'name': 'image_draw',
					'group': 'ai',
					'description': 'Allows draw, clear or replace objects on an image',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['image.draw', 'image.png', 'circle', 100, 100, 50, '#FF0000']], 'result': 'image_drawn.png'}
					]
				},
				'image.style': {
					'name': 'image_style',
					'group': 'ai',
					'description': 'Applies stylistic effects to an image',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['image.style', 'image.png', 'watercolor']], 'result': 'image_styled.png'}
					]
				},
				'image.colorize': {
					'name': 'image_colorize',
					'group': 'ai',
					'description': 'Adds color to a grayscale image',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['image.colorize', 'grayscale.png', '#3366FF']], 'result': 'image_colorized.png'}
					]
				},
				'image.recognize': {
					'name': 'image_recognize',
					'group': 'ai',
					'description': 'Identifies objects or text within an image',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['image.recognize', 'image.png']], 'result': ['cat', 'tree', 'sun']}
					]
				},
				'image.face': {
					'name': 'image_face',
					'group': 'ai',
					'description': 'Detects and processes faces within an image',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['image.face', 'photo.png']], 'result': [{'x': 100, 'y': 120, 'width': 200, 'height': 200}]}
					]
				},
				'image.effect': {
					'name': 'image_effect',
					'group': 'ai',
					'description': 'Applies special effects to an image',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['image.effect', 'image.png', 'blur']], 'result': 'image_effect.png'}
					]
				},
				'video': {
					'name': 'video',
					'group': 'ai',
					'description': 'Create a video',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['video', 'A beach sunset', 10]], 'result': 'video.mp4'}
					]
				},
				'video.crop': {
					'name': 'video_crop',
					'group': 'ai',
					'description': 'Cuts a portion of the video according to specified dimensions',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['video.crop', 'video.mp4', 0, 0, 640, 480]], 'result': 'video_cropped.mp4'}
					]
				},
				'video.text': {
					'name': 'video_text',
					'group': 'ai',
					'description': 'Adds text to a video at specified positions',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['video.text', 'video.mp4', 'Hello', 50, 50, '#FFFFFF', 0, 5]], 'result': 'video_with_text.mp4'}
					]
				},
				'video.image': {
					'name': 'video_image',
					'group': 'ai',
					'description': 'Adds an image to a video',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['video.image', 'video.mp4', 'logo.png', 10, 10, 0, 10]], 'result': 'video_with_image.mp4'}
					]
				},
				'video.sound': {
					'name': 'video_sound',
					'group': 'ai',
					'description': 'Adds audio track to a video',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['video.sound', 'video.mp4', 'music.mp3']], 'result': 'video_with_sound.mp4'}
					]
				},
				'video.video': {
					'name': 'video_video',
					'group': 'ai',
					'description': 'Adds another video clip to a video',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['video.video', 'video1.mp4', 'video2.mp4', 5]], 'result': 'combined_video.mp4'}
					]
				},
				'video.trim': {
					'name': 'video_trim',
					'group': 'ai',
					'description': 'Trims the video to a specified length',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['video.trim', 'video.mp4', 5, 10]], 'result': 'video_trimmed.mp4'}
					]
				},
				'video.size': {
					'name': 'video_size',
					'group': 'ai',
					'description': 'Adjusts the dimensions of a video',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['video.size', 'video.mp4', 1280, 720]], 'result': 'video_resized.mp4'}
					]
				},
				'video.upscale': {
					'name': 'video_upscale',
					'group': 'ai',
					'description': 'Increases the resolution of a video',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['video.upscale', 'video.mp4', 2]], 'result': 'video_upscaled.mp4'}
					]
				},
				'video.speed': {
					'name': 'video_speed',
					'group': 'ai',
					'description': 'Adjusts the playback speed of a video',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['video.speed', 'video.mp4', 1.5]], 'result': 'video_spedup.mp4'}
					]
				},
				'video.volume': {
					'name': 'video_volume',
					'group': 'ai',
					'description': 'Adjusts the volume of the video\'s audio track',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['video.volume', 'video.mp4', 0.5]], 'result': 'video_volume_adjusted.mp4'}
					]
				},
				'video.mute': {
					'name': 'video_mute',
					'group': 'ai',
					'description': 'Removes sound from a video',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['video.mute', 'video.mp4']], 'result': 'video_muted.mp4'}
					]
				},
				'video.face': {
					'name': 'video_face',
					'group': 'ai',
					'description': 'Detects and processes faces within a video',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['video.face', 'video.mp4']], 'result': [{'time': 1.5, 'faces': [{'x': 100, 'y': 120, 'width': 200, 'height': 200}]}]}
					]
				},
				'video.effect': {
					'name': 'video_effect',
					'group': 'ai',
					'description': 'Applies special effects to a video',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['video.effect', 'video.mp4', 'sepia']], 'result': 'video_effect.mp4'}
					]
				},
				'sound': {
					'name': 'sound',
					'group': 'ai',
					'description': 'Create audio track',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['sound', 'Ocean waves', 30]], 'result': 'sound.mp3'}
					]
				},
				'sound.trim': {
					'name': 'sound_trim',
					'group': 'ai',
					'description': 'Trims the audio track to a specified length',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['sound.trim', 'sound.mp3', 5, 15]], 'result': 'sound_trimmed.mp3'}
					]
				},
				'sound.speed': {
					'name': 'sound_speed',
					'group': 'ai',
					'description': 'Adjusts the playback speed of audio',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['sound.speed', 'sound.mp3', 1.2]], 'result': 'sound_spedup.mp3'}
					]
				},
				'sound.volume': {
					'name': 'sound_volume',
					'group': 'ai',
					'description': 'Adjusts the volume of an audio track',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['sound.volume', 'sound.mp3', 0.7]], 'result': 'sound_volume_adjusted.mp3'}
					]
				},
				'sound.effect': {
					'name': 'sound_effect',
					'group': 'ai',
					'description': 'Applies special effects to an audio track',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['sound.effect', 'sound.mp3', 'echo']], 'result': 'sound_effect.mp3'}
					]
				},
				'music': {
					'name': 'music',
					'group': 'ai',
					'description': 'Generates music',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['music', 'Relaxing piano', 180]], 'result': 'music.mp3'}
					]
				},
				'voice': {
					'name': 'voice',
					'group': 'ai',
					'description': 'Text voicing with different voices',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['voice', 'Hello world', 'en-US']], 'result': 'voice.mp3'}
					]
				},
				'voice.list': {
					'name': 'voice_list',
					'group': 'ai',
					'description': 'List of available voices',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['voice.list']], 'result': ['en-US', 'es-ES', 'fr-FR']}
					]
				},
				'voice.recognize': {
					'name': 'voice_recognize',
					'group': 'ai',
					'description': 'Convert voice to text',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['voice.recognize', 'voice.mp3']], 'result': 'Hello world'}
					]
				},
				'voice.stop': {
					'name': 'voice_stop',
					'group': 'ai',
					'description': 'Stop dictation of the text',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['voice.stop']], 'result': True}
					]
				},
				'voice.capture': {
					'name': 'voice_capture',
					'group': 'ai',
					'description': 'Create a specific voice',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['voice.capture', 'sample.mp3', 'My Voice']], 'result': 'custom_voice_model'}
					]
				},
				'motion': {
					'name': 'motion',
					'group': 'ai',
					'description': 'Processes motion-based data',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['motion', 'walking']], 'result': {'speed': 1.2, 'steps': 500}}
					]
				},
				'motion.capture': {
					'name': 'motion_capture',
					'group': 'ai',
					'description': 'Records or analyzes motion data in real-time',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['motion.capture', 10]], 'result': {'positions': [[0,0], [0.1,0], [0.2,0.1]]}}
					]
				},
				'google.voice': {
					'name': 'google_voice',
					'group': 'ai',
					'description': 'Utilizes Google\'s voice recognition services',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['google.voice', 'Hello', 'en-US']], 'result': 'google_voice.mp3'}
					]
				},
				'google.voice.list': {
					'name': 'google_voice_list',
					'group': 'ai',
					'description': 'Lists available voice options via Google services',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['google.voice.list']], 'result': ['en-US-Standard', 'es-ES-Standard']}
					]
				},
				'google.voice.recognize': {
					'name': 'google_voice_recognize',
					'group': 'ai',
					'description': 'Recognizes speech using Google technology',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['google.voice.recognize', 'audio.mp3']], 'result': 'Recognized text'}
					]
				},
				'google.translate': {
					'name': 'google_translate',
					'group': 'ai',
					'description': 'Utilizes Google\'s translation services',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['google.translate', 'Hello', 'en', 'es']], 'result': 'Hola'}
					]
				},
				'deepl.translate': {
					'name': 'deepl_translate',
					'group': 'ai',
					'description': 'Utilizes DeepL\'s translation services',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['deepl.translate', 'Hello', 'en', 'de']], 'result': 'Hallo'}
					]
				},
				'openai.chat': {
					'name': 'openai_chat',
					'group': 'ai',
					'description': 'Conversation using OpenAI\'s chat models',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['openai.chat', 'Explain quantum physics']], 'result': 'Quantum physics is...'}
					]
				},
				'openai.image': {
					'name': 'openai_image',
					'group': 'ai',
					'description': 'Generates or processes images using OpenAI\'s models',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['openai.image', 'A futuristic city']], 'result': 'openai_image.png'}
					]
				},
				'openai.video': {
					'name': 'openai_video',
					'group': 'ai',
					'description': 'Generates or processes videos using OpenAI\'s models',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['openai.video', 'A sunset timelapse', 10]], 'result': 'openai_video.mp4'}
					]
				},
				'openai.translate': {
					'name': 'openai_translate',
					'group': 'ai',
					'description': 'Utilizes OpenAI\'s services for text translation',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['openai.translate', 'Hello', 'en', 'fr']], 'result': 'Bonjour'}
					]
				},
				'deepseek.chat': {
					'name': 'deepseek_chat',
					'group': 'ai',
					'description': 'Conversation using DeepSeek\'s chat models',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['deepseek.chat', 'What is AI?']], 'result': 'AI stands for...'}
					]
				},
				'deepseek.translate': {
					'name': 'deepseek_translate',
					'group': 'ai',
					'description': 'Utilizes DeepSeek\'s services for text translation',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['deepseek.translate', 'Hello', 'en', 'it']], 'result': 'Ciao'}
					]
				},
				'claude.chat': {
					'name': 'claude_chat',
					'group': 'ai',
					'description': 'Conversation using Claude\'s chat models',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['claude.chat', 'Tell me a joke']], 'result': 'Why did the AI...'}
					]
				},
				'stablediffusion.image': {
					'name': 'stablediffusion_image',
					'group': 'ai',
					'description': 'Generates artistic images using Stable Diffusion models',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['stablediffusion.image', 'A dragon flying over mountains']], 'result': 'sd_image.png'}
					]
				},
				'stablediffusion.upscale': {
					'name': 'stablediffusion_upscale',
					'group': 'ai',
					'description': 'Enhances image resolution using Stable Diffusion models',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['stablediffusion.upscale', 'image.png', 2]], 'result': 'image_upscaled.png'}
					]
				},
				'stablediffusion.draw': {
					'name': 'stablediffusion_draw',
					'group': 'ai',
					'description': 'Creating and replacing objects in an image using Stable Diffusion models',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['stablediffusion.draw', 'image.png', 'add a dragon']], 'result': 'image_with_dragon.png'}
					]
				},
				'stablediffusion.background': {
					'name': 'stablediffusion_background',
					'group': 'ai',
					'description': 'Background removal using Stable Diffusion models',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['stablediffusion.background', 'photo.png']], 'result': 'photo_no_bg.png'}
					]
				},
				'stablediffusion.video': {
					'name': 'stablediffusion_video',
					'group': 'ai',
					'description': 'Creates videos using Stable Diffusion\'s models',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['stablediffusion.video', 'A forest animation', 5]], 'result': 'sd_video.mp4'}
					]
				},
				'ollama.chat': {
					'name': 'ollama_chat',
					'group': 'ai',
					'description': 'Conversation using Ollama\'s chat models',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['ollama.chat', 'Explain blockchain']], 'result': 'Blockchain is...'}
					]
				},
				'ui': {
					'name': 'ui',
					'group': 'ui',
					'description': 'Creating a basic element of user interface',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['ui', 'button', 'Click me']], 'result': 'button1'}
					]
				},
				'bg': {
					'name': 'bg',
					'group': 'ui',
					'description': 'Sets or updates the background properties, such as color or image',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['bg', '#3366FF']], 'result': True}
					]
				},
				'show': {
					'name': 'show',
					'group': 'ui',
					'description': 'Displays a UI element to make it visible',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['show', 'button1']], 'result': True}
					]
				},
				'hide': {
					'name': 'hide',
					'group': 'ui',
					'description': 'Hides a UI element to make it invisible',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['hide', 'button1']], 'result': True}
					]
				},
				'enable': {
					'name': 'enable',
					'group': 'ui',
					'description': 'Enables a UI element, making it interactive and functional',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['enable', 'button1']], 'result': True}
					]
				},
				'disable': {
					'name': 'disable',
					'group': 'ui',
					'description': 'Disables a UI element, preventing interaction or use',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['disable', 'button1']], 'result': True}
					]
				},
				'focus': {
					'name': 'focus',
					'group': 'ui',
					'description': 'Sets focus on a specific UI element, making it active or highlighted',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['focus', 'input1']], 'result': True}
					]
				},
				'unfocus': {
					'name': 'unfocus',
					'group': 'ui',
					'description': 'Removes focus from a UI element',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['unfocus']], 'result': True}
					]
				},
				'scale': {
					'name': 'scale',
					'group': 'ui',
					'description': 'Adjusts the size of a UI element by scaling it up or down',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['scale', 'image1', 1.5]], 'result': True}
					]
				},
				'ui.text': {
					'name': 'ui_text',
					'group': 'ui',
					'description': 'Displays or manages text within the user interface',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['ui.text', 'Hello World']], 'result': 'text1'}
					]
				},
				'ui.image': {
					'name': 'ui_image',
					'group': 'ui',
					'description': 'Displays or manages images within the user interface',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['ui.image', 'photo.png']], 'result': 'image1'}
					]
				},
				'ui.video': {
					'name': 'ui_video',
					'group': 'ui',
					'description': 'Handles video playback or displays video content in the UI',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['ui.video', 'video.mp4']], 'result': 'video1'}
					]
				},
				'ui.sound': {
					'name': 'ui_sound',
					'group': 'ui',
					'description': 'Manages sound playback or controls audio settings in the UI',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['ui.sound', 'sound.mp3']], 'result': 'sound1'}
					]
				},
				'ui.camera': {
					'name': 'ui_camera',
					'group': 'ui',
					'description': 'Handles camera input or streams video from a camera in the UI',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['ui.camera']], 'result': 'camera1'}
					]
				},
				'ui.draw': {
					'name': 'ui_draw',
					'group': 'ui',
					'description': 'Enables drawing within the user interface',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['ui.draw', 400, 300]], 'result': 'canvas1'}
					]
				},
				'ui.header': {
					'name': 'ui_header',
					'group': 'ui',
					'description': 'Defines or manages the header section of the user interface',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['ui.header', 'My App']], 'result': 'header1'}
					]
				},
				'ui.footer': {
					'name': 'ui_footer',
					'group': 'ui',
					'description': 'Defines or manages the footer section of the user interface',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['ui.footer', '© 2023']], 'result': 'footer1'}
					]
				},
				'ui.wait': {
					'name': 'ui_wait',
					'group': 'ui',
					'description': 'Displays a waiting indicator within the UI',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['ui.wait']], 'result': 'wait1'}
					]
				},
				'ui.gallery': {
					'name': 'ui_gallery',
					'group': 'ui',
					'description': 'Manages or displays a collection of images or media items',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['ui.gallery', ['img1.jpg', 'img2.jpg']]], 'result': 'gallery1'}
					]
				},
				'ui.button': {
					'name': 'ui_button',
					'group': 'ui',
					'description': 'Defines or manages buttons in the UI for user interaction',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['ui.button', 'Click me']], 'result': 'button1'}
					]
				},
				'ui.select': {
					'name': 'ui_select',
					'group': 'ui',
					'description': 'Creates or manages a selection interface, such as a dropdown menu',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['ui.select', ['Option 1', 'Option 2']]], 'result': 'select1'}
					]
				},
				'ui.switch': {
					'name': 'ui_switch',
					'group': 'ui',
					'description': 'Implements a toggle switch for binary choices in the UI',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['ui.switch', True]], 'result': 'switch1'}
					]
				},
				'ui.progress': {
					'name': 'ui_progress',
					'group': 'ui',
					'description': 'Displays a progress bar or status indicator',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['ui.progress', 50]], 'result': 'progress1'}
					]
				},
				'ui.slider': {
					'name': 'ui_slider',
					'group': 'ui',
					'description': 'Implements a sliding control for adjusting values along a range',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['ui.slider', 0, 100, 50]], 'result': 'slider1'}
					]
				},
				'ui.edit': {
					'name': 'ui_edit',
					'group': 'ui',
					'description': 'Enables text editing or manages editable fields in the UI',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['ui.edit', 'Type here']], 'result': 'edit1'}
					]
				},
				'ui.divider': {
					'name': 'ui_divider',
					'group': 'ui',
					'description': 'Inserts a visual divider or separating line within the UI layout',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['ui.divider']], 'result': 'divider1'}
					]
				},
				'ui.split.h': {
					'name': 'ui_split_h',
					'group': 'ui',
					'description': 'Splits a UI container horizontally to create multiple sections',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['ui.split.h', 'panel1', 0.5]], 'result': ['panel1_left', 'panel1_right']}
					]
				},
				'ui.split.v': {
					'name': 'ui_split_v',
					'group': 'ui',
					'description': 'Splits a UI container vertically to create multiple sections',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['ui.split.v', 'panel1', 0.3]], 'result': ['panel1_top', 'panel1_bottom']}
					]
				},
				'ui.list': {
					'name': 'ui_list',
					'group': 'ui',
					'description': 'Displays a list of items for selection or viewing',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['ui.list', ['Item 1', 'Item 2']]], 'result': 'list1'}
					]
				},
				'ui.tile': {
					'name': 'ui_tile',
					'group': 'ui',
					'description': 'Arranges content in a tiled format for visual organization',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['ui.tile', ['img1.jpg', 'img2.jpg'], 3]], 'result': 'tile1'}
					]
				},
				'ui.chart': {
					'name': 'ui_chart',
					'group': 'ui',
					'description': 'Data visualization using charts and graphs',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['ui.chart', {}]]}
					]
				},
				'ui.color': {
					'name': 'ui_color',
					'group': 'ui',
					'description': 'Color selection or manages color properties in the UI',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['ui.color', '#FF0000']], 'result': 'color1'}
					]
				},
				'ui.date': {
					'name': 'ui_date',
					'group': 'ui',
					'description': 'Date selection or displays date information',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['ui.date']], 'result': 'date1'}
					]
				},
				'ui.menu': {
					'name': 'ui_menu',
					'group': 'ui',
					'description': 'Creates or manages menu options for navigation or actions',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['ui.menu', ['File', 'Edit']]], 'result': 'menu1'}
					]
				},
				'ui.menu.context': {
					'name': 'ui_menu_context',
					'group': 'ui',
					'description': 'Defines a context menu for right-click actions or additional options',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['ui.menu.context', 'element1', ['Copy', 'Paste']]], 'result': True}
					]
				},
				'window': {
					'name': 'window',
					'group': 'ui',
					'description': 'Creates or manages window',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['window', 'My Window', 800, 600]], 'result': 'window1'}
					]
				},
				'window.list': {
					'name': 'window_list',
					'group': 'ui',
					'description': 'List of windows',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['window.list']], 'result': ['window1', 'window2']}
					]
				},
				'title': {
					'name': 'title',
					'group': 'ui',
					'description': 'Sets or updates the title of a window or UI element',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['title', 'window1', 'New Title']], 'result': True}
					]
				},
				'icon': {
					'name': 'icon',
					'group': 'ui',
					'description': 'Defines or changes an icon associated with a window or UI element',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['icon', 'window1', 'app.ico']], 'result': True}
					]
				},
				'size': {
					'name': 'size',
					'group': 'ui',
					'description': 'Adjusts the dimensions or size of a window or UI element',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['size', 'window1', 1024, 768]], 'result': True}
					]
				},
				'size.max': {
					'name': 'size_max',
					'group': 'ui',
					'description': 'Sets the maximum size constraints for a window or UI element',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['size.max', 'window1', 1920, 1080]], 'result': True}
					]
				},
				'size.min': {
					'name': 'size_min',
					'group': 'ui',
					'description': 'Sets the minimum size constraints for a window or UI element',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['size.min', 'window1', 400, 300]], 'result': True}
					]
				},
				'position': {
					'name': 'position',
					'group': 'ui',
					'description': 'Adjusts the position or placement of a window or UI element',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['position', 'window1', 100, 50]], 'result': True}
					]
				},
				'direction': {
					'name': 'direction',
					'group': 'ui',
					'description': 'Text writing direction for the selected language',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['direction', 'rtl']], 'result': True}
					]
				},
				'attention': {
					'name': 'attention',
					'group': 'ui',
					'description': 'Highlights a window or UI element',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['attention', 'window1']], 'result': True}
					]
				},
				'top': {
					'name': 'top',
					'group': 'ui',
					'description': 'Brings a window or UI element to the top layer or foreground',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['top', 'window1']], 'result': True}
					]
				},
				'nofocus': {
					'name': 'nofocus',
					'group': 'ui',
					'description': 'Prevents a UI element from receiving focus or interaction',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['nofocus', 'window1']], 'result': True}
					]
				},
				'noresize': {
					'name': 'noresize',
					'group': 'ui',
					'description': 'Locks the size of a window or UI element, preventing resizing',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['noresize', 'window1']], 'result': True}
					]
				},
				'center': {
					'name': 'center',
					'group': 'ui',
					'description': 'Centers a window or UI element within its parent container or screen',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['center', 'window1']], 'result': True}
					]
				},
				'fullscreen': {
					'name': 'fullscreen',
					'group': 'ui',
					'description': 'Switches a window or UI element to fullscreen mode',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['fullscreen', 'window1']], 'result': True}
					]
				},
				'maximize': {
					'name': 'maximize',
					'group': 'ui',
					'description': 'Minimizes a window to the taskbar or dock',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['maximize', 'window1']], 'result': True}
					]
				},
				'minimize': {
					'name': 'minimize',
					'group': 'ui',
					'description': '',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['minimize', 'window1']], 'result': True}
					]
				},
				'exclusive': {
					'name': 'exclusive',
					'group': 'ui',
					'description': 'Enables exclusive mode restricting other operations',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['exclusive', 'window1']], 'result': True}
					]
				},
				'border': {
					'name': 'border',
					'group': 'ui',
					'description': 'Border properties or visibility for a UI element',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['border', 'window1', False]], 'result': True}
					]
				},
				'filedrop': {
					'name': 'filedrop',
					'group': 'ui',
					'description': 'File drag-and-drop capabilities within the application UI',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['filedrop', 'window1', True]], 'result': True}
					]
				},
				'dialog': {
					'name': 'dialog',
					'group': 'ui',
					'description': 'Dialog box for user prompts or options',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['dialog', 'Are you sure?']], 'result': True}
					]
				},
				'dialog.file': {
					'name': 'dialog_file',
					'group': 'ui',
					'description': 'Opens a file selection dialog',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['dialog.file']], 'result': '/path/to/file.txt'}
					]
				},
				'effect': {
					'name': 'effect',
					'group': 'ui',
					'description': 'Applies visual or audio effect to a UI element',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['effect', 'window1', 'blur']], 'result': True}
					]
				},
				'effect.remove': {
					'name': 'effect_remove',
					'group': 'ui',
					'description': 'Removes applied effect from a UI element',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['effect.remove', 'window1']], 'result': True}
					]
				},
				'tap': {
					'name': 'tap',
					'group': 'input',
					'description': 'Simulates a tap gesture',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['tap', 100, 200]], 'result': True}
					]
				},
				'key': {
					'name': 'key',
					'group': 'input',
					'description': 'Key binding',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['key', 'Ctrl+S', 'save']], 'result': True}
					]
				},
				'key.remove': {
					'name': 'key_remove',
					'group': 'input',
					'description': 'Removes a key binding',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['key.remove', 'Ctrl+S']], 'result': True}
					]
				},
				'key.enable': {
					'name': 'key_enable',
					'group': 'input',
					'description': 'Enables key binding',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['key.enable', 'Ctrl+S']], 'result': True}
					]
				},
				'key.disable': {
					'name': 'key_disable',
					'group': 'input',
					'description': 'Disable key binding',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['key.disable', 'Ctrl+S']], 'result': True}
					]
				},
				'key.press': {
					'name': 'key_press',
					'group': 'input',
					'description': 'Simulates a key press event',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['key.press', 'Enter']], 'result': True}
					]
				},
				'keyboard': {
					'name': 'keyboard',
					'group': 'input',
					'description': 'Keyboard information',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['keyboard']], 'result': {'layout': 'QWERTY', 'language': 'en-US'}}
					]
				},
				'mouse': {
					'name': 'mouse',
					'group': 'input',
					'description': 'Mouse information',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['mouse']], 'result': {'x': 500, 'y': 300, 'buttons': 0}}
					]
				},
				'mouse.lock': {
					'name': 'mouse_lock',
					'group': 'input',
					'description': 'Locks the mouse cursor to prevent it from leaving a designated area',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['mouse.lock', True]], 'result': True}
					]
				},
				'mouse.position': {
					'name': 'mouse_position',
					'group': 'input',
					'description': 'Retrieves or sets the current position of the mouse cursor',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['mouse.position', 400, 300]], 'result': True}
					]
				},
				'mouse.shape': {
					'name': 'mouse_shape',
					'group': 'input',
					'description': 'Change the shape of the mouse cursor',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['mouse.shape', 'pointer']], 'result': True}
					]
				},
				'gamepad': {
					'name': 'gamepad',
					'group': 'input',
					'description': 'Gamepad information',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['gamepad', 0]], 'result': {'buttons': [False], 'axes': [0.0]}}
					]
				},
				'gamepad.vibrate': {
					'name': 'gamepad_vibrate',
					'group': 'input',
					'description': 'Gamepad vibration',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['gamepad.vibrate', 0, 0.5, 0.5]], 'result': True}
					]
				},
				'game': {
					'name': 'game',
					'group': 'game',
					'description': 'Create a custom game',
					'language': ['python', 'js', 'swift', 'kotlin', 'c++', 'godot'],
					'safe': True,
					'param': [],
					'example': [
						{'code': [['game', 'My Game', 800, 600]], 'result': 'game1'}
					]
				}
			}
		},
		'app': {
			'path': '',
			'name': '',
			'argument': []
		},
		'const': {
			'pi': 3.1415926535,
			'e': 2.7182818284,
			'phi': 1.6180339887,
			'sqrt2': 1.4142135623,
			'ln2': 0.6931471805,
			'gamma': 0.5772156649,
			'sqrt3': 1.7320508075,
			'ln10': 2.3025850929,
			'pi^2': 9.8696044011,
			'2pi': 6.2831853071,
			'g': 0.9159655941,
			'zeta3': 1.2020569032,
			'e^pi': 23.1406926327,
			'pi/e': 1.1557273498,
			'sqrt5': 2.2360679775,
			'zeta2': 1.6449340668,
			'pi': 1.7724538509,
			'sqrtpi': 0.3183098861,
			'l': 0.1100010000,
			'c10': 0.1234567891,
			'feigenbaumdelta': 4.6692016091,
			'feigenbaumalfa': 2.5029078750,
			'k': 2.6854520010,
			'a': 1.2824271291,
			'e^gamma': 1.7810724179,
			'sqrt6': 2.4494897427,
			'zeta5': 1.0369277551,
			'lambda': 2.6220575543,
			'cahen': 0.6434105462,
			'pi^3': 31.0062766803,
			'zeta4': 1.0823232337,
			'log210': 3.3219280949,
			'log102': 0.3010299956,
			'log10e': 0.4342944819,
			'conway': 1.3035772690,
			'sqrt7': 2.6457513111,
			'rho': 1.3247179572,
			'delta': 0.1039931210,
			'sqrt2pi': 2.5066282746,
			'1/e': 0.3678794412,
			'gauss': 0.8346268417,
			'omega': 0.5671432904,
			'artin': 0.3739558136,
			'sierpinski': 2.5849817596,
			'wallis': 2.0945514815,
			'ramanujan': 2625374126.0,
			'brun': 1.9021605831,
			'mrb': 0.1878596424,
			'silver': 2.4142135623,
			'eulerbeta': 3.1415926535,
			'zeta2': 1.6449340668,
			'log2e': 1.4426950408,
			'log2pi': 1.6514961295,
			'pi^5': 306.0196847853,
			'sqrtpi': 1.7724538509,
			'lnpi': 1.1447298858,
			'ln1+sqrt2': 0.8813735870,
			'e^e': 15.1542622414,
			'e^1/pi': 1.4391645526,
			'li2': 1.0451637801,
			'sin1': 0.8414709848,
			'cos1': 0.5403023059,
			'tan1': 1.5574077247,
			'sinh1': 1.1752011936,
			'cosh1': 1.5430806348,
			'tanh1': 0.7615941559,
			'gamma^2': 0.3331779239,
			'pi^6': 961.3891935753,
			'pi^7': 3020.2932278,
			'lnphi': 0.4812118251,
			'pi/4': 0.7853981634,
			'pi/2': 1.5707963268,
			'lnsqrt2pi': 0.9189385332,
			'zeta6': 1.0173430619,
			'zeta7': 1.0083492774,
			'gammaeulergelfand': 0.8346268417,
			'cbrt2': 1.2599210499,
			'cbrtpi': 1.4645918875,
			'fthrt2': 1.1892071150,
			'fthrtpi': 1.3313353638,
			'e^0.5': 1.6487212707,
			'lnln2': -0.3665129205,
			'lnln10': 0.8340324452,
			'zeta8': 1.0040773562,
			'zeta9': 1.0020083928,
			'1/pi': 0.3183098861,
			'e^-pi': 0.0432139183,
			'e^sqrt2': 4.1132503788,
			'pi^pi': 36.4621596072,
			'e^pi-pi': 19.9991009792,
			'1+phi': 2.6180339887,
			'lnphi^2': 0.9624236502,
			'lnphi^-1': -0.4812118251,
			'zeta10': 1.0009945751,
			'zeta12': 1.0002460866,
			'zetainf': 1.0
		},
		'device': {},
		'os': {},
		'cloud': {
			'mime': {
				'html': 'text/html',
				'htm': 'text/html',
				'xml': 'application/xml',
				'text': 'text/plain',
				'txt': 'text/plain',
				'void': 'application/void',
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
			'code': {
				100: 'Continue',
				101: 'Switching protocols',
				102: 'Processing',
				103: 'Early Hints',
				200: 'OK',
				201: 'Created',
				202: 'Accepted',
				203: 'Non-Authoritative Information',
				204: 'No Content',
				205: 'Reset Content',
				206: 'Partial Content',
				207: 'Multi-Status',
				208: 'Already Reported',
				226: 'IM Used',
				300: 'Multiple Choices',
				301: 'Moved Permanently',
				302: 'Found (Previously \'Moved Temporarily\')',
				303: 'See Other',
				304: 'Not Modified',
				305: 'Use Proxy',
				306: 'Switch Proxy',
				307: 'Temporary Redirect',
				308: 'Permanent Redirect',
				400: 'Bad Request',
				401: 'Unauthorized',
				402: 'Payment Required',
				403: 'Forbidden',
				404: 'Not Found',
				405: 'Method Not Allowed',
				406: 'Not Acceptable',
				407: 'Proxy Authentication Required',
				408: 'Request Timeout',
				409: 'Conflict',
				410: 'Gone',
				411: 'Length Required',
				412: 'Precondition Failed',
				413: 'Payload Too Large',
				414: 'URI Too Long',
				415: 'Unsupported Media Type',
				416: 'Range Not Satisfiable',
				417: 'Expectation Failed',
				418: 'I\'m a Teapot',
				421: 'Misdirected Request',
				422: 'Unprocessable Entity',
				423: 'Locked',
				424: 'Failed Dependency',
				425: 'Too Early',
				426: 'Upgrade Required',
				428: 'Precondition Required',
				429: 'Too Many Requests',
				431: 'Request Header Fields Too Large',
				451: 'Unavailable For Legal Reasons',
				500: 'Internal Server Error',
				501: 'Not Implemented',
				502: 'Bad Gateway',
				503: 'Service Unavailable',
				504: 'Gateway Timeout',
				505: 'HTTP Version Not Supported',
				506: 'Variant Also Negotiates',
				507: 'Insufficient Storage',
				508: 'Loop Detected',
				510: 'Not Extended',
				511: 'Network Authentication Required'
			}
		},
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
			'words': [
				['find', '{data}', [' ', '\n', '\t']],
				'n',
				'X'
			],
			'sentences': [
				['find', '{data}', ['.', '!', '?']],
				'n',
				'X'
			],
			'lines': [
				['find', '{data}', '\n'],
				'n',
				'X'
			],
			'bytes': [
				['byte', '{data}'],
				'n',
				'X'
			],
			'format': {
				'ini': {
					'encode': [],
					'decode': []
				},
				'html': {
					'encode': [],
					'decode': [],
					'markdown': []
				},
				'xml': {
					'encode': [],
					'decode': []
				},
				'css': {
					'encode': [],
					'decode': []
				}
			},
			'download': {
				'file': [],
				'info': [],
				'audio': [],
				'video': []
			}
		},
		'text': {
			'void': {
				'style': {
					'price': {
						'dot': 5,
						'before': '∞',
						'group': ' '
					}
				}
			}
		}
	}

	# value

	def get(name, default = None, data = None):
		if name.startswith('./'):
			pass
		elif name.startswith('http://') or name.startswith('https://'):
			pass
		if data == None:
			data = void.data
		names = name.split('.')
		names.reverse()
		while len(names) > 0:
			subname = names.pop()
			subtype = type(data)
			last = len(names) == 0
			if subtype is dict:
				if subname not in data:
					return default
				if last:
					return data[subname]
				data = data[subname]
			elif subtype is list:
				try:
					subname = int(subname)
				except:
					return default
				if len(data) <= subname:
					return default
				if last:
					return data[subname]
				data = data[subname]
			else:
				return default

	def set(name: str, value = None, data = None):
		if data == None:
			data = void.data
		names = name.split('.')
		names.reverse()
		while len(names) > 0:
			subname = names.pop()
			subtype = type(data)
			last = len(names) == 0
			if subtype is dict:
				if subname not in data:
					data[subname] = {}
				if last:
					data[subname] = value
					return
				data = data[subname]
			elif subtype is list:
				try:
					subname = int(subname)
				except:
					return
				if len(data) <= subname:
					if len(data) == subname:
						data.append({})
					else:
						return
				if last:
					data[subname] = value
					return
				data = data[subname]
			else:
				return

	def remove(name: str, data = None):
		if data == None:
			data = void.data
		names = name.split('.')
		names.reverse()
		while len(names) > 0:
			subname = names.pop()
			subtype = type(data)
			last = len(names) == 0
			if subtype is dict:
				if subname not in data:
					return
				if last:
					del data[subname]
					return
				data = data[subname]
			elif subtype is list:
				try:
					subname = int(subname)
				except:
					return
				if len(data) <= subname:
					return
				if last:
					del data[subname]
					return
				data = data[subname]
			else:
				return

	def type(data):
		data_type = type(data)
		if data_type is str:
			return 'text'
		elif data_type in [float, int]:
			return 'number'
		elif data_type is bool:
			return 'bool'
		elif data_type is list:
			return 'list'
		elif data_type is dict:
			return 'dict'
		elif data_type is bytes:
			return 'binary'
		return 'none'

	def type_text(data, style = {}):
		result = ''
		if type(style) is str:
			style = void.get('text.void.style.' + style, {})
		if type(style) != dict:
			style = {}
		data_type = type(data)
		if data_type is str:
			result = data
		elif data_type in [float, int]:
			group = void.get('group', '', style)
			if data_type is float:
				fraction = void.get('fraction', '.', style)
				dot = int(void.get('dot', 10, style))
				result = f'{data:_.{dot}f}'.replace('_', group).replace('.', fraction)
			else:
				if group != '':
					result = f'{data:_}'.replace('_', group)
				else:
					result = str(data)
		elif data_type is bool:
			result = 'true' if data else 'false'
		elif data_type in [list, dict]:
			result = void.void_encode(data)
		elif data_type is bytes:
			result = data.decode('utf-8')
		else:
			result = 'none'
		if style != None:
			if type(style) is str:
				style = void.get('text.void.style.' + style)
			if type(style) is dict:
				for name in style:
					value = style[name]
					match name:
						case 'length':
							align = void.get('align', 'start', style)
							space = void.get('space', ' ', style)[:1]
							length = int(value)
							if len(result) > length:
								result = result[:length]
							else:
								match align:
									case 'start':
										result = result.ljust(length, space)
									case 'end':
										result = result.rjust(length, space)
									case 'center':
										result = result.center(length, space)
						case 'before':
							result = str(value) + result
						case 'after':
							result = result + str(value)
		return result

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
		try:
			data = float(data)
		except:
			return 0
		return data if data % 1 != 0 else int(data)

	def type_bool(data):
		return data not in [0, '0', b'0', 'false', 'none', False, None, [], {}]

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
			return result
		return {}

	def type_binary(data):
		if type(data) is str:
			return data.encode('utf-8')
		if type(data) is bytes:
			return data
		return void.type_text(data).encode('utf-8')

	def n(data):
		data_type = type(data)
		if data_type in [str, list, dict, bytes]:
			return len(data)
		return 0

	# control

	def print(data, end: str ='\n'):
		result = None
		data_type = type(data)
		if data_type is str:
			result = data
		elif data_type in [int, float, bool, bytes]:
			result = str(data)
		elif data_type in [dict, list]:
			result = void.void_encode(data, 4)
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
							case 'text':
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
								else:
									value = [value]
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

	def test(name: str = None, group: str = None):
		actions = void.data['description']['action']
		if name == 'group' and group != None:
			actions = {name: value for name, value in actions.items() if value['group'] == group}
		else:
			if name in actions:
				actions = {name: actions[name]}
		void.print('test')
		for name in actions:
			void.print(' ' * 4 + name)
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
					if type(result) is dict:
						for name in result:
							result[name] = round(result[name], int(example['round'])) if result != None else None
					elif type(result) is list:
						for index in range(len(result)):
							result[index] = round(result[index], int(example['round'])) if result != None else None
					else:
						result = round(result, int(example['round'])) if result != None else None
				if 'result' in example:
					error = False
					match example['result']:
						case 'str':
							if type(result) is not str:
								error = True
						case 'number':
							if type(result) not in [int, float]:
								error = True
							elif 'range' in example and type(example['range']) in [list, int, float]:
								range_from = float(example['range'][0]) if type(example['range']) is list and len(example['range']) > 1 else 0
								range_to = float(example['range'][1] if type(example['range']) is list and len(example['range']) > 1 else (example['range'][0] if type(example['range']) is list else example['range']))
								if result < range_from or result > range_to:
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
							'error': {
								'action': name,
								'example': example['code'],
								'expected': example['result'],
								'found': result
							}})
		void.print({'result': 'ok'})

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
		return round(value, dot)

	def floor(value: float):
		return math.floor(value)

	def ceil(value: float):
		return math.ceil(value)

	def log(value: float, base: float = None):
		return math.log(value) if base == None else math.log(value, base)

	def factorial(value: float):
		return math.factorial(value)

	def fibonacci(value: float, multiply: float = 1, shift: float = 0):
		value = int(value)
		if value <= 0:
			return 0
		elif value == 1:
			return 1
		a, b = 0, 1
		result = [0 + shift, 1 * multiply + shift]
		for _ in range(2, value):
			a, b = b, a + b
			result.append(b * multiply + shift)
		return result

	def golden(value: float, name: str = None):
		const = 1.61803398874989484820
		if name == 'short':
			return {
				'short': value,
				'long': value * const,
				'total': value * (1 + const)
				}
		elif name == 'long':
			return {
				'short': value / const,
				'long': value,
				'total': value * (1 + const) / const
				}
		else:
			return {
				'short': (2 - const) * value,
				'long': (const - 1) * value,
				'total': value
				}

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

	def random_seed(seed: str = None):
		if seed == None:
			return void.get('app.seed')
		return void.set('app.seed', seed)

	def random_reseed():
		seed = void.sha256(str(void.time()) + void.hash(40))
		void.random_seed(seed)

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
		chars = string.ascii_letters + string.digits  # a-z, A-Z, 0-9
		return ''.join(random.choices(chars, k=length))

	def uuid():
		pass

	def md5(value: str):
		return hashlib.md5(value)

	def sha1(value: str):
		pass

	def sha256(value: str):
		return hashlib.sha256(value.encode()) 

	def sha512(value: str):
		pass

	def crc32(value: str):
		pass

	def base64_encode(data, charset: str = 'utf-8'):
		if type(data) is not bool:
			data = void.type_text(data).encode()
		return base64.b64encode(data).decode(charset)

	def base64_decode():
		pass

	def gzip_encode(value: str):
		pass

	def gzip_decode():
		pass

	def rsa_encode(value: str):
		pass

	def rsa_decode():
		pass

	def rsa_public():
		pass

	def rsa_private():
		pass

	def ssl_encode(value: str):
		pass

	def ssl_decode():
		pass

	def ssl_check():
		pass

	def bcrypt_encode(value: str):
		pass

	def bcrypt_check():
		pass

	# file

	def file(path: str, data = None):
		extension = void.path_extension(path).lower()
		if data == None:
			match extension:
				case 'json':
					return void.json_decode(void.file_read_text(path))
				case 'void':
					return void.void_decode(void.file_read_text(path))
				case 'csv':
					return void.csv_decode(void.file_read_text(path))
				case 'yaml':
					return void.yaml_decode(void.file_read_text(path))
				case 'txt':
					return void.file_read_text(path)
				case _:
					return void.file_read(path)
		else:
			match extension:
				case 'json':
					void.file_write(path, void.json_encode(data))
				case 'void':
					void.file_write(path, void.void_encode(data))
				case 'csv':
					void.file_write(path, void.csv_encode(data))
				case 'yaml':
					void.file_write(path, void.yaml_encode(data))
				case 'txt':
					if type(data) in [float, int]:
						data = str(data)
					elif type(data) is not str:
						data = void.void_encode(data)
					void.file_write(path, data)
				case _:
					if type(data) in [bytes, str, int, float]:
						void.file_write(path, data)
					else:
						void.file_write(path, void.void_encode(data))

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

	def void_encode(data, indent = '\t', level: int = 0):
		result = ''
		short = indent == None
		indent = (' ' * indent) if type(indent) is int else str(indent)
		indent_current = indent * level
		match data:
			case str():
				if not short:
					result += indent_current + (data if len(data) > 0 else "'") + '\n'
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
						result += indent_current + str(name) + '\n'
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

	def social():
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
		void.random_reseed()
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
					action = void.file(text)
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