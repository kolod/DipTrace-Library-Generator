#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!

import DipTrace
from typing import Optional

import DipTrace.Base


class Category(DipTrace.Base):
	tag = 'Category'
	defaults = {
		'index': '0',
		'name': None
	}

	@property
	def index(self) -> Optional[str]:
		return self.root.get('Index', None)

	@index.setter
	def index(self, index: Optional[str]):
		if index is not None:
			self.root.attrib['Index'] = index
		elif 'Index' in self.root.attrib:
			del self.root.attrib

	@property
	def name(self) -> Optional[str]:
		return self._get_first_text_or_default('Name', None)

	@name.setter
	def name(self, name: Optional[str]):
		if name is not None:
			self._set_first_text('Name', name)
		else:
			for tag in self.root.findall('Name'):
				self.root.delete(tag)
