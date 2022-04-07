#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!

import os
import subprocess
from typing import Optional, List
from termcolor import colored
import lxml.etree
import DipTrace


def to_int(value: Optional[str], default: int = 0) -> int:
	if value is None:
		return default
	else:
		try:
			return int(value)
		except ValueError:
			return default


def from_int(value: int) -> str:
	return str(value)


def to_float(value: Optional[str], default: float = 0.0) -> float:
	if value is None:
		return default
	else:
		try:
			return float(value)
		except ValueError:
			return default


def from_float(value: float) -> str:
	if value >= 1 or value < 0:
		return f'{value:.5g}'
	else:
		return f'{value:.4g}'


def to_bool(value: Optional[str]) -> bool:
	if value is None:
		return False
	else:
		if value == 'Y':
			return True
		else:
			return False


def from_bool(val: bool) -> str:
	if val:
		return 'Y'
	else:
		return 'N'


def sort_attrib(element: lxml.etree.Element, order: List[str]):
	old_attrib = dict(element.attrib)
	element.attrib.clear()
	for key in order:
		if key in old_attrib:
			element.attrib.set(key, old_attrib[key])


def get_correct_filename(filename: str, extensions: List[str]) -> Optional[str]:
	if os.path.isfile(filename):
		return filename

	for extension in extensions:
		path = f'{filename}.{extension}'
		if os.path.isfile(path):
			return path

	return None


def format_xml(filename: str):
	if (filename := get_correct_filename(filename, DipTrace.Base.extensions)) is not None:
		print(colored(f'Format "{filename}"', 'green'))
		parser = lxml.etree.XMLParser(remove_blank_text=True)
		xml = lxml.etree.parse(filename, parser)
		xml.write(filename, method='xml', xml_declaration=True, encoding='utf-8', pretty_print=True)
	else:
		print(colored(f'File "{filename}" not found', 'red'))


def compare(first: str, second: str):
	extensions = ['', 'xml']
	first_path = get_correct_filename(first, extensions)
	second_path = get_correct_filename(second, extensions)
	if first_path is None:
		print(colored(f'Error: File "{first}" not found.', 'red'))
		return

	if second_path is None:
		print(colored(f'Error: File "{second}" not found.', 'red'))
		return

	print(colored(f'Compare "{first_path}" & "{second_path}"', 'green'))
	subprocess.Popen(["C:/Program Files/WinMerge/WinMergeU.exe", '/s', first_path, second_path])
