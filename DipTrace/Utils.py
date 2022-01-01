#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!

import subprocess
import lxml.etree


def to_int(value: str, default: int = 0) -> int:
	try:
		return int(value)
	except ValueError:
		return default


def from_int(value: int) -> str:
	return str(value)


def to_float(value: str, default: float = 0.0) -> float:
	try:
		return float(value)
	except ValueError:
		return default


def from_float(value: float) -> str:
	if value >= 1 or value < 0:
		return f'{value:.5g}'
	else:
		return f'{value:.4g}'


def to_bool(val: str) -> bool:
	if val == 'Y':
		return True
	else:
		return False


def from_bool(val: bool) -> str:
	if val:
		return 'Y'
	else:
		return 'N'


def format_xml(filename: str):
	print(f'Format "{filename}"')
	parser = lxml.etree.XMLParser(remove_blank_text=True)
	xml = lxml.etree.parse(filename, parser)
	xml.write(filename, method='xml', xml_declaration=True, encoding='utf-8', pretty_print=True)


def compare(first: str, second: str):
	print(f'Compare "{first}" & "{second}"')
	subprocess.Popen(["C:/Program Files/WinMerge/WinMergeU.exe", first, second])
