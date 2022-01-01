#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!

from typing import Optional, Union
import DipTrace


class Pin(
	DipTrace.LockedMixin,
	DipTrace.EnabledMixin,
	DipTrace.PointMixin,
	DipTrace.GroupMixin,
):
	tag = 'Pin'
	defaults = {
		**DipTrace.PointMixin.defaults,
		**DipTrace.EnabledMixin.defaults,
		**DipTrace.LockedMixin.defaults,
		'name': '',
		'number': '',
		'pin_type': DipTrace.PinType.Default,
		'electric_type': DipTrace.ElectricType.Undefined,
		'orientation': 0,
		'pad_index': 1,
		'length': 2.54,
		'show_name': False,
		'number_x_shift': 0,
		'number_y_shift': 0,
		'name_x_shift': 0,
		'name_y_shift': 0,
		'signal_delay': 0,
		'number_orientation': 0,
		'name_orientation': 0,
		**DipTrace.GroupMixin.defaults,
		'font': DipTrace.NameFont(),
	}

	@property
	def name(self) -> Optional[str]:
		return self._get_first_text_or_default('Name')

	@name.setter
	def name(self, name: str):
		self._set_first_text('Name', name)

	@property
	def number(self) -> Optional[str]:
		return self._get_first_text_or_default('PadNumber')

	@number.setter
	def number(self, number: Union[str, int]):
		self._set_first_text('PadNumber', str(number))

	@property
	def pin_type(self) -> DipTrace.PinType:
		return DipTrace.PinType.from_str(self.root.get("Type"))

	@pin_type.setter
	def pin_type(self, pin_type: DipTrace.PinType):
		self.root.attrib['Type'] = pin_type.value

	@property
	def electric_type(self) -> DipTrace.ElectricType:
		return DipTrace.ElectricType.from_str(self.root.get("ElectricType"))

	@electric_type.setter
	def electric_type(self, electric_type: DipTrace.ElectricType):
		self.root.attrib['ElectricType'] = electric_type.value

	@property
	def show_name(self) -> bool:
		return DipTrace.to_bool(self.root.attrib.get('ShowName'))

	@show_name.setter
	def show_name(self, state: bool):
		self.root.attrib['ShowName'] = DipTrace.from_bool(state)

	@property
	def font(self) -> DipTrace.NameFont:
		return DipTrace.NameFont(root=self.root.find('NameFont'))

	@font.setter
	def font(self, font: DipTrace.NameFont):
		self.root.replace(self._get_first_or_new('NameFont'), font.root)

	@property
	def orientation(self) -> float:
		return DipTrace.to_float(self.root.get('Orientation'))

	@orientation.setter
	def orientation(self, value: float):
		self.root.attrib['Orientation'] = DipTrace.from_float(value)

	@property
	def length(self) -> float:
		return DipTrace.to_float(self.root.get('Length'))

	@length.setter
	def length(self, value: float):
		self.root.attrib['Length'] = DipTrace.from_float(value)

	@property
	def number_x_shift(self) -> float:
		return DipTrace.to_float(self.root.get('NumXShift'))

	@number_x_shift.setter
	def number_x_shift(self, value: float):
		self.root.attrib['NumXShift'] = DipTrace.from_float(value)

	@property
	def number_y_shift(self) -> float:
		return DipTrace.to_float(self.root.get('NumYShift'))

	@number_y_shift.setter
	def number_y_shift(self, value: float):
		self.root.attrib['NumYShift'] = DipTrace.from_float(value)

	@property
	def number_orientation(self) -> float:
		return DipTrace.to_float(self.root.get('NumOrientation'))

	@number_orientation.setter
	def number_orientation(self, value: float):
		self.root.attrib['NumOrientation'] = DipTrace.from_float(value)

	@property
	def name_x_shift(self) -> float:
		return DipTrace.to_float(self.root.get('NameXShift'))

	@name_x_shift.setter
	def name_x_shift(self, value: float):
		self.root.attrib['NameXShift'] = DipTrace.from_float(value)

	@property
	def name_y_shift(self) -> float:
		return DipTrace.to_float(self.root.get('NameYShift'))

	@name_y_shift.setter
	def name_y_shift(self, value: float):
		self.root.attrib['NameYShift'] = DipTrace.from_float(value)

	@property
	def name_orientation(self) -> float:
		return DipTrace.to_float(self.root.get('NameOrientation'))

	@name_orientation.setter
	def name_orientation(self, value: float):
		self.root.attrib['NameOrientation'] = DipTrace.from_float(value)

	@property
	def pad_index(self) -> int:
		return DipTrace.to_int(self.root.get('PadIndex'))

	@pad_index.setter
	def pad_index(self, value: int):
		self.root.attrib['PadIndex'] = DipTrace.from_int(value)

	@property
	def signal_delay(self) -> float:
		return DipTrace.to_float(self.root.get('SignalDelay')) / 3.0

	@signal_delay.setter
	def signal_delay(self, value: float):
		self.root.attrib['SignalDelay'] = DipTrace.from_float(value * 3.0)
