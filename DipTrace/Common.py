#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!

import enum

from lxml import etree


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


class Common(object):
	__root: etree

	class Side(enum.Enum):
		Top = 'Top'
		Bottom = 'Bottom'

	def __init__(self, root: str):
		self.__root = etree.Element(root)

	def __str__(self) -> str:
		return etree.tostring(self.__root, encoding='utf-8', pretty_print=True).decode('utf-8')

	@property
	def root(self) -> etree:
		return self.__root

	@root.setter
	def root(self, element: etree):
		self.__root = element

	def load(self, xml: etree):
		if xml is etree:
			if xml.tag == self.root.tag:
				self.root = xml
		return self

	def _get_first_text_or_default(self, tag: str, default: str = '') -> str:
		x = self.__root.find(tag)
		if x is not None:
			return x.text
		else:
			return default

	def _get_first_attribute_or_default(self, tag: str, attribute: str, default: str = '') -> str:
		x = self.__root.find(tag)
		if x is not None:
			return x.get(attribute)
		else:
			return default

	def _get_first_or_new(self, tag: str) -> etree:
		x = self.__root.find(tag)
		if x is None:
			return etree.SubElement(self.root, tag)
		else:
			return x

	def _set_first_text(self, tag: str, value: str):
		self._get_first_or_new(tag).text = value


class CommonCoordinates(Common):

	def __init__(self, root: str, x: float = 0.0, y: float = 0.0):
		super().__init__(root)
		self.root.attrib['X'] = from_float(x)
		self.root.attrib['Y'] = from_float(y)

	@property
	def x(self) -> float:
		return to_float(self.root.get('X'))

	@x.setter
	def x(self, x: float):
		self.root.attrib['X'] = from_float(x)

	@property
	def y(self) -> float:
		return to_float(self.root.get('Y'))

	@y.setter
	def y(self, y: float):
		self.root.attrib['Y'] = from_float(y)


if __name__ == "__main__":
	pass
