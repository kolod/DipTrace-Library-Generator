#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!

from typing import Optional
import DipTrace


class ComponentLibrary(DipTrace.LibraryMixin):
	defaults = {
		'type': 'DipTrace-ComponentLibrary',
		'name': '',
		'hint': '',
		'version': '4.2.0.1',
		'units': 'mm',
		'pattern_library': DipTrace.PatternLibrary(),
	}

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

	@property
	def pattern_library(self) -> Optional[str]:
		# TODO: convert xml to object
		return None

	@pattern_library.setter
	def pattern_library(self, library):
		print(str(library))
		self.root.replace(self._get_first_or_new('Library'), library.root)

	def add_components(self, components):
		if type(components) is list:
			for component in components:
				self.add_components(component)
		elif type(components) is DipTrace.Component:
			self._get_first_or_new('Components').append(components.root)
		return self

	def save(self, filename: str):
		with open(filename, 'w', encoding='utf-8') as datafile:
			datafile.write(f'<?xml version="1.0" encoding="utf-8"?>\n{self}')


if __name__ == "__main__":
	pass
