#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!

import os

import lxml.etree
from termcolor import colored
import DipTrace


def store_temp(data, name) -> str:
	if not os.path.exists('temp'):
		os.mkdir('temp')

	filename = f'temp/{name}'
	with open(filename, 'w', encoding='utf-8') as f:
		f.write(data)
		return filename


def compare(filename: str, xpath_first: str, xpath_second: str):
	xml = lxml.etree.parse(filename)
	first = xml.xpath(xpath_first)[0]
	second = xml.xpath(xpath_second)[0]

	if first is None:
		print(colored(f"Can't find first element: '{xpath_first}'", 'red'))
		return

	if second is None:
		print(colored(f"Can't find second element: '{xpath_second}'", 'red'))
		return

	first_text = lxml.etree.tostring(first, xml_declaration=True, encoding='utf-8', pretty_print=True).decode('utf8')
	second_text = lxml.etree.tostring(second, xml_declaration=True, encoding='utf-8', pretty_print=True).decode('utf8')

	first_file = store_temp(first_text, 'first')
	second_file = store_temp(second_text, 'second')

	DipTrace.format_xml(first_file)
	DipTrace.format_xml(second_file)
	DipTrace.compare(first_file, second_file)


if __name__ == '__main__':
	compare('expected/LEDs.elixml', '/Library/Components/Component[1]/Part', '/Library/Components/Component[8]/Part')
