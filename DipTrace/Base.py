#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!

import os
from typing import Optional

import lxml.etree
from termcolor import colored
import DipTrace


class Base(object):
	defaults = {}
	hidden = {}
	extensions = ['xml', 'elixml', 'libxml']
	tag: str

	def __init__(self, *args, **kwargs):
		kwargs = {**self.defaults, **kwargs}
		if (len(args) > 0) and isinstance(args[0], lxml.etree._Element):  # noqa
			self.root = args[0]
		else:
			self.root = lxml.etree.Element(self.tag)
			for key, value in kwargs.items():
				if key in (self.defaults.keys()):
					if callable(value):
						setattr(self, key, value())
					else:
						setattr(self, key, value)

	def __str__(self) -> str:
		if hasattr(self, 'normalize'):
			self.normalize()
		return lxml.etree.tostring(self.root, encoding='utf-8', pretty_print=True).decode('utf-8')

	def save(self, filename: str):
		if hasattr(self, 'extensions') and isinstance(self.extensions, list) and len(self.extensions) > 0:
			name, extension = os.path.splitext(filename)
			if extension not in self.extensions:
				filename = name + '.' + self.extensions[0]

		with open(filename, 'w', encoding='utf-8') as datafile:
			print(colored(f'Saving: "{filename}"', 'green'))
			if hasattr(self, 'normalize'):
				self.normalize()
			if hasattr(self, 'pattern_library'):
				self.pattern_library.embedded()
			else:
				f = getattr(self, 'standalone', None)
				if callable(f):
					f()
			datafile.write(lxml.etree.tostring(
				self.root,
				xml_declaration=True,
				encoding='utf-8',
				pretty_print=True).decode('utf-8')
			)
		return self

	def load(self, filename: str):
		if (filename := DipTrace.get_correct_filename(filename, self.extensions)) is not None:
			self.root = lxml.etree.parse(filename).getroot()
			return self
		else:
			return None

	def _get_first_text_or_default(self, tag: str, default: Optional[str] = '') -> str:
		x = self.root.find(tag)
		if x is not None:
			return x.text
		else:
			return default

	def _get_first_attribute_or_default(self, tag: str, attribute: str, default: str = '') -> str:
		x = self.root.find(tag)
		if x is not None:
			return x.get(attribute)
		else:
			return default

	def _get_first_or_new(self, tag: str) -> lxml.etree:
		x = self.root.find(tag)
		if x is None:
			return lxml.etree.SubElement(self.root, tag)
		else:
			return x

	def _set_first_text(self, tag: str, value: str):
		self._get_first_or_new(tag).text = value

	def _get_all_sub_tags(self, tag: str, sub: str):
		x = self.root.find(tag)
		if x is None:
			lxml.etree.SubElement(self.root, tag)
			return ()
		else:
			return x.findall(sub)
