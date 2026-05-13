import io
import os
import re
import sys
import time
import math
import signal
import struct
import string
import random
import hashlib
import platform
import datetime
import calendar
import importlib
import threading
import traceback
import subprocess

class VOIDlang:

	data = '''
		about
			type
				code
			name
				V O I D lang
			site
				https://voidsp.com
			language
				python
			version
				time
					1778668374
				date
					2026 · 05 · 13
			license
				name
					V O I D license
				url
					https://github.com/voidspawner/void.lang#v-o-i-d-license
				text
					do what you want · you can use it in both private and open source · embed it in free or paid products · modify · create your own solutions based on it · no need to specify the author
			logo
				'                                          ∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞                                         '
				'                                     ∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞                                     '
				'                                  ∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞                                  '
				'                               ∞∞∞∞∞∞∞∞∞∞∞                ∞∞∞∞∞∞∞∞∞∞                                '
				'                              ∞∞∞∞∞∞∞∞                        ∞∞∞∞∞∞∞∞                              '
				'                            ∞∞∞∞∞∞∞                              ∞∞∞∞∞∞∞                            '
				'                           ∞∞∞∞∞∞                                  ∞∞∞∞∞∞                           '
				'                          ∞∞∞∞∞      ∞∞∞∞∞∞           ∞∞∞∞∞∞        ∞∞∞∞∞∞                          '
				'                         ∞∞∞∞∞      ∞∞∞∞∞∞∞           ∞∞∞∞∞∞∞         ∞∞∞∞∞                         '
				'                        ∞∞∞∞∞       ∞∞∞∞∞∞             ∞∞∞∞∞           ∞∞∞∞∞                        '
				'                       ∞∞∞∞∞∞                                          ∞∞∞∞∞                        '
				'                       ∞∞∞∞∞           ∞∞∞∞∞           ∞∞∞∞             ∞∞∞∞∞                       '
				'                ∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞      ∞∞∞∞∞           ∞∞∞∞       ∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞             '
				'            ∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞                          ∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞          '
				'          ∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞     ∞∞∞    ∞∞∞∞∞      ∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞          '
				'         ∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞     ∞∞∞∞∞∞∞∞∞∞∞∞      ∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞          '
				'          ∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞     ∞∞∞∞∞∞∞∞∞∞∞         ∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞           '
				'            ∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞            ∞∞                  ∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞               '
				'                 ∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞                                    ∞∞∞∞∞∞                        '
				'                         ∞∞∞∞∞                                       ∞∞∞∞∞∞                         '
				'                          ∞∞∞∞∞∞                                    ∞∞∞∞∞∞                          '
				'                           ∞∞∞∞∞∞                                 ∞∞∞∞∞∞∞                           '
				'                            ∞∞∞∞∞∞∞                             ∞∞∞∞∞∞∞∞                            '
				'                              ∞∞∞∞∞∞∞∞                       ∞∞∞∞∞∞∞∞∞                              '
				'                                ∞∞∞∞∞∞∞∞∞∞                ∞∞∞∞∞∞∞∞∞∞                                '
				'                                   ∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞                                   '
				'                                     ∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞                                      '
				'                                          ∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞                                          '
			help
				python.exe void.py help
				python3 void.py help action
		lang

		  .: value :.

			get
				group
					value
				method
					get
					a
					s
				action
					none
				alias
					none
				description
					Retrieve a value based on provided parameter name
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name name  type text  default none
					[name default  type any  default none
				example
					[code [[get about.name]]  result V O I D lang
					[code [[get about.unknown 'not found']]  result not found
					[code [[get void.test.json/about.name]]  before [[file void.test.json [about [name  V O I D lang]  list [0 1 2]] ]]  clear [[file.remove void.test.json]]  result V O I D lang
					[code [[get void.test.json/list.1]]  before [[file void.test.json [about [name  V O I D lang]  list [0 1 2]] ]]  clear [[file.remove void.test.json]]  result 1
					[code [[get db.sqldbname.user]]  type list  test false
					[code [[get db.sqldbname.user.id.12345]]  type [dict none]  test false
					[code [[.about.name]]  result V O I D lang
					[code [[.about.{name}]]  before [[= name name]]  clear [[remove name]]  result V O I D lang
			set
				group
					value
				method
					set
				action
					none
				alias
					none
				description
					Assign a value to a specified parameter
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name name  type text  default none
					[name data  type any  default none
				example
					[code [[set some.value 1]]  after [[get some.value]]  clear [[remove some.value]]  result 1
					[code [[set some.text :)]]  after [[get some.text]]  clear [[remove some.value]]  result :)
					[code [[set void.test.json/about.name 'V O I D']]  before [[file void.test.json [about [name  V O I D lang]  list [0 1 2]] ]]  after [[get void.test.json/about.name]]  clear [[file.remove void.test.json]]  result V O I D
					[code [[set void.test.json/list.1 3]]  before [[file void.test.json [about [name  V O I D lang]  list [0 1 2]] ]]  after [[get void.test.json/list.1]]  clear [[file.remove void.test.json]]  result 3
					[code [[set db.sqldbname.user [id 12345  name Thomas  phone +123456789]]]  test false
					[code [[set db.sqldbname.user.id.12345.phone +1234567890]]  test false
			remove
				group
					value
				method
					remove
				action
					none
				alias
					del
				description
					Remove a specified parameter
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name name  type text  default none
				example
					[code [[remove some.value]]  before [[set some.value 1]]  after [[get some.value]]  result none
					[code [[remove void.test.json/about.name]]  before [[file void.test.json [about [name  V O I D lang]  list [0 1 2]] ]]  after [[get void.test.json/about.name]]  clear [[file.remove void.test.json]]  result none
					[code [remove]  before [123]  after [get]  result none
					[code [[remove db.sqldbname]]  test false
					[code [[remove db.sqldbname.user]]  test false
					[code [[remove db.sqldbname.user.id.12345]]  test false
			type
				group
					value
				method
					type
				action
					none
				alias
					none
				description
					Determine the data type
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name data  type any  default none
				example
					[code [[type text]]  result text
					[code [[type 1]]  result number
					[code [[type 1.2]]  result number
					[code [[type true]]  result bool
					[code [[type false]]  result bool
					[code [[type none]]  result none
					[code [[type [1 2 3]]]  result list
					[code [[type [a 1  b 2]]]  result dict
					[code [[type *1]]  result binary
			text
				group
					value
				method
					type_text
				action
					none
				alias
					none
				description
					Specify a data as a text type
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name data  type any
					[name format  type many  default none
				example
					[code [[text 123]]  result '123
					[code [[text true]]  result 'true
					[code [[text none]]  result 'none
					[code [[text [1 2 3]]]  result '[1 2 3
					[code [[text [a 1  b 2]]]  result '[a 1  b 2
					[code [[text *74657874]]  result text
					[code [[text *7465_7874]]  result text
					[code [[text **01100001]]  result a
					[code [[text **0110_0001]]  result a
					[code [[text ***dGV4dA==]]  result text
					[code [[text ***dGV4dA]]  result text
					[code [[text *a]]  result a
					[code [[text *1]]  result '1
					[code [[text *text]]  result text
					[code [[text *'text text']]  result 'text text
					[code [[text *1*a]]  result a
					[code [[text *4*text]]  result text
					[code [[text title [length 10  align center]]]  result '  title   '
					[code [[text 100000 price]]  result '∞100 000
					[code [[text 100000.1 [before ∞  after monthly  group ,  dot .  round 3]]]  result '∞100,000.100 monthly
					[code [[text .image [size  100]]]  test false
					[code [[text .image [width 100  height 100]]]  test false
					[code [[text text + text]]  result 'text+text
					[code [[text number ' ' 123]]  result 'number 123
					[code [[text *abc '*{}']]  result '*abc
					[code [[text *abc [[+ '*' ..]] ]]  result '*abc
			number
				group
					value
				method
					type_number
				action
					none
				alias
					none
				description
					Specify a data as a number type
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name data  type any  default none
				example
					[code [[number text]]  result 0
					[code [[number '123']]  result 123
					[code [[number '45.67']]  result 45.67
					[code [[number true]]  result 1
					[code [[number false]]  result 0
					[code [[number none]]  result 0
					[code [[number []]]  result 0
					[code [[number [text]]]  result 1
					[code [[number [a 1  b 2]]]  result 2
					[code [[number *1]]  result 1
			bool
				group
					value
				method
					type_bool
				action
					none
				alias
					none
				description
					Specify a data as a boolean type
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name data  type any  default none
				example
					[code [[bool text]]  result true
					[code [[bool '0']]  result true
					[code [[bool '']]  result false
					[code [[bool 1]]  result true
					[code [[bool 0]]  result false
					[code [[bool false]]  result false
					[code [[bool none]]  result false
					[code [[bool [0]]]  result true
					[code [[bool []]]  result false
					[code [[bool [a  0]]]  result true
					[code [[bool [ ]]]  result false
					[code [[bool *0]]  result true
					[code [[bool *'']]  result false
			binary
				group
					value
				method
					type_binary
				action
					none
				alias
					none
				description
					Specify a data as a binary type
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name data  type any  default none
				example
					[code [[binary text]]  result *text
					[code [[binary 123]]  result *7B
					[code [[binary true]]  result *01
					[code [[binary none]]  result *00
					[code [[binary [1 2 3]]]  result *'[1 2 3
					[code [[binary [a 1  b 2]]]  result *'[a 1  b 2
					[code [[binary *a]]  result *a
			length
				group
					value
				method
					length
				action
					none
				alias
					~
					len
					mem
				description
					Gets the length of the data
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name data  type any  default none
				example
					[code [[~ text]]  result 4
					[code [[~ [1 2 a]]]  result 3
					[code [[~ [a 1  b 2]]]  result 2
					[code [[~ 123]]  result 1
					[code [[~ -123]]  result 1
					[code [[~ 12345678]]  result 3
					[code [[~ 123.1]]  result 8
					[code [[~ *'123']]  result 3

		  .: expression :.

			+
				group
					expression
				method
					expression_plus
				action
					none
				alias
					and
				description
					Perform addition or AND operation
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name value  type many  default none
				example
					[code [[+ 2 3]]  result 5
					[code [[+ 1 2 3]]  result 6
					[code [2 [+ 3]]  result 5
					[code [2 + 3]  result 5
					[code [[+ text ' ' text]]  result 'text text
					[code [text + ' ' + text]  result 'text text
					[code [text + 1]  result 'text1
					[code [[+ [1 2] [a b]]]  result [1 2 a b
					[code [[1 2 3] + 4]  result [1 2 3 4
					[code [[+ true true]]  result true
					[code [[+ true false]]  result false
					[code [[+ false true]]  result false
					[code [[+ false false]]  result false
					[code [[+ [a 1  b [c 2]] [b [c 3]]]] result [a 1  b [c 3
					[code [[+ *a *b]]  result *'ab
					[code [[+ *a 1]]  result *'a1
			-
				group
					expression
				method
					expression_minus
				action
					none
				alias
					not
				description
					Perform subtraction or NOT operation
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name value  type many  default none
				example
					[code [[- 5 2]]  result 3
					[code [5 - 2 - 1]  result 2
					[code [[- 10]]  result -10
					[code [text - 2]  result te
					[code [file.void - .void]]  result file
					[code [[- true]]  result false
					[code [[- false]]  result true
					[code [[- [1 2 3] 1]]  result [1 2]
					[code [[- [1 2 3] [1 3]]]  result [2]
					[code [[- [a 1  b 2] a]]  result [b 2]
					[code [[- *text 2]]  result *te
					[code [[- *text *xt]]  result *te
			*
				group
					expression
				method
					expression_multiply
				action
					none
				alias
					xor
				description
					Perform multiplication or XOR operation
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name value  type many  default none
				example
					[code [[* 3 4]]  result 12
					[code [2 * 3 * 4]  result 24
					[code [true * true]  result false
					[code [true * false]  result true
					[code [false * true]  result true
					[code [false * false]  result false
					[code [text * 2]  result texttext
					[code [text * ' ']  result t e x t
					[code [[1 2 3] * 2]  result [[1 2 3] [1 2 3
					[code [[a 1  b 2] * 2]  result [[a 1  b 2] [a 1  b 2
					[code [[text text] * ' ']  result 'text text
					[code [*a * 2]  result *'aa
			/
				group
					expression
				method
					expression_divide
				action
					none
				alias
					or
				description
					Perform division or OR operation
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name value  type many  default none
				example
					[code [[/ 10 2]]  result 5
					[code [[/ 7 2]]  result 3.5
					[code [20 / 10 / 2]  result 1
					[code [true / true]  result true
					[code [true / false]  result true
					[code [false / true]  result true
					[code [false / false]  result false
					[code [[/ [1 2 3 4] 2]]  result [[1 2] [3 4
					[code [[/ [a 1  b 2  c 3  d 4] 2]]  result [[a 1  b 2] [c 3  d 4
					[code [text / 2]  result [te xt
					[code ['text text' / ' ']  result [text text]
					[code [*text / 2]  result [*te *xt
			%
				group
					expression
				method
					expression_modulo
				action
					none
				alias
					mod
				description
					Perform modulo operation
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name value  type [int many]  default none
				example
					[code [[% 10 3]]  result 1
					[code [15 % 4]  result 3
			^
				group
					expression
				method
					expression_power
				action
					none
				alias
					pow
				description
					Perform power operator
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name value  type many  default none
				example
					[code [[^ 2 3]]  result 8
					[code [[^ 10 0]]  result 1
					[code [[^ 4 0.5]]  result 2
					[code [2 ^ 3 ^ 2]  result 64
			>>
				group
					expression
				method
					expression_shr
				action
					none
				alias
					shr
				description
					Perform right shift operation
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name value  type many  default none
				example
					[code [[>> 16 2]]  result 4
					[code [[>> 255 4]]  result 15
					[code [[>> true]]  result false
					[code [[>> false]]  result false
					[code [[1 2 3] >> 2]  result [1
					[code [[a 1  b 2] >> 1]  result [a  1]
					[code [text >> 2]  result te
					[code [*text >> 2]  result *te
			<<
				group
					expression
				method
					expression_shl
				action
					none
				alias
					shl
				description
					Perform left shift operation
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name value  type many  default none
				example
					[code [[<< 4 2]]  result 16
					[code [[<< 7 3]]  result 56
					[code [[<< true]]  result false
					[code [[<< [1 2]]]  result [1 2 ''
					[code [[<< [a 1  b 2]]]  result [a 1  b 2
					[code [text << 2]  result 'text  '
					[code [*text << 2]  result *'text  '
			x=
				group
					expression
				method
					expression_notequal
				action
					none
				alias
					!=
				description
					Checks if values are not equal
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name value  type many  default none
				example
					[code [[!= 5 3]]  result true
					[code [[!= a a]]  result false
					[code [a != b]  result true
					[code [true != false]  result true
					[code [[1 2] != [1 2]]  result false
					[code [[a 1  b 2] != [a 1  b 2]]  result false
					[code [text != text]  result false
					[code [*text != *text]  result false
			>
				group
					expression
				method
					expression_greater
				action
					none
				alias
					none
				description
					Checks if left value is greater than right
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name value  type many  default none
				example
					[code [[> 5 3]]  result true
					[code [2 > 4]  result false
					[code [a > b]  return false
					[code [text > tex]  return true
					[code [[1 2 3] > [1 2]]  return true
					[code [*text > *tex]  return true
			<
				group
					expression
				method
					expression_less
				action
					none
				alias
					none
				description
					Checks if left value is less than right
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name value  type many  default none
				example
					[code [[< 5 3]]  result false
					[code [2 < 4]  result true
					[code [a < b]  return true
					[code [text < tex]  return false
					[code [[1 2 3] < [1 2]]  return false
					[code [*text < *tex]  return false
			>=
				group
					expression
				method
					expression_greater_equal
				action
					none
				alias
					none
				description
					Checks if left value is greater than or equal to right
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name value  type many  default none
				example
					[code [[>= 5 3]]  result true
					[code [5 >= 5]  result true
			<=
				group
					expression
				method
					expression_less_equal
				action
					none
				alias
					none
				description
					Checks if left value is less than or equal to right
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name value  type many  default none
				example
					[code [[<= 5 3]]  result false
					[code [5 <= 5]  result true
			->
				group
					expression
				method
					expression_in
				action
					none
				alias
					in
				description
					Checks if value is in a list, subtext in a text or name in a dictionary
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name value  type any
					[name data  type [text list dict
				example
					[code [[-> te text]]  result true
					[code [[-> a [a b c]]]  result true
					[code [[-> a [a 1  b 2]]]  result true
					[code [a -> [a b c]]  result true
					[code [d -> [a b c]]  result false
			x>
				group
					expression
				method
					expression_notin
				action
					none
				alias
					notin
				description
					Checks if value is not in a list, subtext in a text or name not in a dictionary
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name value  type any
					[name data  type [text list dict
				example
					[code [[x> te text]]  result false
					[code [[x> a [a b c]]]  result false
					[code [[x> a [a 1  b 2]]]  result false
					[code [a x> [a b c]]  result false
					[code [d x> [a b c]]  result true
			<-
				group
					expression
				method
					expression_is
				action
					none
				alias
					is
				description
					Checks if value matches a type or one of types
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name data  type any
					[name type  type [text none list
				example
					[code [[<- name text]]  result true
					[code [[<- name number]]  result false
					[code [[<- 123 number]]  result true
					[code [[<- true bool]]  result true
					[code [[<- none none]]  result true
					[code [[<- [1 2] list]]  result true
					[code [[<- [a 1  b 2] dict]]  result true
					[code [[<- name [text dict]]]  result true
					[code [[<- *text binary]]  result true
					[code [123 <- number]  result true
					[code ['123' <- text.number]  result true
			<x
				group
					expression
				method
					expression_isnot
				action
					none
				alias
					isnot
				description
					Checks if value does not match a type or types
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name data  type any
					[name type  type [text none list
				example
					[code [[<x name text]]  result false
					[code [[<x name number]]  result true
					[code [[<x 123 number]]  result false
					[code [[<x true bool]]  result false
					[code [[<x none none]]  result false
					[code [[<x [1 2] list]]  result false
					[code [[<x [a 1  b 2] dict]]  result false
					[code [[<x name [text dict]]]  result false
					[code [[<x *text binary]]  result false
					[code [123 <x number]  result false
					[code ['123' <x text.number]  result false
			=
				group
					expression
				method
					expression_assign
				action
					none
				alias
					==
				description
					Assign value or expression to a parameter or checks if values are equal
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name name  type any
					[name data  type any
				example
					[code [[= x 10] .x]  result 10
					[code [[= name text] .name]  result text
					[code [[= name.subname text] .name.subname]  result text
					[code [[= '' text] .]  result text
					[code [[= none text] .]  result text
					[code [[= x 10] .x = 10]  result true
					[code [20 = 10]  result false
					[code [[= 20 10]]  result false
			+=
				group
					expression
				method
					expression_plus_assign
				action
					none
				alias
					none
				description
					Add and assign value to a parameter
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name name  type text
					[name data  type any  default 1
				example
					[code [[= x 10] [+= x] .x]  result 11
					[code [[= x 10] [+= x 2] .x]  result 12
					[code [[= name text] [+= name] .name]  result 'text '
					[code [[= name text] [+= name 2] .name]  result 'text  '
					[code [[= name text] [+= name end] .name]  result textend
					[code [[= data [1 2 3]] [+= data 2] .data]  result [1 2 3 '' ''
					[code [[= data [a 1  b 2]] [+= data [c  3]] .data]  result [a 1  b 2  c 3
					[code [[= name *text] [+= name end] .name]  result *textend
			=+
				group
					expression
				method
					expression_assign_plus
				action
					none
				alias
					none
				description
					Add to the beginning and assign value to a parameter
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name name  type text
					[name data  type any  default 1
				example
					[code [[= x 10] [=+ x]]  name x  result 11
					[code [[= x 10] [=+ x 2]]  name x  result 12
					[code [[= name text] [=+ name]]  name name  result ' text
					[code [[= name text] [=+ name 2]]  name name  result '  text
					[code [[= name text] [=+ name start]]  name name  result starttext
					[code [[= data [1 2 3]] [=+ data 2]]  name data  result ['' '' 1 2 3
					[code [[= data [a 1  b 2]] [=+ data [c  3]]]  name data  result [c 3  a 1  b 2
					[code [[= name *text] [+= name start]]  name name  result *starttext
			-=
				group
					expression
				method
					expression_minus_assign
				action
					none
				alias
					none
				description
					Subtract and assign value to a parameter
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name name  type text
					[name data  type any  default 1
				example
					[code [[= x 10] [-= x]]  name x  result 9
					[code [[= x 10] [-= x 2]]  name x  result 8
					[code [[= name text] [-= name]]  name name  result tex
					[code [[= name text] [-= name 2]]  name name  result te
					[code [[= name text] [-= name xt]]  name name  result te
					[code [[= data [1 2 3]] [-= data 2]]  name data  result [1 2
					[code [[= data [a 1  b 2]] [-= data b]]  name data  result [a 1
					[code [[= name *text] [-= name xt]]  name name  result *te
			=-
				group
					expression
				method
					expression_assign_minus
				action
					none
				alias
					none
				description
					Subtract from the beginning and assign value to a parameter
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name name  type text
					[name data  type any   default 1
				example
					[code [[= x 10] [=- x]]  name x  result 9
					[code [[= x 10] [=- x 2]]  name x  result 8
					[code [[= name text] [=- name]]  name name  result ext
					[code [[= name text] [=- name 2]]  name name  result xt
					[code [[= name text] [=- name te]]  name name  result xt
					[code [[= data [1 2 3]] [=- data 2]]  name data  result [1
					[code [[= data [a 1  b 2]] [=- data b]]  name data  result [a 1
					[code [[= name *text] [=- name te]]  name name  result *xt
			*=
				group
					expression
				method
					expression_multiply_assign
				action
					none
				alias
					none
				description
					Multiply and assign value to a parameter
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name name  type text
					[name data  type any  default none
				example
					[code [[= x 10] [*= x]]  name x  result 100
					[code [[= x 10] [*= x 2]]  name x  result 20
					[code [[= name text] [*= name 2]]  name name  result texttext
					[code [[= name text] [*= name ' ']]  name name  result t e x t
					[code [[= data [1 2 3]] [*= data 2]]  name data  result [[1 2 3] [1 2 3
					[code [[= data [a 1  b 2]] [*= data 2]]  name data  result [[a 1  b 2] [a 1  b 2
					[code [[= name *text] [*= name ' ']]  name name  result *'t e x t
			/=
				group
					expression
				method
					expression_divide_assign
				action
					none
				alias
					none
				description
					Divide and assign value to a parameter
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name name  type text
					[name data  type any  default none
				example
					[code [[= x 100] [/= x] .x]  result 10
					[code [[= x 10] [/= x 2] .x]  result 5
					[code [[= name text] [/= name 2] .name]  result [te xt
					[code [[= name 'text text'] [/= name ' '] .name]  result [text text
					[code [[= data [1 2 3 4]] [/= data 2] .data]  result [[1 2] [3 4
					[code [[= data [a 1  b 2]] [/= data 2 .data]  result [[a  1] [b  2
					[code [[= name *text] [/= name 2] .name]  result [*te *xt
			%=
				group
					expression
				method
					expression_modulo_assign
				action
					none
				alias
					none
				description
					Modulo and assign value to a parameter
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name name  type text
					[name data  type any  default 2
				example
					[code [[= x 4] [%= x] .x]  result 0
					[code [[= x 10] [%= x 3] .x]  result 1
			^=
				group
					expression
				method
					expression_power_assign
				action
					none
				alias
					none
				description
					Power and assign value to a parameter
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name name  type text
					[name data  type any  default 2
				example
					[code [[= x 10] [^= x] .x]  result 100
					[code [[= x 2] [^= x 3] .x]  result 8
			>>=
				group
					expression
				method
					expression_shr_assign
				action
					none
				alias
					none
				description
					Right shift and assign value to a parameter
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name name  type text
					[name count  type number  default 1
				example
					[code [[= x 16] [>>= x 2] .x]  result 4
					[code [[= x 255] [>>= x 4] .x]  result 15
					[code [[= data [1 2 3]] [>>= data 2] .data]  result [1
					[code [[= data [a 1  b 2]] [>>= data 1] .data]  result [a  1]
					[code [[= name text] [>>= name 2] .name]  result te
					[code [[= name *text] [>>= name 2] .name]  result *te
			<<=
				group
					expression
				method
					expression_shl_assign
				action
					none
				alias
					none
				description
					Left shift and assign value to a parameter
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name name  type text
					[name count  type number  default 1
				example
					[code [[= x 4] [<<= x 2] .x]  result 16
					[code [[= x 7] [<<= x 3] .x]  result 56
					[code [[= data [1 2]] [<<= data 1] .data]  result [1 2 ''
					[code [[= name text] [<<= name 2] .name]  result 'text  '
					[code [[= name *text] [<<= name 2] .name]  result *'text  '

		  .: control :.

			.
				group
					control
				method
					print
				action
					none
				alias
					..
					print
				description
					Output data to the console
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name data  type many
				example
					[code [[. Hi! World]]  output 'Hi! World\n
					[code [[. text text text]]  output 'text text text\n
					[code [[. text none]]  output text
					[code [[. 42]]  output '42\n
					[code [[. [1 2 3]]]  output '[1 2 3\n
					[code [[. [a 1  b 2]]]  output '[a 1  b 2\n
					[code [[. *text]]  output 'text\n
			...
				group
					control
				method
					input
				action
					none
				alias
					input
				description
					Input text from the user
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name text  type text  default none
				example
					[code [..]  input void  result void
					[code [[.. 'Enter name: ']]  input void  result void
			?
				group
					control
				method
					control_if
				action
					none
				alias
					if
				description
					Evaluate a conditional expression
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[]
				example
					[code [[? 1 > 2]]  result false
					[code [[? a # [a b c]]]  result true
					[code [[? a # [a b c]]]  result true
			o
				group
					control
				method
					control_loop
				action
					none
				alias
					loop
				description
					Perform a loop operation
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name data  type any  default none
					[name action  type [text list]  default []
				example
					[code [0 [o 10 [+ 1]]]  result 10
					[code [0 [o [1 5] [+ 1]]]  result 5
					[code [0 [o [1 2 3] [+ .index]]]  result 6
					[code [data = [1 2 3] [o .data [+ .index]]]  result 6
					[code [0 [o [a 1  b 2  c 3] [+ .value]]]  result 6
					[code ['' [o [a 1  b 2  c 3] [+ .name]]]  result abc
					[code ['' [o text [+ ' ' + .value]]]  result ' t e x t
					[code [[o [[. infinite]]]]  test false
					[code [[o [fps 60] [[. 60 fps]]]]  test false
			x
				group
					control
				method
					control_break
				action
					none
				alias
					break
				description
					Exit the current loop or action
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name count  type number  default 1
				example
					[code [0 [o 10 [[? [.index > 2] x] [+ 1] ]]]  result 3
					[code [0 [o 10 [[o 10 [[? [.index > 2] [x 2]] [+ 1] ]]] ]]  result 3
			~>
				group
					control
				method
					control_continue
				action
					none
				alias
					continue
				description
					Skip to the next iteration of the loop
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name count  type number  default 1
				example
					[code [0 [o 10 [+ 1 ~>]]]  result 1
					[code [0 [o 10 [[? [.index % 2] ~>] [+ 1]] ]]  result 5
					[code [0 [o 10 [[? [.index = 2] [[~> 2]]] [+ 1]] ]]  result 8
			<~
				group
					control
				method
					control_repeat
				action
					none
				alias
					repeat
				description
					Repeat the current iteration of the loop
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name count  type number  default 1
				example
					[code [0 [o 10 [+ 1 <~]] ]  result 11
					[code [0 [o 10 [+ 1 [<~ 2]]] ]  result 12
			_
				group
					control
				method
					control_return
				action
					none
				alias
					__
					return
					response
				description
					Return a result from an action
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name data  type any  default none
				example
					[code [[action [1 + 1]]]  result 2
					[code [[action [1 + 1 _ + 1]]]  result none
					[code [[action [1 + 1 [_ ..] + 1]]]  result 2
					[code [[action [1 + 1 __ + 1]]]  result 2
					[code [[action [1 + 1 [_ 4] + 1]]]  result 4
			action
				group
					control
				method
					action
				action
					none
				alias
					none
				description
					Call or initiate an action
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name action  type [text list
					[name data  type [text list
				example
					[code [[action [[upper text]]]]  result TEXT
					[code [[action to_upper [[upper text] __]]]  result none
					[code [[action [to_upper]]]  test false
					[code [[action to_upper]]  test false
			open
				group
					control
				method
					open
				action
					none
				alias
					none
				description
					Open a link in standard way or execute shell command or get a list of open applications
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name name	type text  default none
				example
					[code [open]  test false
					[code [[open https://voidsp.com]]  test false
					[code [[open tol@voidsp.com]]]  test false
					[code [[open +123456789]]]  test false
					[code [[open /path]]]  test false
					[code [[open /path/app]]]  test false
					[code [[open /path/void [file.copy /path_from/file /path_to]]]  test false
					[code [[open pip3 [install voidlang]]]  test false
					[code [[open /path/ffmpeg [i file.mov  an none  none file.mp4]]]  test false
			close
				group
					control
				method
					close
				action
					none
				alias
					none
				description
					Close an application by name or PID
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name name  type [text number list]  default none
				example
					[code [[close App Name]]  test false
					[code [[close 31337]]  test false
					[code [[close [31337 1337]]]  test false
					[code [close]  test false
			code
				group
					control
				method
					code
				action
					none
				alias
					none
				description
					Execute a block of native code
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name code  type text
					[name language  type text  subname true  default none
				example
					[code [[code 'print("Hi! World")']]  test false
					[code [[code print("Hi! World")]]  test false
					[code [[code 'console.log("Hi! World")']]  test false
					[code [[code.js 'console.log("Hi! World")']]  test false
					[code [[code.c++ 'int i = 10; std::cout << i << std::endl;']]  test false
			logger
				group
					control
				method
					logs
				action
					none
				alias
					l
					debug
					warning
					error
				description
					Log information
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name tag  subname true  type any
					[name message  type any  default none
					[name data  type any  default none
				example
					[code [l]  test false
					[code [[l message]]  test false
					[code [[l [time .time  message .message  data .data]]]  test false
					[code [[l.tag info]]  test false
					[code [[l.i.tag info]]  test false
					[code [[l.d.tag debug]]  test false
					[code [[l.w.tag warning]  test false
					[code [[l.e.tag error]  test false
					[code [[l.f.tag fatal]  test false
					[code [[l.info.tag info]  test false
					[code [[l.debug.tag debug]  test false
					[code [[l.warning.tag warning]  test false
					[code [[l.error.tag error]  test false
					[code [[l.fatal.tag fatal]  test false
					[code [[logger tag message]]  test false
					[code [[debug tag message]]  test false
					[code [[warning tag message]]  test false
					[code [[error tag message]]  test false
			test
				group
					control
				method
					test
				action
					test
				alias
					none
				description
					Test one, group or all actions
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name name  type [text many]  default none
				example
					[code [test]  test false
					[code [[test math]]  test false
					[code [[test upper]]  test false
					[code [[test upper lower replace]]  test false
			update
				group
					control
				method
					update
				action
					update
				alias
					none
				description
					Update all code or only the specified action
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name version  type [text number list]  default none
				example
					[code [update]  test false
					[code [update 2026.01.01]  test false
					[code [update 1777211505]  test false
					[code [update encode]  test false
					[code [update [encode decode lz4]]  test false
					[code [update new.action]  test false
			exit
				group
					control
				method
					exit
				action
					none
				alias
					fatal
					xx
				description
					Exit the current application with an exit code
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name message  type many  default none
				example
					[code [exit]  test false
					[code [xx]  test false
					[code [[xx 500]]  test false
					[code [[xx 500 something went wrong]]  test false
					[code [[xx something went wrong]]  test false
					[code [[xx something went wrong 500]]  test false
			os
				group
					control
				method
					os
				action
					none
				alias
					none
				description
					Running the operating system shell
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name shell  type text  subname true  default none
				example
					[code [os]  test false
					[code [[os panels]]  test false
					[code [os.panels]  test false
			info
				group
					control
				method
					info
				action
					info
				alias
					i
					help
					h
				description
					Get info about V O I D lang, os, device, file, directory, drive, url, text, image, video, sound, model, thesaurus or other data
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name name  type text  default none
				example
					[code [info]  type dict
					[code [[info file.jpg]]  type dict  test false
					[code [[info file.txt]]  type dict  test false
					[code [[info /path]]  type dict  test false
					[code [[info c:]]  type dict  test false
					[code [[info https://voidsp.com]]  type dict  test false
					[code [[info .text]]  type dict  test false
					[code [[info .image]]  type dict  test false
					[code [[info laptop]]  type dict  test false
					[code [[info australia]]  type dict  test false
					[code [[info jpy]]  type dict  test false
					[code [[info nvda]]  type dict  test false
			convert
				group
					control
				method
					convert
				action
					convert
				alias
					c
					<>
				description
					Convert data from one format to another
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name from  type text  subname true  default none
					[name to  type text  subname true  default none
					[name data  type any
					[name param  type any  default none
				example
					[code [[convert json [x 10]]]  result '{"x": 10}
					[code [[convert yaml [x 10]]]  result 'x: 10\n
					[code [[convert usd eur 1000]]  test false
					[code [[convert.usd.eur 1000]]  test false
					[code [[convert.inr 1000]]  test false
					[code [[convert AA]]  result 170
					[code [[convert.dec AA]]  result 170
					[code [[convert.hex.dec AA]]  result 170
					[code [[convert.ascii text]]  result *text
					[code [[convert image.jpg image.webp]]  test false
					[code [[convert image.jpg image.webp lossless]]  test false
					[code [[convert image.webp image.jpg 0.9]]  test false
					[code [[convert image.webp image.jpg 90%]]  test false
					[code [[convert video.mov video.mp4]]  test false
					[code [[convert video.webm video.mp4 nosound]]  test false
					[code [[convert video.webm video.mp4 [sound false  quality 70%]]]  test false
					[code [[convert data.json data.void]]  test false
					[code [[convert game.void game.exe]]  test false
					[code [[convert video.mp4 video(frame).png]]  test false
					[code [[convert video(frame).png video.mp4 [fps 60  width 1920  height 1080]]]  test false
			clipboard
				group
					control
				method
					clipboard
				action
					none
				alias
					none
				description
					Storing or retrieving clipboard temporary data
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name name  type many  default none
				example
					[code [[clipboard copied text] clipboard]]  clean [[clipboard '']]  result copied text
					[code [[clipboard 123] clipboard]]  clean [[clipboard '']]  result 123
			sql
				group
					control
				method
					sql
				action
					none
				alias
					none
				description
					Execute an SQL query
				safe
					false
				container
					connect
						[ ]
					disconnect
						[ ]
					use
						[ ]
					transaction
						[ ]
					commit
						[ ]
					rollback
						[ ]
					select
						[ ]
					create
						[ ]
					insert
						[ ]
					update
						[ ]
					delete
						[ ]
					view
						[ ]
					function
						[ ]
					index
						[ ]
					fetch
						[ ]
					all
						[ ]
					cursor
						[ ]
				language
					[python js swift kotlin gdscript c++
				param
					[[name param  type many  subname true
				example
					[code [[sql connect server database login password]]  test false
					[code [[sql [[connect server database login password]] ]]  test false
					[code [[sql.servername disconnect]]  test false
					[code [sql.servername.disconnect]  test false
					[code [[sql use db]]  test false
					[code [[sql SELECT * FROM user]]  test false
					[code [[sql 'INSERT INTO log VALUES ({1},{2})' [{date} {message}]]  test false
					[code [[sql.servername SELECT * FROM notification]]  test false
			chat
				group
					control
				method
					chat
				action
					none
				alias
					:
					ai
				description
					AI conversation and interaction through text or control a virtual or physical bot
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++
				param
					[name data  type any  subname true  default none
				example
					[code [chat]  test false
					[code [chat.Muryashka]  test false
					[code [chat.Murya]  test false
					[code [[chat.character.Kitty a cat who loves to play games often says "meow"]]  test false
					[code [chat.Kitty]  test false
					[code [[chat.Kitty Hello Kitty]]  test false
					[code [chat.gpt]  test false
					[code [chat.gpt.pro]  test false
					[code [chat.pro]  test false
					[code [[chat radius of the Earth]]  test false
					[code [[chat.gpt radius of the Earth]]  test false
					[code [[chat.pro radius of the Earth]]  test false
					[code [[: tell me a story]]  test false
					[code [[: translate to portuguese: Hi World :D]]  test false
					[code [[: svg ginger cat in a box]]  test false
					[code [[: python calculator application]]  test false
					[code [[: image dancing cats]]  test false
					[code [chat.deepseek]  test false
					[code [chat.reasoner]  test false
					[code [chat.v3]  test false
					[code [chat.r1]  test false
					[code [[chat.deepseek radius of the Earth]]  test false
					[code [chat.ollama]  test false
					[code [[chat.ollama radius of the Earth]]  test false
					[code [chat.gemini]  test false
					[code [[chat.gemini radius of the Earth]]  test false
					[code [chat.claude]  test false
					[code [chat.claude.opus]  test false
					[code [chat.claude.sonnet]  test false
					[code [chat.claude.haiku]  test false
					[code [chat.opus]  test false
					[code [chat.sonnet]  test false
					[code [chat.haiku]  test false
					[code [[chat.claude radius of the Earth]]  test false
					[code [chat.bot.go.forward]  test false
					[code [[chat.bot.go [latitude .latitude  longitude .longitude]]]  test false
					[code [chat.bot.stop]  test false
					[code [[chat.bot.take pencil]]  test false
					[code [[chat.bot.put pencil on the table]]  test false
					[code [[chat Murya take a pencil from the table]]  test false
					[code [[chat.Murya put the pencil on the table]]  test false
					[code [[chat.Murya go to the store and buy some milk]]  test false
			say
				group
					control
				method
					say
				action
					none
				alias
					none
				description
					Text voicing with different voices
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name text  type many
					[name language  type text  subname true
				example
					[code [[say Hi! World]]  test false
					[code ['Hi! World' say]  test false
					[code [[say.en Hi! World]]  test false
					[code [[say 'Hi! World' en-us]]  test false
					[code [[say 'Hi! World' file.mp3]]  test false
			recognize
				group
					control
				method
					recognize
				action
					none
				alias
					none
				description
					Convert voice, image or video to text
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++
				param
					[[name file  type text  default none
				example
					[code [recognize]  test false
					[code [[recognize voice.mp3]]  test false
					[code [[recognize cat.jpg]]  test false
			ui
				group
					control
				method
					ui
				action
					none
				alias
					none
				description
					Create a user interface
				safe
					true
				container
					title
						[ ]
					icon
						[ ]
					meta
						[ ]
					size
						[ ]
					border
						[ ]
					bg
						[ ]
					menu
						[ ]
					ontop
						[ ]
					show
						[ ]
					hide
						[ ]
					maximize
						[ ]
					minimize
						[ ]
					fullscreen
						[ ]
					window
						[ ]
					close
						[ ]
					position
						[ ]
					center
						[ ]
					panel
						[ ]
					text
						[ ]
					button
						[ ]
					check
						[ ]
					select
						[ ]
					slider
						[ ]
					progress
						[ ]
					crop
						[ ]
					tile
						[ ]
					list
						[ ]
					chart
						[ ]
					gallery
						[ ]
					ok
						[ ]
					dialog
						example
							[code [[dialog.file]]  test false
							[code [[dialog.date]]  test false
							[code [[dialog.color]]  test false
							[code [[dialog.text]]  test false
							[code [[dialog.select]]  test false
					web
						[ ]
					map
						[ ]
					draw
						[ ]
					image
						[ ]
					video
						[ ]
					sound
						[ ]
					file
						[ ]
					date
						[ ]
					color
						[ ]
					drop
						[ ]
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name param  type many  subname true
				example
					[code [[ui title 'App name']]  test false
					[code [[ui title App name]]  test false
					[code [[ui size 400 200]]  test false
					[code [[ui size [400 200]]]  test false
					[code [ui.center]  test false
					[code [ui.button [title OK  action [exit]]]  test false
					[code [ui.button OK [exit]]  test false
					[code [ui ['press button' [button OK [exit]]]  test false

		  .: text :.

			lower
				group
					text
				method
					lower
				action
					none
				alias
					none
				description
					Convert text to lowercase
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name text  type text
				example
					[[code [[lower TeXt]]  result text
			upper
				group
					text
				method
					upper
				action
					none
				alias
					none
				description
					Convert text to uppercase
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name text  type text
				example
					[[code [[upper text]]  result TEXT
			starts
				group
					text
				method
					starts
				action
					none
				alias
					none
				description
					Check if text starts with a specific substring
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name text  type text
					[name subtext  type text
				example
					[code [[starts 'Hi! World' Hi]]  result true
					[code [[starts 'Hi! World' World]]  result false
			ends
				group
					text
				method
					ends
				action
					none
				alias
					none
				description
					Check if text ends with a specific substring
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name text  type text
					[name subtext  type text
				example
					[code [[ends 'Hi! World' World]]  result true
					[code [[ends 'Hi! World' Hi]]  result false
			strip
				group
					text
				method
					strip
				action
					none
				alias
					none
				description
					Remove leading and trailing characters from text
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name text  type text
					[name subtext  type text  default [' ' '\r' '\n' '\t'
				example
					[code [[strip '\ttext\n']]  result text
					[code [[strip '- text -' '- ']]  result 'text -'
					[code [[strip '- text -' [- ' ']]]  result text
			strip.start
				group
					text
				method
					strip_start
				action
					none
				alias
					none
				description
					Remove leading characters from text
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name text  type text
					[name subtext  type text  default [' ' '\r' '\n' '\t'
				example
					[code [[strip.start '\ttext\n']]  result 'text\n'
					[code [[strip.start '- text -' '- ']]  result 'text -'
					[code [[strip.start '- text -' [- ' ']]]  result 'text -'
			strip.end
				group
					text
				method
					strip_end
				action
					none
				alias
					none
				description
					Remove trailing characters from text
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name text  type text
					[name subtext  type text  default [' ' '\r' '\n' '\t'
				example
					[code [[strip.end '\ttext\n']]  result '\ttext'
					[code [[strip.end '- text -' ' -']]  result '- text'
					[code [[strip.end '- text -' [- ' ']]]  result '- text'
			replace
				group
					text
				method
					replace
				action
					none
				alias
					none
				description
					Replace occurrences of a substring within text
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name text  type text
					[name search  type [text dict]
					[name replace  type [text dict]
				example
					[code [[replace 'Hi! World' World There]]  result 'Hi! There'
					[code [[replace aabbcc b x]]  result aaxxcc
					[code [[replace aabbcc [a x  b y  c z]]]  result xxyyzz
			find
				group
					text
				method
					find
				action
					none
				alias
					none
				description
					Locate a substring within text
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name text  type text
					[name subtext  type text
					[name from  type [int text]  subname true  default none
					[name to  type int  default none
				example
					[code [[find 'Hi! World' World]]  result 4
					[code [[find abcabc b]]  result 1
					[code [[find abcabc b 2]]  result 4
					[code [[find abcabc b 2 4]]  result none
					[code [[find abcabc b -1]]  result 4
					[code [[find.end abcabc c]]  result 5
			parse
				group
					text
				method
					parse
				action
					none
				alias
					none
				description
					Parse text into structured data
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name text  type text
					[name rule  type dict  default none
				example
					[code [[parse 'text1 1\ntext2 2' [apply  rules example]]]  result [[text1 1] [text2 2]]
			part
				group
					text
				method
					part
				action
					none
				alias
					none
				description
					Extract a part of the text or list
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name text  type text
					[name from  type [int dict
					[name to  type int  default none
				example
					[code [[part 'Hi! World' 0 3]] result Hi!
					[code [[part 'Hi! World' 4]] result World
					[code [[part 'Hi! World' 4 -3]] result Wo
					[code [[part 'Hi! World' -1]] result d
					[code [[part 'Hi! World' -5]] result World
					[code [[part 'Hi! World' -5 2]] result Wo
					[code [[part 'Hi! World' [length  3]]] result Hi!
					[code [[part 'Hi! World' [from 4  length 2]]] result Wo
					[code [[part 'Hi! World' [end  5]]] result World
					[code [[part [1 2 3 4 5] 0 3]] result [1 2 3 4]
					[code [[part [1 2 3 4 5] -1]] result [5]
					[code [[part [1 2 3 4 5] [end  2]]] result [4 5]
			split
				group
					text
				method
					split
				action
					none
				alias
					none
				description
					Split text into parts based on a delimiter or list based on a length
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name text  type [text list]
					[name delimiter  type [text number]  default none
				example
					[code [[split 'text text']]  result [text text]
					[code [[split a,b,c ,]]result [a b c]
					[code [[split texttexttext 4]]  result [text text text]
					[code [[split [1 2 3 4] 2]]  result [[1 2] [3 4]]
			join
				group
					text
				method
					join
				action
					none
				alias
					none
				description
					Join a list of text into a single text with a delimiter
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name data  type list
					[name delimiter  type text  default none
				example
					[code [[join [text text]]]  result 'text text
					[code [[join [a b c] ,]]  result a,b,c
					[code [[join [2026 12 31] -]]  result 2023-12-31
			escape
				group
					text
				method
					escape
				action
					none
				alias
					e
				description
					Escape special characters in a text
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name text  type text
					[name format  type text  subname true  default none
				example
					[code [[escape <div>text</div>]]  result &lt;div&gt;text&lt;/div&gt;
					[code [[s <div>text</div> html]]  result &lt;div&gt;text&lt;/div&gt;
					[code [[s.html ''text'']]  result &quot;text&quot;
					[code [[s.url https://voidsp.com]]  result https%3A%2F%2Fvoidsp.com
					[code [s.sql text'text]]  result text''text
					[code [s.json text"]]  result text\\"
			unescape
				group
					text
				method
					unescape
				action
					none
				alias
					u
				description
					Unescape special characters in a text
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name text  type text
					[name format  type text  subname true  default none
				example
					[code [[unescape &lt;div&gt;text&lt;/div&gt;]]  result <div>text</div>
					[code [[u &lt;div&gt;text&lt;/div&gt; html]]  result <div>text</div>
					[code [[u.html &quot;text&quot;]]  result ''text''
					[code [[u.url https%3A%2F%2Fvoidsp.com]]  result https://voidsp.com
					[code [u.sql text''text]]  result text'text
					[code [u.json text\\"]]  result text"
			translate
				group
					text
				method
					translate
				action
					none
				alias
					none
				description
					Translate text from one language to another
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name text  type text
					[name from  type text subname true  default none
					[name to  type text subname true  default none
				example
					[code [[; Hi! World]]  test false
					[code [[; 'Hi! World' en es]]  test false
					[code [[; 'Hi! World' en]]  test false
					[code [[translate.en Hi! World]]  test false
					[code [[translate.en.es Hi! World]]  test false
			check
				group
					text
				method
					check
				action
					none
				alias
					#
				description
					Spell check in different languages
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name text  type text
					[name language  type text  subname true  default none
				example
					[code [[check 'Hi! Warld']]  result [text 'Hi! World'  explain [[position 5  error a  correct o]]  test false
					[code [[check 'Hi! Warld' en]]  result [text 'Hi! World'  explain [[position 5  error a  correct o]]  test false
					[code [[check.en 'Hi! Warld']]  result [text 'Hi! World'  explain [[position 5  error a  correct o]]  test false

		  .: list :.

			push
				group
					list
				method
					push
				action
					none
				alias
					none
				description
					Add an element to the list
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name data  type list
					[name value  type any  default none
					[name index  type [int text]  subname true  default none
				example
					[code [[push [1 2] 3]]  result [1 2 3]
					[code [[push [1 2] 3 0]]  result [3 1 2]
					[code [[push.start [1 2] 3]]  result [3 1 2]
			pop
				group
					list
				method
					pop
				action
					none
				alias
					none
				description
					Remove and return an element from the list
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name data  type list
					[name index  type [int text]  subname true  default none
				example
					[code [[pop [1 2 3]]]  result 3
					[code [[pop [1 2 3] 0]]  result 1
					[code [[pop.start [1 2 3]]]  result 1
			reverse
				group
					list
				method
					reverse
				action
					none
				alias
					none
				description
					Reverse the order of elements in a list
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name data  type list
				example
					[code [[reverse [1 2 3]]]  result [3 2 1]
					[code [[reverse [a b]]]  result [b a]
			unique
				group
					list
				method
					unique
				action
					none
				alias
					none
				description
					Leave only unique values in a list
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name data  type list
				example
					[code [[reverse [1 2 2 1 3]]]  result [1 2 3]
					[code [[reverse [a b a c]]]  result [a b c]
			map
				group
					list
				method
					map
				action
					none
				alias
					none
				description
					Apply an action to each element in a list
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name data  type list
					[name action  type [text list]
				example
					[code [[map [1 2 3] [[* 2]] ]]  result [2 4 6]
					[code [[map [a b] upper ]]  result [A B]
			reduce
				group
					list
				method
					reduce
				action
					none
				alias
					none
				description
					Apply an action cumulatively to the elements in a list
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name data  type list
					[name action  type [text list]
				example
					[code [[reduce [1 2 3 4] [[* .value]] ]]  result 24
					[code [[reduce [1 2 3 4] +]]  result 10
			filter
				group
					list
				method
					filter
				action
					none
				alias
					none
				description
					Apply a filter action to each element in a list
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name data  type list
					[name action  type [text list]
				example
					[code [[filter [1 2 3 4] [[> 2]] ]]  result [3 4]
					[code [[filter [t te tex text] [[? [~ ..] > 2]] ]]  result [tex text]
			names
				group
					list
				method
					names
				action
					none
				alias
					indexes
					keys
				description
					Retrieve all indexes from a list or attribute names from a dictionary
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name data  type dict
				example
					[[code [[values [x 1  y 2]]]  result [x y]
			values
				group
					list
				method
					values
				action
					none
				alias
					none
				description
					Retrieve all values from a dictionary
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name data  type dict
				example
					[[code [[values [x 1  y 2]]]  result [1 2]

		  .: math :.

			sin
				group
					math
				method
					sin
				action
					none
				alias
					none
				description
					Sine of the value
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name value  type number
				result
					number
				example
					[[code [[sin 1]]  round 4  result 0.8415
			cos
				group
					math
				method
					cos
				action
					none
				alias
					none
				description
					Cosine of the value
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name value  type number
				result
					number
				example
					[[code [[cos 1]]  round 4  result 0.5403
			tan
				group
					math
				method
					tan
				action
					none
				alias
					none
				description
					Tangent of the value
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name value  type number
				result
					number
				example
					[[code [[tan 1]]  round 4  result 1.5574
			sinh
				group
					math
				method
					sinh
				action
					none
				alias
					none
				description
					Hyperbolic sine of the value
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name value  type number
				result
					number
				example
					[[code [[sinh 1]]  round 4  result 1.1752
			cosh
				group
					math
				method
					cosh
				action
					none
				alias
					none
				description
					Hyperbolic cosine of the value
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name value  type number
				result
					number
				example
					[[code [[cosh 1]]  round 4  result 1.5431
			tanh
				group
					math
				method
					tanh
				action
					none
				alias
					none
				description
					Hyperbolic tangent of the value
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name value  type number
				result
					number
				example
					[[code [[tanh 1]]  round 4  result 0.7616
			asin
				group
					math
				method
					asin
				action
					none
				alias
					none
				description
					Arc sine of the value
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name value  type number
				result
					number
				example
					[[code [[asin 1]]  round 4  result 1.5708
			acos
				group
					math
				method
					acos
				action
					none
				alias
					none
				description
					Arc cosine of the value
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name value  type number
				result
					number
				example
					[[code [[acos 0.5]]  round 4  result 1.0472
			atan
				group
					math
				method
					atan
				action
					none
				alias
					none
				description
					Arc tangent of the value
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name value  type number
				result
					number
				example
					[[code [[atan 1]]  round 4  result 0.7854
			asinh
				group
					math
				method
					asinh
				action
					none
				alias
					none
				description
					Arc hyperbolic sine of the value
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name value  type number
				result
					number
				example
					[[code [[asinh 0.5]]  round 3  result 0.4812
			acosh
				group
					math
				method
					acosh
				action
					none
				alias
					none
				description
					Arc hyperbolic cosine of the value
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name value  type number
				result
					number
				example
					[[code [[acosh 1.5]]  round 3  result 0.9624
			atanh
				group
					math
				method
					atanh
				action
					none
				alias
					none
				description
					Arc hyperbolic tangent of the value
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name value  type number
				result
					number
				example
					[[code [[atanh 0.5]]  round 3  result 0.5493
			round
				group
					math
				method
					round
				action
					none
				alias
					none
				description
					Rounds a number to the nearest integer or to the specified number of decimal places
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name value  type number
					[name fraction  type number  default 0
				result
					number
				example
					[code [[round 0.1]]  result 0
					[code [[round 0.7]]  result 1
					[code [[round -0.7]]  result -1
					[code [[round 0.123 2]]  result 0.12
			floor
				group
					math
				method
					floor
				action
					none
				alias
					none
				description
					Largest integer less than or equal to a number
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name value  type number
					[name fraction  type number  default 0
				result
					number
				example
					[code [[floor 0.1]]  result 0
					[code [[floor 0.7]]  result 0
					[code [[floor -0.7]]  result -1
			ceil
				group
					math
				method
					ceil
				action
					none
				alias
					none
				description
					Smallest integer greater than or equal to a number
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name value  type number
					[name fraction  type number  default 0
				result
					number
				example
					[code [[ceil 0.1]]  result 1
					[code [[ceil 0.7]]  result 1
					[code [[ceil -0.7]]  result 0
			log
				group
					math
				method
					log
				action
					none
				alias
					ln
				description
					Logarithm of a number (natural by default)
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name value  type number
					[name base  type number
				result
					number
				example
					[code [[log 0.1]]  round 4  result -2.3026
					[code [[log 0.1 2]]  round 4  result -3.3219
					[code [[log 0.1 10]]  result -1
					[code [log]  type number
					[code [ln]  type number
			fact
				group
					math
				method
					factorial
				action
					none
				alias
					none
				description
					Factorial of a given non-negative number
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name value  type number
				result
					number
				example
					[code [[fact 5]]  result 120
					[code [[fact 0]]  result 1
			fib
				group
					math
				method
					fibonacci
				action
					none
				alias
					none
				description
					Fibonacci numbers up to a specified index
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name number  type number
					[name multiply  type number  default 1
					[name shift  type number  default 0
				result
					number
				example
					[code [[fib 5]]  result [0 1 1 2 3
					[code [[fib 7]]  result [0 1 1 2 3 5 8
					[code [[fib 5 3 1]]  result [1 4 4 7 10
			gold
				group
					math
				method
					gold
				action
					none
				alias
					g
				description
					Golden ratio of a number
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name value  type number
					[name part  type text
				result
					dict
				example
					[code [[gold 10]]  round 4  result [short 3.8197  long 6.1803  total 10
					[code [[gold 10 short]]  round 4  result [short 10  long 16.1803  total 26.1803
					[code [[gold 10 long]]  round 4  result [short 6.1803  long 10  total 16.1803
			abs
				group
					math
				method
					abs
				action
					none
				alias
					none
				description
					Absolute value of a number
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name value  type number
				result
					number
				example
					[code [[abs -3.14]]  result 3.14
					[code [[abs 3.14]]  result 3.14
			min
				group
					math
				method
					min
				action
					none
				alias
					none
				description
					Smallest of a list of numbers
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name value  type list
				result
					number
				example
					[code [[min [5 3 8 1]]]  result 1
					[code [[min [-2 -5 0]]]  result -5
			max
				group
					math
				method
					max
				action
					none
				alias
					none
				description
					Largest of a list of numbers
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name value  type list
				result
					number
				example
					[code [[max [5 3 8 1]]]  result 8
					[code [[max [-2 -5 0]]]  result 0
			sum
				group
					math
				method
					sum
				action
					none
				alias
					none
				description
					Sum of a list of numbers
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name value  type list
				result
					number
				example
					[code [[sum [1 2 3 4 5]]]  result 15
					[code [[sum [10 20]]]  result 30
			avg
				group
					math
				method
					avg
				action
					none
				alias
					none
				description
					Average value of a list of numbers
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name value  type list
				result
					number
				example
					[code [[avg [1 2 3 4 5]]]  result 3
					[code [[avg [10 20]]]  result 15
			random
				group
					math
				method
					random
				action
					none
				alias
					none
				description
					Generates a pseudo-random number
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name from  type [number bool text list dict]  default none
					[name to  type number  default none
				result
					[number bool text list
				example
					[code [random]  range [0 1
					[code [[random 10]]  range [0 10
					[code [[random 10 20]]  range [10 20
					[code [[random true]]  in [true false
					[code [[random abcd]]  in [a b c d
					[code [[random [1 2 3]]] in [1 2 3
					[code [[random [a 1  b 2]]]  in [[a 1] [b 2
			random.seed
				group
					math
				method
					random_seed
				action
					none
				alias
					random.reseed
				description
					Receives, sets or refreshes the seed for the random number generator to produce reproducible results
				safe
					false
				container
					none
				language
					[python gdscript asm86
				param
					[[name seed  type text  default none
				result
					text
				example
					[code [[random.seed uniqueseed] random.seed]  result uniqueseed
					[code [[random.reseed] random.seed]  type text  length 256

		  .: time :.

			time
				group
					time
				method
					time
				action
					none
				alias
					timestamp
				description
					Provides current time since the epoch or calculates time passed since a given start time
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name fraction  type [number text]  subname true  default 0
				result
					number
				example
					[code [time]  type number
					[code [[time 4]]  type number
					[code [time.milli]  type number
					[code [time.micro]  type number
					[code [timestamp]  type number
			timer
				group
					time
				method
					timer
				action
					none
				alias
					none
				description
					Creates a timer that can be used to trigger events at specific intervals
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name action type [text list]
					[name name  type text  default none
					[name seconds  type number  default 1
					[name repeat  type [bool number]  default false
				result
					text
				example
					[code [timer [[. time!]]  output time!
					[code [[timer [[. time!]] tik 1]]  output time!
					[code [[timer [[. time!]] tik 1 2]]  output 'time!\ntime!
					[code [[timer [[. time!]] tik 1 true]]  clear [timer.remove]
			timer.remove
				group
					time
				method
					timer_remove
				action
					none
				alias
					none
				description
					Removes previously created timer
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name name  type text  default none
				result
					none
				example
					[code [[timer [[. time!]] tik 1 true] [timer.remove tik]]  output none
					[code [timer.remove
			wait
				group
					time
				method
					wait
				action
					none
				alias
					none
				description
					Pauses execution for a specified number of seconds
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name seconds  type [number text]  subname true  default 1
				result
					none
				example
					[code [[wait 0.01]]
					[code [[wait 1m]]  test false
					[code [[wait 1h]]  test false
					[code [wait.h]  test false
			stopwatch
				group
					time
				method
					stopwatch
				action
					none
				alias
					t
				description
					Stopwatch for calculating the time spent on operations
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name tag  type text  default none
					[name name  type text  default none
				result
					number
				example
					[code [t]  type number
					[code [[t start]]  type number
					[code [[t start] [t stop] [t list]]  type list
					[code [[t laps lap1] [t laps lap2] [t laps list]]  type list
			date
				group
					time
				method
					date
				action
					none
				alias
					none
				description
					Format or parse date-related information
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name time  type [text number]  default none
					[name format  type text  default none
				result
					[number text
				example
					[code [date]  type text
					[code [[date (hour):(minute):(second)]]  length 8
					[code [[date 1678901234]]  type text
					[code [[date 1744095313.123 '(year)-(month)-(day) (hour):(minute):(second).(millisecond)']]  result '2025-04-08 06:55:13.123
					[code [[date 1744095313 (year short).(month short)]]  result '2025.4
					[code [[date '2025-04-08 06:55:13.123' '(year)-(month)-(day) (hour):(minute):(second).(millisecond)']]  result 1744095313.123
					[code [[date '2025-04-08 06:55:13.123']]  result 1744095313.123

		  .: crypto :.

			encrypt
				group
					crypto
				method
					encrypt
				action
					none
				alias
					none
				description
					Encrypts data using the AES256 algorithm and the specified key
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name data  type any
					[name key  type text  default none
				example
					[code [[encrypt text key]]  type binary
					[code [[encrypt text]]  type dict
			decrypt
				group
					crypto
				method
					decrypt
				action
					none
				alias
					none
				description
					Decrypts previously encrypted data using the AES256 algorithm and the specified key
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name data  type [text binary
					[name key  type text
				example
					[code [[decrypt .data key]]  test false
					[code [[decrypt U3tBg8cZyAM5Ir5w0sovXIiXSI9lCYGY3kdHHWmDHiBo key]]  result text
			password
				group
					crypto
				method
					bcrypt_encode
				action
					none
				alias
					none
				description
					Hashes a password using the Argon2, Bcrypt or PBKDF2 algorithm for secure storage
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name password  type text
					[name name  type text  default none
				example
					[code [[password password]]  type text
					[code [[password password argon]]  type text
					[code [[password password bcrypt]]  type text
			password.check
				group
					crypto
				method
					bcrypt_check
				action
					none
				alias
					none
				description
					Verifies a password against a Argon2, Bcrypt or PBKDF2 hashed password
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name hash  type text
					[name password  type text
				example
					[[code [[password.check .hash password]]  type bool  test false
			hash
				group
					crypto
				method
					hash
				action
					none
				alias
					none
				description
					Generates a hash for the data or generates a random text
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name data  type any  default none
					[name algorithm  type text  subname true  default none
				example
					[code [[hash hello]]  result 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824
					[code [hash]  type text
					[code [hash 10]  type text  length 10
					[code [hash 10 letter]  type text  length 10
					[code [hash.letter 10]  type text  length 10
					[code [hash.lower]  type text
					[code [hash.upper]  type text
					[code [hash.number]  type text
					[code [hash.symbol]  type text
					[code [hash text sha1]  result 372ea08cab33e71c02c651dbc83a474d32c676ea
					[code [hash.sha1 text]  result 372ea08cab33e71c02c651dbc83a474d32c676ea
			uuid
				group
					crypto
				method
					uuid
				action
					none
				alias
					none
				description
					Generates a universally unique identifier
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[]
				example
					[[code [uuid]  type text
			sha1
				group
					crypto
				method
					sha1
				action
					none
				alias
					none
				description
					Generates an SHA-1 hash of a text
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name data  type any
				example
					[[code [[sha1 hello]]  result aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d
			sha256
				group
					crypto
				method
					sha256
				action
					none
				alias
					none
				description
					Generates an SHA-256 hash of a text
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name data  type any
				example
					[[code [[sha256 hello]]  result 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824
			sha512
				group
					crypto
				method
					sha512
				action
					none
				alias
					none
				description
					Generates an SHA-512 hash of a text
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name data  type any
				example
					[[code [[sha512 hello]]  result 9b71d224bd62f3785d96d46ad3ea3d73319bfbc2890caadae2dff72519673ca72323c3d99ba5c11d7c7acc6e14b8c5da0c4663475c2e5c3adef46f73bcdec043
			crc32
				group
					crypto
				method
					crc32
				action
					none
				alias
					none
				description
					Calculates the CRC32 checksum of a text
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name data  type any
				example
					[[code [[crc32 hello]]  result 907060870
			base64
				group
					crypto
				method
					base64
				action
					none
				alias
					none
				description
					Encodes the data into Base64 format
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name data  type any
				example
					[[code [[base64 hello]]  result aGVsbG8=
			base64.decode
				group
					crypto
				method
					base64_decode
				action
					none
				alias
					none
				description
					Decodes Base64 encoded data back to its original form
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name data  type text
					[name safe  type bool  subname true  default true
				example
					[code [[base64.decode aGVsbG8=]]  result hello
					[code [[base64.decode aGVsbG8]]  result hello
					[code [[base64.decode.safe aGVsbG8]]  result hello
			gzip
				group
					crypto
				method
					gzip
				action
					none
				alias
					none
				description
					Compresses data using the GZip compression algorithm (popular compression)
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++
				param
					[name data  type any
					[name level  type [number text]  subname true  default none
				example
					[code [[gzip hello]]  result *H4sIAAAAAAAA/8tIzcnJVyjPL8pJAQCFEUoNCwAAAA==
					[code [[gzip hello 1]]  type binary
					[code [[gzip hello 9]]  type binary
					[code [[gzip hello fast]]  type binary
					[code [[gzip hello best]]  type binary
					[code [[gzip.fast hello]]  type binary
					[code [[gzip.best hello]]  type binary
			gzip.decode
				group
					crypto
				method
					gzip_decode
				action
					none
				alias
					none
				description
					Decompresses GZip compressed data
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++
				param
					[[name data  type any
				example
					[[code [[gzip.decode *H4sIAAAAAAAA/8tIzcnJVyjPL8pJAQCFEUoNCwAAAA==]]  result hello
			lzma
				group
					crypto
				method
					lzma
				action
					none
				alias
					none
				description
					Compresses data using the LZMA2 compression algorithm (best compression)
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++
				param
					[name data  type any
					[name level  type [number text  subname true  default none
				example
					[[code [[lzma hello]]  result */Td6WFoAAATm1rRGAgAhAQwAAACPmEGcAQAEaGVsbG8AAAAAsTe52+XaHpsAAR0FuC2Arx+2830BAAAAAARZWg==
					[code [[lzma hello 1]]  test false
					[code [[lzma hello 9]]  test false
					[code [[lzma hello fast]]  test false
					[code [[lzma hello best]]  test false
					[code [[lzma.fast hello]]  test false
					[code [[lzma.best hello]]  test false
			lzma.decode
				group
					crypto
				method
					lzma_decode
				action
					none
				alias
					none
				description
					Decompresses LZMA2 compressed data
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++
				param
					[[name data  type any
				example
					[[code [[lzma.decode */Td6WFoAAATm1rRGAgAhAQwAAACPmEGcAQAEaGVsbG8AAAAAsTe52+XaHpsAAR0FuC2Arx+2830BAAAAAARZWg==]]  result hello
			lz4
				group
					crypto
				method
					lz4
				action
					none
				alias
					none
				description
					Compresses data using the LZ4 compression algorithm (fastest decompression)
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++
				param
					[name data  type any
					[name level  type [number text]  subname true  default none
				example
					[code [[lz4 hello]]  result *BCJNGGhABQAAAAAAAABhBQAAgGhlbGxvAAAAAA==
					[code [[lz4 hello 0]]  test false
					[code [[lz4 hello 16]]  test false
					[code [[lz4 hello fast]]  test false
					[code [[lz4 hello best]]  test false
					[code [[lz4.fast hello]]  test false
					[code [[lz4.best hello]]  test false
			lz4.decode
				group
					crypto
				method
					lz4_decode
				action
					none
				alias
					none
				description
					Decompresses LZ4 compressed data
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++
				param
					[[name data  type any
				example
					[[code [[lz4.decode *BCJNGGhABQAAAAAAAABhBQAAgGhlbGxvAAAAAA==]]  result hello
			lzss
				group
					crypto
				method
					lzss
				action
					none
				alias
					none
				description
					Compresses data using the LZSS compression algorithm (fastest retro compression with minimal memory usage)
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name data  type any
				example
					[[code [[lzss hello]]  result *H2hlbGxv
			lzss.decode
				group
					crypto
				method
					lzss_decode
				action
					none
				alias
					none
				description
					Decompresses LZSS compressed data
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name data  type any
				example
					[[code [[lzss.decode *H2hlbGxv]]  result hello
			deflate
				group
					crypto
				method
					deflate
				action
					none
				alias
					none
				description
					Compresses data using the Deflate (LZSS + Huffman) compression algorithm (best retro compression)
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name data  type any
					[name level  type [number text]  subname true  default none
				example
					[[code [[deflate hello]]  result *y0jNyckHAA==
					[code [[deflate hello 1]]  test false
					[code [[deflate hello 9]]  test false
					[code [[deflate hello fast]]  test false
					[code [[deflate hello best]]  test false
					[code [[deflate.fast hello]]  test false
					[code [[deflate.best hello]]  test false
			deflate.decode
				group
					crypto
				method
					deflate_decode
				action
					none
				alias
					none
				description
					Decompresses Deflate (LZSS + Huffman) compressed data
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name data  type any
				example
					[[code [[deflate.decode *y0jNyckHAA==]]  result hello
			aes
				group
					crypto
				method
					aes
				action
					none
				alias
					none
				description
					Encrypts binary data using the AES256 algorithm and the specified key
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name data  type binary
					[name key  type text
				example
					[[code [[aes *'text' key]]  type binary
			aes.decode
				group
					crypto
				method
					aes_decode
				action
					none
				alias
					none
				description
					Decrypts previously encrypted binary data using the AES256 algorithm and the specified key
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name data  type binary
					[name key  type text
				example
					[[code [[decrypt *vBDRK4FnebbWvIF6PaCgKVkEvLb/TYC8DWThEDmnLJA= key]]  result *'text'
			rsa
				group
					crypto
				method
					rsa_encode
				action
					none
				alias
					none
				description
					Encrypts data using RSA encryption with a public key or generates keys (the maximum data length and encryption speed depends on the key size 4096 = 446 bytes)
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++
				param
					[name data  type any
					[name public  type text
					[name password  type text  default none
					[name length  type [int text]  default none
				example
					[code [rsa]  type dict
					[code [[rsa text .public_key]]  type binary  test false
					[code [[rsa text none .extra_password .key_size]]  type binary  test false
					[code [[rsa.fast 128bytes .public_key]]  type binary  test false
					[code [[rsa.128 128bytes .public_key]]  type binary  test false
					[code [[rsa.446 446bytes .public_key]]  type binary  test false
					[code [[rsa.4096 446bytes .public_key]]  type binary  test false
			rsa.decode
				group
					crypto
				method
					rsa_decode
				action
					none
				alias
					none
				description
					Decrypts data encrypted with RSA encryption
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++
				param
					[name data  type any
					[name private_key  type text
					[name password  type text  default none
				example
					[code [[rsa.decode .encrypted .private_key]]  type binary  test false
					[code [[rsa.decode .encrypted .private_key .extra_password]]  type binary  test false
			ecdhe
				group
					crypto
				method
					ecdhe_encode
				action
					none
				alias
					none
				description
					Creates a pair of keys or creates a shared key from the public and private keys of the sides
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name public_key  type text  default none
					[name private_key  type text  default none
				example
					[code [ecdhe]  type dict
					[code [ecdhe .side1_public_key .side2_private_key]  type text
					[code [ecdhe .side2_public_key .side1_private_key]  type text
			barcode
				group
					crypto
				method
					barcode_encode
				action
					none
				alias
					qr
				description
					Encodes text into a barcode or returns a list of supported code formats
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name text  type any
					[name format  type text  subname true  default none
				example
					[code [barcode]  type dict
					[code [[barcode 8410564006257]]  type dict
					[code [[barcode 8410564006257 ean13]]  type dict
					[code [[barcode.ean13 8410564006257]]  type dict
					[code [[barcode.upc 712345000019]]  type dict
					[code [[barcode.code128 text]]  type dict
					[code [[qr https://voidsp.com]]  type dict
			barcode.decode
				group
					crypto
				method
					barcode_decode
				action
					none
				alias
					qr.decode
				description
					Decodes the barcode image into text
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name image  type binary
					[name format  type text  subname true  default none
				example
					[code [[barcode.decode .image]]  type text
					[code [[barcode.decode .image ean13]]  type text
					[code [[barcode.decode.ean13 .image]]  type text
					[code [[qr.decode .image]]  type text

		  .: file :.

			file
				group
					file
				method
					file
				action
					none
				alias
					<<<
					>>>
					file.read
					file.write
					file.create
					file.clear
				description
					Read or write data to a file at a specified path
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name path  type text
					[name data  type any  default none
					[name format  type text  subname true  default none
				example
					[code [[file file.txt]]  type [text binary]  test false
					[code [[<<< file.txt]]  type [text binary]  test false
					[code [[file data.void]]  type any  test false
					[code [[file data.json]]  type any  test false
					[code [[file data.csv]]  type list  test false
					[code [[file.line file.txt]]  type list  test false
					[code [[file.utf8 file.txt]]  type text  test false
					[code [[file.1252 file.txt]]  type text  test false
					[code [[file file.txt text]]  test false
					[code [[>>> file.txt text]]  test false
					[code [[file.utf8 file.txt .text]]  test false
					[code [[file.1252 file.txt .text]]  test false
					[code [[file data.void .data]]  test false
					[code [[file data.json .data]]  test false
					[code [[file data.csv .data]]  type any  test false
					[code [[file.create file.txt]]  test false
					[code [[file.clear file.txt]]  test false
			file.exists
				group
					file
				method
					file_exists
				action
					none
				alias
					is_file
				description
					Checks if a specified file exists at the given path
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name path  type text
				example
					[code [[file.exists file.txt]]  type bool  test false
					[code [[file.exists /path/to/file.txt]]  type bool  test false
			file.remove
				group
					file
				method
					file_remove
				action
					none
				alias
					file.trash
				description
					Removes a specified file
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name path  type [text list
					[name trash  type bool  default none
				example
					[code [[file.remove file.txt]]  test false
					[code [[file.remove /path/to/file.txt]]  test false
					[code [[file.remove file1.txt file2.txt]]  test false
					[code [[file.trash file.txt]]  test false
			file.copy
				group
					file
				method
					file_copy
				action
					none
				alias
					none
				description
					Copies a specified file to a new location
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name source  type text
					[name destination  type text  default none
				example
					[code [[file.copy /path/to/file.txt /destination/file.txt]]  test false
					[code [[file.copy /path/to/file.txt /destination]]  test false
					[code [[file.copy /path/to/file.txt]]  test false
			file.move
				group
					file
				method
					file_move
				action
					none
				alias
					file.rename
				description
					Moves a specified file to a new location or renames it
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name source  type text
					[name destination  type text
				example
					[code [[file.move /path/to/file.txt /destination/file.txt]]  test false
					[code [[file.move /path/to/file.txt /destination]]  test false
					[code [[file.rename file.txt backup.txt]]  test false
					[code [[file.rename /path/to/file.txt backup.txt]]  test false
			file.info
				group
					file
				method
					file_info
				action
					none
				alias
					none
				description
					Retrieves information about a specified file
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name path  type text
					[name data  type any  default true
					[name component  type text  subname true  default none
				example
					[code [[file.info /path/to/file.txt]]  type dict  test false
					[code [[file.info.name /path/to/file.txt]]  type text  test false
					[code [[file.info.extension /path/to/file.txt]]  type text  test false
					[code [[file.info.file /path/to/file.txt]]  type text  test false
					[code [[file.info.dir /path/to/file.txt]]  type text  test false
					[code [[file.info.drive /path/to/file.txt]]  type text  test false
					[code [[file.info.size /path/to/file.txt]]  type number  test false
					[code [[file.info.owner /path/to/file.txt]]  type text  test false
					[code [[file.info.group /path/to/file.txt]]  type text  test false
					[code [[file.info.permission /path/to/file.txt]]  type dict  test false
					[code [[file.info.time /path/to/file.txt]]  type number  test false
					[code [[file.info.time.create /path/to/file.txt]]  type number  test false
					[code [[file.info.permission /path/to/file.txt [read true  write true]]]  test false
					[code [[file.info.permission /path/to/file.txt [owner [read true  write true]  group [read true  write true]]]]  test false
					[code [[file.info.permission /path/to/file.txt hidden]]  test false
					[code [[file.info.permission /path/to/file.txt readonly]]  test false
					[code [[file.owner /path/to/file.txt]]  type text  test false
					[code [[file.time /path/to/file.txt]]  type number  test false
					[code [[file.permission /path/to/file.txt [read true  write true]]]  test false
					[code [[file.permission.execute.owner /path/to/file.txt true]]  test false
					[code [[file.permission.execute /path/to/file.txt true]]  test false
					[code [[info.owner /path/to/file.txt]]  type text  test false
					[code [[info.time /path/to/file.txt]]  type number  test false
			file.sha256
				group
					file
				method
					file_sha256
				action
					none
				alias
					none
				description
					Computes the SHA256 checksum of a specified file
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name path  type text
				example
					[[code [[file.sha256 file.txt]]  type text  test false
			file.sha512
				group
					file
				method
					file_sha512
				action
					none
				alias
					none
				description
					Computes the SHA512 checksum of a specified file
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name path  type text
				example
					[[code [[file.sha512 file.txt]]  type text  test false
			file.crc32
				group
					file
				method
					file_crc32
				action
					none
				alias
					none
				description
					Computes the CRC32 checksum of a specified file
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name path  type text
				example
					[[code [[file.crc32 file.txt]]  type text  test false
			file.base64
				group
					file
				method
					file_base64
				action
					none
				alias
					none
				description
					Encodes a specified file to base64 format
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name path  type text
				example
					[[code [[file.base64 file.txt]]  type text  test false
			file.gzip
				group
					file
				method
					file_gzip
				action
					none
				alias
					none
				description
					Compresses a specified file using GZip compression
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++
				param
					[name source  type text
					[name destination  type text  default none
					[name param  type [text number dct]  default none
				example
					[code [[file.gzip file.txt file.gz]]  test false
					[code [[file.gzip file.txt]]  test false
					[code [[file.gzip file.txt file.txt.gz 7]]  test false
					[code [[file.gzip file.txt 7]]  test false
					[code [[file.gzip file.txt file.txt.gz best]]  test false
					[code [[file.gzip file.txt file.txt.gz fast]]  test false
					[code [[file.gzip file.txt file.txt.gz [compression  9]]]  test false
					[code [[file.gzip /path/to/file.txt /destination/file.gz]]  test false
			file.zip
				group
					file
				method
					file_zip
				action
					none
				alias
					none
				description
					Compresses a specified file into a ZIP archive
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++
				param
					[name source  type [text list
					[name destination  type text  default none
					[name param  type [text number dict]  default none
				example
					[code [[file.zip file.txt file.zip]]  test false
					[code [[file.zip file.txt]]  test false
					[code [[file.zip file.txt file.zip 7]]  test false
					[code [[file.zip file.txt 7]]  test false
					[code [[file.zip file.txt file.zip best]]  test false
					[code [[file.zip file.txt file.zip fast]]  test false
					[code [[file.zip file.txt file.zip [compression 9  overwrite true]]]  test false
					[code [[file.zip /path/to/file.txt /destination/file.zip]]  test false
					[code [[file.zip [file1.txt file2.txt] files.zip]]  test false
			file.void
				group
					file
				method
					file_void
				action
					none
				alias
					dir.void
					drive.void
				description
					Compresses the specified file using LZMA2 compression and places it in a container
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name source  type [text list
					[name destination  type [text dict]  default none
					[name param  type [text number dct]  default none
				example
					[code [[file.void file.txt file.void]]  test false
					[code [[file.void file.txt]]  test false
					[code [[file.void file.txt file.void 7]]  test false
					[code [[file.void file.txt 7]]  test false
					[code [[file.void file.txt file.void best]]  test false
					[code [[file.void file.txt file.void fast]]  test false
					[code [[file.void file.txt [compression 9  key password]]]  test false
					[code [[file.void file.txt file.void password]]  test false
					[code [[file.void file.txt file.void key.txt]]  test false
					[code [[file.void /path/to/file.txt /destination/file.void]]  test false
					[code [[file.void [file1.txt file2.txt] files.void]]  test false
			file.extract
				group
					file
				method
					file_extract
				action
					none
				alias
					none
				description
					Decompresses a compressed files and directories from an archive
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name source  type [text list
					[name destination  type text  default none
					[name param  type [text number dct]  default none
				example
					[code [[file.extract file.void]]  test false
					[code [[file.extract file.void /path/to/extract]]  test false
					[code [[file.extract file.void /path/to/extract password]]  test false
					[code [[file.extract file.void /path/to/extract key.txt]]  test false
					[code [[file.extract file.void [source [file1.txt file2.txt]  destination /path/to/extract  key password]]]  test false
					[code [[file.extract file.zip]]  test false
					[code [[file.extract file.zip [file1.txt file2.txt]]]  test false
					[code [[file.extract file.zip [source [file1.txt file2.txt]  destination /path/to/extract  overwrite true  remove true]]]  test false
					[code [[file.extract file.txt.gz /path/to/extract]]  test false
					[code [[file.extract dir.tar.gz /path/to/extract]]  test false
					[code [[file.extract dir.tar /path/to/extract]]  test false
			link
				group
					file
				method
					link
				action
					none
				alias
					none
				description
					Creates a symlink at the given path
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name source  type text
					[name destination  type text
				example
					[code [[link /path/to/file.txt /path/to/link]]  type bool  test false
					[code [[link /path /path/to/link]]  type bool  test false
					[code [[link /mnt/drive /path/to/link]]  type bool  test false
			link.exists
				group
					file
				method
					link_exists
				action
					none
				alias
					is_link
				description
					Checks if a specified symlink exists at the given path
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name path  type text
				example
					[[code [[link.exists /path/to/link]]  type bool  test false
			dir
				group
					file
				method
					dir
				action
					none
				alias
					none
				description
					Lists the contents of a specified directory
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name path  type text
					[name param  type [bool list]  default none
				example
					[code [dir]  type list  test false
					[code [[dir /path]]  type list  test false
					[code [[dir /path owner]]  type list  test false
					[code [[dir /path [owner time sha256 sort]]]  type list  test false
			dir.create
				group
					file
				method
					dir_create
				action
					none
				alias
					none
				description
					Creates a new directory
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name path  type text
				example
					[[code [[dir.create /path/to/create]  test false
			dir.exists
				group
					file
				method
					dir_exists
				action
					none
				alias
					is_dir
				description
					Checks if a specified directory exists at the given path
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name path  type text
				example
					[[code [[dir.exists /path/to/check]]  type bool  test false
			dir.remove
				group
					file
				method
					dir_remove
				action
					none
				alias
					dir.trash
				description
					Removes a specified directory
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name path  type text
				example
					[code [[dir.remove /path/to/remove]]  test false
					[code [[dir.trash /path/to/remove]]  test false
			dir.clear
				group
					file
				method
					dir_clear
				action
					none
				alias
					none
				description
					Clears all contents of a directory without removing itself
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name path  type text
				example
					[[code [[dir.clear /path/to/clear]]  test false
			dir.copy
				group
					file
				method
					dir_copy
				action
					none
				alias
					none
				description
					Copies a directory to a new location
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name source  type text
					[name destination  type text  default none
				example
					[code [[file.copy /path/to/file.txt /path/destination/file.txt]]  test false
					[code [[file.copy /path/to/file.txt /path/destination]]  test false
					[code [[file.copy /path/to/file.txt]]  test false
					[code [[dir.copy /path/to/copy /path/destination]]  test false
					[code [[dir.copy /path/to/copy]]  test false
					[code [[drive.copy e f]]  test false
					[code [[drive.copy /mnt/drive /mnt/backup]]  test false
			dir.move
				group
					file
				method
					dir_move
				action
					none
				alias
					dir.rename
				description
					Moves a specified directory to a new location or renames it
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name source  type text
					[name destination  type text
				example
					[code [[file.move /path/to/file.txt /path/destination/file.txt]]  test false
					[code [[file.move /path/to/file.txt /path/destination]]  test false
					[code [[dir.move /path/to/move /]]  test false
					[code [[dir.move /path/to/move /destination]]  test false
					[code [[dir.move e f]]  test false
					[code [[dir.move /mnt/drive /mnt/backup]]  test false
					[code [[file.rename file.txt backup.txt]]  test false
					[code [[file.rename /path/to/file.txt backup.txt]]  test false
					[code [[dir.rename /path backup]]  test false
					[code [[drive.rename e name]]  test false
					[code [[drive.rename /mnt/drive name]]  test false
			dir.info
				group
					file
				method
					dir_info
				action
					none
				alias
					none
				description
					Retrieves information about a specified directory
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name path  type text
					[name data  type any  default true
					[name component  type text  subname true  default none
				example
					[code [[dir.info /path]]  type dict  test false
					[code [[dir.info.size /path]]  type number  test false
					[code [[dir.info.owner /path]]  type text  test false
					[code [[dir.info.files /path]]  type number  test false
					[code [[dir.info.permission.read.owner /path true]]  test false
					[code [[dir.info.permission.read /path true]]  test false
					[code [[info.owner /path]]  type text  test false
					[code [[info.time /path]]  type number  test false
			dir.sha256
				group
					file
				method
					dir_sha256
				action
					none
				alias
					none
				description
					Computes the SHA256 checksum of a specified directory
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name path  type text
				example
					[[code [[dir.sha256 /path/to/hash]]  type text  test false
			dir.sha512
				group
					file
				method
					dir_sha512
				action
					none
				alias
					none
				description
					Computes the SHA512 checksum of a specified directory
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name path  type text
				example
					[[code [[dir.sha512 /path/to/hash]]  type text  test false
			dir.gzip
				group
					file
				method
					dir_gzip
				action
					none
				alias
					none
				description
					Compresses a specified file, directory or drive using GZip compression
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++
				param
					[name source  type text
					[name destination  type text  default none
					[name param  type [text number dct]  default none
				example
					[code [[file.gzip file.txt file.gz]]  test false
					[code [[file.gzip file.txt]]  test false
					[code [[file.gzip file.txt file.txt.gz 7]]  test false
					[code [[file.gzip file.txt 7]]  test false
					[code [[file.gzip file.txt file.txt.gz best]]  test false
					[code [[file.gzip file.txt file.txt.gz fast]]  test false
					[code [[file.gzip file.txt file.txt.gz [compression  9]]]  test false
					[code [[file.gzip /path/to/file.txt /destination/file.gz]]  test false
					[code [[dir.gzip /path dir.tar.gz]]  test false
					[code [[drive.gzip e drive.tar.gz]]  test false
					[code [[drive.gzip /mnt/drive drive.tar.gz]]  test false
			dir.zip
				group
					file
				method
					dir_zip
				action
					none
				alias
					none
				description
					Compresses a specified file, directory or drive into a ZIP archive
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++
				param
					[name source  type [text list
					[name destination  type text  default none
					[name param  type [text number dict]  default none
				example
					[code [[file.zip file.txt file.zip]]  test false
					[code [[file.zip file.txt]]  test false
					[code [[file.zip file.txt file.zip 7]]  test false
					[code [[file.zip file.txt 7]]  test false
					[code [[file.zip file.txt file.zip best]]  test false
					[code [[file.zip file.txt file.zip fast]]  test false
					[code [[file.zip file.txt file.zip [compression 9  overwrite true]]]  test false
					[code [[file.zip /path/to/file.txt /destination/file.zip]]  test false
					[code [[file.zip [file1.txt file2.txt] files.zip]]  test false
					[code [[dir.zip /path dir.zip]]  test false
					[code [[drive.zip e drive.zip]]  test false
					[code [[drive.zip /mnt/drive drive.zip]]  test false
			dir.void
				group
					file
				method
					dir_void
				action
					none
				alias
					none
				description
					Compresses the specified file, directory or drive using LZMA2 compression and places it in a container
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name source  type [text list
					[name destination  type [text dict]  default none
					[name param  type [text number dct]  default none
				example
					[code [[file.void file.txt file.void]]  test false
					[code [[file.void file.txt]]  test false
					[code [[file.void file.txt file.void 7]]  test false
					[code [[file.void file.txt 7]]  test false
					[code [[file.void file.txt file.void best]]  test false
					[code [[file.void file.txt file.void fast]]  test false
					[code [[file.void file.txt [compression 9  key password]]]  test false
					[code [[file.void file.txt file.void password]]  test false
					[code [[file.void file.txt file.void key.txt]]  test false
					[code [[file.void /path/to/file.txt /destination/file.void]]  test false
					[code [[file.void [file1.txt file2.txt] files.void]]  test false
					[code [[dir.void /path dir.void]]  test false
					[code [[drive.void e drive.void]]  test false
					[code [[drive.void /mnt/drive drive.void]]  test false
			dir.magic
				group
					file
				method
					dir_magic
				action
					none
				alias
					none
				description
					Automatically convert files in the specified directory
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name path  type text
					[name effect  type text  subname true
					[name param  type many  default none
				example
					[code [[dir.magic.jpg /path/to/magic]]  test false
					[code [[dir.magic.jpg /path/to/magic 90%]]  test false
					[code [[dir.magic.png /path/to/magic]]  test false
					[code [[dir.magic.webp /path/to/magic]]  test false
					[code [[dir.magic.webp.lossless /path/to/magic]]  test false
					[code [[dir.magic.webp.loop /path/to/magic]]  test false
					[code [[dir.magic.gif /path/to/magic]]  test false
					[code [[dir.magic.video /path/to/magic mykey]]  test false
					[code [[dir.magic.mp4 /path/to/magic mykey]]  test false
					[code [[dir.magic.unique /path/to/magic]]  test false
					[code [[dir.magic.zip /path/to/magic]]  test false
					[code [[dir.magic.cloud /path/to/magic]]  test false
					[code [[dir.magic.encrypt /path/to/magic]]  test false
					[code [[dir.magic.manga /path/to/magic translate colorize]]  test false
					[code [[dir.magic.x2 /path/to/magic]]  test false
					[code [[dir.magic.grayscale /path/to/magic]]  test false
					[code [[dir.magic.crop /path/to/magic [width 200  height 100]]]  test false
					[code [[dir.magic.run /path/to/magic]]  test false
			drive
				group
					file
				method
					drive
				action
					none
				alias
					drive.info
				description
					Lists all available drives on the system
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name path  type text  default none
				example
					[code [drive]  type list
					[code [drive /mnt/storage]  type dict  test false
					[code [drive E]  type dict  test false
					[code [drive.info /mnt/storage]  type dict  test false
			drive.create
				group
					file
				method
					drive_create
				action
					drive.create
				alias
					none
				description
					Creates a volume or partition with the specified parameters
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name path  type text
					[name size [int text]  default none
					[name format  type text   default none
					[name name  type text  default none
				example
					[code [[drive.create .id 100gb ext4 backup]]  test false
					[code [[drive.create .id 100_000_000_000 ext4 backup]]  test false
			drive.exists
				group
					file
				method
					drive_exists
				action
					none
				alias
					is_drive
				description
					Checks if a specified drive exists at the given path
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name path  type text
				example
					[code [[drive.exists /mnt/storage]]  type bool  test false
					[code [[drive.exists .id]]  type bool  test false
					[code [[is_drive .id]]  type bool  test false
			drive.remove
				group
					file
				method
					drive_remove
				action
					drive.remove
				alias
					none
				description
					Removes a volume or partition
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name path  type text
				example
					[code [[drive.remove /mnt/storage]]  test false
					[code [[drive.remove E]]  test false
					[code [[drive.remove .partition.id]]  test false
			drive.clear
				group
					file
				method
					drive_clear
				action
					drive.clear
				alias
					drive.format
				description
					 Clears or format a volume
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name path  type text
					[name format  type text  default none
				example
					[code [[drive.clear /mnt/storage]]  test false
					[code [[drive.clear E]]  test false
					[code [[drive.clear .volume.id]]  test false
					[code [[drive.format E fat32]]  test false
			drive.rename
				group
					file
				method
					drive_rename
				action
					drive.rename
				alias
					none
				description
					Renames a volume
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name path  type text
					[name name  type text]
				example
					[code [[drive.rename /mnt/storage backup]]  test false
					[code [[drive.rename E backup]]  test false
			drive.mount
				group
					file
				method
					drive_mount
				action
					drive.mount
				alias
					none
				description
					Mounts a volume to make it accessible
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name name  type text
					[name path  type text  default none
				example
					[code [[drive.mount data]]  test false
					[code [[drive.mount .id /mnt/storage]]  test false
					[code [[drive.mount storage.iso E]]  test false
			drive.unmount
				group
					file
				method
					drive_unmount
				action
					drive.unmount
				alias
					none
				description
					Unmounts a volume
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name name  type text
				example
					[code [[drive.unmount storage]]  test false
					[code [[drive.unmount /mnt/storage]]  test false
					[code [[drive.unmount E]]  test false
			drive.resize
				group
					file
				method
					drive_resize
				action
					drive.resize
				alias
					none
				description
					Resizes an existing volume or partition
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name name  type text
					[name size  type [number text
				example
					[code [[drive.resize storage 100gb]]  test false
					[code [[drive.resize storage 100_000_000_000]]  test false
					[code [[drive.resize .partition.id 100gb]]  test false
			drive.check
				group
					file
				method
					drive_check
				action
					drive.check
				alias
					none
				description
					Checks the volume for errors and corrects them
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name path  type text
				example
					[code [[drive.check /mnt/storage]]  test false
					[code [[drive.check E]]  test false
			drive.defrag
				group
					file
				method
					drive_defrag
				action
					drive.defrag
				alias
					none
				description
					Defragments the files on the volume
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name path  type text
				example
					[code [[drive.defrag /mnt/storage]]  test false
					[code [[drive.defrag E]]  test false
			drive.os
				group
					file
				method
					drive_os
				action
					drive.os
				alias
					none
				description
					Makes the volume bootable or retrieves a list of available operating system images
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name path  type text
					[name os  type text  default none
				example
					[code [drive.os]  type list  test false
					[code [[drive.os /mnt/storage]]  test false
					[code [[drive.os /mnt/storage osname]]  test false
					[code [[drive.os /mnt/storage /path/to/os.iso]]  test false
			path
				group
					file
				method
					path
				action
					none
				alias
					none
				description
					Returns components of a specified path or builds a path
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name path  type [text list
					[name component  type text  subname true  default none
				example
					[code [[path /path/to/file.txt]]  type dict
					[code [[path.full path/to/file.txt]]  type text
					[code [[path.file /path/to/file.txt]]  result file.txt
					[code [[path.name /path/to/file.txt]]]  result file
					[code [[path.extension /path/to/file.txt]]  result txt
					[code [[path.extension /path/to/file.tar.gz]]  result gz
					[code [[path.dir /path/to/file.txt]]  result /path/to
					[code [[path.drive c:\path\to\file.txt]]  result C
					[code [[path.drive /mnt/data/file.txt]]  result data
					[code [[path.drive /Volumes/data/file.txt]]  result data
					[code [[path.strip file.txt]]  result file
					[code [[path.strip /path/to/file.tar.gz]]  result /path/to/file.tar
					[code [[path.strip /path/to/file.tar]]  result /path/to/file
					[code [[path.strip /path/to/file]]  result /path/to
					[code [[path.strip /path/to]]  result /path
					[code [[path.strip /path]]  result /
					[code [[path.build /path to file.txt]]  result /path/to/file.txt
					[code [[path /path to file.txt]]  result /path/to/file.txt
					[code [[path [/path to file.txt]]]  result /path/to/file.txt

		  .: format :.

			void
				group
					format
				method
					void
				action
					none
				alias
					none
				description
					Encodes data into the V O I D format
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name data  type any
					[name param  type dict  default none
				example
					[code [[void {'key':'value'}]]	result '{\n\t\'key\': \'value\'\n}']
					[code [[void [1,2,3] '	']]	result '[\n	1,\n	2,\n	3\n]']
			void.decode
				group
					format
				method
					void_decode
				action
					none
				alias
					none
				description
					Decodes data from the V O I D format
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name text  type text
					[name param  type dict  default none
				example
					[code [[void.decode '{\'key\':\'value\'}']]	result {'key':'value'}]
					[code [[void.decode '[1,2,3]']]	result [1,2,3]]
			json
				group
					format
				method
					json
				action
					none
				alias
					none
				description
					Encodes data into the JSON format
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name data  type any
					[name param  type [dict text]  default none
				example
					[code [[json.encode text]]  result "text"
					[code [[json.encode 'text\r\n\t']]  result text\r\n\t
					[code [[json.encode 123]]  result 123
					[code [[json.encode true]]  result 'true
					[code [[json.encode false]]  result 'false
					[code [[json.encode none]]  result null
					[code [[json.encode ☺ [unicode  false]]]  result "\u263A"
					[code [[json.encode [[name Thomas  age 25] [name Alice  age 20]] ]]  result [{"name":"Thomas","age":25},{"name":"Alice","age":20}]
					[code [[json.encode [[name Thomas  age 25] [name Alice  age 20]] short]]  result [{"name":"Thomas","age":25},{"name":"Alice","age":20}]
					[code [[json.encode [[name Thomas  age 25] [name Alice  age 20]] [indent  2]]]  result '[\n  {\n    "name": "Thomas",\n    "age": 25\n  },\n  {\n    "name": "Alice",\n    "age": 20\n  }\n]
					[code [[json.encode [[name Thomas  age 25] [name Alice  age 20]] 2]]  result '[\n  {\n    "name": "Thomas",\n    "age": 25\n  },\n  {\n    "name": "Alice",\n    "age": 20\n  }\n]
					[code [[json.encode [[name Thomas  age 25] [name Alice  age 20]] '\t']]  result '[\n\t{\n\t\t "name": "Thomas",\n\t\t"age": 25\n\t},\n\t{\n\t\t"name": "Alice",\n\t\t"age": 20\n\t}\n]
					[code [[json.encode [[name Thomas  age 25] [name Alice  age 20]] full]]  result '[\n\t{\n\t\t "name": "Thomas",\n\t\t"age": 25\n\t},\n\t{\n\t\t"name": "Alice",\n\t\t"age": 20\n\t}\n]
			json.decode
				group
					format
				method
					json_decode
				action
					none
				alias
					none
				description
					Decodes data from the JSON format
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name text  type text
					[name param  type [text dict]  default none
				example
					[code [[json.decode "text"]]  result text
					[code [[json.decode 123]]  result 123
					[code [[json.decode 'true']]  result true
					[code [[json.decode 'false']]  result false
					[code [[json.decode null]]  result none
					[code [[json.decode "\u263A"]]  result ☺
					[code [[json.decode [{"name":"Thomas","age":25},{"name":"Alice","age":20}] ]]  result [[name Thomas  age 25] [name Alice  age 20
			csv
				group
					format
				method
					csv
				action
					csv.encode
				alias
					none
				description
					Encodes data into the CSV format
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name data  type any
					[name param  type [text dict]  default [delimiter  ,]
				example
					[code [[csv [[Name Age] [Thomas 25] [Alice 20]] ]]  result 'Name,Age\nThomas,25\nAlice,20
					[code [[csv [[Name Age] [Thomas 25] [Alice 20]] ;]]  result 'Name;Age\nThomas;25\nAlice;20
					[code [[csv [[Name Age] [Thomas 25] [Alice 20]] [delimiter  ;]]]  result 'Name;Age\nThomas;25\nAlice;20
					[code [[csv [[text text"text]] ]]  result text,"text""text"
			csv.decode
				group
					format
				method
					csv_decode
				action
					csv.decode
				alias
					none
				description
					Decodes data from the CSV format
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name text  type text
					[name param  type dict  default [delimiter  ,]
				example
					[code [[csv.decode 'Name,Age\nThomas,25\nAlice,20']]  result [[Name Age] [Thomas 25] [Alice 20
					[code [[csv.decode 'Name;Age\nThomas;25\nAlice;20' ;]]  result [[Name Age] [Thomas 25] [Alice 20
					[code [[csv.decode text,"text""text" ]]  result [[text text"text]]
			yaml
				group
					format
				method
					yaml
				action
					none
				alias
					none
				description
					Encodes data into the YAML format
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++
				param
					[name data  type any
					[name param  type [text dict]  default none
				example
					[code [[yaml.encode text]]  result text
					[code [[yaml.encode 'text\r\n\t']]  result "text\r\n\t"
					[code [[yaml.encode 123]]  result 123
					[code [[yaml.encode true]]  result 'true
					[code [[yaml.encode false]]  result 'false
					[code [[yaml.encode none]]  result null
					[code [[yaml.encode ☺ [unicode  false]]]  result "\u263A"
					[code [[yaml.encode [[name Thomas  age 25] [name Alice  age 20]] ]]  result '- name: Thomas\n  age: 25\n- name: Alice\n  age: 20
					[code [[yaml.encode [[name Thomas  age 25] [name Alice  age 20]] full]]  result '- name: Thomas\n  age: 25\n- name: Alice\n  age: 20
					[code [[yaml.encode [[name Thomas  age 25] [name Alice  age 20]] short]]  result [{"name":"Thomas","age":25},{"name":"Alice","age":20}]
			yaml.decode
				group
					format
				method
					yaml_decode
				action
					none
				alias
					none
				description
					Decodes data from the YAML format
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++
				param
					[name text  type text
					[name param  type dict  default none
				example
					[code [[yaml.decode text]]  result text
					[code [[yaml.decode 123]]  result 123
					[code [[yaml.decode 'true']]  result true
					[code [[yaml.decode 'false']]  result false
					[code [[yaml.decode null]]  result none
					[code [[yaml.decode "\u263A"]]  result ☺
					[code [[yaml.decode '- name: Thomas\n  age: 25\n- name: Alice\n  age: 20']]  result [[name Thomas  age 25] [name Alice  age 20
					[code [[yaml.decode '[{"name":"Thomas","age":25},{"name":"Alice","age":20}]']]  result [[name Thomas  age 25] [name Alice  age 20
			xml
				group
					format
				method
					xml
				action
					xml.encode
				alias
					none
				description
					Encodes data into the XML format
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name data  type any
					[name param  type dict  default [attribute  @]
				example
					[code [[xml [root  item [a b]]]]  result '<root><item>a</item><item>b</item></root>
					[code [[xml [person  [@id 1  name Thomas]]]]  result '<person id="1"><name>John</name></person>
					[code [[xml [person  [#id 1  name Thomas]] [attribute  #]]]  result '<person id="1"><name>John</name></person>
			xml.decode
				group
					format
				method
					xml_decode
				action
					xml.decode
				alias
					none
				description
					Decodes data from the XML format
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name text  type text
					[name param  type dict  default [attribute  @]
				example
					[code [[xml.decode '<root><item>a</item><item>b</item></root>']]  result [root  item [a b
					[code [[xml.decode '<person id="1"><name>Thomas</name></person>']]  result [person  [@id 1  name Thomas
					[code [[xml.decode '<person id="1"><name>Thomas</name></person>' [attribute  #]]]  result [person  [#id 1  name Thomas
			ini
				group
					format
				method
					ini
				action
					ini.encode
				alias
					none
				description
					Encodes data into the INI format
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name data  type any
					[name param  type dict  default [delimiter  ,]
				example
					[code [[ini [section  [name  data]]]]  result '[section]\nname=data
					[code [[ini [user  [name Thomas  task [10 20 30]]] ]]  result '[user]\nname=Thomas\ntask=10,20,30
					[code [[ini [user  [name Thomas  task [10 20 30]]] |]]  result '[user]\nname=Thomas\ntask=10|20|30
					[code [[ini [user  [name Thomas  task [10 20 30]]] [list  |]]]  result '[user]\nname=Thomas\ntask=10|20|30
			ini.decode
				group
					format
				method
					ini_decode
				action
					ini.decode
				alias
					none
				description
					Decodes data from the INI format
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name text  type text
					[name param  type dict  default [delimiter  ,]
				example
					[code [[ini.decode '[section]\nname=data']]  result [section  [name  data
					[code [[ini.decode '[user]\nname=Thomas\ntask=10,20,30']]  result [user  [name Thomas  task [10 20 30
					[code [[ini.decode '[user]\nname=Thomas\ntask=10,20,30' none]]  result [user  [name Thomas  task 10,20,30

		  .: cloud :.

			cloud
				group
					cloud
				method
					cloud
				action
					none
				alias
					none
				description
					Runs cloud services for data management
				safe
					false
				container
					true
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name type  type text  default none
					[name param  type any  default none
				example
					[code [cloud]  test false
					[code [cloud.file]  test false
					[code [[cloud.file /path/to/share]]  test false
					[code [cloud.web]  test false
					[code [[cloud.web .param]]  test false
					[code [[cloud.api .param]]  test false
					[code [[cloud.mail .param]]  test false
					[code [[cloud.proxy .param]]  test false
					[code [[cloud.vpn .param]]  test false
					[code [[cloud.desktop .param]]  test false
			request
				group
					cloud
				method
					request
				action
					none
				alias
					r
				description
					Sends an HTTP request to a specified URL
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name url  type text
					[name param  type dict  default none
					[name method  type text  subname true  default none
				example
					[code [[r https://voidsp.com]]	type dict  test false
					[code [[r.get https://voidsp.com]]	type dict	test false
					[code [[r https://voidsp.com [method post  header [key .key  name .name]  type json  data [1 2 3] ]]]  type dict  test false
					[code [[r.post [url https://voidsp.com  header [key .key  Content-Type multipart/form-data]  form [name .name  data .data] ]]]  type dict  test false
					[code [[info https://voidsp.com]]  type dict  test false
			download
				group
					cloud
				method
					download
				action
					none
				alias
					d
				description
					Downloads content from a specified URL
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name url  type [text list
					[name path  type text  default none
					[name component  type text  subname true  default none
				example
					[code [[d https://voidsp.com/video.mp4]]  test false
					[code [[d https://voidsp.com/video.mp4 /path/to/download.mp4]]  test false
					[code [[d youtube.com/watch?v=12345ABCDEF]]  test false
					[code [[d.info youtube.com/watch?v=12345ABCDEF]]  type dict  test false
					[code [[d.720 youtube.com/watch?v=12345ABCDEF]]  test false
					[code [[d.video youtube.com/watch?v=12345ABCDEF]]  test false
					[code [[d.video.720 youtube.com/watch?v=12345ABCDEF]]  test false
					[code [[d.sound youtube.com/watch?v=12345ABCDEF]]  test false
					[code [[d.subtitle youtube.com/watch?v=12345ABCDEF]]  test false
					[code [[info youtube.com/watch?v=12345ABCDEF]]  type dict  test false
			cookie
				group
					cloud
				method
					cookie
				action
					none
				alias
					cookie.remove
				description
					Receives or sets a specified cookie
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++
				param
					[name name  type text
					[name data  type any  default none
					[name param  type any  subname true  default none
				example
					[code [cookie]  test false
					[code [[cookie session]]  test false
					[code [[cookie session .session.id]]  test false
					[code [[cookie session .session.id 86400]]  test false
					[code [[cookie session .session.id day]]  test false
					[code [[cookie session .session.id 1776865494]]  test false
					[code [[cookie [name session  data .session.id  expired day  domain /]]]  test false
					[code [[cookie session none 0]]  test false
					[code [[cookie.remove session]]  test false
			notify
				group
					cloud
				method
					notify
				action
					none
				alias
					none
				description
					Send notification
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name message  type any  default none
					[name name  type text  subname true  default none
				example
					[code [notify]  test false
					[code [[notify message]]  test false
					[code [[notify.os message]]  test false
					[code [[notify.push .token message]]  test false
					[code [[notify.push [token .token  text message  sound sound.wav  badge 3  image .image]]  test false
					[code [[notify.mail to@voidsp.com message]]  test false
					[code [[notify.mail [to [to1@voidsp.com to2@voidsp.com]  text .html  from from@voidsp.com  copy copy@mvoidsp.com  attachment [.file1 .file2]]]  test false
					[code [[notify.sms +123456789 message]]  test false
					[code [[notify.call +123456789 message]]  test false
					[code [[notify.social.telegram account message]]  test false
					[code [[notify.telegram account message]]  test false
			social
				group
					cloud
				method
					social
				action
					none
				alias
					none
				description
					Interact with social API or get a list of available social networks
				safe
					false
				container
					true
				language
					[python js swift kotlin gdscript c++
				param
					[name name  type text  subname true  default none
					[name data  type dict  default none
				example
					[code [social]  type list
					[code [[social telegram.bot [name bot  token .token  action .action]]  test false
					[code [[social telegram.send [token .token  to .account  text .text  attachment [.image1 .image2]]]  test false
					[code [[social.youtube.upload [token .token  title .title  description .desctipion  tags .tags  video .video  publish true]]]  test false
					[code [[social.tiktok.upload [token .token  title .title  description .desctipion  tags .tags  video .video  publish true]]]  test false

		  .: device :.

			device
				group
					device
				method
					device
				action
					none
				alias
					none
				description
					Retrieves or sets hardware device parameters
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name name  type text  subname true  default none
					[name data  type any  default none
				example
					[code [device]  type dict
					[code [[device name]]  type dict
					[code [device.name]  type dict
					[code [[device orientation landscape]]  test false
					[code [[device.orientation landscape]]  test false
			cpu
				group
					device
				method
					cpu
				action
					none
				alias
					none
				description
					Current CPU usage
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[]
				example
					[[code [cpu]  type number
			gpu
				group
					device
				method
					gpu
				action
					none
				alias
					none
				description
					Current GPU usage
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++
				param
					[]
				example
					[[code [gpu]  type number
			memory
				group
					device
				method
					memory
				action
					none
				alias
					none
				description
					Current memory usage
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[]
				example
					[[code [memory]  type dict
			battery
				group
					device
				method
					battery
				action
					none
				alias
					none
				description
					Remaining battery charge
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++
				param
					[]
				example
					[[code [battery]  type number
			fps
				group
					device
				method
					fps
				action
					none
				alias
					none
				description
					Retrieves or sets frames per second for video or graphical rendering
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name fps  type number  default none
				example
					[code [fps]  type number
					[code [[fps 60]]  test false
			vsync
				group
					device
				method
					vsync
				action
					none
				alias
					none
				description
					Vertical sync settings to prevent screen tearing
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name vsync  type bool  subname true  default none
				example
					[code [vsync]  type bool
					[code [[vsync true]]  test false
					[code [vsync.on]  test false
					[code [vsync.off]  test false
					[code [vsync.toggle]  test false
			resolution
				group
					device
				method
					resolution
				action
					none
				alias
					none
				description
					Retrieves or stes the screen resolution
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name resolution  type list  default none
				example
					[code [resolution]  type list  test false
					[code [[resolution [1920 1080]]]  test false
					[code [[resolution 1920 1080]]  test false
			orientation
				group
					device
				method
					orientation
				action
					none
				alias
					none
				description
					Retrieves or stes the orientation of a device's display
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++
				param
					[[name orientation  type text  default none
				example
					[code [orientation]  type text  test false
					[code [[orientation portrait]]  test false
					[code [[orientation landscape]]  test false
					[code [[orientation portrait upside down]]  test false
			dark
				group
					device
				method
					dark
				action
					none
				alias
					none
				description
					Retrieves or stes the dark mode setting for user interfaces
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name dark  type bool  default none
				example
					[code [dark]  type bool  test false
					[code [[dark true]]  test false
					[code [[dark on]]  test false
					[code [[dark.off]]  test false
					[code [[dark.toggle]]  test false
			pixel
				group
					device
				method
					pixel
				action
					none
				alias
					none
				description
					Retrieves or sets the color of the pixel displayed on the screen
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name position  type list
					[name color  type [text list]  default none
				example
					[code [[pixel [10 10]]]  type list  test false
					[code [[pixel 10 10]]  type list  test false
					[code [[pixel [10 10] green]]  type list  test false
					[code [[pixel 10 10 green]]  type list  test false
					[code [[pixel [10 10] green]]  type list  test false
					[code [[pixel [10 10] [100 150 200]]]  type list  test false
					[code [[pixel [10 10] [0.39 0.59 0.78]]]  type list  test false
			symbol
				group
					device
				method
					symbol
				action
					none
				alias
					clear
				description
					Retrieves or sets the symbol on the screen in text mode
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name position  type list
					[name symbol  type text  default none
				example
					[code [[symbol [10 10]]]  type text  test false
					[code [[symbol 10 10]]  type text  test false
					[code [[symbol [10 10] A]]  type text  test false
					[code [[symbol 10 10 A]]  type text  test false
					[code [clear]  test false
			cursor
				group
					device
				method
					cursor
				action
					none
				alias
					none
				description
					Retrieves or sets the cursor position on the screen and its visibility in text mode
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name position  type list  default none
					[name visibility  type bool  subname true  default none
				example
					[code [cursor]  type list  test false
					[code [[cursor [10 10]]]  test false
					[code [[cursor 10 10]]  test false
					[code [[cursor [10 10] true]]  test false
					[code [[cursor [10 10] hide]]  test false
					[code [cursor.visibility]  type bool  test false
					[code [cursor.show]  test false
					[code [cursor.hide]  test false
					[code [[cursor show]]  test false
					[code [[cursor hide]]  test false
			camera
				group
					device
				method
					camera
				action
					none
				alias
					cam
				description
					Capturing image and video from a built-in or external camera
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name name  type text  subname true  default none
				example
					[code [camera]  test false
					[code [camera.name]  test false
					[code [camera.image]  test false
					[code [camera.record]  test false
					[code [camera.stop]  test false
			microphone
				group
					device
				method
					camera
				action
					none
				alias
					mic
				description
					Capturing audio from a built-in or external microphone
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name name  type text  subname true  default none
				example
					[code [mic]  test false
					[code [mic.name]  test false
					[code [mic.record]  test false
					[code [mic.stop]  test false
			flashlight
				group
					device
				method
					flashlight
				action
					none
				alias
					none
				description
					Turns on or off the device's flashlight
				safe
					false
				container
					none
				language
					[swift kotlin gdscript c++
				param
					[[name level  type [number bool]  subname true  default none
				example
					[code [flashlight]  test false
					[code [[flashlight true]]  test false
					[code [flashlight.on]  test false
					[code [flashlight.off]  test false
					[code [flashlight.toggle]  test false
					[code [[flashlight 0.8]]  test false
					[code [[flashlight 80%]]  test false
			location
				group
					device
				method
					location
				action
					none
				alias
					none
				description
					Retrieves the current geographic location using GPS or network triangulation
				safe
					false
				container
					none
				language
					[js swift kotlin gdscript c++
				param
					[[name switch  type bool  default none
				example
					[code [location]  type dict  test false
					[code [[location true]]  test false
					[code [location.on]  test false
					[code [location.off]  test false
			accelerometer
				group
					device
				method
					accelerometer
				action
					none
				alias
					none
				description
					Provides access to the accelerometer sensor to detect acceleration forces
				safe
					false
				container
					none
				language
					[js swift kotlin gdscript c++
				param
					[]
				example
					[[code [accelerometer]  type dict  test false
			compass
				group
					device
				method
					compass
				action
					none
				alias
					none
				description
					Accesses the magnetic compass sensor to determine orientation relative to the Earth's magnetic field
				safe
					false
				container
					none
				language
					[js swift kotlin gdscript c++
				param
					[name latitude  type number  default none
					[name longitude  type number  default none
				example
					[code [compass]  type number  test false
					[code [[compass [40 30]]]  type number  test false
					[code [[compass 40 30]]  type number  test false
			gyroscope
				group
					device
				method
					gyroscope
				action
					none
				alias
					none
				description
					Provides access to the gyroscope sensor for motion detection
				safe
					false
				container
					none
				language
					[js swift kotlin gdscript c++
				param
					[]
				example
					[[code [gyroscope]  type dict  test false
			proximity
				group
					device
				method
					proximity
				action
					none
				alias
					none
				description
					Detects the proximity of objects in relation to the device's proximity sensor
				safe
					false
				container
					none
				language
					[swift kotlin gdscript c++
				param
					[[name distance  type number  default none
				example
					[code [proximity]  type dict  test false
					[code [[proximity 0.5]  type number  test false
			brightness
				group
					device
				method
					brightness
				action
					none
				alias
					none
				description
					Manages the screen brightness level of the device
				safe
					false
				container
					none
				language
					[swift kotlin gdscript c++
				param
					[[name level  type number  default none
				example
					[code [brightness]  type number  test false
					[code [[brightness 0.8]]  type number  test false
					[code [[brightness 80%]]  type number  test false
			volume
				group
					device
				method
					volume
				action
					none
				alias
					none
				description
					Manages the sound level of the device
				safe
					false
				container
					none
				language
					[swift kotlin gdscript c++
				param
					[name level  type number  default none
					[name name  type text  subname true  default true
				example
					[code [volume]  type number  test false
					[code [[volume 0.8]]  test false
					[code [[volume 80%]]  test false
					[code [volume.music]  type number  test false
					[code [[volume 0.8 music]]  test false
			calendar
				group
					device
				method
					calendar
				action
					none
				alias
					none
				description
					Calendar events on a device
				safe
					false
				container
					none
				language
					[swift kotlin gdscript c++
				param
					[name date  type [text number]  default none
					[name time  type [text number]  default none
					[name text  type text  default none
					[name param  type [text dict]  default none
					[name action  type text  subname true  default none
				example
					[code [calendar]  type dict  test false
					[code [[calendar 2026.01.01]]  type dict  test false
					[code [[calendar 2026.01.01 11:30]]  type dict  test false
					[code [[calendar 2026.01.01 11:30-12:30 meeting]]  test false
					[code [[calendar 2026.01.01 11:30-12:30 meeting alert]]  test false
					[code [[calendar.remove 2026.01.01 11:30]]  test false
					[code [[calendar.clear]]  test false
			gallery
				group
					device
				method
					gallery
				action
					none
				alias
					none
				description
					Photo and video library on a device
				safe
					false
				container
					none
				language
					[swift kotlin gdscript c++
				param
					[name data  type [text number binary list dict]  default none
					[name action  type text  subname true  default none
				example
					[code [gallery]  type dict  test false
					[code [[gallery 10]]  type list  test false
					[code [[gallery 2026.01.01]]  type list  test false
					[code [[gallery .id]]  type dict  test false
					[code [[gallery .image]]  type dict  test false
					[code [[gallery.remove .id]]  test false
			contacts
				group
					device
				method
					contacts
				action
					none
				alias
					none
				description
					Contact list on a device
				safe
					false
				container
					none
				language
					[swift kotlin gdscript c++
				param
					[name data  type [text number dict]  default none
					[name action  type text  subname true  default none
				example
					[code [contacts]  type dict  test false
					[code [[contacts .id]]  type dict  test false
					[code [[contacts [name Thomas  phone +123456789]]]  test false
					[code [[contacts.remove .id]]  type dict  test false
			call
				group
					device
				method
					call
				action
					none
				alias
					none
				description
					Initiate a voice or video call to a specified recipient
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++
				param
					[]
				example
					[code [call]  test false
					[code [[call +123456789]]  test false
			sms
				group
					device
				method
					sms
				action
					none
				alias
					none
				description
					Send a text message (SMS) to a specified recipient
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++
				param
					[]
				example
					[code [sms]  test false
					[code [[sms +123456789 Hi!]]  test false
			net
				group
					device
				method
					net
				action
					none
				alias
					none
				description
					Retrieves information about Network or connect
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name action  type text  subname true  default none
					[name name  type text  default none
				example
					[code [net]  type dict  test false
					[code [net.connect]  test false
					[code [[net.connect name]]  test false
					[code [net.disconnect]  test false
			wifi
				group
					device
				method
					wifi
				action
					none
				alias
					none
				description
					Retrieves information about Wi-Fi or connect
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++
				param
					[name action  type text  subname true  default none
					[name name  type text  default none
					[name password  type text  default none
				example
					[code [wifi]  type dict  test false
					[code [[wifi.connect name]]  test false
					[code [[wifi.connect name password]]  test false
					[code [wifi.disconnect]  test false
			bluetooth
				group
					device
				method
					bluetooth
				action
					none
				alias
					none
				description
					Retrieves information about Bluetooth or connect
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++
				param
					[name action  type text  subname true  default none
					[name name  type text  default none
					[name data  type any  default none
				example
					[code [bluetooth]  type dict  test false
					[code [[bluetooth.connect name]]  test false
					[code [[bluetooth.send name .data]]  test false
					[code [bluetooth.disconnect]  test false
			cellular
				group
					device
				method
					cellular
				action
					none
				alias
					none
				description
					Retrieves information about Cellular or connect
				safe
					false
				container
					none
				language
					[python js swift kotlin gdscript c++
				param
					[name action  type text  subname true  default none
					[name name  type text  default none
				example
					[code [cellular]  type dict  test false
					[code [cellular.connect]  test false
					[code [[cellular.connect name]]  test false
					[code [cellular.disconnect]  test false
			keyboard
				group
					device
				method
					keyboard
				action
					none
				alias
					key
				description
					Keyboard information
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[[name action  type text  default none
				example
					[code [keyboard]  test false
					[code [keyboard.show]  test false
					[code [keyboard.hide]  test false
					[code [keyboard.toggle]  test false
					[code [keyboard.size]  test false
					[code [key.a [[. key A pressed]]]  test false
					[code [key.space [[. key SPACE pressed]]]  test false
					[code [key.esc [[. key ESC pressed]]]  test false
					[code [key.shift.a [[. key SHIFT+A pressed]]]  test false
			mouse
				group
					device
				method
					mouse
				action
					none
				alias
					none
				description
					Mouse information
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[name action  type text  subname true  default none
					[name data  type any  default none
				example
					[code [mouse]  test false
					[code [mouse.show]  test false
					[code [mouse.hide]  test false
					[code [mouse.toggle]  test false
					[code [mouse.cursor]  test false
					[code [[mouse.cursor wait]]  test false
					[code [[mouse.cursor hand]]  test false
					[code [mouse.wait]  test false
					[code [mouse.hand]  test false
					[code [mouse.normal]  test false
					[code [mouse.position]  type dict  test false
					[code [[mouse.left [[. left button pressed]]]]  test false
					[code [[mouse.right [[. right button pressed]]]]  test false
					[code [[mouse.middle [[. middle button pressed]]]]  test false
					[code [[mouse.scroll [[. scroll]]]]  test false
					[code [[mouse.scroll.up [[. scroll up]]]]  test false
					[code [[mouse.scroll.down [[. scroll up]]]]  test false
			gamepad
				group
					device
				method
					gamepad
				action
					none
				alias
					none
				description
					Gamepad information
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++
				param
					[]
				example
					[[code [gamepad]  type dict  test false
			tap
				group
					device
				method
					tap
				action
					none
				alias
					click
				description
					Simulates a tap or click gesture
				safe
					true
				container
					none
				language
					[python js swift kotlin gdscript c++
				param
					[name position  type [text number list]  default none
					[name duration  type number  default none
					[name gesture  type text  subname true  default none
				example
					[code [tap]  test false
					[code [[tap 100 100]]  test false
					[code [[tap [100 100]]]  test false
					[code [[tap 100 100 0.5]]  test false
					[code [tap 0.5]  test false
					[code [tap.long]  test false
					[code [tap.double]  test false
					[code [tap.zoomin 0.5]  test false
					[code [tap.zoomout 0.5]  test false
					[code [tap.rotate 180]  test false
					[code [tap.rotate -180]  test false
					[code [tap.scroll 10%]  test false
					[code [tap.key.a]  test false
					[code [tap.key.shift.a]  test false
					[code [tap.mouse.left]  test false
					[code [tap.gamepad.x]  test false
					[code [tap.gamepad.left]  test false


		  .: content :.

			image
				group
					content
				method
					image
				action
					none
				alias
					none
				description
					Create an image
				safe
					true
				container
					crop
						[ ]
					size
						[ ]
					zoom
						[ ]
					flip
						[ ]
					rotate
						[ ]
					grayscale
						[ ]
					rgb
						[ ]
					yuv
						[ ]
					indexed
						[ ]
					color
						[ ]
					levels
						[ ]
					curves
						[ ]
					monochrome
						[ ]
					brightness
						[ ]
					contrast
						[ ]
					hue
						[ ]
					saturation
						[ ]
					lightness
						[ ]
					sharpness
						[ ]
					vignette
						[ ]
					style
						[ ]
					blur
						[ ]
					distort
						[ ]
					noise
						[ ]
					border
						[ ]
					fill
						[ ]
					paint
						[ ]
					bezier
						[ ]
					select
						[ ]
					copy
						[ ]
					paste
						[ ]
					mask
						[ ]
					text
						[ ]
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[]
				example
					[]
			video
				group
					content
				method
					video
				action
					none
				alias
					movie
					clip
					anime
				description
					Create a video
				safe
					true
				container
					speed
						[ ]
					reverse
						[ ]
					mute
						[ ]
					gain
						[ ]
					pan
						[ ]
					pitch
						[ ]
					fade.in
						[ ]
					fade.out
						[ ]
					crop
						[ ]
					size
						[ ]
					zoom
						[ ]
					flip
						[ ]
					rotate
						[ ]
					grayscale
						[ ]
					color
						[ ]
					levels
						[ ]
					curves
						[ ]
					monochrome
						[ ]
					brightness
						[ ]
					contrast
						[ ]
					hue
						[ ]
					saturation
						[ ]
					lightness
						[ ]
					sharpness
						[ ]
					vignette
						[ ]
					style
						[ ]
					blur
						[ ]
					distort
						[ ]
					noise
						[ ]
					border
						[ ]
					fill
						[ ]
					paint
						[ ]
					bezier
						[ ]
					select
						[ ]
					copy
						[ ]
					paste
						[ ]
					mask
						[ ]
					text
						[ ]
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[]
				example
					[]
			sound
				group
					content
				method
					sound
				action
					none
				alias
					music
				description
					Create an audio track
				safe
					true
				container
					speed
						[ ]
					reverse
						[ ]
					mute
						[ ]
					gain
						[ ]
					pan
						[ ]
					pitch
						[ ]
					fade.in
						[ ]
					fade.out
						[ ]
					crop
						[ ]
					clean
						[ ]
					novoice
						[ ]
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[]
				example
					[]
			model
				group
					content
				method
					model
				action
					none
				alias
					none
				description
					Create a 3D model
				safe
					true
				container
					true
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[]
				example
					[]
			book
				group
					content
				method
					book
				action
					none
				alias
					document
					spreadsheet
					presentation
					comics
					manga
				description
					Create a book, comic or manga
				safe
					true
				container
					true
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[]
				example
					[]
			game
				group
					content
				method
					game
				action
					none
				alias
					2d
					3d
					vn
				description
					Create a 2D, 3D or visual novel game
				safe
					true
				container
					true
				language
					[python js swift kotlin gdscript c++ asm86
				param
					[]
				example
					[]
		pi
			3.14159265358979323846
		e
			2.71828182845904523536
		phi
			1.61803398874989484820
		gamma
			0.57721566490153286060
		os
			none
		language
			none
		app
			os
				type
				name
				version
				user
				language
				delimiter
					path
						/
					line
						'\n
				path
					ffmpeg
						none
					yt-dlp
						none
			device
				name
				imei
				fps
				cpu
				gpu
			file
			path
			param
			ui
				cli
			cli
				color
					true
				indent
					2
			stopwatch
				[ ]
			timer
				[ ]
			cloud
				mime

				  .: data :.

					void
						application/void
					json
						application/json
					jsonl
						application/jsonl
					jsonld
						application/ld+json
					yaml
						application/x-yaml
					xml
						application/xml
					csv
						text/csv
					ini
						text/plain
					sql
						application/sql
					log
						text/plain
					bin
						application/octet-stream

				  .: document :.

					text
						text/plain
					txt
						text/plain
					pdf
						application/pdf
					djvu
						image/vnd.djvu
					doc
						application/msword
					docx
						application/vnd.openxmlformats-officedocument.wordprocessingml.document
					xls
						application/vnd.ms-excel
					xlsx
						application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
					ppt
						application/vnd.ms-powerpoint
					pptx
						application/vnd.openxmlformats-officedocument.presentationml.presentation
					rtf
						application/rtf
					epub
						application/epub+zip
					abw
						application/x-abiword
					azw
						application/vnd.amazon.ebook
					odp
						application/vnd.oasis.opendocument.presentation
					ods
						application/vnd.oasis.opendocument.spreadsheet
					odt
						application/vnd.oasis.opendocument.text
					ics
						text/calendar

				  .: html :.

					html
						text/html
					htm
						text/html
					xhtml
						application/xhtml+xml
					css
						text/css

				  .: font :.

					ttf
						font/ttf
					otf
						font/otf
					sfnt
						font/sfnt
					woff
						font/woff
					woff2
						font/woff2
					eot
						application/vnd.ms-fontobject

				  .: subtitle :.

					vtt
						text/vtt
					srt
						application/x-subrip
					ass
						text/x-ssa
					ssa
						text/x-ssa
					ttml
						application/ttml+xml
					sub
						text/x-microdvd
					smi
						application/x-sami
					sami
						application/x-sami

				  .: image :.

					jpeg
						image/jpeg
					jpg
						image/jpeg
					png
						image/png
					apng
						image/apng
					gif
						image/gif
					svg
						image/svg+xml
					webp
						image/webp
					heif
						image/heif
					heic
						image/heic
					tiff
						image/tiff
					tif
						image/tiff
					avif
						image/avif
					ico
						image/x-icon
					icon
						image/vnd.microsoft.icon
					icns
						image/x-icns

				  .: audio :.

					mp3
						audio/mpeg
					mpa
						audio/mpeg
					mp2
						audio/mpeg
					wma
						audio/x-ms-wma
					wav
						audio/x-wav
					flac
						audio/flac
					ogg
						application/ogg
					oga
						audio/ogg
					weba
						audio/webm
					cda
						application/x-cdf
					aac
						audio/aac
					ac3
						audio/ac3
					mid
						audio/midi
					midi
						audio/x-midi
					s3m
						audio/s3m
					it
						audio/it
					mod
						audio/x-mod
					xm
						audio/xm

				  .: video :.

					mp4
						video/mp4
					mpeg
						video/mpeg
					mpg
						video/mpeg
					mpv
						video/mpeg
					webm
						video/webm
					ogx
						application/ogg
					ogv
						video/ogg
					qt
						video/quicktime
					mov
						ideo/quicktime
					m4v
						video/x-m4v
					wmv
						video/x-ms-wmv
					avi
						video/x-msvideo
					mkv
						application/x-matroska
					mjpeg
						multipart/x-mixed-replace
					ts
						video/mp2t

				  .: 3d :.

					gltf
						model/gltf+json
					glb
						model/gltf-binary
					obj
						model/obj
					stl
						model/stl
					fbx
						application/vnd.autodesk.fbx
					dae
						model/vnd.collada+xml
					3ds
						model/x-3ds
					ply
						model/ply
					usd
						model/vnd.usd
					usdz
						model/vnd.usdz+zip
					x3d
						model/x3d+xml
					wrl
						model/vrml
					vrml
						model/vrml

				  .: archive :.

					zip
						application/zip
					gz
						application/gzip
					7z
						application/x-7z-compressed
					tar
						application/x-tar
					rar
						application/vnd.rar
					bz
						application/x-bzip
					bz2
						application/x-bzip2

				  .: code :.

					py
						applycation/x-python-code
					php
						application/x-httpd-php
					java
						application/java
					jar
						application/java-archive
					kt
						text/x-kotlin
					swift
						application/swift
					m
						text/x-objective-c
					mm
						text/x-objective-c++
					c
						text/x-csrc
					cpp
						text/x-c++src
					h
						text/x-chdr
					cs
						text/x-csharp
					rs
						text/rust
					gd
						text/x-gdscript
					js
						text/javascript
					mjs
						text/javascript
					lua
						text/x-lua
					sh
						application/x-sh
					csh
						application/x-csh
					bat
						application/x-bat

				  .: form :.

					form data
						multipart/form-data
					form mixed
						multipart/mixed
					form alternative
						multipart/alternative
					form text
						application/x-www-form-urlencoded
				code
					100
						Continue
					101
						Switching protocols
					102
						Processing
					103
						Early Hints
					200
						OK
					201
						Created
					202
						Accepted
					203
						Non-Authoritative Information
					204
						No Content
					205
						Reset Content
					206
						Partial Content
					207
						Multi-Status
					208
						Already Reported
					226
						IM Used
					300
						Multiple Choices
					301
						Moved Permanently
					302
						Found Redirection
					303
						See Other
					304
						Not Modified
					305
						Use Proxy
					306
						Switch Proxy
					307
						Temporary Redirect
					308
						Permanent Redirect
					400
						Bad Request
					401
						Unauthorized
					402
						Payment Required
					403
						Forbidden
					404
						Not Found
					405
						Method Not Allowed
					406
						Not Acceptable
					407
						Proxy Authentication Required
					408
						Request Timeout
					409
						Conflict
					410
						Gone
					411
						Length Required
					412
						Precondition Failed
					413
						Payload Too Large
					414
						URI Too Long
					415
						Unsupported Media Type
					416
						Range Not Satisfiable
					417
						Expectation Failed
					418
						I'm a Teapot
					421
						Misdirected Request
					422
						Unprocessable Entity
					423
						Locked
					424
						Failed Dependency
					425
						Too Early
					426
						Upgrade Required
					428
						Precondition Required
					429
						Too Many Requests
					431
						Request Header Fields Too Large
					451
						Unavailable For Legal Reasons
					500
						Internal Server Error
					501
						Not Implemented
					502
						Bad Gateway
					503
						Service Unavailable
					504
						Gateway Timeout
					505
						HTTP Version Not Supported
					506
						Variant Also Negotiates
					507
						Insufficient Storage
					508
						Loop Detected
					510
						Not Extended
					511
						Network Authentication Required
			db
				[ ]
			log
				none
			format
				text
					json
					jsonl
					jsonld
					yaml
					csv
					ini
					xml
					sql
					log
					text
					txt
					vtt
					srt
					ass
					ssa
					ttml
					sub
					smi
					sami
					html
					htm
					xhtml
					css
					py
					php
					java
					kt
					swift
					m
					mm
					c
					cpp
					h
					cs
					rs
					gd
					js
					mjs
					lua
					sh
					csh
					bat
			ai
				chatgpt
					key
					url
				deepeek
					key
					url
				ollama
					key
					url
				claude
					key
					url
				gemini
					key
					url
			void
				[ ]
		run
			[]
		action
			convert
				[]
			info
				[]
			test
				[]
			drive
				mount
					[? .os
						[[mac linux]
							[]
					]
						windows
							[]
				unmount
					[? .os
						[[mac linux]
							[]
					]
						windows
							[]
				create
					[? .os
						[[mac linux]
							[]
					]
						windows
							[]
				resize
					[? .os
						[[mac linux]
							[]
					]
						windows
							[]
				clear
					[? .os
						[[mac linux]
							[]
					]
						windows
							[]
				remove
					[? .os
						[[mac linux]
							[]
					]
						windows
							[]
			csv
				encode
					[]
				decode
					[parse .text .parse.csv
					__
			xml
				encode
					[]
				decode
					[parse .text .parse.xml
					__
			ini
				encode
					[]
				decode
					[parse .text .parse.ini
					__
			download
				[]
		text
			void
				language
					en
						English
					ru
						Русский
					zh
						...
				memory
					b
					kb
					mb
					gb
					tb
					eb
					pb
	'''

	modules = {}

  # module

	@classmethod
	def module(cls, name: str, name_install: str = None):
		if name in cls.modules:
			return cls.modules[name]
		try:
			module = importlib.import_module(name)
			cls.modules[name] = module
			return module
		except ImportError:
			if name_install is None:
				name_install = name
			candidates = [
				[sys.executable, '-m', 'pip', 'install', name_install] + (['--break-system-packages'] if sys.platform != 'win32' else []),
				['pip3', 'install', name_install],
				['pip', 'install', name_install]
			]
			for cmd in candidates:
				try:
					result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
					if result.returncode == 0:
						break
				except Exception:
					pass
			else:
				cls.xx('module', 'not installed', name)
			os.execv(sys.executable, [sys.executable] + sys.argv)
			cls.exit()


  # run

	@classmethod
	def run(cls):
		cls.t('run')
		file = sys.argv[0]
		path = os.getcwd()
		param = sys.argv[1:]
		param = [cls.void_decode(text) for text in param]
		cls.set('app.file', file)
		cls.set('app.path', path)
		cls.set('app.param', param)
		match platform.system():
			case 'Windows':
				os_type = 'windows'
			case 'Linux':
				os_type = 'linux'
			case 'Darwin':
				os_type = 'mac'
			case _:
				os_type = 'unknown'
		cls.set('os', os_type)
		cls.set('app.os.type', os_type)
		cls.random_reseed()
		if len(param) > 0:
			name = str(param[0]).strip()
			result = None
			if cls.path_extension(name, 'py') and cls.file_exists(name):
				cls.code(cls.file(name))
			elif cls.path_extension(name, 'void', 'json', 'yaml') and cls.file_exists(name):
				result = cls.action(cls.file(name))
			elif cls.path_extension(name, 'zip') and cls.file_exists(name):
				path_extract = cls.path(cls.path_dir(name), 'void.' + cls.hash(8))
				cls.file_extract(name, path_extract)
				if cls.file_exists(cls.path(path_extract, 'run.void')):
					result = cls.action(cls.file(cls.path(path_extract, 'run.void')))
				elif cls.file_exists(cls.path(path_extract, 'run.json')):
					result = cls.action(cls.file(cls.path(path_extract, 'run.json')))
				elif cls.file_exists(cls.path(path_extract, 'run.yaml')):
					result = cls.action(cls.file(cls.path(path_extract, 'run.yaml')))
				cls.dir_remove(path_extract)
			else:
				if name.startswith('['):
					data = cls.json_decode(name)
					if data is None:
						data = cls.yaml_decode(name)
						if data is None:
							data = cls.void_decode(name)
					if data is not None:
						result = cls.action(data)
				elif name.startswith('{'):
					data = cls.json_decode(name)
					if data is None:
						data = cls.yaml_decode(name)
					if data is not None:
						result = cls.action(data)
				else:
					result = cls.action([param])
		elif cls.file_exists('run.void'):
			result = cls.action(cls.file('run.void'))
		elif cls.file_exists('run.json'):
			result = cls.action(cls.file('run.json'))
		elif cls.file_exists('run.yaml'):
			result = cls.action(cls.file('run.yaml'))
		elif cls.file_exists('run.zip/run.void'):
			result = cls.action(cls.file('run.zip/run.void'))
		elif cls.file_exists('run.zip/run.json'):
			result = cls.action(cls.file('run.zip/run.json'))
		elif cls.file_exists('run.zip/run.yaml'):
			result = cls.action(cls.file('run.zip/run.yaml'))
		else:
			result = app.get('about')
		if result not in ['', b'', None] and cls.get('app.ui') == 'cli':
			cls.print(result)


  # value

	@classmethod
	def get(cls, name: str = None, default = None, storage = None):
		if '/' in name or '\\' in name:
			path = cls.path_start(name)
			path_extension = cls.path_extension(path).lower()
			if path_extension in ['void', 'json', 'csv', 'yaml', 'xml', 'ini'] and cls.file_exists(path):
				storage = cls.file(path)
				if not isinstance(storage, (dict, list)):
					return default
				name = cls.path_end(name)
			else:
				return default
		else:
			if storage is None:
				storage = cls.data
		if name is None:
			return storage
		for part in name.split('.'):
			if isinstance(storage, dict) and part in storage:
				storage = storage[part]
			elif isinstance(storage, list):
				try:
					index = int(part)
					if 0 <= index < len(storage):
						storage = storage[index]
					else:
						return default
				except ValueError:
					return default
			else:
				return default
		return storage

	@classmethod
	def set(cls, name: str, data = None, storage = None):
		if '/' in name or '\\' in name:
			path = cls.path_start(name)
			path_extension = cls.path_extension(path).lower()
			if path_extension in ['void', 'json', 'csv', 'yaml', 'xml', 'ini'] and cls.file_exists(path):
				storage = cls.file(path)
				if not isinstance(storage, (dict, list)):
					return default
				name = cls.path_end(name)
				storage_type = 'file'
				storage_data = storage
			else:
				return
		else:
			if storage == None:
				storage = cls.data
			storage_type = None
		parts = name.split('.')
		for index, part in enumerate(parts[:-1]):
			if isinstance(storage, dict):
				if part not in storage or not isinstance(storage[part], (dict, list)):
					storage[part] = [] if parts[index+1].isdigit() else {}
				storage = storage[part]
			elif isinstance(storage, list):
				try:
					storage = storage[int(part)]
				except (ValueError, IndexError):
					return
		last = parts[-1]
		if isinstance(storage, dict):
			storage[last] = data
		elif isinstance(storage, list):
			try:
				index = int(last)
				if index == len(storage):
					storage.append(data)
				else:
					storage[index] = data
			except ValueError:
				pass
		if storage_type is not None:
			match storage_type:
				case 'file':
					cls.file(path, storage_data)

	@classmethod
	def remove(cls, name: str, storage = None):
		if '/' in name or '\\' in name:
			path = cls.path_start(name)
			path_extension = cls.path_extension(path).lower()
			if path_extension in ['void', 'json', 'csv', 'yaml', 'xml', 'ini'] and cls.file_exists(path):
				storage = cls.file(path)
				if not isinstance(storage, (dict, list)):
					return default
				name = cls.path_end(name)
				storage_type = 'file'
				storage_data = storage
			else:
				return
		else:
			if storage == None:
				storage = cls.data
			storage_type = None
		parts = name.split('.')		
		for part in parts[:-1]:
			if isinstance(storage, dict) and part in storage:
				storage = storage[part]
			elif isinstance(storage, list):
				try:
					storage = storage[int(part)]
				except (ValueError, IndexError):
					return
			else:
				return
		last = parts[-1]
		try:
			if isinstance(storage, dict) and last in storage:
				del storage[last]
			elif isinstance(storage, list):
				del storage[int(last)]
			if storage_type is not None:
				match storage_type:
					case 'file':
						cls.file(path, storage_data)
		except (ValueError, IndexError):
			pass

	@classmethod
	def type(cls, data):
		if data is None:
			return 'none'
		if isinstance(data, bool):
			return 'bool'
		if isinstance(data, str):
			return 'text'
		if isinstance(data, (float, int)):
			return 'number'
		if isinstance(data, list):
			return 'list'
		if isinstance(data, dict):
			return 'dict'
		if isinstance(data, bytes):
			return 'binary'

	@classmethod
	def text(cls, data):
		if data is None:
			return 'none'
		if data == True:
			return 'true'
		if data == False:
			return 'false'
		if isinstance(data, str):
			return data
		if isinstance(data, (int, float)):
			return str(data)
		if isinstance(data, bytes):
			try:
				return data.decode('utf-8')
			except:
				return ''
		if isinstance(data, (list, dict)):
			return cls.json(data)
		return ''

	@classmethod
	def number(cls, data, digits: int = 0):
		if isinstance(data, (int, float)):
			result = data
		elif data is None:
			result = 0
		elif data == True:
			result = 1
		elif data == False:
			result = 0
		elif isinstance(data, (str, bytes)):
			try:
				result = int(data)
			except:
				try:
					result = float(data)
				except:
					result = 0
		elif isinstance(data, (list, dict)):
			result = len(data)
		else:
			result = 0
		if digits is not None:
			if digits == 0:
				result = int(result)
			elif digits > 0:
				result = round(result, digits)
			else:
				result = int(result * (10 ** -digits))
		return result

	@classmethod
	def bool(cls, data):
		return bool(data)

	@classmethod
	def binary(cls, data):
		if isinstance(data, str):
			return data.encode('utf-8')
		if isinstance(data, bytes):
			return data
		return cls.text(data).encode('utf-8')

	@classmethod
	def length(cls, data, real: bool = False):
		if real:
			sys.getsizeof(data)
		if data is None:
			return 0
		if isinstance(data, (str, list, dict, bytes)):
			return len(data)
		if isinstance(data, bool):
			return 1
		if isinstance(data, int):
			return (data.bit_length() + 7) // 8
		if isinstance(data, float):
			return (sys.float_info.mant_dig + math.ceil(math.log2(sys.float_info.max_10_exp - sys.float_info.min_10_exp)) + 1) // 8

	@classmethod
	def len(cls, data):
		return cls.length(data)

	@classmethod
	def mem(cls, data):
		return cls.length(data, True)


  # expression

	@classmethod
	def expression_plus(cls):
		pass

	@classmethod
	def expression_and(cls):
		return cls.expression_plus()

	@classmethod
	def expression_minus(cls):
		pass

	@classmethod
	def expression_not(cls):
		return cls.expression_minus()

	@classmethod
	def expression_multiply(cls):
		pass

	@classmethod
	def expression_xor(cls):
		return cls.expression_multiply()

	@classmethod
	def expression_divide(cls):
		pass

	@classmethod
	def expression_or(cls):
		return cls.expression_divide()

	@classmethod
	def expression_modulo(cls):
		pass

	@classmethod
	def expression_mod(cls):
		return cls.expression_modulo()

	@classmethod
	def expression_power(cls):
		pass

	@classmethod
	def expression_pow(cls):
		return cls.expression_power()

	@classmethod
	def expression_shr(cls):
		pass

	@classmethod
	def expression_shl(cls):
		pass

	@classmethod
	def expression_notequal(cls):
		pass

	@classmethod
	def expression_greater(cls):
		pass

	@classmethod
	def expression_less(cls):
		pass

	@classmethod
	def expression_greater_equal(cls):
		pass

	@classmethod
	def expression_less_equal(cls):
		pass

	@classmethod
	def expression_in(cls):
		pass

	@classmethod
	def expression_notin(cls):
		pass

	@classmethod
	def expression_is(cls):
		pass

	@classmethod
	def expression_isnot(cls):
		pass

	@classmethod
	def expression_assign(cls):
		pass

	@classmethod
	def expression_plus_assign(cls):
		pass

	@classmethod
	def expression_assign_plus(cls):
		pass

	@classmethod
	def expression_minus_assign(cls):
		pass

	@classmethod
	def expression_assign_minus(cls):
		pass

	@classmethod
	def expression_multiply_assign(cls):
		pass

	@classmethod
	def expression_divide_assign(cls):
		pass

	@classmethod
	def expression_modulo_assign(cls):
		pass

	@classmethod
	def expression_power_assign(cls):
		pass

	@classmethod
	def expression_shr_assign(cls):
		pass

	@classmethod
	def expression_shl_assign(cls):
		pass


  # control

	@classmethod
	def print(cls, *data):
		if len(data) > 0:
			data = [('true' if value == True else ('false' if value == False else ('none' if value is None else value))) for value in data]
			if len(data) == 1:
				if isinstance(data[0], (list, dict)):
					print(cls.json(data[0]))
				else:
					print(*data)
			else:
				print(*data)
		else:
			print()

	@classmethod
	def printn(cls, *data):
		cls.print(*data, {'newline': None})

	@classmethod
	def input(cls, text: str = None):
		return input(text if text is not None else '')

	@classmethod
	def control_if(cls):
		pass

	@classmethod
	def control_loop(cls):
		pass

	@classmethod
	def control_break(cls):
		pass

	@classmethod
	def control_continue(cls):
		pass

	@classmethod
	def control_repeat(cls):
		pass

	@classmethod
	def control_return(cls):
		pass

	@classmethod
	def action(cls, action):
		result = None
		for action_data in action:
			name = action_data[0].replace('.', '_')
			if hasattr(cls, name):
				method = getattr(cls, name)
				result = method(*action_data[1:])
		return result

	@classmethod
	def open(cls):
		pass

	@classmethod
	def close(cls, pid):
		pass

	@classmethod
	def code(void, text: str):
		exec(text)

	@classmethod
	def logger(cls):
		pass

	@classmethod
	def l(cls):
		return cls.logger()

	@classmethod
	def debug(cls, tag: str, data = None):
		pass

	@classmethod
	def warning(cls, tag: str, data = None):
		pass

	@classmethod
	def error(cls, tag: str, data = None):
		print()
		print(tag)
		print(data)
		print()

	@classmethod
	def test(cls, name = None):
		pass

	@classmethod
	def update(cls, name = None):
		pass

	@classmethod
	def exit(cls, *data):
		if len(data) > 0 and isinstance(data[0], int):
			code = data[0]
			data = data[1:]
		else:
			code = 0
		if len(data):
			cls.print(*data)
		exit(code)

	@classmethod
	def xx(cls, *data):
		cls.exit(1, *data)

	@classmethod
	def fatal(cls, *data):
		cls.exit(1, *data)

	@classmethod
	def os(cls):
		pass

	@classmethod
	def info(cls, name: str):
		pass

	@classmethod
	def i(cls, name: str):
		return cls.info(name)

	@classmethod
	def help(cls, name: str):
		return cls.info(name)

	@classmethod
	def h(cls, name: str):
		return cls.info(name)

	@classmethod
	def convert(cls, value, name_from, name_to = None):
		pass

	@classmethod
	def c(cls, value, name_from, name_to = None):
		return cls.convert(value, name_from, name_to)

	@classmethod
	def clipboard(cls, data = None):
		pass

	@classmethod
	def sql(cls):
		pass

	@classmethod
	def chat(cls, text: str, model: str = None, character: str = None, reference = None):
		pass

	@classmethod
	def ai(cls, text: str, model: str = None, character: str = None, reference = None):
		return cls.chat(text, model, character, reference)

	@classmethod
	def say(cls, text: str, voice: str = None):
		pass

	@classmethod
	def recognize(cls, data, text: str = None):
		pass

	@classmethod
	def ui(cls):
		pass


  # text

	@classmethod
	def lower(cls):
		pass

	@classmethod
	def upper(cls):
		pass

	@classmethod
	def starts(cls):
		pass

	@classmethod
	def ends(cls):
		pass

	@classmethod
	def strip(cls):
		pass

	@classmethod
	def strip_start(cls):
		pass

	@classmethod
	def strip_end(cls):
		pass

	@classmethod
	def replace(cls):
		pass

	@classmethod
	def find(cls):
		pass

	@classmethod
	def find_end(cls):
		pass

	@classmethod
	def parse(cls):
		pass

	@classmethod
	def part(cls):
		pass

	@classmethod
	def split(cls):
		pass

	@classmethod
	def join(cls):
		pass

	@classmethod
	def escape(cls, text: str, format: str = None):
		pass

	@classmethod
	def e(cls, text: str, format: str = None):
		return cls.escape(text, format)

	@classmethod
	def unescape(cls, text: str, format: str = None):
		pass

	@classmethod
	def u(cls, text: str, format: str = None):
		return cls.uescape(text, format)

	@classmethod
	def translate(cls):
		pass

	@classmethod
	def check(cls):
		pass


  # list

	@classmethod
	def push(cls):
		pass

	@classmethod
	def pop(cls):
		pass

	@classmethod
	def reverse(cls):
		pass

	@classmethod
	def unique(cls):
		pass

	@classmethod
	def map(cls):
		pass

	@classmethod
	def reduce(cls):
		pass

	@classmethod
	def filter(cls):
		pass

	@classmethod
	def names(cls):
		pass

	@classmethod
	def values(cls):
		pass


  # math

	@classmethod
	def sin(cls, value: float):
		return math.sin(value)

	@classmethod
	def cos(cls, value: float):
		return math.cos(value)

	@classmethod
	def tan(cls, value: float):
		return math.tan(value)

	@classmethod
	def sinh(cls, value: float):
		return math.sinh(value)

	@classmethod
	def cosh(cls, value: float):
		return math.cosh(value)

	@classmethod
	def tanh(cls, value: float):
		return math.tanh(value)

	@classmethod
	def asin(cls, value: float):
		return math.asin(value)

	@classmethod
	def acos(cls, value: float):
		return math.acos(value)

	@classmethod
	def atan(cls, value: float):
		return math.atan(value)

	@classmethod
	def asinh(cls, value: float):
		return math.asinh(value)

	@classmethod
	def acosh(cls, value: float):
		return math.acosh(value)

	@classmethod
	def atanh(cls, value: float):
		return math.atanh(value)

	@classmethod
	def round(cls, value: float, digits: int = 0):
		return round(value, digits)

	@classmethod
	def floor(cls, value: float):
		return math.floor(value)

	@classmethod
	def ceil(cls, value: float):
		return math.ceil(value)

	@classmethod
	def log(cls, value: float, base: float = None):
		return math.log(value) if base == None else math.log(value, base)

	@classmethod
	def ln(cls, value: float, base: float = None):
		return cls.log(value)

	@classmethod
	def factorial(cls, value: float):
		return math.factorial(value)

	@classmethod
	def fact(cls, value: float):
		return cls.factorial(value)

	@classmethod
	def fibonacci(cls, value: float, multiply: float = 1, shift: float = 0):
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

	@classmethod
	def fib(cls, value: float, multiply: float = 1, shift: float = 0):
		return cls.fibonacci(value)

	@classmethod
	def gold(cls, value: float, component: str = None):
		phi = 1.61803398874989484820
		if component == 'short':
			return {
				'short': value,
				'long': value * phi,
				'total': value * (1 + phi)
				}
		elif component == 'long':
			return {
				'short': value / phi,
				'long': value,
				'total': value * (1 + phi) / phi
				}
		return {
			'short': (2 - phi) * value,
			'long': (phi - 1) * value,
			'total': value
			}

	@classmethod
	def g(cls, value: float, component: str = None):
		return cls.gold(value, component)

	@classmethod
	def abs(cls, value: float):
		return abs(value)

	@classmethod
	def min(cls, value: list):
		return min(value)

	@classmethod
	def max(cls, value: list):
		return max(value)

	@classmethod
	def sum(cls, value: list):
		result = 0
		for value in value:
			if type(value) in [int, float]:
				result += value
		return result

	@classmethod
	def avg(cls, value: list):
		if len(value) == 0:
			return 0
		return cls.sum(value) / float(len(value))

	@classmethod
	def random(cls, value = None, to = None):
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

	@classmethod
	def random_seed(cls, seed = None):
		if seed == None:
			return cls.get('app.random.seed')
		elif seed == '':
			seed = cls.sha256(str(cls.time()) + cls.hash(64))
		random.seed(seed)
		cls.set('app.random.seed', seed)

	@classmethod
	def random_reseed(cls):
		cls.random_seed('')


  # time

	@classmethod
	def time(cls, digits: int = None):
		return time.time() if digits is None else cls.number(time.time(), digits)

	@classmethod
	def timestamp(cls):
		return cls.time(0)

	@classmethod
	def time_milli(cls):
		return cls.time(-3)

	@classmethod
	def time_micro(cls):
		return cls.time(-6)

	@classmethod
	def timer(cls):
		pass

	@classmethod
	def timer_remove(cls, name: str = None):
		pass

	@classmethod
	def wait(cls, seconds: float = 1):
		time.sleep(seconds)

	@classmethod
	def stopwatch(cls, tag: str = '', digits: int = None):
		result = time.time()
		if digits is None or tag not in cls.data['t']:
			cls.data['t'][tag] = result
		else:
			cls.print(f'{tag} · {cls.number(result - cls.data["t"][tag], digits)}')
		return result

	@classmethod
	def t(cls, tag: str = None, digits: int = None):
		return cls.stopwatch(tag, digits)

	@classmethod
	def date(cls):
		pass


  # crypto

	@classmethod
	def encrypt(cls, data, key: str = None):
		if data is None:
			data = b'n'
		elif data == True:
			data = b'1'
		elif data == False:
			data = b'0'
		elif isinstance(data, bytes):
			data = data + b'b'
		elif isinstance(data, str):
			data = data.encode() + b't'
		elif isinstance(data, int):
			data = str(data).encode() + b'i'
		elif isinstance(data, float):
			data = str(data).encode() + b'f'
		elif isinstance(data, (list, dict)):
			data = cls.json(data).encode() + b'j'
		else:
			data = str(data).encode() + b'b'
		if key is not None:
			return cls.aes(data, key)
		key = cls.hash(64)
		return {
			'data': cls.aes(data, key),
			'key': key
		}

	@classmethod
	def decrypt(cls, data, key: str):
		if isinstance(data, str):
			data = cls.base64_decode(data)
		data = cls.aes_decode(data, key)
		if data is not None and len(data) > 0:
			data_type = data[-1:]
			data = data[:-1]
			match data_type:
				case b'n':
					return None
				case b'1':
					return True
				case b'0':
					return False
				case b'b':
					return data
				case b't':
					return data.decode('utf-8')
				case b'i':
					return int(data)
				case b'f':
					return float(data)
				case b'j':
					return cls.json_decode(data.decode('utf-8'))

	@classmethod
	def password(cls, password: str, name: str = None):
		if not password: return None
		match name:
			case 'argon' | 'argon2':
				argon = cls.module('argon2', 'argon2-cffi').PasswordHasher()
				return argon.hash(password)
			case 'bcrypt':
				bcrypt = cls.module('bcrypt')
				return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
			case _:
				base64 = cls.module('base64')
				salt = os.urandom(32)
				rounds = 600_000
				key = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, rounds)
				salt_base64 = base64.b64encode(salt).decode()
				key_base64 = base64.b64encode(key).decode()
				return f'$pbkdf2${rounds}${salt_base64}${key_base64}'

	@classmethod
	def password_check(cls, password_hashed: str, password: str):
		if not password_hashed or not password: return False
		try:
			if password_hashed.startswith('$argon2'):
				argon = cls.module('argon2', 'argon2-cffi').PasswordHasher()
				argon.verify(password_hashed, password)
				return True
			elif password_hashed.startswith(('$2b$', '$2a$', '$2y$')):
				bcrypt = cls.module('bcrypt')
				return bcrypt.checkpw(password.encode(), password_hashed.encode())
			elif password_hashed.startswith('$pbkdf2$'):
				hmac = cls.module('hmac')
				base64 = cls.module('base64')
				_, _, rounds, salt_base64, key_base64 = password_hashed.split('$')
				salt = base64.b64decode(salt_base64)
				rounds = int(rounds)
				original_key = base64.b64decode(key_base64)
				key = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, rounds)
				return hmac.compare_digest(original_key, key)
			else:
				cls.error('password.check', 'unknown hash format')
				return False
		except Exception as e:
			cls.error('password.check', e)
			return False

	@classmethod
	def hash(cls, data = 32, *param):
		if data is None:
			data = 32
		if type(data) is int:
			alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
			alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
			number = '0123456789'
			symbol = '!@#$%^&*()_+-=`~:;.,<>|/{}[]'
			characters = ''
			if 'letter' in param or 'letters' in param or 'alphabet' in param:
				characters += alphabet_lower + alphabet_upper
			else:
				if 'lower' in param:
					characters += alphabet_lower
				if 'upper' in param:
					characters += alphabet_upper
			if 'number' in param or 'numbers' in param or 'digit' in param:
				characters += number
			if 'symbol' in param or 'symbols' in param or'special' in param:
				characters += symbol
			if len(characters) == 0:
				if len(param) == 1 and type(param[0]) is str:
					characters = param[0]
				else:
					characters = alphabet_lower + alphabet_upper + number
			secrets = cls.module('secrets')
			if data <= 1000:
				return ''.join(secrets.choice(characters) for _ in range(data))
			return ''.join([
				*(secrets.choice(characters) for _ in range(1000)),
				*random.choices(characters, k=data - 1000)
			])
		match str(param[0]) if len(param) > 0 else '':
			case 'sha1':
				return cls.sha1(data)
			case 'sha256':
				return cls.sha256(data)
			case 'sha512':
				return cls.sha512(data)
			case 'crc32':
				return cls.crc32(data)
			case 'base64':
				return cls.base64(data)
			case 'argon' | 'argon2':
				return cls.password(str(data), 'argon') 
			case 'bcrypt':
				return cls.password(str(data), 'bcrypt')
			case 'pbk' | 'pbkdf' | 'pbkdf2':
				return cls.password(str(data), 'pbkdf2')
			case 'number' | 'digit':
				result = int(hashlib.sha256(data if isinstance(data, bytes) else str(data).encode()).hexdigest(), 16)
				if len(param) > 1 and type(param[1]) is int:
					result = int(str(result)[:param[1]])
				return result
			case _:
				return cls.sha256(data)

	@classmethod
	def uuid(cls, clean: bool = False):
		uuid = cls.module('uuid')
		result = uuid.uuid4()
		return str(result) if not clean else result.hex

	@classmethod
	def sha1(cls, data):
		if not isinstance(data, bytes):
			data = str(data if data is not None else '').encode()
		return hashlib.sha1(data).hexdigest()

	@classmethod
	def sha256(cls, data):
		if not isinstance(data, bytes):
			data = str(data if data is not None else '').encode()
		return hashlib.sha256(data).hexdigest()

	@classmethod
	def sha512(cls, data):
		if not isinstance(data, bytes):
			data = str(data if data is not None else '').encode()
		return hashlib.sha512(data).hexdigest()

	@classmethod
	def crc32(cls, data):
		zlib = cls.module('zlib')
		if not isinstance(data, bytes):
			data = str(data if data is not None else '').encode()
		return zlib.crc32(data)

	@classmethod
	def base64(cls, data, safe: bool = False):
		if not isinstance(data, bytes):
			data = str(data if data is not None else '').encode()
		base64 = cls.module('base64')
		data = base64.b64encode(data if type(data) is bytes else str(data).encode()).decode()
		return data if not safe else data.replace('/', '_').replace('=', '')

	@classmethod
	def base64_safe(cls, data):
		return cls.base64(data, True)

	@classmethod
	def base64_decode(cls, data, safe: bool = False, format: str = 'text'):
		base64 = cls.module('base64')
		if not isinstance(data, bytes):
			data = str(data)
			if safe:
				if '_' in data:
					data = data.replace('_', '/')
				if len(data) % 4 != 0:
					data += '=' * (4 - len(data) % 4)
			data = data.encode()
		try:
			data = base64.b64decode(data)
		except: return
		if format not in [None, '', 'binary']:
			try:
				return data.decode('utf-8' if format == 'text' else format)
			except: return data

	@classmethod
	def base64_decode_safe(cls, data):
		return cls.base64_decode(data, True)

	@classmethod
	def gzip(cls, data, compression = None):
		gzip = cls.module('gzip')
		if not isinstance(data, bytes):
			data = str(data if data is not None else '').encode()
		if compression in ['best', None]:
			compression = 9
		elif compression == 'fast':
			compression = 1
		else:
			try:
				compression = int(compression)
				if compression < 0:
					compression = 0
				elif compression > 9:
					compression = 9
			except:
				compression = 9
		buffer = io.BytesIO()
		with gzip.GzipFile(fileobj=buffer, mode='wb', compresslevel=compression, mtime=0) as temp:
			temp.write(data)
		return buffer.getvalue()

	@classmethod
	def gzip_fast(cls, data):
		return cls.gzip(data, 'fast')

	@classmethod
	def gzip_best(cls, data):
		return cls.gzip(data, 'best')

	@classmethod
	def gzip_decode(cls, data: bytes):
		if not data: return
		gzip = cls.module('gzip')
		try:
			return gzip.decompress(data)
		except: return

	@classmethod
	def lzma(cls, data, compression = None):
		lzma = cls.module('lzma')
		if not isinstance(data, bytes):
			data = str(data if data is not None else '').encode()
		if compression in ['best', None]:
			compression = lzma.PRESET_EXTREME
		elif compression == 'fast':
			compression = 0
		else:
			try:
				compression = int(compression)
				if compression < 0:
					compression = 0
				elif compression > 9:
					compression = 9
			except:
				compression = 9
		return lzma.compress(bytes(data), preset=compression)

	@classmethod
	def lzma_fast(cls, data):
		return cls.lzma(data, 'fast')

	@classmethod
	def lzma_best(cls, data):
		return cls.lzma(data, 'best')

	@classmethod
	def lzma_decode(cls, data: bytes):
		if not data: return
		lzma = cls.module('lzma')
		try:
			return lzma.decompress(data)
		except: return

	@classmethod
	def lz4(cls, data, compression = None):
		lz4_frame = cls.module('lz4.frame')
		if not isinstance(data, bytes):
			data = str(data if data is not None else '').encode()
		if compression in ['best', None]:
			compression = lz4_frame.COMPRESSIONLEVEL_MAX
		elif compression == 'fast':
			compression = 0
		else:
			try:
				compression = int(compression)
				if compression < 0:
					compression = 0
				elif compression > 16:
					compression = 16
			except:
				compression = 16
		return lz4_frame.compress(data, compression_level=compression)

	@classmethod
	def lz4_fast(cls, data):
		return cls.lz4(data, 'fast')

	@classmethod
	def lz4_best(cls, data):
		return cls.lz4(data, 'best')

	@classmethod
	def lz4_decode(cls, data):
		if not data: return
		lz4_frame = cls.module('lz4.frame')
		return lz4_frame.decompress(data)

	@classmethod
	def lzss(cls, data):
		if not isinstance(data, bytes):
			data = str(data if data is not None else '').encode()
		window_size = 4096
		match_max = 18
		match_min = 3
		res = bytearray()
		si, n = 0, len(data)
		pos_hash = {}
		while si < n:
			control_idx = len(res)
			res.append(0)
			control_byte = 0			
			for bit in range(8):
				if si >= n: break
				best_len, best_off = 0, 0
				if si + match_min <= n:
					three_gram = data[si:si+3]
					if three_gram in pos_hash:
						window_start = si - window_size
						for old_pos in reversed(pos_hash[three_gram]):
							if old_pos < window_start: break 
							cur_len = 3
							while cur_len < match_max and si + cur_len < n and \
								  data[old_pos + cur_len] == data[si + cur_len]:
								cur_len += 1
							if cur_len > best_len:
								best_len = cur_len
								best_off = si - old_pos
								if best_len == match_max: break
				if best_len >= match_min:
					packet = (((best_off - 1) & 0xFFF) << 4) | ((best_len - match_min) & 0x0F)
					res.append((packet >> 8) & 0xFF); res.append(packet & 0xFF)
					for i in range(best_len):
						if si + i + 3 <= n:
							tg = data[si+i:si+i+3]
							if tg not in pos_hash: pos_hash[tg] = []
							pos_hash[tg].append(si+i)
					si += best_len
				else:
					control_byte |= (1 << bit)
					res.append(data[si])
					if si + 3 <= n:
						tg = data[si:si+3]
						if tg not in pos_hash: pos_hash[tg] = []
						pos_hash[tg].append(si)
					si += 1
			res[control_idx] = control_byte
			if si % 10000 == 0:
				threshold = si - window_size
				for k in list(pos_hash.keys()):
					pos_hash[k] = [p for p in pos_hash[k] if p >= threshold]
					if not pos_hash[k]: del pos_hash[k]
		return bytes(res)

	@classmethod
	def lzss_decode(cls, data: bytes):
		if not data: return
		match_min = 3
		res = bytearray()
		si, data_len = 0, len(data)
		while si < data_len:
			control = data[si]
			si += 1
			for bit in range(8):
				if si >= data_len: break
				if (control >> bit) & 1:
					res.append(data[si])
					si += 1
				else:
					if si + 1 >= data_len: break
					packet = (data[si] << 8) | data[si+1]
					si += 2
					offset = (packet >> 4) + 1
					length = (packet & 0x0F) + match_min
					curr_res_len = len(res)
					start_pos = curr_res_len - offset
					if offset >= length:
						res.extend(res[start_pos : start_pos + length])
					else:
						for i in range(length):
							res.append(res[len(res) - offset])
		return bytes(res)

	@classmethod
	def deflate(cls, data, compression = None):
		zlib = cls.module('zlib')
		if not isinstance(data, bytes):
			data = str(data if data is not None else '').encode()
		if compression in ['best', None]:
			compression = 9
		elif compression == 'fast':
			compression = 1
		else:
			try:
				compression = int(compression)
				if compression < 0:
					compression = 0
				elif compression > 9:
					compression = 9
			except:
				compression = 9
		compressor = zlib.compressobj(level=compression, method=zlib.DEFLATED, wbits=-15)
		return compressor.compress(data) + compressor.flush()

	@classmethod
	def deflate_fast(cls, data):
		return cls.deflate(data, 'fast')

	@classmethod
	def deflate_best(cls, data):
		return cls.deflate(data, 'best')

	@classmethod
	def deflate_decode(cls, data):
		if not data: return
		zlib = cls.module('zlib')
		try:
			return zlib.decompress(data, -15)
		except: return

	@classmethod
	def aes(cls, data, key: str):
		if not isinstance(data, bytes):
			data = str(data if data is not None else '').encode()
		try:
			aes_gcm = cls.module('cryptography.hazmat.primitives.ciphers.aead', 'cryptography').AESGCM
			hashes = cls.module('cryptography.hazmat.primitives.hashes', 'cryptography')
			digest = hashes.Hash(hashes.SHA256())
			digest.update(key.encode())
			key_bytes = digest.finalize()
			aes = aes_gcm(key_bytes)
			nonce = os.urandom(12)
			return nonce + aes.encrypt(nonce, data, None)
		except Exception:
			cls.error('aes.encode')

	@classmethod
	def aes_decode(cls, data: bytes, key: str):
		if data is None or len(data) < 12: return
		try:
			aes_gcm = cls.module('cryptography.hazmat.primitives.ciphers.aead', 'cryptography').AESGCM
			hashes = cls.module('cryptography.hazmat.primitives.hashes', 'cryptography')
			digest = hashes.Hash(hashes.SHA256())
			digest.update(key.encode())
			key_bytes = digest.finalize()
			aes = aes_gcm(key_bytes)
			nonce = data[:12]
			encrypted = data[12:]
			return aes.decrypt(nonce, encrypted, None)
		except Exception:
			cls.error('aes.decode')
			return

	@classmethod
	def rsa(cls, data = None, public_key = None, password: str = None, length = None):
		try:
			serialization = cls.module('cryptography.hazmat.primitives.serialization', 'cryptography')
			padding = cls.module('cryptography.hazmat.primitives.asymmetric.padding', 'cryptography')
			hashes = cls.module('cryptography.hazmat.primitives.hashes', 'cryptography')
			if length == None:
				key_size = 4096
				length = 446
			elif length == 'fast':
				key_size = 1552
				length = 128
			else:
				length = int(length) 
				if length % 8 != 0 or length < 1024:
					key_size = (length + 66) * 8
				else:
					key_size = length
					length = key_size // 8 - (2 * (256 // 8)) - 2
				if key_size < 1024:
					key_size = 1024
			result = None
			if public_key is None:
				rsa = cls.module('cryptography.hazmat.primitives.asymmetric.rsa', 'cryptography')
				encryption = serialization.NoEncryption() if password is None else serialization.BestAvailableEncryption(password.encode())
				private_key = rsa.generate_private_key(public_exponent=65537, key_size=key_size)
				public_key = private_key.public_key()
				public_key_pem = public_key.public_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo).decode()
				private_key_pem = private_key.private_bytes(encoding=serialization.Encoding.PEM, format=serialization.PrivateFormat.PKCS8, encryption_algorithm=encryption).decode()
				public_key_base64 = ''.join(public_key_pem.strip().splitlines()[1:-1])
				private_key_base64 = ''.join(private_key_pem.strip().splitlines()[1:-1])
				result = {
					'public': public_key_base64,
					'private': private_key_base64,
					'pem': {
						'public': public_key_pem,
						'private': private_key_pem
					}
				}
				if data is None:
					return result
			if not isinstance(data, bytes):
				data = str(data if data is not None else '').encode()
			if len(data) > length:
				cls.error('rsa.encode', f'max length {length} exceeded')
				return
			if isinstance(public_key, str):
				if 'PUBLIC KEY' not in public_key:
					public_key = f"-----BEGIN PUBLIC KEY-----\n{public_key}\n-----END PUBLIC KEY-----"
				public_key = serialization.load_pem_public_key(str(public_key).encode())
			data_encrypted = public_key.encrypt(data, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
			return data_encrypted if result is None else (result | {'data': data_encrypted})
		except Exception as e:
			cls.error('rsa.encode', e)

	@classmethod
	def rsa_fast(cls, data: bytes = None, public_key = None, password: str = None):
		return cls.rsa(data, public_key, password, 'fast')

	@classmethod
	def rsa_decode(cls, data: bytes, private_key, password: str = None):
		if not data: return
		try:
			serialization = cls.module('cryptography.hazmat.primitives.serialization', 'cryptography')
			padding = cls.module('cryptography.hazmat.primitives.asymmetric.padding', 'cryptography')
			hashes = cls.module('cryptography.hazmat.primitives.hashes', 'cryptography')
			if not isinstance(private_key, bytes):
				private_key = str(private_key)
				if 'PRIVATE KEY' not in private_key:
					encrypted = 'ENCRYPTED ' if password is not None else ''
					private_key = f"-----BEGIN {encrypted}PRIVATE KEY-----\n{private_key}\n-----END {encrypted}PRIVATE KEY-----"
				private_key = serialization.load_pem_private_key(private_key.encode(),  password=password.encode() if password is not None else None)
				return private_key.decrypt(data, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
		except Exception as e:
			cls.error('rsa.decode', e)

	@classmethod
	def ecdhe(cls, public_key: str = None, private_key: str = None):
		try:
			ec = cls.module('cryptography.hazmat.primitives.asymmetric.ec', 'cryptography')
			serialization = cls.module('cryptography.hazmat.primitives.serialization', 'cryptography')
			hashes = cls.module('cryptography.hazmat.primitives.hashes', 'cryptography')
			if public_key is None or private_key is None:
				private_key = ec.generate_private_key(ec.SECP256R1())
				public_key = private_key.public_key()
				public_bytes = public_key.public_bytes(serialization.Encoding.PEM, serialization.PublicFormat.SubjectPublicKeyInfo).decode().strip().splitlines()[1:-1]
				private_bytes = private_key.private_bytes(serialization.Encoding.PEM, serialization.PrivateFormat.PKCS8, serialization.NoEncryption()).decode().strip().splitlines()[1:-1]		
				return {
					'public': ''.join(public_bytes),
					'private': ''.join(private_bytes)
				}
			private_key_pem = f'-----BEGIN PRIVATE KEY-----\n{private_key}\n-----END PRIVATE KEY-----'
			private_key_obj = serialization.load_pem_private_key(private_key_pem.encode(), password=None)
			public_key_pem = f'-----BEGIN PUBLIC KEY-----\n{public_key}\n-----END PUBLIC KEY-----'
			public_key_obj = serialization.load_pem_public_key(public_key_pem.encode())
			shared_key = private_key_obj.exchange(ec.ECDH(), public_key_obj)
			digest = hashes.Hash(hashes.SHA256())
			digest.update(shared_key)
			return digest.finalize()
		except Exception as e:
			cls.error('ecdhe', e)

	@classmethod
	def barcode(cls, text = None, format: str = None):
		try:
			if text == None:
				barcode = cls.module('barcode', 'python-barcode')
				formats = barcode.PROVIDED_BARCODES + ['qr']
				return formats
			text = str(text)
			if format:
				format = format.lower()
			if format in ['qr', 'qrcode']:
				qrcode = cls.module('qrcode')
				qr = qrcode.QRCode(version=1, border=1)
				qr.add_data(text)
				qr.make(fit=True)
				result = io.StringIO()
				qr.print_ascii(out=result, invert=True)
				return {
					'data': qr.get_matrix(),
					'text': result.getvalue()
				}
			if not text.isdigit():
				format = 'code128'
			else:
				match len(text):
					case 8:
						format = 'ean8'
					case 12:
						format = 'upca'
					case 13:
						format = 'ean13'
					case 14:
						format = 'itf14'
					case _:
						format = 'code128'
			barcode = cls.module('barcode', 'python-barcode')
			code_class = barcode.get_barcode_class(format)
			code_obj = code_class(text)
			code_lines = code_obj.build()
			one = len(code_lines) == 1 
			result = {
				'data': [char == '1' for char in code_lines[0]] if one else code_lines,
				'text': '' if one else []
			}
			for line in code_lines:
				if len(line) % 2 != 0:
					line += '0'
				bars = []
				for i in range(0, len(line), 2):
					pair = line[i:i+2]
					if pair == '11':
						bars.append('█')
					elif pair == '10':
						bars.append('▌')
					elif pair == '01':
						bars.append('▐')
					else:
						bars.append(' ')
				line_text = ''.join(bars)
				if one:
					result['text'] = '\n'.join([line_text] * 10)
					result['line'] = line_text
				else:
					result['text'].append(line_text) 
			if not one:
				result['text'] = '\n'.join(result['text'])
			return result
		except Exception as e:
			cls.error('barcode', e)

	@classmethod
	def qr(cls, text: str):
		return cls.barcode(text, 'qr')

	@classmethod
	def barcode_decode(cls, image, format: str = None):
		return cls.recognize(image, format)

	@classmethod
	def qr_decode(cls, image):
		return cls.barcode_decode(image, 'qr')


  # file

	@classmethod
	def file(cls, path: str, data = None, format: str = None, extra = None):
		if format is None:
			format = cls.path_extension(path).lower()
			auto = True
		else:
			auto = False
		if data == None:
			if not cls.file_exists(path): return
			match format:
				case 'binary':
					with open(path, 'rb') as file:
						return file.read()
				case 'text' | 'txt':
					with open(path, 'r', encoding='utf-8') as file:
						return file.read()
				case 'line':
					with open(path, 'r', encoding='utf-8') as file:
						data = file.read()
						if '\r\n' in data:
							return data.split('\r\n')
						return data.split('\n')
				case 'void':
					with open(path, 'rb') as file:
						return cls.void_decode(file.read())
				case 'json':
					with open(path, 'r', encoding='utf-8') as file:
						return cls.json_decode(file.read())
				case 'csv':
					delimiter = extra if type(extra) is str else ','
					with open(path, 'r', encoding='utf-8') as file:
						return cls.csv_decode(file.read(), delimiter=delimiter)
				case 'yaml':
					with open(path, 'r', encoding='utf-8') as file:
						return cls.yaml_decode(file.read())
				case 'xml':
					with open(path, 'r', encoding='utf-8') as file:
						return cls.xml_decode(file.read())
				case 'ini':
					with open(path, 'r', encoding='utf-8') as file:
						return cls.ini_decode(file.read())
				case _:
					if format in cls.get('app.format.text'):
						with open(path, 'r', encoding='utf-8') as file:
							return file.read()
					with open(path, 'rb') as file:
						data = file.read()
					boms = [
							('utf-32', b'\xff\xfe\x00\x00'),
							('utf-32', b'\x00\x00\xfe\xff'),
							('utf-16', b'\xff\xfe'),
							('utf-16', b'\xfe\xff'),
							('utf-8',  b'\xef\xbb\xbf')
						]
					for encoding, signature in boms:
						if data.startswith(signature):
							try:
								return data.decode(encoding)
							except UnicodeDecodeError:
								continue
					try:
						 return data.decode(format)
					except:
						return data
		else:
			match format:
				case 'binary':
					with open(path, 'wb') as file:
						file.write(data)
				case 'text' | 'txt':
					with open(path, 'w', encoding='utf-8') as file:
						file.write(str(data))
				case 'line':
					if type(data) is list:
						delimiter = cls.get('app.os.delimiter.line')
						data = delimiter.join(map(str, data))
					else:
						data = str(data)
					with open(path, 'w', encoding='utf-8') as file:
						file.write(data)
				case 'void':
					data = cls.void(data)
					with open(path, 'w', encoding='utf-8') as file:
						file.write(data if data is not None else '')
				case 'json':
					data = cls.json(data)
					with open(path, 'w', encoding='utf-8') as file:
						file.write(data if data is not None else '')
				case 'csv':
					delimiter = extra if type(extra) is str else ','
					data = cls.csv(data, delimiter)
					with open(path, 'w', encoding='utf-8') as file:
						file.write(data if data is not None else '')
				case 'yaml':
					data = cls.yaml(data)
					with open(path, 'w', encoding='utf-8') as file:
						file.write(data if data is not None else '')
				case 'xml':
					data = cls.xml(data)
					data = '<?xml version="1.0" encoding="UTF-8"?>' + (('\n' + data) if type(data) is str else '')
					with open(path, 'w', encoding='utf-8') as file:
						file.write(data)
				case 'ini':
					data = cls.ini(data)
					with open(path, 'w', encoding='utf-8') as file:
						file.write(data if data is not None else '')
				case _:
					try:
						if auto:
							if isinstance(data, str) or format in cls.get('app.format.text'):
								with open(path, 'w', encoding='utf-8') as file:
									file.write(str(data) if data is not None else '')
							else:
								with open(path, 'wb') as file:
									if data is None:
										file.write(b'')
									elif data == True:
										file.write(b'\x01')
									elif data == False:
										file.write(b'\x00')
									elif isinstance(data, str):
										file.write(data.encode())
									elif not isinstance(data, bytes):
										file.write(str(data).encode())
									else:
										file.write(data)
						else:
							if data is None:
								data = ''
							elif isinstance(data, bytes):
								data = data.decode(format)
							else:
								data = str(data)
							with open(path, 'w', encoding=format) as file:
								file.write(data)
					except Exception as e:
						cls.error('file.write', e)

	@classmethod
	def file_read(cls, path: str):
		return cls.file(path)

	@classmethod
	def file_write(cls, path: str, data = None, format: str = None, extra = None):
		return cls.file(path, data if data is not None else b'', format, extra)

	@classmethod
	def file_binary(cls, path: str, data = None):
		return cls.file(path, data, 'binary')

	@classmethod
	def file_text(cls, path: str, data = None):
		return cls.file(path, data, 'text')

	@classmethod
	def file_line(cls, path: str, data = None):
		return cls.file(path, data, 'line')

	@classmethod
	def file_ascii(cls, path: str, data = None):
		return cls.file(path, data, 'ascii')

	@classmethod
	def file_void(cls, path: str, data = None):
		return cls.file(path, data, 'void')

	@classmethod
	def file_json(cls, path: str, data = None):
		return cls.file(path, data, 'json')

	@classmethod
	def file_csv(cls, path: str, data = None, delimiter: str = None):
		return cls.file(path, data, 'csv', delimiter)

	@classmethod
	def file_yaml(cls, path: str, data = None):
		return cls.file(path, data, 'yaml')

	@classmethod
	def file_xml(cls, path: str, data = None):
		return cls.file(path, data, 'xml')

	@classmethod
	def file_ini(cls, path: str, data = None):
		return cls.file(path, data, 'ini')

	@classmethod
	def file_create(cls, path: str):
		cls.file(path, b'', 'binary')

	@classmethod
	def file_clear(cls, path: str):
		cls.file(path, b'', 'binary')

	@classmethod
	def file_exists(cls, path: str):
		return os.path.isfile(path)

	@classmethod
	def is_file(cls, path: str) -> bool:
		return cls.file_exists(path)

	@classmethod
	def file_remove(cls, path: str, trash: bool = False):
		pass

	@classmethod
	def file_trash(cls, path: str, trash: bool = False):
		cls.file_remove(path, trash)

	@classmethod
	def file_copy(cls, source: str, destination: str = None):
		pass

	@classmethod
	def file_move(cls, source: str, destination: str = None):
		pass

	@classmethod
	def file_rename(cls, path: str, name: str = None):
		pass

	@classmethod
	def file_info(cls, path: str):
		pass

	@classmethod
	def file_sha256(cls, path: str):
		data = cls.file_binary(path)
		if data is not None:
			return cls.sha256(data)

	@classmethod
	def file_sha512(cls, path: str):
		data = cls.file_binary(path)
		if data is not None:
			return cls.sha512(data)

	@classmethod
	def file_crc32(cls, path: str):
		pass

	@classmethod
	def file_base64(cls, path: str):
		pass

	@classmethod
	def file_gzip(cls, source: str, destination: str = None, compression = None):
		pass

	@classmethod
	def file_zip(cls, source, destination: str = None, compression = None):
		pass

	@classmethod
	def file_void(cls, source, destination: str = None, compression = None, key: str = None):
		pass

	@classmethod
	def file_extract(cls, source, destination: str = None):
		pass

	@classmethod
	def link(cls, source: str, destination: str):
		pass

	@classmethod
	def link_exists(cls, path: str):
		pass

	@classmethod
	def is_link(cls, path: str) -> bool:
		return cls.link_exists(path)

	@classmethod
	def dir(cls, path: str):
		pass

	@classmethod
	def dir_create(cls, path: str, recursive: bool = True):
		pass

	@classmethod
	def dir_exists(cls, path: str) -> bool:
		return os.path.isdir(path)

	@classmethod
	def is_dir(cls, path: str) -> bool:
		return cls.dir_exists(path)

	@classmethod
	def dir_remove(cls, path: str, trash: bool = False):
		pass

	@classmethod
	def dir_trash(cls, path: str):
		cls.dir_remove(path) 

	@classmethod
	def dir_clear(cls, path: str):
		pass

	@classmethod
	def dir_copy(cls, source: str, destination: str = None):
		pass

	@classmethod
	def dir_move(cls, source: str, destination: str = None):
		pass

	@classmethod
	def dir_rename(cls, path: str, name: str = None):
		pass

	@classmethod
	def dir_info(cls, path: str):
		pass

	@classmethod
	def dir_sha256(cls, path: str, content: bool = True, time: bool = True, size: bool = True, permission: bool = True):
		pass

	@classmethod
	def dir_sha512(cls, path: str, content: bool = True, time: bool = True, size: bool = True, permission: bool = True):
		pass

	@classmethod
	def dir_gzip(cls, source: str, destination: str = None, compression = None):
		pass

	@classmethod
	def dir_zip(cls, source, destination: str = None, compression = None):
		pass

	@classmethod
	def dir_void(cls, source, destination: str = None, compression = None, key: str = None):
		pass

	@classmethod
	def drive(cls, path: str = None):
		pass

	@classmethod
	def drive_info(cls, path: str = None):
		return cls.drive(path)

	@classmethod
	def drive_create(cls, path: str, size, format: str = None, name: str = None):
		pass

	@classmethod
	def drive_exists(cls, path: str):
		pass

	@classmethod
	def is_drive(cls, path: str) -> bool:
		return cls.drive_exists(path)

	@classmethod
	def drive_remove(cls, path: str):
		pass

	@classmethod
	def drive_clear(cls, path: str, format: str = None, name: str = None):
		pass

	@classmethod
	def drive_format(cls, path: str, format: str = None, name: str = None):
		cls.drive_clear(id, format, name)

	@classmethod
	def drive_rename(cls, path: str, name: str):
		pass

	@classmethod
	def drive_mount(cls, path: str):
		pass

	@classmethod
	def drive_unmount(cls, path: str):
		pass

	@classmethod
	def drive_resize(cls, path: str, size):
		pass

	@classmethod
	def drive_check(cls, path: str):
		pass

	@classmethod
	def drive_defrag(cls, path: str):
		pass

	@classmethod
	def drive_os(cls, path: str = None, name: str = None):
		pass

	@classmethod
	def path(cls, *path):
		if len(path) == 0:
			return os.getcwd()
		if len(path) == 1 and type(path[0]) is str:
			path = path[0]
			return {
				'full': cls.path_full(path),
				'file': cls.path_file(path),
				'name': cls.path_name(path),
				'extension': cls.path_extension(path),
				'dir': cls.path_dir(path),
				'drive': cls.path_drive(path)
			}
		#delimiter = cls.get('app.os.delimiter.path')
		delimiter = '/'
		if len(path) == 2 and path[1] in ['full', 'file', 'name', 'extension', 'dir', 'drive', 'strip', 'start', 'end']:
			component = path[1]
			path = str(path[0])
		else:
			component = 'build'
			if len(path) > 0 and type(path[0]) is list:
				path = path[0]
		match component:
			case 'full':
				if len(path) > 0:
					if path[0] == '/':
						return path
					if len(path) > 1 and path[1] == ':':
						return path + ('\\' if len(path) == 2 else '')
				return os.getcwd() + delimiter + path
			case 'file' | 'end':
				index = path.rfind('/')
				if index >= 0:
					return path[index+1:]
				index = path.rfind('\\')
				if index >= 0:
					return path[index+1:]
			case 'name':
				index = path.rfind('/')
				if index >= 0:
					path = path[index+1:]
				else:
					index = path.rfind('\\')
					if index >= 0:
						path = path[index+1:]
				index = path.rfind('.')
				if index >= 0:
					return path[0:index]
				return path
			case 'extension':
				index = path.rfind('.')
				if index >= 0:
					return path[index+1:]
			case 'dir' | 'start':
				if path.rfind('.') > 0:
					index = path.rfind('/')
					if index >= 0:
						return path[0:index]
					index = path.rfind('\\')
					if index >= 0:
						path = path[0:index]
						if len(path) == 2 and path[1] == ':':
							return path + '\\'
				return path
			case 'drive':
				index = path.find(':')
				if index >= 0:
					return path[0:index].upper()
				if path.startswith('/mnt/') and len(path) > 5:
					path = path[5:]
					index = path.find('/')
					if index >= 0:
						return path[:index]
					return
				if path.startswith('/Volumes/') and len(path) > 9:
					path = path[9:]
					index = path.find('/')
					if index >= 0:
						return path[:index]
					return
			case 'strip':
				index = path.rfind('.')
				if index >= 0:
					return path[0:index]
				index = path.rfind('/')
				if index >= 0:
					return path[0:index]
				index = path.rfind('\\')
				if index >= 0:
					path = path[0:index]
					if len(path) == 2 and path[1] == ':':
						path += '\\'
					return path
			case _:
				result = ''
				for index, name in enumerate(path):
					name = str(name).strip().rstrip('/').rstrip('\\')
					if index == 0:
						if not (name.startswith('/') or (len(name) > 1 and name[1] == ':')):
							name = os.getcwd() + delimiter + name
					else:
						name = name.lstrip('/').lstrip('\\')
						name = delimiter + name
					result += name
				return result

	@classmethod
	def path_full(cls, path: str):
		return cls.path(path, 'full')

	@classmethod
	def path_file(cls, path: str):
		return cls.path(path, 'file')

	@classmethod
	def path_end(cls, path: str):
		return cls.path(path, 'end')

	@classmethod
	def path_name(cls, path: str):
		return cls.path(path, 'name')

	@classmethod
	def path_extension(cls, path: str, *extension):
		result = cls.path(path, 'extension')
		if len(extension):
			return result in extension
		return result

	@classmethod
	def path_dir(cls, path: str):
		return cls.path(path, 'dir')

	@classmethod
	def path_start(cls, path: str):
		return cls.path(path, 'start')

	@classmethod
	def path_dir(cls, path: str):
		return cls.path(path, 'dir')

	@classmethod
	def path_drive(cls, path: str):
		return cls.path(path, 'drive')

	@classmethod
	def path_strip(cls, path: str):
		return cls.path(path, 'strip')

	@classmethod
	def path_build(cls, *path):
		return cls.path(path, 'build')


  # format

	@classmethod
	def void(cls, data, style: str = None, indent = '\t', level: int = 0):
		pass

	@classmethod
	def void_decode(cls, data):
		if isinstance(data, str):
			if data == 'none':
				return None
			if data == 'true':
				return True
			if data == 'false':
				return False
			if data.isdigit():
				return cls.number(data)
		return data

	@classmethod
	def json(cls, data, compact: bool = False, indent = 2, unicode: bool = True):
		try:
			json = cls.module('json')
			if not compact:
				separators = (', ', ': ')
			else:
				indent = None
				separators = (',', ':')
			return json.dumps(data, ensure_ascii=not unicode, indent=indent, separators=separators)
		except:
			return

	@classmethod
	def json_decode(cls, text: str):
		try:
			json = cls.module('json')
			return json.loads(text)
		except:
			return

	@classmethod
	def csv(cls, data, delimiter: str = ','):
		try:
			csv = cls.module('csv')
			result = io.StringIO()
			writer = csv.writer(result, delimiter=delimiter)
			for row in data:
				writer.writerow(row)
			return result.getvalue()
		except:
			return

	@classmethod
	def csv_decode(cls, text: str, delimiter: str = ','):
		try:
			csv = cls.module('csv')
			return list(csv.reader(io.StringIO(text), delimiter=delimiter))
		except:
			return

	@classmethod
	def yaml(cls, data, compact: bool = False, sort: bool = False, unicode: bool = True):
		try:
			yaml = cls.module('yaml', 'pyyaml')
			return yaml.dump(data, default_flow_style=compact, sort_keys=sort, allow_unicode=unicode)
		except:
			return

	@classmethod
	def yaml_decode(cls, text: str):
		try:
			yaml = cls.module('yaml', 'pyyaml')
			return yaml.safe_load(text)
		except:
			return

	@classmethod
	def xml(cls, data: dict, compact: bool = False, indent = 2):
		try:
			xml = cls.module('xml.etree.ElementTree')
			def build(parent, data_item):
				if isinstance(data_item, dict):
					for name, value in data_item.items():
						if name.startswith('@'):
							parent.set(name[1:], str(value))
						elif name == '#text':
							parent.text = str(value)
						elif isinstance(value, list):
							for item in value:
								child = xml.SubElement(parent, name)
								build(child, item)
						else:
							child = xml.SubElement(parent, name)
							build(child, value)
				else:
					parent.text = str(data_item)
			if len(data) == 1:
				root = list(data.keys())[0]
				root_element = xml.Element(root)
				build(root_element, data[root])
			else:
				root_element = xml.Element('xml')
				build(root_element, data)
			if not compact and hasattr(xml, 'indent'):
				if type(indent) is int:
					indent = ' ' * indent
				elif type(indent) is not str:
					indent = '  '
				xml.indent(root_element, space=indent, level=0)
			return xml.tostring(root_element, encoding='unicode')
		except Exception as e:
			return

	@classmethod
	def xml_decode(cls, text: str):
		try:
			xml = cls.module('xml.etree.ElementTree')
			def build(element):
				res = {'@' + name: value for name, value in element.attrib.items()}
				children = list(element)
				if children:
					for child in children:
						child_data = build(child)
						for tag, value in child_data.items():
							if tag in res:
								if not isinstance(res[tag], list):
									res[tag] = [res[tag]]
								res[tag].append(value)
							else:
								res[tag] = value
				else:
					if element.text and element.text.strip():
						text_value = element.text.strip()
						if not res:
							return {element.tag: text_value}
						res['#text'] = text_value
				if not res and not children:
					return {element.tag: None}					
				return {element.tag: res}
			root_node = xml.fromstring(text)
			return build(root_node)
		except Exception as e:
			return

	@classmethod
	def ini(cls, data: dict):
		try:
			configparser = cls.module('configparser')
			config = configparser.ConfigParser()
			for section, content in data.items():
				if isinstance(content, dict):
					config[str(section)] = {str(k): str(v) for k, v in content.items()}
				else:
					if 'DEFAULT' not in config:
						config['DEFAULT'] = {}
					config['DEFAULT'][str(section)] = str(content)
			
			output = io.StringIO()
			config.write(output)
			return output.getvalue()
		except:
			return

	@classmethod
	def ini_decode(cls, text: str):
		try:
			configparser = cls.module('configparser')
			config = configparser.ConfigParser()
			config.read_string(text)
			result = {}
			for section in config.sections():
				result[section] = dict(config.items(section))
			if dict(config.defaults()):
				result['DEFAULT'] = dict(config.defaults())				
			return result
		except:
			return None


	# cloud

	@classmethod
	def cloud(cls):
		pass

	@classmethod
	def cloud_file(cls):
		pass

	@classmethod
	def cloud_web(cls):
		pass

	@classmethod
	def cloud_api(cls):
		pass

	@classmethod
	def cloud_socket(cls):
		pass

	@classmethod
	def cloud_mail(cls):
		pass

	@classmethod
	def cloud_vpn(cls):
		pass

	@classmethod
	def cloud_proxy(cls):
		pass

	@classmethod
	def cloud_stream(cls):
		pass

	@classmethod
	def cloud_desktop(cls):
		pass

	@classmethod
	def request(cls):
		pass

	@classmethod
	def r(cls):
		pass

	@classmethod
	def download(cls):
		pass

	@classmethod
	def d(cls):
		pass

	@classmethod
	def cookie(cls):
		pass

	@classmethod
	def cookie_remove(cls):
		pass

	@classmethod
	def notify(cls):
		pass

	@classmethod
	def notify_os(cls):
		pass

	@classmethod
	def notify_push(cls):
		pass

	@classmethod
	def notify_mail(cls):
		pass

	@classmethod
	def notify_sms(cls):
		pass

	@classmethod
	def notify_call(cls):
		pass

	@classmethod
	def notify_social(cls):
		pass

	@classmethod
	def social(cls):
		pass

	@classmethod
	def social_google(cls):
		pass

	@classmethod
	def social_yandex(cls):
		pass

	@classmethod
	def social_baidu(cls):
		pass

	@classmethod
	def social_youtube(cls):
		pass

	@classmethod
	def social_tiktok(cls):
		pass

	@classmethod
	def social_douyin(cls):
		pass

	@classmethod
	def social_x(cls):
		pass

	@classmethod
	def social_reddit(cls):
		pass

	@classmethod
	def social_telegram(cls):
		pass

	@classmethod
	def social_wechat(cls):
		pass

	@classmethod
	def social_twitch(cls):
		pass

	@classmethod
	def social_facebook(cls):
		pass

	@classmethod
	def social_whatsapp(cls):
		pass

	@classmethod
	def social_instagram(cls):
		pass

	@classmethod
	def social_vk(cls):
		pass

	@classmethod
	def social_line(cls):
		pass

	@classmethod
	def social_linkedin(cls):
		pass

	@classmethod
	def social_steam(cls):
		pass


  # device

	@classmethod
	def device(cls):
		pass

	@classmethod
	def cpu(cls):
		pass

	@classmethod
	def gpu(cls):
		pass

	@classmethod
	def memory(cls):
		pass

	@classmethod
	def battery(cls):
		pass

	@classmethod
	def fps(cls):
		pass

	@classmethod
	def vsync(cls):
		pass

	@classmethod
	def resolution(cls):
		pass

	@classmethod
	def orientation(cls):
		pass

	@classmethod
	def dark(cls):
		pass

	@classmethod
	def pixel(cls):
		pass

	@classmethod
	def symbol(cls):
		pass

	@classmethod
	def clear(cls):
		pass

	@classmethod
	def cursor(cls):
		pass

	@classmethod
	def flashlight(cls):
		pass

	@classmethod
	def location(cls):
		pass

	@classmethod
	def accelerometer(cls):
		pass

	@classmethod
	def gyroscope(cls):
		pass

	@classmethod
	def compass(cls):
		pass

	@classmethod
	def proximity(cls):
		pass

	@classmethod
	def brightness(cls):
		pass

	@classmethod
	def volume(cls):
		pass

	@classmethod
	def calendar(cls):
		pass

	@classmethod
	def gallery(cls):
		pass

	@classmethod
	def contacts(cls):
		pass

	@classmethod
	def call(cls):
		pass

	@classmethod
	def sms(cls):
		pass

	@classmethod
	def net(cls):
		pass

	@classmethod
	def wifi(cls):
		pass

	@classmethod
	def bluetooth(cls):
		pass

	@classmethod
	def cellular(cls):
		pass

	@classmethod
	def keyboard(cls):
		pass

	@classmethod
	def mouse(cls):
		pass

	@classmethod
	def gamepad(cls):
		pass

	@classmethod
	def tap(cls):
		pass

	@classmethod
	def click(cls):
		return cls.tap()


  # content

	@classmethod
	def image(cls):
		pass

	@classmethod
	def video(cls):
		pass

	@classmethod
	def movie(cls):
		return cls.video()

	@classmethod
	def clip(cls):
		return cls.video()

	@classmethod
	def anime(cls):
		return cls.video()

	@classmethod
	def sound(cls):
		pass

	@classmethod
	def music(cls):
		return cls.sound()

	@classmethod
	def model(cls):
		pass

	@classmethod
	def book(cls):
		pass

	@classmethod
	def document(cls):
		return cls.book()

	@classmethod
	def spreadsheet(cls):
		return cls.book()

	@classmethod
	def presentation(cls):
		return cls.book()

	@classmethod
	def comics(cls):
		return cls.book()

	@classmethod
	def manga(cls):
		return cls.book()

	@classmethod
	def game(cls):
		pass

	@classmethod
	def game_2d(cls):
		return cls.game()

	@classmethod
	def game_3d(cls):
		return cls.game()

	@classmethod
	def game_vn(cls):
		return cls.game()


if isinstance(VOIDlang.data, str):
	#VOIDlang.data = cls.void_decode(cls.data)
	VOIDlang.data = {
		'app': {
			'os': {
				'delimiter': {
					'line': '\n'
				},
				'path': {
					'ffmpeg': None,
					'yt-dlp': None
				}
			},
			'ui': 'cli',
			'format': {
				'text': ['php', 'text', 'txt', 'py', 'json']
			}
		},
		't': {}
	}

if __name__ == '__main__':
	VOIDlang.run()
