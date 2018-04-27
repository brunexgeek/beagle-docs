#!/usr/bin/python

import sys
import os
import re

if len(sys.argv) > 1:
	sourceFile = sys.argv[0]
else:
	sourceFile = os.path.dirname( os.path.realpath(sys.argv[0]) )
	sourceFile = os.path.join(sourceFile, 'language/grammar.txt')

pos = sourceFile.rfind('.')
if pos >= 0:
	outputFile = sourceFile[0:pos] + '.rst'
else:
	outputFile = sourceFile + '.rst'

contained = False

with open(sourceFile, 'rt') as input:
	with open(outputFile, 'wt') as output:
		output.write('Grammar\n')
		output.write('=======\n\n')

		output.write(".. role:: bgram-string\n\n")
		output.write(".. role:: bgram-detail\n\n")

		for line in input:
			line = line.strip()

			if len(line) == 0:
				output.write('\n')
				continue
			elif (line[0] == '#'):
				continue
			elif line[0] == '!':
				output.write( line[1:].strip() );
				output.write('\n')
				contained = False
				continue

			if not contained:
				contained = True
				output.write(".. container:: grammar\n\n")


			output.write('\t');

			if line[0] == ':':

				output.write('\t: ')

				tokens = [ i for i in re.split( r'(\w+|"[^"]+"|\'[^\']+\'|<[^>]+>|\d+| |\?|\(|\)|\.|\*)', line[1:].strip() ) if len(i) > 0]
				for i in tokens:
					if i != ' ':
						output.write('\ ')

					if i == '*':
						output.write('\\' + i )
					elif i[0] == '"':
						output.write(':bgram-string:`' + i + '`')
					elif i[0] == '<':
						output.write(':bgram-detail:`' + i + '`')
					elif len(i) == 1:
						output.write(i)
					else:
						output.write(':ref:`' + i + '<section-' + i + '>`')
				output.write('\n\n')
			elif line[0] == ';':
				output.write('\t;\n')
			else:
				output.write('.. _section-' + line + ':\n')
				output.write('\t.. rst-class:: non-terminal\n\n\t')
				output.write(line)
				output.write('\n')

