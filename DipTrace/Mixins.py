#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!

import lxml.etree
from typing import Optional

import DipTrace


class Base(object):
	defaults = {}
	tag: str

	def __init__(self, *args, **kwargs):
		kwargs = {**self.defaults, **kwargs}
		if ('root' in kwargs.keys()) and (kwargs['root'] is not None):
			self.root = kwargs['root']
		else:
			self.root = lxml.etree.Element(self.tag)
		for key, value in kwargs.items():
			if key in (self.defaults.keys()):
				setattr(self, key, value)

	def __str__(self) -> str:
		return lxml.etree.tostring(self.root, encoding='utf-8', pretty_print=True).decode('utf-8')

	def save(self, filename: str):
		self.root.write(filename, method='xml', xml_declaration=True, encoding='utf-8', pretty_print=True)

	def load(self, filename: str):
		self.root = lxml.etree.parse(filename).getroot()
		return self

	def _get_first_text_or_default(self, tag: str, default: str = '') -> str:
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


class GroupMixin(Base):
	defaults = {'group': 0}

	@property
	def group(self) -> int:
		return DipTrace.to_int(self.root.get('Group'))

	@group.setter
	def group(self, group):
		self.root.attrib['Group'] = DipTrace.from_int(group)


class PointMixin(Base):
	defaults = {'x': 0.0, 'y': 0.0}

	@property
	def x(self) -> float:
		return DipTrace.to_float(self.root.get('X'))

	@x.setter
	def x(self, x: float):
		self.root.attrib['X'] = DipTrace.from_float(x)

	@property
	def y(self) -> float:
		return DipTrace.to_float(self.root.get('Y'))

	@y.setter
	def y(self, y: float):
		self.root.attrib['Y'] = DipTrace.from_float(y)


class EnabledMixin(Base):
	defaults = {'enabled': True}

	@property
	def enabled(self) -> bool:
		return DipTrace.to_bool(self.root.attrib.get('Enabled'))

	@enabled.setter
	def enabled(self, state: bool):
		self.root.attrib['Enabled'] = DipTrace.from_bool(state)


class LockedMixin(Base):
	defaults = {'locked': True}

	@property
	def locked(self) -> bool:
		return DipTrace.to_bool(self.root.attrib.get('Locked'))

	@locked.setter
	def locked(self, state: bool):
		self.root.attrib['Locked'] = DipTrace.from_bool(state)


class LibraryMixin(Base):
	tag = 'Library'
	defaults = {
		'version': '4.2.0.1',
		'units': 'mm',
		'name': '',
		'hint': '',
	}

	@property
	def type(self):
		return self.root.get("Type")

	@type.setter
	def type(self, value):
		self.root.attrib['Type'] = value

	@property
	def name(self) -> Optional[str]:
		return self.root.get("Name")

	@name.setter
	def name(self, name: str):
		self.root.attrib['Name'] = name

	@property
	def hint(self) -> Optional[str]:
		return self.root.get("Hint")

	@hint.setter
	def hint(self, hint: str):
		self.root.attrib['Hint'] = hint

	@property
	def version(self) -> Optional[str]:
		return self.root.get("Version")

	@version.setter
	def version(self, version: str):
		self.root.attrib['Version'] = version

	@property
	def units(self) -> Optional[str]:
		return self.root.get("Units")

	@units.setter
	def units(self, units: str):
		self.root.attrib['Units'] = units


if __name__ == "__main__":
	pass
