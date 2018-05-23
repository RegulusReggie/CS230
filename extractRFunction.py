#!/usr/bin/env python 
import re
import sys

def getFunctions(filestring):
	linecount = filestring.count("\n")
	if not filestring.endswith("\n"):
		linecount += 1
	blocks_linenos = []
	# find starting and ending line point of each function
	lines = filestring.split('\n')
	for line in lines:
		line = re.sub('".*?"', '', line)
		line = re.sub("'.*?'", '', line)
	i = 0
	lineSearchIdx = 0
	while i < len(lines):
		funcDefIndex = lines[i].find('function', lineSearchIdx)
		if funcDefIndex != -1:
			start_lineno = i
			
			# matching function argument parentheses
			pointer = lines[i].find('(', funcDefIndex)
			while pointer == -1 and i < len(lines) - 1:
				i += 1
				pointer = lines[i].find('(', 0)
			if pointer == -1:
				break

			num_left_par = 1
			pointer += 1
			while i < len(lines) and num_left_par != 0:
				while pointer < len(lines[i]) and num_left_par != 0:
					if lines[i][pointer] == '(':
						num_left_par += 1
					if lines[i][pointer] == ')':
						num_left_par -= 1
					pointer += 1
				if num_left_par == 0:
					break
				i += 1
				pointer = 0
			if i >= len(lines):
				break

			# find the very next non whitespace character
			while i < len(lines):
				while pointer < len(lines[i]) and lines[i][pointer] == ' ':
					pointer += 1
				if pointer < len(lines[i]):
					break
				i += 1
				pointer = 0
			if i >= len(lines):
				break

			if lines[i][pointer] == '{':
				# matching function declaration curly braces
				curly_pointer = pointer + 1
				num_left_curly = 1
				while i < len(lines) and num_left_curly != 0:
					while curly_pointer < len(lines[i]) and num_left_curly != 0:
						if lines[i][curly_pointer] == '{':
							num_left_curly += 1
						if lines[i][curly_pointer] == '}':
							num_left_curly -= 1
						curly_pointer += 1
					if num_left_curly == 0:
						break
					i += 1
					curly_pointer = 0
				if i >= len(lines):
					break
				end_lineno = i
				lineSearchIdx = curly_pointer
			else:
				# matching inline function declaration
				# ignore anything after function() in this line, treat them as inline function declaration
				end_lineno = i
				i += 1
				lineSearchIdx = 0

			blocks_linenos.append((start_lineno, end_lineno))
		else:
			i += 1
			lineSearchIdx = 0

	strings = [""] * len(blocks_linenos)
	for i, line in enumerate(filestring.split('\n')):
		for j, linenos in enumerate(blocks_linenos):
			if i >= linenos[0] and i <= linenos[1]:
				strings[j] += line + "\n"
	for string in strings:
		string = string[:-1]
	return (blocks_linenos, strings)

if __name__ == '__main__':
	with open(sys.argv[1]) as f:
		blocks_linenos, strings = getFunctions(f.read())
		print('===============')
		for i, linenos in enumerate(blocks_linenos):
			print(linenos[0], linenos[1])
			for line in strings[i].split('\n'):
				print(line)
			print('===============')

		f.close()
