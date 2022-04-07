#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!

import DipTrace
from typing import Optional, List


class ComponentLibrary(DipTrace.LibraryMixin):
	extensions = ['elixml', 'xml', 'libxml']
	defaults = {
		'type': 'DipTrace-ComponentLibrary',
		'name': '',
		'hint': '',
		'version': '4.2.0.1',
		'units': DipTrace.Units.mm,
		'pattern_library': DipTrace.PatternLibrary(),
		'components': []
	}

	@property
	def pattern_library(self) -> Optional[DipTrace.PatternLibrary]:
		if (x := self.root.find('Library')) is not None:
			return DipTrace.PatternLibrary(x)
		else:
			return None

	@pattern_library.setter
	def pattern_library(self, library):
		self.root.replace(self._get_first_or_new('Library'), library.root)

	@property
	def components(self) -> Optional[List[DipTrace.Component]]:
		if (x := self.root.find('Components')) is not None:
			return list(map(lambda v: DipTrace.Component(v), x.findall('Component')))
		else:
			return None

	@components.setter
	def components(self, components: Optional[List[DipTrace.Component]]):
		if components is not None:
			x = self._get_first_or_new('Components')
			for component in components:
				x.append(component.root)
		elif x := self.root.find('Components'):
			self.root.remove(x)

	def normalize(self):
		if (components := self.root.find('Components')) is not None:
			if (component := components.find('Component')) is not None:
				for pin in component.findall('Part/Pins/Pin'):
					if pin.attrib.get('Group', None) is "0":
						del pin.attrib['Group']
				for pin in component.findall('Part/Shapes/Shape'):
					if pin.attrib.get('Group', None) is "0":
						del pin.attrib['Group']
