#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!

from typing import Tuple, Optional
import DipTrace


class Pattern(
	DipTrace.ReferenceMixin,
	DipTrace.WidthHeightMixin,
	DipTrace.ShapesMixin,
	DipTrace.PadsMixin,
	DipTrace.TypeLockedMixin,
	DipTrace.DimensionsMixin,
	DipTrace.OrientationMixin,
	DipTrace.OriginMixin,
	DipTrace.CategoryMixin
):
	tag = 'Pattern'
	defaults = {
		**DipTrace.ReferenceMixin.defaults,
		'mounting': 'None',
		**DipTrace.WidthHeightMixin.defaults,
		**DipTrace.OrientationMixin.defaults,
		'name': '',
		'value': '',
		**DipTrace.CategoryMixin.defaults,
		'origin': None,
		'default_pad': None,
		**DipTrace.TypeLockedMixin.defaults,
		'type': DipTrace.PatternType.Free,
		'parameters': (0.0, 0.0, 0.0, 0, 0),
		**DipTrace.PadsMixin.defaults,
		**DipTrace.ShapesMixin.defaults,
		**DipTrace.DimensionsMixin.defaults,
		'model': None,
	}

	@property
	def type(self) -> DipTrace.PatternType:
		return DipTrace.PatternType.from_str(self.root.get('Type'))

	@type.setter
	def type(self, t: DipTrace.PatternType):
		self.root.attrib['Type'] = t.value

	@property
	def mounting(self) -> str:
		return self.root.get('Mounting')

	@mounting.setter
	def mounting(self, value: str):
		self.root.attrib['Mounting'] = value

	@property
	def name(self) -> str:
		return self._get_first_text_or_default('Name')

	@name.setter
	def name(self, value: str):
		self._set_first_text('Name', value)

	@property
	def value(self) -> str:
		return self._get_first_text_or_default('Value')

	@value.setter
	def value(self, value: str):
		self._set_first_text('Value', value)

	@property
	def default_pad_type(self) -> str:
		return self._get_first_attribute_or_default('DefPad', 'PadType')

	@default_pad_type.setter
	def default_pad_type(self, name: str):
		self._get_first_or_new('DefPad').attrib['PadType'] = name

	@property
	def parameters(self) -> Tuple[float, float, float, int, int]:
		return (
			DipTrace.to_float(self.root.get('Float1')),
			DipTrace.to_float(self.root.get('Float2')),
			DipTrace.to_float(self.root.get('Float3')),
			DipTrace.to_int(self.root.get('Int1')),
			DipTrace.to_int(self.root.get('Int2')),
		)

	@parameters.setter
	def parameters(self, parameters: Tuple[float, float, float, int, int]):
		self.root.attrib['Float1'] = DipTrace.from_float(parameters[0])
		self.root.attrib['Float2'] = DipTrace.from_float(parameters[1])
		self.root.attrib['Float3'] = DipTrace.from_float(parameters[2])
		self.root.attrib['Int1'] = DipTrace.from_int(parameters[3])
		self.root.attrib['Int2'] = DipTrace.from_int(parameters[4])

	@property
	def default_pad(self) -> Optional[str]:
		if (x := self.root.find('DefPad')) is not None:
			return x.attribget('PadType')
		else:
			return None

	@default_pad.setter
	def default_pad(self, pad: Optional[str]):
		if pad is not None:
			self._get_first_or_new('DefPad').attrib['PadType'] = pad
		elif (x := self.root.find('DefPad')) is not None:
			self.root.remove(x)

	@property
	def model(self) -> Optional[DipTrace.Model3D]:
		if (x := self.root.find('Model3D')) is not None:
			return DipTrace.Model3D(x)
		else:
			return None

	@model.setter
	def model(self, model: Optional[DipTrace.Model3D]):
		if model is not None:
			self.root.replace(self._get_first_or_new('Model3D'), model.root)
		elif (x := self.root.find('Model3D')) is not None:
			self.root.remove(x)
