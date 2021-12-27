#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!

from enum import Enum
from typing import Optional, Union
import DipTrace


class Pin(DipTrace.CommonCoordinates):
	class ElectricType(Enum):
		Undefined = 'Undefined'
		Passive = 'Passive'
		Input = 'Input'
		Output = 'Output'
		Bidirectional = 'Bidirectional'
		OpenHigh = 'Open High'
		OpenLow = 'Open Low'
		PassiveHigh = 'Passive High'
		PassiveLow = 'Passive Low'
		ThreeState = '3 State'
		Power = 'Power'

	class PinType(Enum):
		Default = 'Default'
		Dot = 'Dot'
		PolarityIn = 'Polarity In'
		PolarityOut = 'Polarity Out'
		NonLogic = 'Non Logic'
		Open = 'Open'
		OpenHigh = 'Open High'
		ThreeState = '3 State'
		Hysteresis = 'Hysteresis'
		Amplifier = 'Amplifier'
		Postponed = 'Postponed'
		Shift = 'Shift'
		Clock = 'Clock'
		Generator = 'Generator'

	def __init__(self, name: str = '', number: str = '', x: float = 0.0, y: float = 0.0):
		super().__init__('Pin', x, y)
		self.name = name
		self.number = number
		self.enabled = True
		self.locked = False
		self.pin_type = self.PinType.Default
		self.electric_type = self.ElectricType.Undefined
		self.orientation = 0
		self.pad_index = 1
		self.length = 2.54
		self.show_name = False
		self.number_x_shift = 0
		self.number_y_shift = 0
		self.name_x_shift = 0
		self.name_y_shift = 0
		self.signal_delay = 0
		self.number_orientation = 0
		self.name_orientation = 0
		self.font = DipTrace.NameFont()

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
	def electric_type(self) -> Optional[ElectricType]:
		return self.root.get("ElectricType")

	@electric_type.setter
	def electric_type(self, electric_type: ElectricType):
		self.root.attrib['ElectricType'] = electric_type.name

	@property
	def pin_type(self) -> Optional[PinType]:
		return self.root.get("Type")

	@pin_type.setter
	def pin_type(self, pin_type: PinType):
		self.root.attrib['Type'] = pin_type.name

	@property
	def enabled(self) -> bool:
		return DipTrace.to_bool(self.root.attrib.get('Enabled'))

	@enabled.setter
	def enabled(self, state: bool):
		self.root.attrib['Enabled'] = DipTrace.from_bool(state)

	@property
	def locked(self) -> bool:
		return DipTrace.to_bool(self.root.attrib.get('Locked'))

	@locked.setter
	def locked(self, state: bool):
		self.root.attrib['Locked'] = DipTrace.from_bool(state)

	@property
	def show_name(self) -> bool:
		return DipTrace.to_bool(self.root.attrib.get('ShowName'))

	@show_name.setter
	def show_name(self, state: bool):
		self.root.attrib['ShowName'] = DipTrace.from_bool(state)

	@property
	def font(self):
		return DipTrace.NameFont().load(self.root.find('NameFont'))

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


if __name__ == "__main__":
	pass
