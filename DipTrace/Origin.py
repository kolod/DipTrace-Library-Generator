#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!

import DipTrace
from typing import Optional


class Origin(DipTrace.PointMixin):
	tag = 'Origin'
	defaults = {
		**DipTrace.PointMixin.defaults,
		'cross': None,
		'circle': None,
		'common': None,
		'courtyard': None
	}

	@property
	def cross(self) -> Optional[bool]:
		if 'Cross' in self.root.attrib:
			return DipTrace.to_bool(self.root.get('Cross'))
		else:
			return None

	@cross.setter
	def cross(self, cross: Optional[bool]):
		if cross is not None:
			self.root.attrib['Cross'] = DipTrace.from_bool(cross)
		elif 'Cross' in self.root.attrib:
			self.root.attrib.pop('Cross')

	@property
	def circle(self) -> Optional[bool]:
		if 'Circle' in self.root.attrib:
			return DipTrace.to_bool(self.root.get('Circle'))
		else:
			return None

	@circle.setter
	def circle(self, circle: Optional[bool]):
		if circle is not None:
			self.root.attrib['Circle'] = DipTrace.from_bool(circle)
		elif 'Circle' in self.root.attrib:
			self.root.attrib.pop('Circle')

	@property
	def common(self) -> Optional[DipTrace.Visible]:
		if 'Common' in self.root.attrib:
			return DipTrace.Visible.from_str(self.root.get('Common'))
		else:
			return None

	@common.setter
	def common(self, common: Optional[DipTrace.Visible]):
		if common is not None:
			self.root.attrib['Common'] = common.value
		elif 'Common' in self.root.attrib:
			self.root.attrib.pop('Common')

	@property
	def courtyard(self) -> Optional[DipTrace.Visible]:
		if 'Courtyard' in self.root.attrib:
			return DipTrace.Visible.from_str(self.root.get('Courtyard'))
		else:
			return None

	@courtyard.setter
	def courtyard(self, courtyard: Optional[DipTrace.Visible]):
		if courtyard is not None:
			self.root.attrib['Courtyard'] = courtyard.value
		elif 'Courtyard' in self.root.attrib:
			self.root.attrib.pop('Courtyard')


class OriginMixin(DipTrace.Base):
	defaults = {
		'origin': Origin()
	}

	@property
	def origin(self) -> Optional[Origin]:
		if (x := self.root.find('Origin')) is not None:
			return Origin(x)
		else:
			return None

	@origin.setter
	def origin(self, origin: Optional[Origin]):
		if origin is not None:
			self.root.replace(self._get_first_or_new('Origin'), origin.root)
		elif (x := self.root.find('Origin')) is not None:
			self.root.remove(x)
