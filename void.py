import importlib
import traceback
import os
import sys
import platform
import subprocess
import signal
import struct
import string
import re
import time
import math
import random
import hashlib
import json
import gzip as gz
from datetime import datetime

class void:

	modules = {
		'psutil': None,
		'platform': None,
		'base64': None,
		'tkinter': None
	}
	data = {
		'about': {
			'name': 'V O I D lang',
			'site': 'https://voidsp.com',
			'language': 'python',
			'version': {
				'time': 1761401661,
				'date': '2025·10·25'
			},
			'license': {
				'name': 'V O I D license',
				'url': 'https://github.com/voidspawner/void.lang#v-o-i-d-license',
				'text': 'do what you want · you can use it in both private and open source · embed it in free or paid products · modify · create your own solutions based on it · no need to specify the author'
			}
		},
		'doc': {

			# value

			'get': {
				'group': 'value',
				'method': 'get',
				'alias': None,
				'description': 'Retrieve a value based on provided parameter name',
				'safe': True,
				'container': None,
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'param': [
					{'name': 'name', 'type': 'text', 'default': None},
					{'name': 'default', 'type': 'any', 'default': None}
				],
				'example': [
					{'code': [['get', 'about.name']], 'result': 'V O I D lang'},
					{'code': [['get', 'about.unknown', 'empty']], 'result': 'empty'},
					{'code': [['get', 'void.test.json/about.name']], 'before': [['file', 'void.test.json', {"about":{"name": "V O I D lang"},"list":[0,1,2]}]], 'clean': [['file.remove', 'void.test.json']], 'result': 'V O I D lang'},
					{'code': [['get', 'void.test.json/list.1']], 'before': [['file', 'void.test.json', {"about":{"name": "V O I D lang"},"list":[0,1,2]}]], 'clean': [['file.remove', 'void.test.json']], 'result': 1}
				]
			},
			'set': {
				'group': 'value',
				'method': 'set',
				'alias': None,
				'description': 'Assign a value to a specified parameter',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'name', 'type': 'text', 'default': None},
					{'name': 'data', 'type': 'any', 'default': None}
				],
				'example': [
					{'code': [['set', 'some.value', 1]], 'after': [['get', 'some.value']], 'result': 1},						
					{'code': [['set', 'some.text', ':)']], 'after': [['get', 'some.text']], 'result': ':)'},
					{'code': [['set', 'void.test.json/about.name', 'V O I D']], 'before': [['file', 'void.test.json', {"about":{"name": "V O I D lang"},"list":[0,1,2]}]], 'after': [['get', 'void.test.json/about.name']], 'clean': [['file.remove', 'void.test.json']], 'result': 'V O I D'},
					{'code': [['set', 'void.test.json/list.1', 2]], 'before': [['file', 'void.test.json', {"about":{"name": "V O I D lang"},"list":[0,1,2]}]], 'after': [['get', 'void.test.json/list.1']], 'claen': [['file.remove', 'void.test.json']], 'result': 2}
				]
			},
			'remove': {
				'group': 'value',
				'method': 'remove',
				'alias': None,
				'description': 'Remove a specified parameter or value',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'name', 'type': 'text'}
				],
				'example': [
					{'code': [['remove', 'some.value']], 'before': [['set', 'some.value', 1]], 'after': [['get', 'some.value']], 'result': None},
					{'code': [['remove', 'void.test.json/about.name']], 'before': [['file', 'void.test.json', {"about":{"name": "V O I D lang"},"list":[0,1,2]}]], 'after': [['get', 'void.test.json/about.name']], 'clean': [['file.remove', 'void.test.json']], 'result': None}
				]
			},
			'type': {
				'group': 'value',
				'method': 'type',
				'alias': None,
				'description': 'Determine the data type of a specified parameter',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'data', 'type': 'any'}
				],
				'example': [
					{'code': [['type', 'text']], 'result': 'text'},
					{'code': [['type', 1]], 'result': 'number'},
					{'code': [['type', 1.2]], 'result': 'number'},
					{'code': [['type', True]], 'result': 'bool'},
					{'code': [['type', False]], 'result': 'bool'},
					{'code': [['type', None]], 'result': 'none'},
					{'code': [['type', {'a': 1}]], 'result': 'dict'},
					{'code': [['type', [1,2,3]]], 'result': 'list'},
					{'code': [['type', b'1']], 'result': 'binary'}
				]
			},
			'text': {
				'group': 'value',
				'method': 'type_text',
				'alias': None,
				'description': 'Specify a parameter as a text type',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'data', 'type': 'any'},
					{'name': 'style', 'type': ['text', 'dict'], 'default': {}}
				],
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
				'group': 'value',
				'method': 'type_number',
				'alias': None,
				'description': 'Specify a parameter as a number type',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'data', 'type': 'any'}
				],
				'example': [
					{'code': [['number', '123']], 'result': 123},
					{'code': [['number', 45.67]], 'result': 45.67}
				]
			},
			'bool': {
				'group': 'value',
				'method': 'type_bool',
				'alias': None,
				'description': 'Specify a parameter as a boolean type',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'data', 'type': 'any'}
				],
				'example': [
					{'code': [['bool', 1]], 'result': True},
					{'code': [['bool', 'false']], 'result': False},
					{'code': [['bool', None]], 'result': False},
					{'code': [['bool', 'none']], 'result': False}
				]
			},
			'list': {
				'group': 'value',
				'method': 'type_list',
				'alias': None,
				'description': 'Specify a parameter as a list type',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'data', 'type': 'any'}
				],
				'example': [
					{'code': [['list', 123]], 'result': [123]},
					{'code': [['list', 'a']], 'result': ['a']},
					{'code': [['list', [123, 'a']]], 'result': [123, 'a']}
				]
			},
			'binary': {
				'group': 'value',
				'method': 'type_binary',
				'alias': None,
				'description': 'Specify a parameter as a binary type',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'data', 'type': 'any'}
				],
				'example': [
					{'code': [['binary', 'a']], 'result': b'a'},
					{'code': [['binary', 1]], 'result': b'1'}
				]
			},
			'length': {
				'group': 'value',
				'method': 'length',
				'alias': 'l',
				'description': 'Gets the length of the text, the number of items in a list or dictionary, the count of bytes in a number',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'data', 'type': 'any'}
				],
				'example': [
					{'code': [['l', 'text']], 'result': 4},
					{'code': [['l', [1, 2, 'a']]], 'result': 3},
					{'code': [['l', {'a': 1, 'b': 2}]], 'result': 2},
					{'code': [['l', 123]], 'result': 1},
					{'code': [['l', -123]], 'result': 1},
					{'code': [['l', 12345678]], 'result': 3},
					{'code': [['l', 123.1]], 'result': 8}
				]
			},

			# expression

			'+': {
				'group': 'expression',
				'method': 'expression_plus',
				'alias': None,
				'description': 'Perform addition or AND operation',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'first', 'type': 'any', 'default': '{}'},
					{'name': 'second', 'type': 'any', 'default': None}
				],
				'example': [
					{'code': [['+', 2, 3]], 'result': 5},
					{'code': [['+', True]], 'result': False},
					{'code': [['+', False]], 'result': False},
					{'code': [['+', True, True]], 'result': True},
					{'code': [['+', True, False]], 'result': False},
					{'code': [['+', False, True]], 'result': False},
					{'code': [['+', False, False]], 'result': False},
					{'code': [['+', 'a', 'b']], 'result': 'ab'},
					{'code': [['+', 'a', 2]], 'result': 'a  '},
					{'code': [['+', ['a'], ['b']]], 'result': ['a', 'b']},
					{'code': [['+', ['a'], 2]], 'result': ['a', None, None]},
					{'code': [['+', {'a': 1, 'b': {'c': 3}}, {'b': {'c': 5}}]], 'result': {'a': 1, 'b': {'c': 5}}},
					{'code': [['+', {'a': 1}, 'b']], 'result': {'a': 1, 'b': None}},
					{'code': [['+', {'a': 1}, 1]], 'result': [{'a': 1}, {'a': 1}]},
					{'code': [['+', b'a', b'b']], 'result': b'ab'},
					{'code': [['+', b'a', 'b']], 'result': b'ab'},
					{'code': [['+', b'a', 1]], 'result': b'a1'}
				]
			},
			'-': {
				'group': 'expression',
				'method': 'expression_minus',
				'alias': None,
				'description': 'Perform subtraction or NOT operation',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'first', 'type': 'any', 'default': '{}'},
					{'name': 'second', 'type': 'any', 'default': None}
				],
				'example': [
					{'code': [['-', 5, 2]], 'result': 3},
					{'code': [['-', 10]], 'result': -10},
					{'code': [['-', True]], 'result': False},
					{'code': [['-', False]], 'result': True},
					{'code': [['-', True, True]], 'result': False},
					{'code': [['-', False, True]], 'result': False},
					{'code': [['-', True, False]], 'result': True},
					{'code': [['-', False, False]], 'result': False},
					{'code': [['-', 'file.json', '.json']], 'result': 'file'},
					{'code': [['-', 'text', 2]], 'result': 'te'},
					{'code': [['-', [1, 2, 3], 1]], 'result': [1, 2]},
					{'code': [['-', {'a': 1, 'b': 2}, 'a']], 'result': {'b': 2}},
					{'code': [['-', {'a': 1, 'b': 2}, 1]], 'length': 1},
					{'code': [['-', b'text', 2]], 'result': b'te'},
					{'code': [['-', b'text', 't']], 'result': b'tex'},
					{'code': [['-', b'text', b't']], 'result': b'tex'}
				]
			},
			'*': {
				'group': 'expression',
				'method': 'expression_multiply',
				'alias': None,
				'description': 'Perform multiplication or XOR operation',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'first', 'type': 'any', 'default': '{}'},
					{'name': 'second', 'type': 'any', 'default': None}
				],
				'example': [
					{'code': [['*', 3, 4]], 'result': 12},
					{'code': [['*', True]], 'result': True},
					{'code': [['*', False]], 'result': False},
					{'code': [['*', True, True]], 'result': False},
					{'code': [['*', True, False]], 'result': True},
					{'code': [['*', False, True]], 'result': True},
					{'code': [['*', False, False]], 'result': False},
					{'code': [['*', 'a', 3]], 'result': 'aaa'},
					{'code': [['*', ['a'], 2]], 'result': ['a', 'a']},
					{'code': [['*', ['a', 'b'], ' ']], 'result': 'a b'},
					{'code': [['*', {'a': 1}, 2]], 'result': [{'a': 1}, {'a': 1}]},
					{'code': [['*', b'a', 2]], 'result': b'aa'}
				]
			},
			'/': {
				'group': 'expression',
				'method': 'expression_divide',
				'alias': None,
				'description': 'Perform division or OR operation',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'first', 'type': 'any', 'default': '{}'},
					{'name': 'second', 'type': 'any', 'default': None}
				],
				'example': [
					{'code': [['/', 10, 2]], 'result': 5},
					{'code': [['/', 7, 2]], 'result': 3.5},
					{'code': [['/', True]], 'result': True},
					{'code': [['/', False]], 'result': False},
					{'code': [['/', True, True]], 'result': True},
					{'code': [['/', True, False]], 'result': True},
					{'code': [['/', False, True]], 'result': True},
					{'code': [['/', False, False]], 'result': False},
					{'code': [['/', 'a b', ' ']], 'result': ['a', 'b']},
				]
			},
			'%': {
				'group': 'expression',
				'method': 'expression_modulo',
				'alias': None,
				'description': 'Perform modulo operation',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'first', 'type': 'any', 'default': '{}'},
					{'name': 'second', 'type': 'any', 'default': None}
				],
				'example': [
					{'code': [['%', 10, 3]], 'result': 1},
					{'code': [['%', 15, 4]], 'result': 3}
				]
			},
			'^': {
				'group': 'expression',
				'method': 'expression_power',
				'alias': None,
				'description': 'Elevation operator',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'first', 'type': 'any', 'default': '{}'},
					{'name': 'second', 'type': 'any', 'default': None}
				],
				'example': [
					{'code': [['^', 2, 3]], 'result': 8},
					{'code': [['^', 10, 0]], 'result': 1},
					{'code': [['^', 4, 0.5]], 'result': 2}
				]
			},
			'>>': {
				'group': 'expression',
				'method': 'expression_shr',
				'alias': None,
				'description': 'Perform right shift operation',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'data', 'type': 'any', 'default': '{}'},
					{'name': 'count', 'type': 'number', 'default': 1}
				],
				'example': [
					{'code': [['>>', 16, 2]], 'result': 4},
					{'code': [['>>', 255, 4]], 'result': 15},
					{'code': [['>>', True]], 'result': False},
				]
			},
			'<<': {
				'group': 'expression',
				'method': 'expression_shl',
				'alias': None,
				'description': 'Perform left shift operation',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'data', 'type': 'any', 'default': '{}'},
					{'name': 'count', 'type': 'number', 'default': 1}
				],
				'example': [
					{'code': [['<<', 4, 2]], 'result': 16},
					{'code': [['<<', 7, 3]], 'result': 56},
					{'code': [['<<', True]], 'result': False}
				]
			},
			'==': {
				'group': 'expression',
				'method': 'expression_equal',
				'alias': None,
				'description': 'Checks if left value is equal to right',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'first', 'type': 'any', 'default': None},
					{'name': 'second', 'type': 'any', 'default': None}
				],
				'example': [
					{'code': [['==', 5, 5]], 'result': True},
					{'code': [['==', 'a', 'b']], 'result': False}
				]
			},
			'!=': {
				'group': 'expression',
				'method': 'expression_notequal',
				'alias': None,
				'description': 'Check if values are not equal',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'first', 'type': 'any', 'default': None},
					{'name': 'second', 'type': 'any', 'default': None}
				],
				'example': [
					{'code': [['!=', 5, 3]], 'result': True},
					{'code': [['!=', 'a', 'a']], 'result': False}
				]
			},
			'>': {
				'group': 'expression',
				'method': 'expression_greater',
				'alias': None,
				'description': 'Checks if left value is greater than right',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'first', 'type': 'any', 'default': None},
					{'name': 'second', 'type': 'any', 'default': None}
				],
				'example': [
					{'code': [['>', 5, 3]], 'result': True},
					{'code': [['>', 2, 4]], 'result': False}
				]
			},
			'<': {
				'group': 'expression',
				'method': 'expression_less',
				'alias': None,
				'description': 'Checks if left value is less than right',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'first', 'type': 'any', 'default': None},
					{'name': 'second', 'type': 'any', 'default': None}
				],
				'example': [
					{'code': [['<', 3, 5]], 'result': True},
					{'code': [['<', 4, 2]], 'result': False}
				]
			},
			'>=': {
				'group': 'expression',
				'method': 'expression_greater_equal',
				'alias': None,
				'description': 'Checks if left value is greater than or equal to right',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'first', 'type': 'any', 'default': None},
					{'name': 'second', 'type': 'any', 'default': None}
				],
				'example': [
					{'code': [['>=', 5, 3]], 'result': True},
					{'code': [['>=', 5, 5]], 'result': True},
					{'code': [['>=', 4, 5]], 'result': False}
				]
			},
			'<=': {
				'group': 'expression',
				'method': 'expression_less_equal',
				'alias': None,
				'description': 'Checks if left value is less than or equal to right',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'first', 'type': 'any', 'default': None},
					{'name': 'second', 'type': 'any', 'default': None}
				],
				'example': [
					{'code': [['<=', 3, 5]], 'result': True},
					{'code': [['<=', 5, 5]], 'result': True},
					{'code': [['<=', 6, 5]], 'result': False}
				]
			},
			'<>': {
				'group': 'expression',
				'method': 'expression_in',
				'alias': None,
				'description': 'Checks if value is in a list or subtext in a text or name in a dictionary',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'first', 'type': 'any', 'default': None},
					{'name': 'second', 'type': 'any', 'default': None}
				],
				'example': [
					{'code': [['<>', 'te', 'text']], 'result': True},
					{'code': [['<>', 'a', ['a', 'b', 'c']]], 'result': True},
					{'code': [['<>', 'a', {'a': 1}]], 'result': True},
					{'code': [['<>', 'd', ['a', 'b', 'c']]], 'result': False}
				]
			},
			'><': {
				'group': 'expression',
				'method': 'expression_notin',
				'alias': None,
				'description': 'Checks if value is not in a list or subtext in a text or or name not in a dictionary',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'first', 'type': 'any', 'default': None},
					{'name': 'second', 'type': 'any', 'default': None}
				],
				'example': [
					{'code': [['><', 'a', 'text']], 'result': True},
					{'code': [['><', 'd', ['a', 'b', 'c']]], 'result': True},
					{'code': [['><', 'b', {'a': 1}]], 'result': True},
					{'code': [['><', 'a', ['a', 'b', 'c']]], 'result': False}
				]
			},
			'~': {
				'group': 'expression',
				'method': 'expression_is',
				'alias': None,
				'description': 'Checks if value is in a list or name in a dictionary',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'data', 'type': 'any', 'default': None},
					{'name': 'type', 'type': 'text', 'default': None}
				],
				'example': [
					{'code': [['~', 'name', 'text']], 'result': True},
					{'code': [['~', 'name', 'number']], 'result': False},
					{'code': [['~', 123, 'number']], 'result': True},
					{'code': [['~', True, 'bool']], 'result': True},
					{'code': [['~', None, 'none']], 'result': True},
					{'code': [['~', [1, 2], 'list']], 'result': True},
					{'code': [['~', {'a': 1}, 'dict']], 'result': True},
					{'code': [['~', 'name', ['text', 'dict']]], 'result': True},
					{'code': [['~', b'text', 'binary']], 'result': True}
				]
			},
			'!~': {
				'group': 'expression',
				'method': 'expression_isnot',
				'alias': None,
				'description': 'Checks if value is not in a list or name not in a dictionary',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'data', 'type': 'any', 'default': None},
					{'name': 'type', 'type': 'text', 'default': None}
				],
				'example': [
					{'code': [['!~', 'name', 'number']], 'result': True},
					{'code': [['!~', 123, 'text']], 'result': True},
					{'code': [['!~', 123, ['list', 'dict']]], 'result': True}
				]
			},
			'=': {
				'group': 'expression',
				'method': 'expression_assign',
				'alias': None,
				'description': 'Assign value to a variable',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'name', 'type': 'text', 'default': None},
					{'name': 'data', 'type': 'any', 'default': None}
				],
				'example': [
					{'code': [['=', 'x', 10]], 'result': 10},
					{'code': [['=', 'name', 'John']], 'result': 'John'}
				]
			},
			'+=': {
				'group': 'expression',
				'method': 'expression_plus_assign',
				'alias': None,
				'description': 'Add and assign value to a variable',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'name', 'type': 'text', 'default': None},
					{'name': 'data', 'type': 'any', 'default': None}
				],
				'example': [
					{'code': [['=', 'x', 5], ['+=', 'x', 3]], 'result': 8},
					{'code': [['=', 's', 'a'], ['+=', 's', 'b']], 'result': 'ab'}
				]
			},
			'=+': {
				'group': 'expression',
				'method': 'expression_assign_plus',
				'alias': None,
				'description': 'Assign and add value to a variable',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'name', 'type': 'text', 'default': None},
					{'name': 'data', 'type': 'any', 'default': None}
				],
				'example': [
					{'code': [['=+', 'x', 5, 3]], 'result': 8},
					{'code': [['=+', 's', 'a', 'b']], 'result': 'ab'}
				]
			},
			'-=': {
				'group': 'expression',
				'method': 'expression_minus_assign',
				'alias': None,
				'description': 'Subtract and assign value to a variable',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'name', 'type': 'text', 'default': None},
					{'name': 'data', 'type': 'any', 'default': None}
				],
				'example': [
					{'code': [['=', 'x', 10], ['-=', 'x', 4]], 'result': 6},
					{'code': [['=', 'y', 7.5], ['-=', 'y', 2.5]], 'result': 5.0}
				]
			},
			'*=': {
				'group': 'expression',
				'method': 'expression_multiply_assign',
				'alias': None,
				'description': 'Multiply and assign value to a variable',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'name', 'type': 'text', 'default': None},
					{'name': 'data', 'type': 'any', 'default': None}
				],
				'example': [
					{'code': [['=', 'x', 3], ['*=', 'x', 4]], 'result': 12},
					{'code': [['=', 's', 'a'], ['*=', 's', 3]], 'result': 'aaa'}
				]
			},
			'/=': {
				'group': 'expression',
				'method': 'expression_divide_assign',
				'alias': None,
				'description': 'Divide and assign value to a variable',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'name', 'type': 'text', 'default': None},
					{'name': 'data', 'type': 'any', 'default': None}
				],
				'example': [
					{'code': [['=', 'x', 10], ['/=', 'x', 2]], 'result': 5},
					{'code': [['=', 'y', 7], ['/=', 'y', 2]], 'result': 3.5}
				]
			},
			'%=': {
				'group': 'expression',
				'method': 'expression_modulo_assign',
				'alias': None,
				'description': 'Modulo and assign value to a variable',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'name', 'type': 'text', 'default': None},
					{'name': 'data', 'type': 'any', 'default': None}
				],
				'example': [
					{'code': [['=', 'x', 10], ['%=', 'x', 3]], 'result': 1},
					{'code': [['=', 'y', 15], ['%=', 'y', 4]], 'result': 3}
				]
			},
			'^=': {
				'group': 'expression',
				'method': 'expression_power_assign',
				'alias': None,
				'description': 'Elevation and assign value to a variable',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'name', 'type': 'text', 'default': None},
					{'name': 'data', 'type': 'any', 'default': 2}
				],
				'example': [
					{'code': [['=', 'x', 2], ['~=', 'x', 3]], 'result': 8},
					{'code': [['=', 'y', 5], ['~=', 'y', 0]], 'result': 1}
				]
			},
			'>>=': {
				'group': 'expression',
				'method': 'expression_shr_assign',
				'alias': None,
				'description': 'Right shift and assign value to a variable',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'name', 'type': 'text', 'default': None},
					{'name': 'count', 'type': 'number', 'default': 1}
				],
				'example': [
					{'code': [['=', 'x', 16], ['>>=', 'x', 2]], 'result': 4},
					{'code': [['=', 'y', 255], ['>>=', 'y', 4]], 'result': 15}
				]
			},
			'<<=': {
				'group': 'expression',
				'method': 'expression_shl_assign',
				'alias': None,
				'description': 'Left shift and assign value to a variable',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'name', 'type': 'text', 'default': None},
					{'name': 'count', 'type': 'number', 'default': 1}
				],
				'example': [
					{'code': [['=', 'x', 4], ['<<=', 'x', 2]], 'result': 16},
					{'code': [['=', 'y', 7], ['<<=', 'y', 3]], 'result': 56}
				]
			},


			# control

			'print': {
				'group': 'control',
				'method': 'print',
				'alias': '.',
				'description': 'Output data to the console',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'data', 'type': 'any', 'many': True, 'default': '{}'},
					{'name': 'end', 'type': 'text', 'default': '\n'}
				],
				'example': [
					{'code': [['.', 'Hello']], 'result': 'Hello\n', 'output': 'shell'},
					{'code': [['.', 42]], 'result': '42\n', 'output': 'shell'},
					{'code': [['.', 'Hello', 'there']], 'result': 'Hello there\n', 'output': 'shell'}
				]
			},
			'printn': {
				'group': 'control',
				'method': 'printn',
				'alias': '..',
				'description': 'Output data to the console without newline',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'data', 'type': 'any', 'many': True, 'default': '{}'}
				],
				'example': [
					{'code': [['..', 'Hello']], 'result': 'Hello', 'output': 'shell'},
					{'code': [['..', 42]], 'result': '42', 'output': 'shell'},
					{'code': [['..', 'Hello', 'there']], 'result': 'Hello there', 'output': 'shell'}
				]
			},
			'input': {
				'group': 'control',
				'method': None,
				'alias': '...',
				'description': 'Input text from the user',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'text', 'type': 'text', 'default': ''}
				],
				'example': [
					{'code': [['.?', 'Enter name: ']], 'test': False},
					{'code': [['.?']], 'test': False}
				]
			},
			'if': {
				'group': 'control',
				'method': None,
				'alias': '?',
				'description': 'Evaluate a conditional expression',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['?', ['>', 5, 3], 'yes', 'no']], 'result': 'yes'},
					{'code': [['?', ['==', 2, 3], 'equal', 'not equal']], 'result': 'not equal'}
				]
			},
			'loop': {
				'group': 'control',
				'method': None,
				'alias': 'o',
				'description': 'Perform a loop operation',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['o', ['<', 'i', 3], [['.', 'i'], ['=', 'i', ['+', 'i', 1]]]]], 'test': False},
					{'code': [['o', ['<', 'i', 5], [['.', ['*', 'i', 2]], ['=', 'i', ['+', 'i', 1]]]]], 'test': False}
				]
			},
			'break': {
				'group': 'control',
				'method': None,
				'alias': 'x',
				'description': 'Exit the current loop',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['o', True, [['.', 'looping'], ['?', ['==', 'i', 3], [['x']], []]]]], 'test': False}
				]
			},
			'continue': {
				'group': 'control',
				'method': None,
				'alias': 'x>',
				'description': 'Skip to the next iteration of the loop',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['o', ['<', 'i', 5], [['?', ['==', 'i', 2], [['->']], [['.', 'i']]]]]], 'test': False}
				]
			},
			'repeat': {
				'group': 'control',
				'method': None,
				'alias': '<x',
				'description': 'Repeat the current iteration of the loop',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['o', ['<', 'i', 3], [['?', ['==', 'i', 1], [['<-']], [['.', 'i']]]]]], 'test': False}
				]
			},
			'return': {
				'group': 'control',
				'method': None,
				'alias': ['X', 'response'],
				'description': 'Return a result from an action',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'result', 'default': None}
				],
				'example': [
					{'code': [['action', [1, ['+', 1], 'X']]], 'result': 2},
					{'code': [['action', [1, ['+', 1], ['X', '{}']]]], 'result': None}
				]
			},
			'action': {
				'group': 'control',
				'method': 'action',
				'alias': None,
				'description': 'Initiate or call an action',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['action', 'greet', [], [['.', 'Hello!']]], ['greet']], 'test': False},
					{'code': [['action', 'add', ['a', 'b'], [[':', ['+', 'a', 'b']]]], ['add', 2, 3]], 'result': 5}
				]
			},
			'open': {
				'group': 'control',
				'method': 'open',
				'alias': None,
				'description': 'Open a link in standard way or execute shell command',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [
					{'name': 'name', 'type': 'text', 'default': None}
				],
				'example': [
					{'code': [['open', 'https://example.com']], 'test': False},
					{'code': [['open', 'file.txt']], 'test': False}
				]
			},
			'close': {
				'group': 'control',
				'method': 'close',
				'alias': None,
				'description': 'Close an application by name or PID',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [
					{'name': 'name', 'type': 'text', 'default': None}
				],
				'example': [
					{'code': [['close', 'App Name']], 'test': False},
					{'code': [['close', 31337]], 'test': False}
				]
			},
			'code': {
				'group': 'control',
				'method': 'code',
				'alias': None,
				'description': 'Execute a block of native code',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['code', 'python', 'print("Hello from Python")']], 'test': False},
					{'code': [['code', 'js', 'console.log("Hello from JS")']], 'test': False}
				]
			},
			'info': {
				'group': 'control',
				'method': 'info',
				'alias': 'i',
				'description': 'Log data',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['l', 'Debug info']], 'test': False},
					{'code': [['l', ['+', 'x=', 'x']]], 'test': False}
				]
			},
			'convert': {
				'group': 'control',
				'method': 'convert',
				'alias': 'c',
				'description': 'Convert data from one format to another',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['convert', 'json', {'x': 10}]], 'result': '{"x": 10}'},
					{'code': [['convert', 'yaml', {'x': 10}]], 'result': 'x: 10\n'}
				]
			},
			'clipboard': {
				'group': 'control',
				'method': 'clipboard',
				'alias': None,
				'description': 'Storing or retrieving clipboard temporary data',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [
						['clipboard', 'copied text'],
						['clipboard']
					], 'result': 'copied text'},
					{'code': [['clipboard', None]], 'test': False}
				]
			},
			'sql': {
				'group': 'control',
				'method': 'sql',
				'alias': None,
				'description': 'Execute SQL query',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': True,
				'param': [],
				'example': [
					{'code': [['sql', 'connect', 'server', 'database', 'login', 'password']], 'test': False},
					{'code': [['sql', 'disconnect']], 'test': False},
					{'code': [['sql', 'db1', 'connect', 'server', 'database', 'login', 'password']], 'test': False},
					{'code': [['sql', 'db1', 'disconnect']], 'test': False},
					{'code': [['sql', 'SELECT * FROM user']], 'result': [], 'test': False},
					{'code': [['sql', 'INSERT INTO log VALUES ({1},{2})', ['date', 'message']]], 'test': False},
					{'code': [['sql', 'set', 'user', [1, 'name', 'mylogin', 'mypassword']]], 'test': False},
					{'code': [['sql', 'set', 'user', 1, {'name': 'newname'}]], 'test': False},
					{'code': [['sql', 'get', 'user']], 'test': False},
					{'code': [['sql', 'get', 'user', 1]], 'test': False},
					{'code': [['sql', 'remove', 'user', 1]], 'test': False}
				]
			},
			'test': {
				'group': 'control',
				'method': 'test',
				'alias': None,
				'description': 'Test one or all actions',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [
					{'name': 'name', 'type': 'text', 'default': None}
				],
				'example': [
					{'code': [['test']], 'test': False},
					{'code': [['test', 'upper']], 'length': 3},
					{'code': [['test', 'math']], 'length': 3}
				]
			},
			'help': {
				'group': 'control',
				'method': 'help',
				'alias': 'h',
				'description': 'Show description and use of the action',
				'safe': True,
				'container': None,
				'param': [
					{'name': 'name', 'type': 'text', 'default': None}
				],
				'example': [
					{'code': [['h']], 'test': False},
					{'code': [['h', 'upper']], 'test': False}
				]
			},
			'exit': {
				'group': 'control',
				'method': 'exit',
				'alias': 'xx',
				'description': 'Exit the current application',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['xx']], 'test': False},
					{'code': [['xx', 500]], 'test': False},
					{'code': [['xx', 'something went wrong']], 'test': False}
				]
			},
			'chat': {
				'group': 'control',
				'method': 'chat',
				'alias': None,
				'description': 'AI conversation and interaction through text',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': True,
				'param': [],
				'example': [
					{'code': [['chat', 'What\'s the weather today?']], 'result': 'The weather is sunny and warm.'}
				]
			},
			'say': {
				'group': 'control',
				'method': 'say',
				'alias': None,
				'description': 'Text voicing with different voices',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['voice', 'Hello world', 'en-US']], 'result': 'voice.mp3'}
				]
			},
			'voice': {
				'group': 'control',
				'method': 'voice',
				'alias': None,
				'description': 'List of available voices',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['voice.list']], 'result': ['en-US', 'es-ES', 'fr-FR']}
				]
			},
			'recognize': {
				'group': 'control',
				'method': 'recognize',
				'alias': None,
				'description': 'Convert voice to text',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['voice.recognize', 'voice.mp3']], 'result': 'Hello world'}
				]
			},
			'capture': {
				'group': 'control',
				'method': 'capture',
				'alias': None,
				'description': 'Records or analyzes motion data in real-time',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['motion.capture', 10]], 'result': {'positions': [[0,0], [0.1,0], [0.2,0.1]]}}
				]
			},
			'ui': {
				'group': 'control',
				'method': 'ui',
				'alias': ['app', 'game', 'web', 'cli'],
				'description': 'Create a user interface',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': {
					'bg': {
						'description': '',
						'param': []
					},
					'title': {
						'description': '',
						'param': []					
					}
				},
				'param': [],
				'example': [
					{'code': [['ui', 'button', 'Click me']], 'result': 'button1'}
				]
			},

			# text

			'lower': {
				'group': 'text',
				'method': 'lower',
				'alias': None,
				'description': 'Convert text to lowercase',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'text', 'type': 'text', 'default': ''}
				],
				'example': [
					{'code': [['lower', 'TeXt']], 'result': 'text'}
				]
			},
			'upper': {
				'group': 'text',
				'method': 'upper',
				'alias': None,
				'description': 'Convert text to uppercase',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'text', 'type': 'text', 'default': ''},
					{'name': 'type', 'type': 'text', 'default': None}
				],
				'example': [
					{'code': [['upper', 'text']], 'result': 'TEXT'},
					{'code': [['upper', 'text title', 'title']], 'result': 'Text Title'},
					{'code': [['upper', 'text sentence', 'sentence']], 'result': 'Text sentence'}
				]
			},
			'starts': {
				'group': 'text',
				'method': 'starts',
				'alias': None,
				'description': 'Check if text starts with a specific substring',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'text', 'type': 'text', 'default': ''},
					{'name': 'subtext', 'type': 'text', 'default': ''}
				],
				'example': [
					{'code': [['starts', 'Hi World', 'Hi']], 'result': True},
					{'code': [['starts', 'Hi World', 'World']], 'result': False}
				]
			},
			'ends': {
				'group': 'text',
				'method': 'ends',
				'alias': None,
				'description': 'Check if text ends with a specific substring',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'text', 'type': 'text', 'default': ''},
					{'name': 'subtext', 'type': 'text', 'default': ''}
				],
				'example': [
					{'code': [['ends', 'Hi World', 'World']], 'result': True},
					{'code': [['ends', 'Hi World', 'Hi']], 'result': False}
				]
			},
			'strip': {
				'group': 'text',
				'method': 'strip',
				'alias': None,
				'description': 'Remove leading and trailing characters from text',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'text', 'type': 'text', 'default': ''},
					{'name': 'character', 'type': 'text', 'default': [' ', '\r', '\n', '\t']}
				],
				'example': [
					{'code': [['strip', '  text  ']], 'result': 'text'},
					{'code': [['strip', '\ttext\n']], 'result': 'text'},
					{'code': [['strip', '- text -', '- ']], 'result': 'text -'},
					{'code': [['strip', '- text -', ['-', ' ']]], 'result': 'text'}
				]
			},
			'strip.start': {
				'group': 'text',
				'method': 'strip_start',
				'alias': None,
				'description': 'Remove leading characters from text',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None, 
				'param': [
					{'name': 'text', 'type': 'text', 'default': ''},
					{'name': 'character', 'type': 'text', 'default': [' ', '\r', '\n', '\t']}
				],
				'example': [
					{'code': [['strip.start', '  text  ']], 'result': 'text  '},
					{'code': [['strip.start', '\ttext\n']], 'result': 'text\n'},
					{'code': [['strip.start', '- text -', '- ']], 'result': 'text -'},
					{'code': [['strip.start', '- text -', ['-', ' ']]], 'result': 'text -'}
				]
			},
			'strip.end': {
				'group': 'text',
				'method': 'strip_end',
				'alias': None,
				'description': 'Remove trailing characters from text',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'text', 'type': 'text', 'default': ''},
					{'name': 'character', 'type': 'text', 'default': [' ', '\r', '\n', '\t']}
				],
				'example': [
					{'code': [['strip.end', '  text  ']], 'result': '  text'},
					{'code': [['strip.end', '\ttext\n']], 'result': '\ttext'},
					{'code': [['strip.end', '- text -', '- ']], 'result': '- text -'},
					{'code': [['strip.end', '- text -', ['-', ' ']]], 'result': '- text'}
				]
			},
			'replace': {
				'group': 'text',
				'method': 'replace',
				'alias': None,
				'description': 'Replace occurrences of a substring within text',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'text', 'type': 'text', 'default': ''},
					{'name': 'search', 'type': ['text', 'dict'], 'default': None},
					{'name': 'replace', 'type': 'text', 'default': None}
				],
				'example': [
					{'code': [['replace', 'hello world', 'world', 'there']], 'result': 'hello there'},
					{'code': [['replace', 'aabbcc', 'b', 'x']], 'result': 'aaxxcc'}
				]
			},
			'find': {
				'group': 'text',
				'method': 'find',
				'alias': None,
				'description': 'Locate a substring within text',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['find', 'hello world', 'world']], 'result': 6},
					{'code': [['find', 'abcabc', 'b']], 'result': 1}
				]
			},
			'parse': {
				'group': 'text',
				'method': 'parse',
				'alias': None,
				'description': 'Parse text into structured data',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['parse', 'json', '{"x": 5}']], 'result': {'x': 5}},
					{'code': [['parse', 'number', '42']], 'result': 42}
				]
			},
			'part': {
				'group': 'text',
				'method': 'part',
				'alias': None,
				'description': 'Extract a part of the text or list',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['part', 'hello world', 0, 5]], 'result': 'hello'},
					{'code': [['part', 'abcdef', 2, 4]], 'result': 'cd'}
				]
			},
			'split': {
				'group': 'text',
				'method': 'split',
				'alias': None,
				'description': 'Split text into parts based on a delimiter',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['split', 'a,b,c', ',']], 'result': ['a', 'b', 'c']},
					{'code': [['split', 'one two three', ' ']], 'result': ['one', 'two', 'three']}
				]
			},
			'join': {
				'group': 'text',
				'method': 'join',
				'alias': None,
				'description': 'Join a list of strings into a single string with a delimiter',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['join', ['a', 'b', 'c'], ',']], 'result': 'a,b,c'},
					{'code': [['join', ['2023', '12', '31'], '-']], 'result': '2023-12-31'}
				]
			},
			'date': {
				'group': 'text',
				'method': 'date',
				'alias': None,
				'description': 'Format or parse date-related information',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'name', 'type': 'text', 'default': None}
				],
				'example': [
					{'code': [['date', '{year}-{month}-{day} {hour}:{minute}:{second}.{millisecond}', 1744095313.123]], 'result': '2025-04-08 06:55:13.123'},
					{'code': [['date', '{month short}', 1744095313]], 'result': '4'},
					{'code': [['date', '2025-04-08 06:55:13.123', '{year}-{month}-{day} {hour}:{minute}:{second}.{millisecond}']], 'result': 1744095313.123}
				]
			},
			'escape': {
				'group': 'text',
				'method': 'escape',
				'alias': 'e',
				'description': 'Escape special characters in a text',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['escape.html', '<div>Test</div>']], 'result': '&lt;div&gt;Test&lt;/div&gt;'},
					{'code': [['escape.html', '\'Quote\'']], 'result': '&quot;Quote&quot;'}
				]
			},
			'unescape': {
				'group': 'text',
				'method': 'unescape',
				'alias': None,
				'description': 'Unescape special characters in a text',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['unescape.html', '&lt;div&gt;Test&lt;/div&gt;']], 'result': '<div>Test</div>'},
					{'code': [['unescape.html', '&quot;Quote&quot;']], 'result': '\'Quote\''}
				]
			},
			'words': {
				'group': 'text',
				'method': 'words',
				'alias': None,
				'description': 'Split text into words',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'text', 'type': 'text', 'default': ''}
				],
				'example': [
					{'code': [['words', 'Hello world! How are you?']], 'result': ['Hello', 'world', 'How', 'are', 'you']},
					{'code': [['words', 'one,two,three', ',']], 'result': ['one', 'two', 'three']}
				]
			},
			'sentences': {
				'group': 'text',
				'method': 'sentences',
				'alias': None,
				'description': 'Split text into sentences',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'text', 'type': 'text', 'default': ''}
				],
				'example': [
					{'code': [['sentences', 'First sentence. Second one! Third?']], 'result': ['First sentence.', 'Second one!', 'Third?']}
				]
			},
			'lines': {
				'group': 'text',
				'method': 'lines',
				'alias': None,
				'description': 'Split text into lines',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'text', 'type': 'text', 'default': ''}
				],
				'example': [
					{'code': [['lines', 'text\ntext\n\t\ntext\n\n']], 'result': ['text', 'text', 'text']}
				]
			},
			'translate': {
				'group': 'text',
				'method': 'translate',
				'alias': None,
				'description': 'Translate text from one language to another',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'text', 'type': 'text', 'default': ''},
					{'name': 'from', 'type': 'text', 'default': None},
					{'name': 'to', 'type': 'text', 'default': None}
				],
				'example': [
					{'code': [['translate', 'Hello']], 'result': 'translate to the current language', 'test': False},
					{'code': [['translate', 'Hello', 'en', 'es']], 'result': 'Hola'},
					{'code': [['translate', 'es', 'Hello']], 'result': 'Hola'}
				]
			},
			'spellcheck': {
				'group': 'text',
				'method': 'spellcheck',
				'alias': None,
				'description': 'Spell check in different languages',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'text', 'type': 'text', 'default': ''},
					{'name': 'language', 'type': 'text', 'default': None}
				],
				'example': [
					{'code': [['spellcheck', 'Hi Warld']], 'result': {'text': 'Hi World', 'error': [{'position': 3, 'text': 'Warld', 'correct': 'World'}]}}
				]
			},

			# list

			'push': {
				'group': 'list',
				'method': 'push',
				'alias': None,
				'description': 'Add an element to the end of a list',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['push', [1, 2], 3]], 'result': [1, 2, 3]},
					{'code': [['push', [], 'new']], 'result': ['new']}
				]
			},
			'pop': {
				'group': 'list',
				'method': 'pop',
				'alias': None,
				'description': 'Remove and return an element from the end of a list',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['pop', [1, 2, 3]]], 'result': 3},
					{'code': [['pop', ['a']]], 'result': 'a'}
				]
			},
			'merge': {
				'group': 'list',
				'method': 'merge',
				'alias': None,
				'description': 'Combine multiple lists into one',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['merge', [1, 2], [3, 4]]], 'result': [1, 2, 3, 4]},
					{'code': [['merge', ['a'], ['b', 'c']]], 'result': ['a', 'b', 'c']}
				]
			},
			'reverse': {
				'group': 'list',
				'method': 'reverse',
				'alias': None,
				'description': 'Reverse the order of elements in a list',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['reverse', [1, 2, 3]]], 'result': [3, 2, 1]},
					{'code': [['reverse', ['a', 'b']]], 'result': ['b', 'a']}
				]
			},
			'shuffle': {
				'group': 'list',
				'method': 'shuffle',
				'alias': None,
				'description': 'Randomly reorder elements in a list',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['shuffle', [1, 2, 3, 4]]], 'test': False},
					{'code': [['shuffle', ['a', 'b', 'c']]], 'test': False}
				]
			},
			'unique': {
				'group': 'list',
				'method': 'unique',
				'alias': None,
				'description': 'Leave only unique values in a list',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['unique', [1, 2, 3, 4, 2, 1]]], 'result': [1, 2, 3, 4], 'test': False},
					{'code': [['unique', ['a', 'a', 'b']]],  'result': ['a', 'b'], 'test': False}
				]
			},
			'map': {
				'group': 'list',
				'method': 'map',
				'alias': None,
				'description': 'Apply a function to each element in a list',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['map', [1, 2, 3], ['*', 'item', 2]]], 'result': [2, 4, 6]},
					{'code': [['map', ['a', 'b'], ['upper', 'item']]], 'result': ['A', 'B']}
				]
			},
			'reduce': {
				'group': 'list',
				'method': 'reduce',
				'alias': None,
				'description': 'Apply a function cumulatively to the elements in a list',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['reduce', [1, 2, 3, 4], ['+', 'acc', 'item'], 0]], 'result': 10},
					{'code': [['reduce', [2, 3, 4], ['*', 'acc', 'item'], 1]], 'result': 24}
				]
			},
			'filter': {
				'group': 'list',
				'method': 'filter',
				'alias': None,
				'description': 'Apply a filter function to each element in a list',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['filter', [1, 2, 3], ['>', 2]]], 'result': [3]}
				]
			},
			'indexes': {
				'group': 'list',
				'method': 'names',
				'alias': None,
				'description': 'Retrieve all keys or attribute names from a structure',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['names', {'x': 1, 'y': 2}]], 'result': ['x', 'y']},
					{'code': [['names', ['a', 'b', 'c']]], 'result': ['0', '1', '2']}
				]
			},
			'values': {
				'group': 'list',
				'method': 'values',
				'alias': None,
				'description': 'Retrieve all values from a structure',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['values', {'x': 1, 'y': 2}]], 'result': [1, 2]},
					{'code': [['values', ['a', 'b', 'c']]], 'result': ['a', 'b', 'c']}
				]
			},

			# math

			'sin': {
				'group': 'math',
				'method': 'sin',
				'alias': None,
				'description': 'Sine of the value (in radians)',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'value', 'type': 'number'}
				],
				'example': [
					{'code': [['sin', 0.1]], 'result': 0.0998, 'round': 4}
				]
			},
			'cos': {
				'group': 'math',
				'method': 'cos',
				'alias': None,
				'description': 'Cosine of the value (in radians)',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'value', 'type': 'number'}
				],
				'example': [
					{'code': [['cos', 0.1]], 'result': 0.995, 'round': 3}
				]
			},
			'tan': {
				'group': 'math',
				'method': 'tan',
				'alias': None,
				'description': 'Tangent of the value (in radians)',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'value', 'type': 'number'}
				],
				'example': [
					{'code': [['tan', 0.1]], 'result': 0.1, 'round': 3}
				]
			},
			'sinh': {
				'group': 'math',
				'method': 'sinh',
				'alias': None,
				'description': 'Hyperbolic sine of the value',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'value', 'type': 'number'}
				],
				'example': [
					{'code': [['sinh', 0.1]], 'result': 0.1, 'round': 3}
				]
			},
			'cosh': {
				'group': 'math',
				'method': 'cosh',
				'alias': None,
				'description': 'Hyperbolic cosine of the value',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'value', 'type': 'number'}
				],
				'example': [
					{'code': [['cosh', 0.1]], 'result': 1.005, 'round': 3}
				]
			},
			'tanh': {
				'group': 'math',
				'method': 'tanh',
				'alias': None,
				'description': 'Hyperbolic tangent of the valu',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'value', 'type': 'number'}
				],
				'example': [
					{'code': [['tanh', 0.1]], 'result': 0.1, 'round': 3}
				]
			},
			'asin': {
				'group': 'math',
				'method': 'asin',
				'alias': None,
				'description': 'Arc sine of the value',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'value', 'type': 'number'}
				],
				'example': [
					{'code': [['asin', 0.1]], 'result': 0.1, 'round': 3}
				]
			},
			'acos': {
				'group': 'math',
				'method': 'acos',
				'alias': None,
				'description': 'Arc cosine of the value',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'value', 'type': 'number'}
				],
				'example': [
					{'code': [['acos', 0.1]], 'result': 1.471, 'round': 3}
				]
			},
			'atan': {
				'group': 'math',
				'method': 'atan',
				'alias': None,
				'description': 'Arc tangent of the value',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'value', 'type': 'number'}
				],
				'example': [
					{'code': [['atan', 0.1]], 'result': 0.1, 'round': 3}
				]
			},
			'asinh': {
				'group': 'math',
				'method': 'asinh',
				'alias': None,
				'description': 'Arc hyperbolic sine of the value',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'value', 'type': 'number'}
				],
				'example': [
					{'code': [['asinh', 0.1]], 'result': 0.1, 'round': 3}
				]
			},
			'acosh': {
				'group': 'math',
				'method': 'acosh',
				'alias': None,
				'description': 'Arc hyperbolic cosine of the value',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'value', 'type': 'number'}
				],
				'example': [
					{'code': [['acosh', 2]], 'result': 1.317, 'round': 3}
				]
			},
			'atanh': {
				'group': 'math',
				'method': 'atanh',
				'alias': None,
				'description': 'Arc hyperbolic tangent of the value',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'value', 'type': 'number'}
				],
				'example': [
					{'code': [['atanh', 0.1]], 'result': 0.1, 'round': 3}
				]
			},
			'round': {
				'group': 'math',
				'method': 'round',
				'alias': None,
				'description': 'Rounds a number to the nearest integer or to the specified number of decimal places',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'value', 'type': 'number'}
				],
				'example': [
					{'code': [['round', 0.1]], 'result': 0},
					{'code': [['round', 0.7]], 'result': 1},
					{'code': [['round', -0.7]], 'result': -1},
					{'code': [['round', 0.123, 2]], 'result': 0.12}
				]
			},
			'floor': {
				'group': 'math',
				'method': 'floor',
				'alias': None,
				'description': 'Largest integer less than or equal to a number',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'value', 'type': 'number'}
				],
				'example': [
					{'code': [['floor', 0.1]], 'result': 0},
					{'code': [['floor', 0.1]], 'result': 0},
					{'code': [['floor', 0.7]], 'result': 0},
					{'code': [['floor', -0.7]], 'result': -1}
				]
			},
			'ceil': {
				'group': 'math',
				'method': 'ceil',
				'alias': None,
				'description': 'Smallest integer greater than or equal to a number',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'value', 'type': 'number'}
				],
				'example': [
					{'code': [['ceil', 0.1]], 'result': 1},
					{'code': [['ceil', 0.7]], 'result': 1},
					{'code': [['ceil', -0.7]], 'result': 0}
				]
			},
			'log': {
				'group': 'math',
				'method': 'log',
				'alias': None,
				'description': 'Logarithm (natural by default) of a number',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'value', 'type': 'number'},
					{'name': 'base', 'type': 'number', 'default': None}
				],
				'example': [
					{'code': [['log', 0.1]], 'result': -2.303, 'round': 3},
					{'code': [['log', 0.1, 2]], 'result': -3.322, 'round': 3},
					{'code': [['log', 0.1, 10]], 'result': -1, 'round': 3}
				]
			},
			'fact': {
				'group': 'math',
				'method': 'factorial',
				'alias': None,
				'description': 'Factorial of a given non-negative number',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'value', 'type': 'number'}
				],
				'example': [
					{'code': [['fact', 5]], 'result': 120},
					{'code': [['fact', 0]], 'result': 1}
				]
			},
			'fib': {
				'group': 'math',
				'method': 'fibonacci',
				'alias': None,
				'description': 'Fibonacci numbers up to a specified index',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'number', 'type': 'number', 'default': 10},
					{'name': 'multiply', 'type': 'number', 'default': 1},
					{'name': 'shift', 'type': 'number', 'default': 0}
				],
				'example': [
					{'code': [['fib', 5]], 'result': [0, 1, 1, 2, 3]},
					{'code': [['fib', 7]], 'result': [0, 1, 1, 2, 3, 5, 8]},
					{'code': [['fib', 5, 3, 1]], 'result': [1, 4, 4, 7, 10]},
				]
			},
			'gr': {
				'group': 'math',
				'method': 'golden_ratio',
				'alias': None,
				'description': 'Golden ratio of a number',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'value', 'type': 'number'},
					{'name': 'part', 'type': 'number', 'default': None}
				],
				'example': [
					{'code': [['gr', 10]], 'result': {'short': 3.820, 'long': 6.180, 'total': 10}, 'round': 3},
					{'code': [['gr', 10, 'short']], 'result': {'short': 10, 'long': 16.18, 'total': 26.18}, 'round': 3},
					{'code': [['gr', 10, 'long']], 'result': {'short': 6.18, 'long': 10, 'total': 16.18}, 'round': 3}
				]
			},
			'abs': {
				'group': 'math',
				'method': 'abs',
				'alias': None,
				'description': 'Absolute value of a number',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'value', 'type': 'number'}
				],
				'example': [
					{'code': [['abs', -5]], 'result': 5},
					{'code': [['abs', 3.14]], 'result': 3.14}
				]
			},
			'min': {
				'group': 'math',
				'method': 'min',
				'alias': None,
				'description': 'Smallest of a list of numbers',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'list', 'type': 'list'}
				],
				'example': [
					{'code': [['min', [5, 3, 8, 1]]], 'result': 1},
					{'code': [['min', [-2, -5, 0]]], 'result': -5}
				]
			},
			'max': {
				'group': 'math',
				'method': 'max',
				'alias': None,
				'description': 'Largest of a list of numbers',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'list', 'type': 'list'}
				],
				'example': [
					{'code': [['max', [5, 3, 8, 1]]], 'result': 8},
					{'code': [['max', [-2, -5, 0]]], 'result': 0}
				]
			},
			'avg': {
				'group': 'math',
				'method': 'avg',
				'alias': None,
				'description': 'Average value of a list of numbers',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'list', 'type': 'list'}
				],
				'example': [
					{'code': [['avg', [1, 2, 3, 4, 5]]], 'result': 3},
					{'code': [['avg', [10, 20]]], 'result': 15}
				]
			},
			'sum': {
				'group': 'math',
				'method': 'sum',
				'alias': None,
				'description': 'Sum of a list of numbers',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'list', 'type': 'list'}
				],
				'example': [
					{'code': [['sum', [1, 2, 3, 4, 5]]], 'result': 15},
					{'code': [['sum', [10, 20, 30]]], 'result': 60}
				]
			},
			'random': {
				'group': 'math',
				'method': 'random',
				'alias': None,
				'description': 'Generates a pseudo-random number',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'from', 'type': ['number', 'text', 'dict', 'list'], 'default': None},
					{'name': 'to', 'type': 'number', 'default': None}
				],
				'example': [
					{'code': [['random']], 'type': 'number', 'range': [0, 1]},
					{'code': [['random', 10]], 'type': 'number', 'range': [0, 10]},
					{'code': [['random', 10, 20]], 'type': 'number', 'range': [10, 20]},
					{'code': [['random', True]], 'type': 'bool'},
					{'code': [['random', 'abcd']], 'type': 'text', 'length': 1},
					{'code': [['random', [1, 2, 3]]], 'type': 'number', 'range': [1, 3]},
					{'code': [['random', {'a': 1, 'b': 2}]], 'type': 'number', 'range': [1, 2]}
				]
			},
			'random.seed': {
				'group': 'math',
				'method': 'random_seed',
				'alias': None,
				'description': 'Sets or gets the seed for the random number generator to produce reproducible results',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
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

			# time

			'time': {
				'group': 'time',
				'method': 'time',
				'alias': None,
				'description': 'Provides current time since the epoch (1970-01-01 00:00:00 UTC) or calculates time passed since a given start time',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'dot', 'type': 'number', 'default': 0}
				],
				'example': [
					{'code': [['time']], 'result': 1678901234, 'test': False},
					{'code': [['time', 1678901234]], 'result': 34, 'test': False}
				]
			},
			'timer': {
				'group': 'time',
				'method': 'timer',
				'alias': None,
				'description': 'Creates a timer that can be used to trigger events at specific intervals',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['timer', 'start', 5]], 'result': 'timer_id_1'}
				]
			},
			'timer.remove': {
				'group': 'time',
				'method': 'timer_remove',
				'alias': None,
				'description': 'Removes previously created timer',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['timer.remove', 'timer_id_1']], 'result': True}
				]
			},
			'timecheck': {
				'group': 'time',
				'method': 'timecheck',
				'alias': 't',
				'description': 'Stopwatch for calculating the time spent on operations',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['t', 'start']], 'result': None},
					{'code': [['t', 'stop']], 'result': 1.234, 'round': 3}
				]
			},
			'wait': {
				'group': 'time',
				'method': 'wait',
				'alias': None,
				'description': 'Pauses execution for a specified number of seconds',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'seconds', 'type': 'number', 'default': 1}
				],
				'example': [
					{'code': [['wait', 0.1]], 'result': None}
				]
			},

			# crypto

			'encrypt': {
				'group': 'crypto',
				'method': 'encrypt',
				'alias': None,
				'description': 'Encrypts data using a specified key',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['encrypt', 'secret', 'mykey']], 'result': 'aGVsbG8='}
				]
			},
			'decrypt': {
				'group': 'crypto',
				'method': 'decrypt',
				'alias': None,
				'description': 'Decrypts previously encrypted data using the specified key',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['decrypt', 'aGVsbG8=', 'mykey']], 'result': 'secret'}
				]
			},
			'hash': {
				'group': 'crypto',
				'method': 'hash',
				'alias': None,
				'description': 'Generates a hash for the data or generates a random text',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['hash', 'hello']], 'result': '2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824'}
				]
			},
			'uuid': {
				'group': 'crypto',
				'method': 'uuid',
				'alias': None,
				'description': 'Generates a universally unique identifier',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['uuid']], 'result': '550e8400-e29b-41d4-a716-446655440000'}
				]
			},
			'md5': {
				'group': 'crypto',
				'method': 'md5',
				'alias': None,
				'description': 'Generates an MD5 hash of a text',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['md5', 'hello']], 'result': '5d41402abc4b2a76b9719d911017c592'}
				]
			},
			'sha1': {
				'group': 'crypto',
				'method': 'sha1',
				'alias': None,
				'description': 'Generates an SHA-1 hash of a text',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['sha1', 'hello']], 'result': 'aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d'}
				]
			},
			'sha256': {
				'group': 'crypto',
				'method': 'sha256',
				'alias': None,
				'description': 'Generates an SHA-256 hash of a text',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['sha256', 'hello']], 'result': '2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824'}
				]
			},
			'sha512': {
				'group': 'crypto',
				'method': 'sha512',
				'alias': None,
				'description': 'Generates an SHA-512 hash of a text',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['sha512', 'hello']], 'result': '9b71d224bd62f3785d96d46ad3ea3d73319bfbc2890caadae2dff72519673ca72323c3d99ba5c11d7c7acc6e14b8c5da0c4663475c2e5c3adef46f73bcdec043'}
				]
			},
			'crc32': {
				'group': 'crypto',
				'method': 'crc32',
				'alias': None,
				'description': 'Calculates the CRC32 checksum of a text',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['crc32', 'hello']], 'result': 907060870}
				]
			},
			'base64': {
				'group': 'crypto',
				'method': 'base64_encode',
				'alias': None,
				'description': 'Encodes the data into Base64 format',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['base64', 'hello']], 'result': 'aGVsbG8='}
				]
			},
			'base64.decode': {
				'group': 'crypto',
				'method': 'base64_decode',
				'alias': None,
				'description': 'Decodes Base64 encoded data back to its original form',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['base64.decode', 'aGVsbG8=']], 'result': 'hello'}
				]
			},
			'base85': {
				'group': 'crypto',
				'method': 'base85_encode',
				'alias': None,
				'description': 'Encodes the data into Base85 format',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['base64', 'hello']], 'result': 'aGVsbG8='}
				]
			},
			'base85.decode': {
				'group': 'crypto',
				'method': 'base85_decode',
				'alias': None,
				'description': 'Decodes Base85 encoded data back to its original form',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['base64.decode', 'aGVsbG8=']], 'result': 'hello'}
				]
			},
			'gzip': {
				'group': 'crypto',
				'method': 'gzip_encode',
				'alias': None,
				'description': 'Compresses data using the GZip compression algorithm',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['gzip', 'hello']], 'result': 'H4sIAAAAAAAA/8tIzcnJVyjPL8pJAQCFEUoNCwAAAA=='}
				]
			},
			'gzip.decode': {
				'group': 'crypto',
				'method': 'gzip_decode',
				'alias': None,
				'description': 'Decompresses GZip compressed data',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['gzip.decode', 'H4sIAAAAAAAA/8tIzcnJVyjPL8pJAQCFEUoNCwAAAA==']], 'result': 'hello'}
				]
			},
			'rsa': {
				'group': 'crypto',
				'method': 'rsa_encode',
				'alias': None,
				'description': 'Encrypts data using RSA encryption with a public key',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['rsa', 'secret', 'public_key']], 'result': 'encrypted_data'}
				]
			},
			'rsa.decode': {
				'group': 'crypto',
				'method': 'rsa_decode',
				'alias': None,
				'description': 'Decrypts data encrypted with RSA using the corresponding private key',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['rsa.decode', 'encrypted_data', 'private_key']], 'result': 'secret'}
				]
			},
			'ssl': {
				'group': 'crypto',
				'method': 'ssl_encode',
				'alias': None,
				'description': 'Performs SSL encryption on data to secure communication',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['ssl', 'data']], 'result': 'encrypted_ssl_data'}
				]
			},
			'ssl.decode': {
				'group': 'crypto',
				'method': 'ssl_decode',
				'alias': None,
				'description': 'Decrypts data encrypted with SSL for secure data transfer',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['ssl.decode', 'encrypted_ssl_data']], 'result': 'data'}
				]
			},
			'bcrypt': {
				'group': 'crypto',
				'method': 'bcrypt_encode',
				'alias': None,
				'description': 'Hashes a password using the bcrypt algorithm for secure storage',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['bcrypt', 'password']], 'result': '$2a$12$saltpasswordhash'}
				]
			},
			'bcrypt.check': {
				'group': 'crypto',
				'method': 'bcrypt_check',
				'alias': None,
				'description': 'Verifies a password against a bcrypt hashed password',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['bcrypt.check', 'password', '$2a$12$saltpasswordhash']], 'result': True}
				]
			},

			# file

			'file': {
				'group': 'file',
				'method': 'file',
				'alias': None,
				'description': 'Read or write data to a file at a specified path',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['file', 'read', 'test.txt']], 'result': 'file contents'},
					{'code': [['file', 'write', 'test.txt', 'new content']], 'result': True}
				]
			},
			'file.exists': {
				'group': 'file',
				'method': 'file_exists',
				'alias': None,
				'description': 'Checks if a specified file exists at the given path',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['file.exists', 'test.txt']], 'result': True}
				]
			},
			'file.lines': {
				'group': 'file',
				'method': 'file_read_lines',
				'alias': None,
				'description': 'Reads a specified file line by line into a list',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['file.read.lines', 'test.txt']], 'result': ['line1', 'line2', 'line3']}
				]
			},
			'file.remove': {
				'group': 'file',
				'method': 'file_remove',
				'alias': None,
				'description': 'Removes a specified file from the file system',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['file.remove', 'test.txt']], 'result': True}
				]
			},
			'file.move': {
				'group': 'file',
				'method': 'file_move',
				'alias': None,
				'description': 'Moves a specified file to a new location',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['file.move', 'old.txt', 'new.txt']], 'result': True}
				]
			},
			'file.copy': {
				'group': 'file',
				'method': 'file_copy',
				'alias': None,
				'description': 'Copies a specified file to a new location',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['file.copy', 'source.txt', 'dest.txt']], 'result': True}
				]
			},
			'file.rename': {
				'group': 'file',
				'method': 'file_rename',
				'alias': None,
				'description': 'Renames a specified file',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['file.rename', 'old.txt', 'new.txt']], 'result': True}
				]
			},
			'file.link': {
				'group': 'file',
				'method': 'file_link',
				'alias': None,
				'description': 'Creates a hard link to a specified file',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['file.link', 'source.txt', 'link.txt']], 'result': True}
				]
			},
			'file.link.exists': {
				'group': 'file',
				'method': 'file_link_exists',
				'alias': None,
				'description': 'Checks if a hard link exists at the given path',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['file.link.exists', 'link.txt']], 'result': True}
				]
			},
			'file.info': {
				'group': 'file',
				'method': 'file_info',
				'alias': None,
				'description': 'Retrieves information about a specified file',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['file.info', 'test.txt']], 'result': {'size': 1024, 'modified': 1678901234}}
				]
			},
			'file.size': {
				'group': 'file',
				'method': 'file_size',
				'alias': None,
				'description': 'Returns the size of a specified file in bytes',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['file.size', 'test.txt']], 'result': 1024}
				]
			},
			'file.permission': {
				'group': 'file',
				'method': 'file_permission',
				'alias': None,
				'description': 'Retrieves or sets permissions for a specified file',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['file.permission', 'test.txt', 'rw-r--r--']], 'result': True}
				]
			},
			'file.time': {
				'group': 'file',
				'method': 'file_time',
				'alias': None,
				'description': 'Gets or sets the modified timestamp for a specified file',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['file.time', 'test.txt']], 'result': 1678901234}
				]
			},
			'file.sha256': {
				'group': 'file',
				'method': 'file_sha256',
				'alias': None,
				'description': 'Computes the SHA256 checksum of a specified file',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [
					{'name': 'path', 'type': 'text'}
				],
				'example': [
					{'code': [['file.sha256', 'test.txt']], 'result': '2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824'}
				]
			},
			'file.sha512': {
				'group': 'file',
				'method': 'file_sha512',
				'alias': None,
				'description': 'Computes the SHA512 checksum of a specified file',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [
					{'name': 'path', 'type': 'text'}
				],
				'example': [
					{'code': [['file.sha256', 'test.txt']], 'result': '2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824'}
				]
			},
			'file.crc32': {
				'group': 'file',
				'method': 'file_crc32',
				'alias': None,
				'description': 'Computes the CRC32 checksum for a specified file',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['file.crc32', 'test.txt']], 'result': 907060870}
				]
			},
			'file.base64': {
				'group': 'file',
				'method': 'file_base64',
				'alias': None,
				'description': 'Encodes a specified file to base64 format',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['file.base64', 'test.txt']], 'result': 'aGVsbG8='}
				]
			},
			'file.zip': {
				'group': 'file',
				'method': 'file_zip',
				'alias': None,
				'description': 'Compresses a specified file into a ZIP archive',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['file.zip', 'test.txt', 'archive.zip']], 'result': True}
				]
			},
			'file.zip.list': {
				'group': 'file',
				'method': 'file_zip_list',
				'alias': None,
				'description': 'Lists the files contained within a ZIP archive',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['file.zip.list', 'archive.zip']], 'result': ['test.txt']}
				]
			},
			'file.zip.exists': {
				'group': 'file',
				'method': 'file_zip_exists',
				'alias': None,
				'description': 'Checks if a specific file exists within a ZIP archive',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['file.zip.exists', 'archive.zip', 'test.txt']], 'result': True}
				]
			},
			'file.zip.read': {
				'group': 'file',
				'method': 'file_zip_read',
				'alias': None,
				'description': 'Reads a specific file from within a ZIP archive',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['file.zip.read', 'archive.zip', 'test.txt']], 'result': 'file contents'}
				]
			},
			'file.zip.remove': {
				'group': 'file',
				'method': 'file_zip_remove',
				'alias': None,
				'description': 'Removes a specific file from a ZIP archive',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['file.zip.remove', 'archive.zip', 'test.txt']]}
				]
			},
			'file.unzip': {
				'group': 'file',
				'method': 'file_unzip',
				'alias': None,
				'description': 'Extracts files from a ZIP archive into a specified directory',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['file.unzip', 'archive.zip', 'destination']]}
				]
			},
			'file.gzip': {
				'group': 'file',
				'method': 'file_gzip',
				'alias': None,
				'description': 'Compresses a specified file using GZip compression',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['file.gzip', 'test.txt', 'test.txt.gz']]}
				]
			},
			'file.ungzip': {
				'group': 'file',
				'method': 'file_ungzip',
				'alias': None,
				'description': 'Decompresses a GZip-compressed file',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['file.ungzip', 'test.txt.gz', 'test.txt']], 'result': True}
				]
			},
			'file.void': {
				'group': 'file',
				'method': 'file_void',
				'alias': None,
				'description': 'Compresses the specified file using GZip compression and places it in a Void container',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['file.void', 'test.txt', 'test.void']], 'result': True}
				]
			},
			'file.unvoid': {
				'group': 'file',
				'method': 'file_unvoid',
				'alias': None,
				'description': 'Decompresses a GZip-compressed files and directories from a Void container',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['file.unvoid', 'test.void', 'output']], 'result': True}
				]
			},
			'dir': {
				'group': 'file',
				'method': 'dir',
				'alias': None,
				'description': 'Lists the contents of a specified directory',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['dir.list', 'folder']], 'result': ['file1.txt', 'file2.txt', 'subfolder']},
					{'code': [['dir.list', 'project/src']], 'result': ['main.py', 'utils.py']}
				]
			},
			'dir.create': {
				'group': 'file',
				'method': 'dir_create',
				'alias': None,
				'description': 'Creates a new directory at a specified path',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['dir.create', 'new_folder']], 'test': False},
					{'code': [['dir.create', 'path/to/folder']], 'test': False}
				]
			},
			'dir.exists': {
				'group': 'file',
				'method': 'dir_exists',
				'alias': None,
				'description': 'Checks if a specified directory exists',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['dir.exists', 'folder']], 'result': True},
					{'code': [['dir.exists', 'nonexistent']], 'result': False}
				]
			},
			'dir.remove': {
				'group': 'file',
				'method': 'dir_remove',
				'alias': None,
				'description': 'Removes a specified directory and its contents',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['dir.remove', 'temp']], 'test': False},
					{'code': [['dir.remove', 'old_backup']], 'test': False}
				]
			},
			'dir.move': {
				'group': 'file',
				'method': 'dir_move',
				'alias': None,
				'description': 'Moves a specified directory to a new location',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['dir.move', 'old', 'new']], 'test': False},
					{'code': [['dir.move', 'temp', 'perm']], 'test': False}
				]
			},
			'dir.copy': {
				'group': 'file',
				'method': 'dir_copy',
				'alias': None,
				'description': 'Copies a specified directory and its contents to a new location',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['dir.copy', 'source', 'destination']], 'test': False},
					{'code': [['dir.copy', 'backup', 'archive/backup']], 'test': False}
				]
			},
			'dir.rename': {
				'group': 'file',
				'method': 'dir_rename',
				'alias': None,
				'description': 'Renames a specified directory',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['dir.rename', 'old_name', 'new_name']], 'test': False},
					{'code': [['dir.rename', 'temp', 'final']], 'test': False}
				]
			},
			'dir.clear': {
				'group': 'file',
				'method': 'dir_clear',
				'alias': None,
				'description': 'Clears all contents of a specified directory without deleting the directory itself',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['dir.clear', 'temp']], 'test': False},
					{'code': [['dir.clear', 'cache']], 'test': False}
				]
			},
			'dir.info': {
				'group': 'file',
				'method': 'dir_info',
				'alias': None,
				'description': 'Retrieves information about a specified directory',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['dir.info', 'folder']], 'result': {'size': 1024, 'files': 10, 'modified': 1672531200}, 'test': False},
					{'code': [['dir.info', 'project']], 'result': {'size': 2048, 'files': 15, 'modified': 1672531200}, 'test': False}
				]
			},
			'dir.size': {
				'group': 'file',
				'method': 'dir_size',
				'alias': None,
				'description': 'Calculates the total size of a specified directory and its contents',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['dir.size', 'data']], 'result': 1048576},
					{'code': [['dir.size', 'downloads']], 'result': 5242880}
				]
			},
			'dir.permission': {
				'group': 'file',
				'method': 'dir_permission',
				'alias': None,
				'description': 'Gets or sets the permissions of a specified directory',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['dir.permission', 'scripts', '755']], 'test': False},
					{'code': [['dir.permission', 'uploads', '775']], 'test': False}
				]
			},
			'dir.time': {
				'group': 'file',
				'method': 'dir_time',
				'alias': None,
				'description': 'Gets or sets the timestamps of a specified directory',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['dir.time', 'logs']], 'result': 1672531200, 'test': False},
					{'code': [['dir.time', 'backups', 'created']], 'result': 1672531200, 'test': False}
				]
			},
			'dir.zip': {
				'group': 'file',
				'method': 'dir_zip',
				'alias': None,
				'description': 'Compresses a specified directory into a ZIP archive',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['dir.zip', 'archive.zip', 'folder']], 'test': False},
					{'code': [['dir.zip', 'backup.zip', 'data']], 'test': False}
				]
			},
			'dir.void': {
				'group': 'file',
				'method': 'dir_void',
				'alias': None,
				'description': 'Compresses a specified directory into a Void container',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['dir.void', 'data']], 'result': 'data.void', 'test': False},
					{'code': [['dir.void', 'project', 'backup.void']], 'test': False}
				]
			},
			'drive': {
				'group': 'file',
				'method': 'drive_list',
				'alias': None,
				'description': 'Lists all available drives on the system',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['drive.list']], 'result': ['C:', 'D:', 'E:'], 'test': False},
					{'code': [['drive.list', 'removable']], 'result': ['D:', 'E:'], 'test': False}
				]
			},
			'drive.name': {
				'group': 'file',
				'method': 'drive_name',
				'alias': None,
				'description': 'Gets or sets the name of a specified drive',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['drive.name', 'C:']], 'result': 'System'},
					{'code': [['drive.name', 'D:', 'Data']], 'test': False}
				]
			},
			'drive.size': {
				'group': 'file',
				'method': 'drive_size',
				'alias': None,
				'description': 'Total size of a specified drive',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['drive.size', 'C:']], 'result': 256000000000},
					{'code': [['drive.size', 'D:']], 'result': 1000000000000}
				]
			},
			'drive.used': {
				'group': 'file',
				'method': 'drive_used',
				'alias': None,
				'description': 'Amount of used space on a specified drive',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['drive.used', 'C:']], 'result': 128000000000},
					{'code': [['drive.used', 'D:']], 'result': 500000000000}
				]
			},
			'drive.free': {
				'group': 'file',
				'method': 'drive_free',
				'alias': None,
				'description': 'Amount of free space on a specified drive',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['drive.free', 'C:']], 'result': 128000000000},
					{'code': [['drive.free', 'D:']], 'result': 500000000000}
				]
			},
			'drive.info': {
				'group': 'file',
				'method': 'drive_info',
				'alias': None,
				'description': 'Retrieves information about a specified drive',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['drive.info', 'C:']], 'result': {'size': 256000000000, 'free': 128000000000, 'type': 'SSD'}, 'test': False},
					{'code': [['drive.info', 'D:']], 'result': {'size': 1000000000000, 'free': 500000000000, 'type': 'HDD'}, 'test': False}
				]
			},
			'drive.mount': {
				'group': 'file',
				'method': 'drive_mount',
				'alias': None,
				'description': 'Mounts a drive to make it accessible',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['drive.mount', '/dev/sdb1', 'D:']], 'test': False},
					{'code': [['drive.mount', 'image.iso', 'E:']], 'test': False}
				]
			},
			'drive.unmount': {
				'group': 'file',
				'method': 'drive_unmount',
				'alias': None,
				'description': 'Unmounts a drive',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['drive.unmount', 'D:']], 'test': False},
					{'code': [['drive.unmount', 'E:']], 'test': False}
				]
			},
			'drive.create': {
				'group': 'file',
				'method': 'drive_create',
				'alias': None,
				'description': 'Creates a new virtual drive or volume',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['drive.create', 'virtual', 1000000000]], 'test': False},
					{'code': [['drive.create', 'ramdisk', 4000000000, 'RAM']], 'test': False}
				]
			},
			'drive.resize': {
				'group': 'file',
				'method': 'drive_resize',
				'alias': None,
				'description': 'Resizes an existing drive partition or volume',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['drive.resize', 'virtual', 2000000000]], 'test': False},
					{'code': [['drive.resize', 'D:', 1500000000000]], 'test': False}
				]
			},
			'drive.format': {
				'group': 'file',
				'method': 'drive_format',
				'alias': None,
				'description': 'Formats a drive with a specified file system',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['drive.format', 'D:', 'NTFS']], 'test': False},
					{'code': [['drive.format', 'E:', 'FAT32']], 'test': False}
				]
			},
			'drive.remove': {
				'group': 'file',
				'method': 'drive_remove',
				'alias': None,
				'description': 'Removes or deletes a specified drive or partition',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['drive.remove', 'virtual']], 'test': False},
					{'code': [['drive.remove', 'ramdisk']], 'test': False}
				]
			},
			'path': {
				'group': 'file',
				'method': 'path',
				'alias': None,
				'description': 'Returns components of a specified file path',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['path.drive', 'C:/Windows/System32']], 'result': 'C:'},
					{'code': [['path.drive', '/mnt/data/file.txt']], 'result': ''}
				]
			},
			'path.drive': {
				'group': 'file',
				'method': 'path_drive',
				'alias': None,
				'description': 'Drive component of a specified file path',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['path.drive', 'C:/Windows/System32']], 'result': 'C:'},
					{'code': [['path.drive', '/mnt/data/file.txt']], 'result': ''}
				]
			},
			'path.dir': {
				'group': 'file',
				'method': 'path_dir',
				'alias': None,
				'description': 'Directory portion of a specified file path',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['path.dir', 'C:/Windows/System32/kernel32.dll']], 'result': 'C:/Windows/System32'},
					{'code': [['path.dir', '/home/user/docs/file.txt']], 'result': '/home/user/docs'}
				]
			},
			'path.file': {
				'group': 'file',
				'method': 'path_file',
				'alias': None,
				'description': 'File portion of a specified file path',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['path.file', 'C:/Windows/System32/kernel32.dll']], 'result': 'kernel32.dll'},
					{'code': [['path.file', '/home/user/docs/report.pdf']], 'result': 'report.pdf'}
				]
			},
			'path.name': {
				'group': 'file',
				'method': 'path_name',
				'alias': None,
				'description': 'Name of the file without extension from a specified path',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['path.name', 'document.txt']], 'result': 'document'},
					{'code': [['path.name', '/path/to/file.name.ext']], 'result': 'file.name'}
				]
			},
			'path.extension': {
				'group': 'file',
				'method': 'path_extension',
				'alias': None,
				'description': 'File extension from a specified file path',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['path.extension', 'image.png']], 'result': '.png'},
					{'code': [['path.extension', 'archive.tar.gz']], 'result': '.gz'}
				]
			},
			'path.strip': {
				'group': 'file',
				'method': 'path_strip',
				'alias': None,
				'description': 'Removes the extension from a specified path',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['path.strip', 'file.txt']], 'result': 'file'},
					{'code': [['path.strip', '/path/to/document.pdf']], 'result': '/path/to/document'}
				]
			},

			# format

			'void': {
				'group': 'format',
				'method': 'void_encode',
				'alias': None,
				'description': 'Encodes data into the Void format',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [
					{'name': 'data', 'type': 'any'},
					{'name': 'indent', 'type': 'text', 'default': '\t'}
				],
				'example': [
					{'code': [['void', {'key': 'value'}]], 'result': '{\n\t\'key\': \'value\'\n}'},
					{'code': [['void', [1, 2, 3], '  ']], 'result': '[\n  1,\n  2,\n  3\n]'}
				]
			},
			'void.decode': {
				'group': 'format',
				'method': 'void_decode',
				'alias': None,
				'description': 'Decodes data from the Void format',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['void.decode', '{\'key\':\'value\'}']], 'result': {'key': 'value'}},
					{'code': [['void.decode', '[1,2,3]']], 'result': [1, 2, 3]}
				]
			},
			'json': {
				'group': 'format',
				'method': 'json_encode',
				'alias': None,
				'description': 'Encodes data into the JSON format',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['json', {'name': 'John', 'age': 30}]], 'result': '{\'name\':\'John\',\'age\':30}'},
					{'code': [['json', [True, False]]], 'result': '[true,false]'}
				]
			},
			'json.decode': {
				'group': 'format',
				'method': 'json_decode',
				'alias': None,
				'description': 'Decodes data from the JSON format',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['json.decode', '{\'x\':5,\'y\':10}']], 'result': {'x': 5, 'y': 10}},
					{'code': [['json.decode', '[\'a\',\'b\']']], 'result': ['a', 'b']}
				]
			},
			'csv': {
				'group': 'format',
				'method': 'csv_encode',
				'alias': None,
				'description': 'Encodes data into the CSV format',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['csv', [['Name', 'Age'], ['John', 30], ['Alice', 25]]]], 'result': 'Name,Age\nJohn,30\nAlice,25'},
					{'code': [['csv', {'a': [1,2], 'b': [3,4]}]], 'result': 'a,b\n1,3\n2,4'}
				]
			},
			'csv.decode': {
				'group': 'format',
				'method': 'csv_decode',
				'alias': None,
				'description': 'Decodes data from the CSV format',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['csv.decode', 'a,b,c\n1,2,3']], 'result': [{'a':'1','b':'2','c':'3'}]},
					{'code': [['csv.decode', 'x;y\n4;5', ';']], 'result': [{'x':'4','y':'5'}]}
				]
			},
			'yaml': {
				'group': 'format',
				'method': 'yaml_encode',
				'alias': None,
				'description': 'Encodes data into the YAML format',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['yaml', {'name': 'John', 'skills': ['Python', 'JS']}]], 'result': 'name: John\nskills:\n  - Python\n  - JS'},
					{'code': [['yaml', [1, 2, 3]]], 'result': '- 1\n- 2\n- 3'}
				]
			},
			'yaml.decode': {
				'group': 'format',
				'method': 'yaml_decode',
				'alias': None,
				'description': 'Decodes data from the YAML format',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['yaml.decode', 'key: value']], 'result': {'key': 'value'}},
					{'code': [['yaml.decode', '- 1\n- 2']], 'result': [1, 2]}
				]
			},
			'ini': {
				'group': 'format',
				'method': 'ini_encode',
				'alias': None,
				'description': 'Encodes data into the INI format',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['ini', {'section': {'key': 'value'}}]], 'result': '[section]\nkey=value'},
					{'code': [['ini', {'user': {'name': 'John'}, 'db': {'port': 3306}}]], 'result': '[user]\nname=John\n\n[db]\nport=3306'}
				]
			},
			'ini.decode': {
				'group': 'format',
				'method': 'ini_decode',
				'alias': None,
				'description': 'Decodes data from the INI format',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['ini.decode', '[section]\nkey=value']], 'result': {'section': {'key': 'value'}}},
					{'code': [['ini.decode', '[user]\nname=John']], 'result': {'user': {'name': 'John'}}}
				]
			},
			'xml': {
				'group': 'format',
				'method': 'xml_encode',
				'alias': None,
				'description': 'Encodes data into the XML format',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['xml', {'root': {'item': ['a', 'b']}}]], 'result': '<root><item>a</item><item>b</item></root>'},
					{'code': [['xml', {'person': {'@id': 1, 'name': 'John'}}]], 'result': '<person id=\'1\'><name>John</name></person>'}
				]
			},
			'xml.decode': {
				'group': 'format',
				'method': 'xml_decode',
				'alias': None,
				'description': 'Decodes data from the XML format',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['xml.decode', '<root><x>1</x></root>']], 'result': {'root': {'x': '1'}}},
					{'code': [['xml.decode', '<person id=\'1\'><name>John</name></person>']], 'result': {'person': {'@id': '1', 'name': 'John'}}}
				]
			},

			# communication

			'cloud': {
				'group': 'communication',
				'method': 'cloud',
				'alias': None,
				'description': 'Runs cloud storage or services for data management',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': True,
				'param': [],
				'example': [
					{'code': [['cloud', 'start']], 'test': False},
					{'code': [['cloud', 'status']], 'result': 'running', 'test': False}
				]
			},
			'request': {
				'group': 'communication',
				'method': 'request',
				'alias': 'r',
				'description': 'Sends an HTTP (GET by default) request to a specified URL',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': {
					'get': {},
					'post': {},
					'put': {},
					'delete': {},
					'method': {},
					'url': {},
					'header': {},
					'cookie': {},
					'data': {},
					'done': {},
					'error': {}
				},
				'param': [],
				'example': [
					{'code': [['r', 'https://api.example.com/data']], 'test': False},
					{'code': [['r', 'https://example.com', {'headers': {'Accept': 'application/json'}}]], 'test': False}
				]
			},
			'download': {
				'group': 'communication',
				'method': 'download',
				'alias': 'd',
				'description': 'Downloads content from a specified URL',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': {
					'url': {},
					'video': {},
					'audio': {},
					'subtitles': {},
					'': {},
					'': {},
					'': {},
					'': {},
					'': {},
					'': {},
				},
				'param': [],
				'example': [
					{'code': [['dl', 'https://example.com/file.txt', 'local.txt']], 'test': False},
					{'code': [['dl', 'https://example.com/image.jpg']], 'test': False}
				]
			},
			'cookie': {
				'group': 'communication',
				'method': 'cookie',
				'alias': None,
				'description': 'Gets or sets a specified cookie',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['cookie', 'session', 'abc123']], 'test': False},
					{'code': [['cookie', 'user']], 'result': 'john_doe', 'test': False}
				]
			},
			'cookie.remove': {
				'group': 'communication',
				'method': 'cookie_remove',
				'alias': None,
				'description': 'Removes a specified cookie from the client\'s storage',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['cookie.remove', 'session']], 'test': False},
					{'code': [['cookie.remove', 'temp']], 'test': False}
				]
			},
			'social': {
				'group': 'communication',
				'method': 'social',
				'alias': None,
				'description': 'Interacting with social API',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': True,
				'param': [],
				'example': [
					{'code': [['social', 'tiktok', 'upload', 'clip.mp4']], 'test': False},
					{'code': [['social', 'telegram', 'send', '@name', 'Text']], 'test': False},
					{'code': [['social', 'telegram', 'bot', 'bot_action']], 'test': False}
				]
			},
			'notification': {
				'group': 'communication',
				'method': 'notification',
				'alias': None,
				'description': 'Send notification',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['notification', 'New message']], 'test': False},
					{'code': [['notification', 'Alert', {'sound': True}]], 'test': False}
				]
			},
			'mail': {
				'group': 'communication',
				'method': 'mail',
				'alias': None,
				'description': 'Send mail',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['mail', 'user@example.com', 'Subject', 'Body']], 'test': False},
					{'code': [['mail', 'test@example.com', 'Hello', 'Content', {'cc': 'copy@example.com'}]], 'test': False}
				]
			},
			'call': {
				'group': 'communication',
				'method': 'call',
				'alias': None,
				'description': 'Initiate a voice or video call to a specified recipient',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['call', '+1234567890']], 'test': False},
					{'code': [['call', 'user@domain.com', 'video']], 'test': False}
				]
			},
			'sms': {
				'group': 'communication',
				'method': 'sms',
				'alias': None,
				'description': 'Send a text message (SMS) to a specified recipient',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['sms', '+1234567890', 'Hello']], 'test': False},
					{'code': [['sms', '+0987654321', 'Your code: 1234']], 'test': False}
				]
			},

			# device

			'device': {
				'group': 'device',
				'method': 'device',
				'alias': None,
				'description': 'Information related to the hardware device',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['device']], 'result': {'model': 'iPhone12,1', 'manufacturer': 'Apple'}, 'test': False},
					{'code': [['device', 'id']], 'result': 'A12B3C4D', 'test': False}
				]
			},
			'cpu': {
				'group': 'device',
				'method': 'cpu',
				'alias': None,
				'description': 'Information about the CPU, including its usage and specifications',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['cpu']], 'result': {'cores': 8, 'usage': 34.5}, 'test': False},
					{'code': [['cpu', 'temperature']], 'result': 65.2, 'test': False}
				]
			},
			'fps': {
				'group': 'device',
				'method': 'fps',
				'alias': None,
				'description': 'Frames per second for video or graphical rendering',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['fps']], 'result': 60, 'test': False},
					{'code': [['fps', 'set', 30]], 'test': False}
				]
			},
			'vsync': {
				'group': 'device',
				'method': 'vsync',
				'alias': None,
				'description': 'Vertical sync settings to reduce screen tearing during rendering',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['vsync']], 'result': True, 'test': False},
					{'code': [['vsync', 'set', False]], 'test': False}
				]
			},
			'resolution': {
				'group': 'device',
				'method': 'resolution',
				'alias': None,
				'description': 'Screen resolution',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['resolution']], 'result': [1920, 1080], 'test': False},
					{'code': [['resolution', 'set', 1280, 720]], 'test': False}
				]
			},
			'orientation': {
				'group': 'device',
				'method': 'orientation',
				'alias': None,
				'description': 'Orientation of a device\'s display (landscape or portrait)',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['orientation']], 'result': 'landscape', 'test': False},
					{'code': [['orientation', 'set', 'portrait']], 'test': False}
				]
			},
			'dark': {
				'group': 'device',
				'method': 'darkmode',
				'alias': None,
				'description': 'Dark mode setting for user interfaces',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['darkmode']], 'result': True, 'test': False},
					{'code': [['darkmode', 'set', False]], 'test': False}
				]
			},
			'pixel': {
				'group': 'device',
				'method': 'pixel',
				'alias': None,
				'description': 'Color of the pixel displayed on the screen',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['pixel', 100, 200]], 'result': [255, 0, 0], 'test': False},
					{'code': [['pixel', 'set', 150, 300, [0, 255, 0]]], 'test': False}
				]
			},
			'char': {
				'group': 'device',
				'method': 'textmode_character',
				'alias': None,
				'description': 'Symbol on the screen in text mode',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['textmode.character', 10, 5]], 'result': 'A', 'test': False},
					{'code': [['textmode.character', 'set', 12, 7, 'B']], 'test': False}
				]
			},
			'cursor': {
				'group': 'device',
				'method': 'textmode_cursor',
				'alias': None,
				'description': 'Cursor position on the screen in text mode',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['textmode.cursor']], 'result': [5, 10], 'test': False},
					{'code': [['textmode.cursor', 'set', 0, 0]], 'test': False}
				]
			},
			'clear': {
				'group': 'device',
				'method': 'textmode_clear',
				'alias': None,
				'description': 'Clears the screen in text mode',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['textmode.clear']], 'test': False},
					{'code': [['textmode.clear', 'green']], 'test': False}
				]
			},
			'light': {
				'group': 'device',
				'method': 'flashlight',
				'alias': None,
				'description': 'Turns on or off the device\'s flashlight',
				'language': ['swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['flashlight', 'on']], 'test': False},
					{'code': [['flashlight', 'off']], 'test': False}
				]
			},
			'location': {
				'group': 'device',
				'method': 'location',
				'alias': None,
				'description': 'Retrieves the current geographic location using GPS or network triangulation',
				'language': ['js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['location']], 'result': {'lat': 55.7558, 'lon': 37.6173}, 'test': False},
					{'code': [['location', 'accuracy', 10]], 'test': False}
				]
			},
			'gyroscope': {
				'group': 'device',
				'method': 'gyroscope',
				'alias': None,
				'description': 'Provides access to the gyroscope sensor for motion detection',
				'language': ['js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['gyroscope']], 'result': {'x': 0.1, 'y': -0.2, 'z': 0.05}, 'test': False},
					{'code': [['gyroscope', 'frequency', 10]], 'test': False}
				]
			},
			'accelerometer': {
				'group': 'device',
				'method': 'accelerometer',
				'alias': None,
				'description': 'Provides access to the accelerometer sensor to detect acceleration forces',
				'language': ['js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['accelerometer']], 'result': {'x': 0.0, 'y': 0.0, 'z': 9.8}, 'test': False},
					{'code': [['accelerometer', 'calibrate']], 'test': False}
				]
			},
			'compass': {
				'group': 'device',
				'method': 'compass',
				'alias': None,
				'description': 'Accesses the magnetic compass sensor to determine orientation relative to the Earth\'s magnetic field',
				'language': ['js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['compass']], 'result': 180.5, 'test': False},
					{'code': [['compass', 'calibrate']], 'test': False}
				]
			},
			'proximity': {
				'group': 'device',
				'method': 'proximity',
				'alias': None,
				'description': 'Detects the proximity of objects in relation to the device\'s proximity sensor',
				'language': ['swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['proximity']], 'result': 5.2, 'test': False},
					{'code': [['proximity', 'threshold', 10]], 'test': False}
				]
			},
			'brightness': {
				'group': 'device',
				'method': 'brightness',
				'alias': None,
				'description': 'Manages the screen brightness level of the device',
				'language': ['swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['brightness']], 'result': 80, 'test': False},
					{'code': [['brightness', 'set', 50]], 'test': False}
				]
			},
			'calendar': {
				'group': 'device',
				'method': 'calendar',
				'alias': None,
				'description': 'Calendar events on a device',
				'language': ['swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['calendar', 'events']], 'result': [], 'test': False},
					{'code': [['calendar', 'add', 'Meeting', '2023-12-01 14:00']], 'test': False}
				]
			},
			'gallery': {
				'group': 'device',
				'method': 'gallery',
				'alias': None,
				'description': 'Photo and video library on a device',
				'language': ['swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['gallery', 'photos']], 'result': ['photo1.jpg', 'photo2.jpg'], 'test': False},
					{'code': [['gallery', 'save', 'new.jpg']], 'test': False}
				]
			},
			'contacts': {
				'group': 'device',
				'method': 'contacts',
				'alias': None,
				'description': 'Contact list on a device',
				'language': ['swift', 'kotlin', 'gdscript', 'c++'],
				'safe': False,
				'container': None,
				'param': [],
				'example': [
					{'code': [['contacts']], 'result': [{'name': 'John', 'phone': '+1234567890'}], 'test': False},
					{'code': [['contacts', 'add', 'Alice', '+0987654321']], 'test': False}
				]
			},
			'keyboard': {
				'group': 'device',
				'method': 'keyboard',
				'alias': None,
				'description': 'Keyboard information',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['keyboard']], 'result': {'layout': 'QWERTY', 'language': 'en-US'}}
				]
			},
			'mouse': {
				'group': 'device',
				'method': 'mouse',
				'alias': None,
				'description': 'Mouse information',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['mouse']], 'result': {'x': 500, 'y': 300, 'buttons': 0}}
				]
			},
			'gamepad': {
				'group': 'device',
				'method': 'gamepad',
				'alias': None,
				'description': 'Gamepad information',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['gamepad', 0]], 'result': {'buttons': [False], 'axes': [0.0]}}
				]
			},
			'tap': {
				'group': 'device',
				'method': 'tap',
				'alias': None,
				'description': 'Simulates a tap gesture',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['tap', 100, 200]], 'result': True}
				]
			},
			'key': {
				'group': 'device',
				'method': 'key',
				'alias': None,
				'description': 'Key binding',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': None,
				'param': [],
				'example': [
					{'code': [['key', 'Ctrl+S', 'save']], 'result': True}
				]
			},

			# content

			'image': {
				'group': 'content',
				'method': 'image',
				'alias': None,
				'description': 'Create an image',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': True,
				'param': [],
				'example': [
					{'code': [['image', 'A sunset over mountains']], 'result': 'image.png'}
				]
			},
			'video': {
				'group': 'content',
				'method': 'video',
				'alias': ['movie', 'anime'],
				'description': 'Create a video',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': True,
				'param': [],
				'example': [
					{'code': [['video', 'A beach sunset', 10]], 'result': 'video.mp4'}
				]
			},
			'sound': {
				'group': 'content',
				'method': 'sound',
				'alias': None,
				'description': 'Create audio track',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': True,
				'param': [],
				'example': [
					{'code': [['sound', 'Ocean waves', 30]], 'result': 'sound.mp3'}
				]
			},
			'music': {
				'group': 'content',
				'method': 'music',
				'alias': None,
				'description': 'Generates music',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': True,
				'param': [],
				'example': [
					{'code': [['music', 'Relaxing piano', 180]], 'result': 'music.mp3'}
				]
			},
			'model': {
				'group': 'content',
				'method': 'model',
				'alias': None,
				'description': 'Create 3D model',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': True,
				'param': [],
				'example': []
			},
			'book': {
				'group': 'content',
				'method': 'book',
				'alias': ['novel', 'manga'],
				'description': 'Create a book, comic, manga',
				'language': ['python', 'js', 'swift', 'kotlin', 'gdscript', 'c++'],
				'safe': True,
				'container': True,
				'param': [],
				'example': []
			}
		},
		'alias': {
			'.': 'print',
			'..': 'printn',
			'...': 'input',
			'?': 'if',
			'c': 'convert',
			'd': 'download',
			'e': 'escape',
			'h': 'help',
			'i': 'info',
			'l': 'length',
			'o': 'loop',
			'r': 'request',
			't': 'timecheck',
			'x': 'break',
			'x>': 'continue',
			'<x': 'repeat',
			'X': 'return',
			'response': 'return',
			'xx': 'exit',
			'app': 'ui',
			'game': 'ui',
			'web': 'ui',
			'cli': 'ui'
		},
		'pi': 3.1415926535,
		'pi2': 9.8696044011,
		'2pi': 6.2831853071,
		'e': 2.7182818284,
		'epi': 23.1406926327,
		'pie': 1.1557273498,
		'phi': 1.6180339887,
		'sqrt2': 1.4142135623,
		'sqrt3': 1.7320508075,
		'sqrt5': 2.2360679775,
		'ln2': 0.6931471805,
		'ln10': 2.3025850929,
		'gamma': 0.5772156649,
		'app': {
			'path': '',
			'name': '',
			'argument': []
		},
		'device': {
			'fps': None,
			'cpu': {},
			'gpu': {}
		},
		'os': {
			'type': None,
			'name': None,
			'version': None
		},
		'cloud': {
			'mime': {
				# data
				'void': 'application/void',
				'json': 'application/json',
				'jsonl': 'application/jsonl',
				'jsonld': 'application/ld+json',
				'yaml': 'application/x-yaml',
				'csv': 'text/csv',
				'ini': 'text/plain',
				'xml': 'application/xml',
				'sql': 'application/sql',
				'bin': 'application/octet-stream',
				# document
				'text': 'text/plain',
				'txt': 'text/plain',
				'pdf': 'application/pdf',
				'djvu': 'image/vnd.djvu',
				'doc': 'application/msword',
				'docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
				'xls': 'application/vnd.ms-excel',
				'xlsx': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
				'ppt': 'application/vnd.ms-powerpoint',
				'pptx': 'application/vnd.openxmlformats-officedocument.presentationml.presentation',
				'rtf': 'application/rtf',
				'epub': 'application/epub+zip',
				'abw': 'application/x-abiword',
				'azw': 'application/vnd.amazon.ebook',
				'odp': 'application/vnd.oasis.opendocument.presentation',
				'ods': 'application/vnd.oasis.opendocument.spreadsheet',
				'odt': 'application/vnd.oasis.opendocument.text',
				'ics': 'text/calendar',
				# html
				'html': 'text/html',
				'htm': 'text/html',
				'xhtml': 'application/xhtml+xml',
				'css': 'text/css',
				# font
				'ttf': 'font/ttf',
				'otf': 'font/otf',
				'sfnt': 'font/sfnt',
				'woff': 'font/woff',
				'woff2': 'font/woff2',
				'eot': 'application/vnd.ms-fontobject',
				# image
				'jpeg': 'image/jpeg',
				'jpg': 'image/jpeg',
				'png': 'image/png',
				'apng': 'image/apng',
				'gif': 'image/gif',
				'svg': 'image/svg+xml',
				'webp': 'image/webp',
				'heif': 'image/heif',
				'heic': 'image/heic',
				'tiff': 'image/tiff',
				'tif': 'image/tiff',
				'avif': 'image/avif',
				'ico': 'image/x-icon',
				'icon': 'image/vnd.microsoft.icon',
				'icns': 'image/x-icns',
				# audio
				'mp3': 'audio/mpeg',
				'mpa': 'audio/mpeg',
				'mp2': 'audio/mpeg',
				'wma': 'audio/x-ms-wma',
				'wav': 'audio/x-wav',
				'flac': 'audio/flac',
				'ogg': 'application/ogg',
				'oga': 'audio/ogg',
				'weba': 'audio/webm',
				'cda': 'application/x-cdf',
				'aac': 'audio/aac',
				'ac3': 'audio/ac3',
				'mid': 'audio/midi',
				'midi': 'audio/x-midi',
				's3m': 'audio/s3m',
				'it':  'audio/it',
				'mod': 'audio/x-mod',
				'xm':  'audio/xm',
				# video
				'mp4': 'video/mp4',
				'mpeg': 'video/mpeg',
				'mpg': 'video/mpeg',
				'mpv': 'video/mpeg',
				'webm': 'video/webm',
				'ogx': 'application/ogg',
				'ogv': 'video/ogg',
				'qt': 'video/quicktime',
				'mov': 'ideo/quicktime',
				'm4v': 'video/x-m4v',
				'wmv': 'video/x-ms-wmv',
				'avi': 'video/x-msvideo',
				'mkv': 'application/x-matroska',
				'mjpeg': 'multipart/x-mixed-replace',
				'ts': 'video/mp2t',
				# 3d
				'gltf': 'model/gltf+json',
				'glb': 'model/gltf-binary',
				'obj': 'model/obj',
				'stl': 'model/stl',
				'fbx': 'application/vnd.autodesk.fbx',
				'dae': 'model/vnd.collada+xml',
				'3ds': 'model/x-3ds',
				'ply': 'model/ply',
				'usd': 'model/vnd.usd',
				'usdz': 'model/vnd.usdz+zip',
				'x3d': 'model/x3d+xml',
				'wrl': 'model/vrml',
				'vrml': 'model/vrml',
				# archive
				'zip': 'application/zip',
				'gz': 'application/gzip',
				'7z': 'application/x-7z-compressed',
				'tar': 'application/x-tar',
				'arc': 'application/x-freearc',
				'rar': 'application/vnd.rar',
				'bz': 'application/x-bzip',
				'bz2': 'application/x-bzip2',
				'mpkg': 'application/vnd.apple.installer+xml',
				# code
				'py': 'applycation/x-python-code',
				'php': 'application/x-httpd-php',
				'java': 'application/java',
				'jar': 'application/java-archive',
				'kt':  'text/x-kotlin',
				'swift': 'application/swift',
				'c':   'text/x-csrc',
				'cpp': 'text/x-c++src',
				'h':   'text/x-chdr',
				'cs': 'text/x-csharp',
				'gd': 'text/x-gdscript',
				'js': 'text/javascript',
				'mjs': 'text/javascript',
				'lua': 'text/x-lua',
				'sh': 'application/x-sh',
				'csh': 'application/x-csh',
				'bat': 'application/x-bat',
				'ps1': 'text/x-powershell',
				# form
				'form data': 'multipart/form-data',
				'form mixed': 'multipart/mixed',
				'form alternative': 'multipart/alternative',
				'form text': 'application/x-www-form-urlencoded'
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
		'info': {},
		'db': {},
		'ai': {},
		'run': [],
		'action': {},
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
		if '/' in name or '\\' in name:
			path_outer = void.path_dir(name)
			path_extension = void.path_extension(path_outer).lower()
			if path_extension in ['void', 'json', 'csv', 'yaml', 'ini', 'xml'] and void.file_exists(path_outer):
				data = void.file(path_outer)
				name = void.path_file(name)
			else:
				return default
		elif data == None:
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
		if '/' in name or '\\' in name:
			path_outer = void.path_dir(name)
			path_extension = void.path_extension(path_outer).lower()
			if path_extension in ['void', 'json', 'csv', 'yaml', 'ini', 'xml'] and void.file_exists(path_outer):
				data_file = void.file(path_outer)
				data = data_file
				name = void.path_file(name)
				file = True
			else:
				return
		elif data == None:
			data = void.data
			file = False
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
					if file:
						void.file(path_outer, data_file)
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
					if file:
						void.file(path_outer, data_file)
					return
				data = data[subname]
			else:
				return

	def remove(name: str, data = None):
		if '/' in name or '\\' in name:
			path_outer = void.path_dir(name)
			path_extension = void.path_extension(path_outer).lower()
			if path_extension in ['void', 'json', 'csv', 'yaml', 'ini', 'xml'] and void.file_exists(path_outer):
				data_file = void.file(path_outer)
				data = data_file
				name = void.path_file(name)
				file = True
			else:
				return
		elif data == None:
			data = void.data
			file = False
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
					if file:
						void.file(path_outer, data_file)
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
					if file:
						void.file(path_outer, data_file)
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

	def length(data):
		data_type = type(data)
		if data_type in [str, list, dict, bytes]:
			return len(data)
		elif data_type is int:
			return (data.bit_length() + 7) // 8
		elif data_type is float:
			return 8
		return 0

	def expression_plus(first = None, second = None):
		match first:
			case bool():
				return first or bool(second)
			case int() | float():
				if second is None:
					return first + 1
				if type(second) in [int, float]:
					return first + second
				if type(second) is str:
					return void.number(second)
			case str():
				if second is None:
					return first + ' '
				if type(second) is str:
					return first + second
				if type(second) is int:
					return first + ' ' * second
			case list():
				if second is None:
					return first + first
				if type(second) is list:
					return first + second
				if type(second) is int:
					return first + [None for _ in range(second)]
			case dict():
				if type(second) is dict:
					return void.merge(first, second)
				if type(second) is str:
					return void.merge(first, {second: None})
				if type(second) is int and second > 0:
					return [first for _ in range(second + 1)]
			case bytes():
				if second is None:
					return first + first
				if type(second) is bytes:
					return first + second
				if type(second) is str:
					return first + second.encode()
				if type(second) in [int, float]:
					return first + bytes(str(second).encode())
				if type(second) is bool:
					return first + bytes(int(second))

	def expression_minus(first, second):
		match first:
			case bool():
				return first and not bool(second)
			case int() | float():
				if second is None:
					return first + 1
				if type(second) in [int, float]:
					return first + second
				if type(second) is str:
					return void.number(second)
			case str():
				if second is None:
					return first.strip()
				if type(second) is str:
					return first + second
				if type(second) is int:
					return first + first * second
			case list():
				if second is None:
					return first + first
				if type(second) is list:
					return first + second
				if type(second) is int:
					return first + first * second
			case dict():
				if type(second) is dict:
					return void.merge(first, second)
			case bytes():
				if second is None:
					return first + first
				if type(second) is bytes:
					return first + second
				if type(second) is str:
					return first + second.encode()
				if type(second) is int:
					return first + first * second

	def expression_multiply(first, second):
		pass

	def expression_(first, second):
		pass
	def expression_(first, second):
		pass
	def expression_(first, second):
		pass
	def expression_(first, second):
		pass
	def expression_(first, second):
		pass
	def expression_(first, second):
		pass
	def expression_(first, second):
		pass
	def expression_(first, second):
		pass
	def expression_(first, second):
		pass
	def expression_(first, second):
		pass
	def expression_(first, second):
		pass
	def expression_(first, second):
		pass
	def expression_(first, second):
		pass
	def expression_(first, second):
		pass
	def expression_(first, second):
		pass
	def expression_(first, second):
		pass
	def expression_(first, second):
		pass
	def expression_(first, second):
		pass
	def expression_(first, second):
		pass
	def expression_(first, second):
		pass
	def expression_(first, second):
		pass
	def expression_(first, second):
		pass
	def expression_(first, second):
		pass
	def expression_(first, second):
		pass
	def expression_(first, second):
		pass
	def expression_(first, second):
		pass
	def expression_(first, second):
		pass
	def expression_(first, second):
		pass
	def expression_(first, second):
		pass
	def expression_(first, second):
		pass
	def expression_(first, second):
		pass
	def expression_(first, second):
		pass
	def expression_(first, second):
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
			result = void.void_encode(data, 4)
		print(result, end=end)

	def print_raw(data):
		print(data, end='')

	def action(action):
		doc = void.data['doc']
		alias = void.data['alias']
		variable = {
			'result': None
		}
		result = None
		for action in (action if type(action) is list else [action]):
			if type(action) is not list:
				action = [action]
			elif len(action) == 0:
				continue
			name = action[0]
			name_type = type(name)
			if name_type is str:
				if name in alias:
					name = alias[name]
				if name in doc:
					info = doc[name]
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
							if 'type' in param:
								type_list = param['type'] if type(param['type']) is list else [param['type']]
								for param_type in type_list:
									match param_type:
										case 'text':
											if type(value) is str:
												value = str(value)
												found = True
												break
										case 'number':
											if type(value) in [int, float]:
												try:
													value = float(value)
													if value % 1 == 0:
														value = int(value)
													found = True
													break
												except:
													pass
										case 'int':
											if type(value) is int:
												try:
													value = int(value)
													found = True
													break
												except:
													pass
										case 'float':
											if type(value) is float:
												try:
													value = float(value)
													found = True
													break
												except:
													pass
										case 'bool':
											if type(value) is bool:
												try:
													value = bool(value)
													found = True
													break
												except:
													pass
										case 'list':
											if type(value) is str:
												value = list(void.json_decode(value))
											elif type(value) is not list:
												value = [value]
											found = True
											break
										case 'dict':
											if type(value) is str:
												value_decoded = void.json_decode(value)
												if type(value_decoded) is not dict:
													continue
												else:
													value = value_decoded
											elif type(value) is not dict:
												continue
											found = True
											break
										case 'any':
											found = True
											break
								if not found:
									value = param['default'] if 'default' in param else None
								params[index] = value
							index += 1
						if skip:
							continue
					if 'method' in info and info['method'] != None:
						for index in range(len(params)):
							if type(params[index]) is str:
								if params[index] == '{}':
									params[index] = result
						method = getattr(void, str(info['method']))
						#params.append(variable)
						result = method(*params)
					else:
						pass
				else:
					action = void.get('action.' + name)
					if action != None: 
						result = void.action(action)
			else:
				result = name
		return result

	def open(text: str):
		if text in ['', None]:
			return
		process = subprocess.Popen(text.split(' '))
		return {
			'pid': process.pid
		}

	def close(name, soft: bool = False):
		if type(name) not in [str, int]:
			return False
		if type(name) is int or name.isdigit():
			try:
				os.kill(int(name), signal.SIGTERM if soft else signal.SIGKILL)
				return True
			except ProcessLookupError:
				return False
		else:
			system = platform.system()			
			try:
				match void.get('os.type'):
					case 'windows':
						subprocess.run(['taskkill', '/f' if not soft else '', '/t', '/im', name], check=True)
						return True
					case 'linux' | 'mac':
						subprocess.run(['pkill', name], check=True)
						return True
					case _:
						return False
			except subprocess.CalledProcessError:
				return False
			except FileNotFoundError:
				return False

	def code(text: str):
		exec(text)

	def exit(code = -1):
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
		start = time.time()
		doc = void.data['doc']
		if name in set(action['group'] for action in doc.values()):
			doc = {action_name: action for action_name, action in doc.items() if action['group'] == name}
		else:
			if name in doc:
				doc = {name: doc[name]}
		tested = []
		try:
			for name in doc:
				tested.append(name)
				action = doc[name]
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
					if 'clean' in example:
						void.action(list(example['clean']))
					if 'round' in example:
						if type(result) is dict:
							for name in result:
								result[name] = round(result[name], int(example['round'])) if result != None else None
						elif type(result) is list:
							for index in range(len(result)):
								result[index] = round(result[index], int(example['round'])) if result != None else None
						else:
							result = round(result, int(example['round'])) if result != None else None
					error = False
					if 'length' in example and type(result) in [str, list, dict]:
						error = len(result) != example['length']
					if 'result' in example:
						if result != example['result']:
							error = True					
					if 'type' in example:
						match example['type']:
							case 'text':
								if type(result) is not str:
									error = True
								else:
									if 'range' in example and type(example['range']) in [list, int, float, str]:
										rng = example['range']
										if type(rng) in [int, float, str]:
											if len(result) != int(rng):
												error = True
										elif type(rng) is list:
											if len(rng) > 2:
												range_from = int(rng[0])
												range_to = int(rng[1])
												if len(result) < range_from or len(result) > range_to:
													error = True											
											elif len(rng) == 1:
												if len(result) != int(rng[0]):
													error = True
									if 'symbol' in example:
										if not re.fullmatch('[' + str(example['symbol']) + ']{' + str(len(result)) + '}', result):
											error = True
							case 'number':
								if type(result) not in [int, float]:
									error = True
								else:
									if 'range' in example and type(example['range']) in [list, int, float, str]:
										rng = example['range']
										if type(rng) in [int, float, str]:
											if result != int(rng):
												error = True
										elif type(rng) is list:
											if len(rng) > 2:
												range_from = int(rng[0])
												range_to = int(rng[1])
												if result < range_from or result > range_to:
													error = True											
											elif len(rng) == 1:
												if len(result) != int(rng[0]):
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
								error = True
					if error:
						expected = {}
						if 'result' in example:
							expected['result'] = example['result']
						if 'type' in example:
							expected['type'] = example['type']
						if 'range' in example:
							expected['range'] = example['range']
						if 'symbol' in example:
							expected['symbol'] = example['symbol']
						if len(expected) == 1 and 'result' in expected:
							expected = expected['result']
						elif len(expected) == 0:
							expected = None
						return {
							'test': tested,
							'error': {
								'action': name,
								'example': example['code'],
								'expected': expected,
								'found': result
							}}
		except Exception as e:
			_, message, trace = sys.exc_info()
			last_frame = traceback.extract_tb(trace)[-1]
			return {
				'test': tested,
				'error': {
					'reason': str(e),
					'line': last_frame.lineno,
					'text': last_frame.line
				}
			}
		return {
			'test': tested,
			'time': void.date(time.time() - start, '(second) sec'),
			'result': 'ok'
		}

	def help(name: str = None):
		doc = void.data['doc']
		if name == None:
			return void.data['about']
		elif name == 'all':
			return list(doc.keys())
		elif name == 'full':
			return doc
		elif name in doc:
			return {name: doc[name]}
		else:
			result = []
			for action_name in doc:
				if name in action_name:
					result.append(action_name)
			return result if len(result) > 0 else ''

	def v(name: str, action = None):
		pass

	def os(name: str = None):
		match name:
			case 'mac':
				pass
			case 'language':
				pass
			case 'user':
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

		if name == None:
			return data['os']['type']
		return data['os']['type'] == name

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

	def replace(text: str, search, replace = None):
		if type(search) is str:
			if replace == None:
				return text
			search = {search: str(replace)}
		if type(search) is not dict:
			return text
		result = text
		for name in search:
			if '()' in name:
				part = name.split('()')
				result = re.sub(r'(' + part[0] + ').*?(' + part[1] + ')', r'\1' + str(search[name]) + r'\2', text)
			else:
				result = result.replace(str(name), str(search[name]))
		return result

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

	def date(timestamp: float = None, format: str = ''):
		dt = datetime.now() if timestamp == None else datetime.fromtimestamp(timestamp)
		timestamp = int(dt.timestamp())
		return void.replace(format, {
			'(time)': timestamp,
			'(year)': dt.year,
			'(month)': dt.month,
			'(day)': dt.day,
			'(hour)': dt.hour,
			'(minute)': dt.minute,
			'(second)': dt.second,
			'(millisecond)': dt.microsecond // 1000 - timestamp * 1_000,
			'(microsecond)': dt.microsecond - timestamp * 1_000_000,
			'(nanosecond)': time.time_ns() - timestamp * 1_000_000_000,
			'(weekday)': dt.weekday(),
			'(yearshort)': str(dt.year)[-2:],
			'(monthfull)': str(dt.month).zfill(2),
			'(dayfull)': str(dt.day).zfill(2),
			'(hourfull)': str(dt.hour).zfill(2),
			'(minutefull)': str(dt.minute).zfill(2),
			'(secondfull)': str(dt.second).zfill(2),
			'(seconds)': ''
			})

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

	def golden_ratio(value: float, part: str = None):
		const = 1.61803398874989484820
		if part == 'short':
			return {
				'short': value,
				'long': value * const,
				'total': value * (1 + const)
				}
		elif part == 'long':
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
		print(value)
		if value == None and to == None:
			return random.random()
		if value != None and to != None:
			if type(value) is int and type(to) is int:
				return random.randint(value, to)
			return random.uniform(float(value), float(to))
		if value == None and to != None:
			value = to
			to = None
		if type(value) is bool:
			return random.choice([True, False])
		if type(value) is str:
			return random.choice(value)
		if type(value) is list:
			return random.choice(value)
		if type(value) is dict:
			return random.choice(list(value.values()))
		if value != None and to == None:
			if type(value) is int:
				return random.randint(0, value)
			return random.uniform(0, float(value))

	def random_seed(seed: str = None):
		if seed == None:
			return void.get('app.seed')
		void.set('app.seed', seed)

	def random_reseed():
		seed = void.sha256(str(void.time()) + void.hash(40))
		void.random_seed(seed)

	# time

	def t(name: str = None):
		void.timecheck(name)

	def timecheck(name: str = None):
		pass

	def time(dot: int = 0):
		result = time.time()
		if dot == 0:
			result = int(result)
		elif dot > 0:
			result = round(result, dot)
		else:
			result = round(result * (10 ** -dot))
		return result

	def timer(action, seconds: float = 1, name: str = None):
		pass

	def timer_remove(name: str):
		pass

	def timepast(time: float = None):
		pass

	def wait(seconds: float = 1):
		time.sleep(seconds)

	# crypto

	def encrypt(data, key: str = None):
		pass

	def decrypt(data, key: str):
		pass

	def hash(length: str = 64, symbols: str = None):
		chars = (string.ascii_letters + string.digits) if symbols == None else symbols
		return ''.join(random.choices(chars, k=length))

	def uuid():
		pass

	def md5(value: str):
		return hashlib.md5(value)

	def sha1(value: str):
		pass

	def sha256(value: str):
		return '' + hashlib.sha256(value.encode()).hexdigest()

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
					if type(data) is str:
						void.file_write(path, data)
					elif type(data) in [bytes, bytearray, int, float]:
						data = bytes(data)
						void.file_write(path, data)
					else:
						void.file_write(path, void.void_encode(data))

	def file_exists(path: str):
		return os.path.isfile(path)

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
		try:
			os.remove(path)
		except OSError:
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
		try:
			with open(path, 'rb') as file:
				return hashlib.sha256(file.read()).hexdigest()
		except Exception as e:
			return None

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

	def drive_list():
		result = []
		for drive in psutil.disk_partitions():
			result.append({
				'method': drive[0],
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

	def void_encode(data, indent = '\t', level: int = 0, base64:bool = False, base85:bool = False, gzip:bool = False):
		if type(indent) is int:
			indent = ' ' * indent
		data_binary = {}
		result = void.void_encode_iterate(data, indent, level, base64, base85, gzip, False, data_binary)
		if len(data_binary) > 0:
			result = b'\xef\xbb\xbf' + result.encode()
			for unique in list(data_binary):
				result = result.replace(unique, data_binary[unique])
				del data_binary[unique]
		return result

	def void_encode_iterate(data, indent: str = '\t', level: int = 0, base64: bool = False, base85: bool = False, gzip: bool = False, inlist: bool = False, data_binary: dict = {}):
		prefix = indent * (level if not inlist else level - 1)
		match data:
			case bool():
				return prefix + 'true' if data else prefix + 'false'
			case int() | float():
				return prefix + f'{data:,}'.replace(',', ' ')
			case str():
				if data == '':
					result = '""'
				elif data == '"':
					result = '"'
				elif data == '[':
					result = '"['
				elif data == ' ':
					result = '" "'
				else:
					if data in ['true', 'false', 'none']:
						result = '"' + data
					else:
						escape = '\r' in data or '\n' in data or '\t' in data
						if escape:
							result = data.replace('\\r', '\\\\r').replace('\\n', '\\\\n').replace('\\t', '\\\\t').replace('\r', '\\r').replace('\n', '\\n').replace('\t', '\\t')
						else:
							result = data
						if data[0] == '"' or escape:
							result = '"' + result
							if result[-1] == '"':
								result += '"'
				return prefix + result
			case list():
				if len(data) == 0:
					return prefix + '['
				if inlist:
					result = prefix + '[\n'
				else:
					result = ''
				for value in data:
					result += void.void_encode_iterate(value, indent=indent, level=level+1, base64=base64, base85=base85, gzip=gzip, inlist=True, data_binary=data_binary) + '\n'
				return result.rstrip('\n')
			case dict():
				if len(data) == 0:
					return prefix + '['
				if inlist:
					result = prefix + '[\n'
					prefix += '\t'
				else:
					result = ''
				for name in data:
					value = data[name]
					result += prefix + void.void_encode_iterate(str(name)) + '\n' + void.void_encode_iterate(value, indent=indent, level=level+1, base64=base64, base85=base85, gzip=gzip, data_binary=data_binary) + '\n'
				return result.rstrip('\n')
			case bytes():
				if gzip:
					data = gz.compress(data, mtime=0)
				if base64:
					return f'{prefix}*\n{prefix}\t' + b64.b64encode(data).decode()
				elif base85:
					return f'{prefix}*\n{prefix}\t' + b64.b85encode(data).decode()
				unique = void.hash(64)
				data_binary[unique.encode()] = data
				return f'{prefix}*\n{prefix}\t{len(data)}\n{prefix}\t{unique}'
			case _:
				return prefix + 'none'

	def void_decode(data, gzip:bool = True):
		description = []
		i = 0
		line = b''
		indent = 0

		if type(data) is str:
			data = data.encode()
		elif type(data) is bytes:
			if data.startswith(b'\xef\xbb\xbf'):
				data = data[3:]
		else:
			return
		data += b'\n'
		while i < len(data):
			c = data[i:i+1]
			i += 1
			if c == b'\n':
				indent = 0
				for b in line:
					if b == 9:
						indent += 1
					else:
						break
				value = line[indent:].decode('utf-8').rstrip('\r')
				line = b''
				if value == '*':
					binary_line = b''
					i += indent + 1
					while data[i:i+1] != b'\n':
						binary_line += data[i:i+1]
						i += 1
					i += 1
					binary_line = binary_line.rstrip(b'\r')
					if data[i:i+indent+1] != b'\t' * (indent + 1):
						try:
							if re.fullmatch(r'^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$', binary_line.decode('ascii')):
								value = b64.b64decode(binary_line, validate=True)
							else:
								raise Exception()
						except Exception:
							try:
								value = b64.b85decode(binary_line)
							except Exception:
								value = None
						if gzip and value.startswith(b'\x1f\x8b'):
							value = gz.decompress(value)
						try:
							value = value.decode('utf-8')
						except:
							pass
					else:
						i += indent + 1
						binary_length = int(binary_line.decode())
						value = data[i:i+binary_length]
						i += binary_length
						if gzip and value.startswith(b'\x1f\x8b'):
							value = gz.decompress(value)
				else:
					value = value.strip()
					if len(value) == 0:
						continue
					match value:
						case 'none': value = None
						case 'true': value = True
						case 'false': value = False
						case '[' | '[]': value = []
						case '""' | '': value = ''
						case '"': value = '"'
						case '" "': value = ' '
						case _:
							if value[0] == '"':
								value = value[1:]
								if value.endswith('"'):
									value = value[:-1]
								value = value.replace('\\\\r', '\x01').replace('\\\\n', '\x02').replace('\\\\t', '\x03').replace('\\r', '\r').replace('\\n', '\n').replace('\\t', '\t').replace('\x01', '\\r').replace('\x02', '\\n').replace('\x03', '\\t')
							else:
								number = value.replace(' ', '').replace('_', '')
								try:
									value = int(number)
								except:
									try:
										value = float(number)
									except:
										pass
				description.append((indent, value))
			else:
				line += c

		def parse(description: list, level: int = 0):
			result = None
			index = 0
			while index < len(description):
				indent, value = description[index]
				if indent == level:
					if result == None:
						result = value
					elif type(result) is list:
						result.append(value)
					elif type(result) in [str, int, float, bool]:
						result = [result, value]
					elif type(result) is dict:
						result[str(value)] = None
				elif indent == level + 1:
					if type(result) is list:
						if not result:
							result = parse(description[index:], level + 1)
						else:
							prev = result[-1]
							if type(prev) is list:  
								result[-1] = parse(description[index:], level + 1)
							else:
								result[-1] = {str(result[-1]):parse(description[index:], level + 1)}
						while index < len(description) and description[index][0] > level:
							index += 1
						continue
					elif type(result) in [str, int, float, bool]:
						result = {str(result):parse(description[index:], level + 1)}
						while index < len(description) and description[index][0] > level:
							index += 1
						continue
					elif type(result) is dict:
						key = description[index-1][1]
						result[str(key)] = parse(description[index:], level + 1)
						while index < len(description) and description[index][0] > level:
							index += 1
						continue
				elif indent < level:
					return result
				index += 1
			return result

		return parse(description)

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

	# communication

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

	def cookie(name: str, value = None):
		pass

	def cookie_remove(name: str):
		pass

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
					'method': name,
					'list': protocol
					})
		if hasattr(psutil, 'sensors_temperatures'):
			sensor = psutil.sensors_temperatures()
			if len(sensor) > 0:
				temperature = []
				for sensor in sensor:
					temperature.append({
						'method': sensor[0],
						'current': sensor[1],
						'high': sensor[2],
						'critical': sensor[3]
						})
		if hasattr(psutil, 'sensors_battery'):
			sensor = psutil.sensors_fans()
			for name in sensor:
				fan.append({
					'method': name,
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
				'method': platform.processor(),
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

	def ui_text(renderer: None):
		if renderer == None:
			renderer = void.get('ui.renderer')
		match renderer:
			case 'web':
				pass
			case 'cli':
				pass
			case 'app':
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

	# helper

	def module(name: str):
		if name not in void.modules or void.modules[name] == None:
			void.modules[name] = importlib.import_module(name)
		return void.modules[name]

	# run

	def run():
		void.t('run')
		arguments = sys.argv[1:]
		void.set('app.name', sys.argv[0])
		void.set('app.path', os.getcwd())
		void.set('app.argument', arguments)
		match platform.system():
			case 'Windows':
				void.set('app.type', 'windows')
			case 'Linux':
				void.set('app.type', 'linux')
			case 'Darwin':
				void.set('app.type', 'mac')
			case _:
				void.set('unknown')
		void.set('app.type', arguments)
		void.random_reseed()
		result = None
		if len(arguments) > 0:
			text = arguments[0]
			if text in void.data['doc'] or text in void.data['alias'] or text in void.data['action']:
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
						void.action(action)
					elif type(action) is dict:
						void.data = void.merge(void.data, action)
						if 'run' in void.data and type(void.data['run']) is list:
							void.action(void.data['run'])
		if result not in ['', None]:
			void.print(result)

if __name__ == '__main__':
	void.run()
