#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!

import enum


class DipTraceEnum(enum.Enum):
	@classmethod
	def from_str(cls, value: str):
		for k, v in cls.__members__.items():
			if k == value:
				return v
		raise ValueError(f'"{cls.__name__}" enum not found for "{value}"')


class Side(DipTraceEnum):
	Top = 'Top'
	Bottom = 'Bottom'


class ElectricType(DipTraceEnum):
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


class PinType(DipTraceEnum):
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


class SpiceModelType(DipTraceEnum):
	SubCkt = 'SubCkt'


class PartType(DipTraceEnum):
	Normal = 'Normal'
	Power = 'Power'
	NetPort = 'Net Port'


class ShapeType(DipTraceEnum):
	Line = 'Line'
	Arrow = 'Arrow'
	Arc = 'Arc'
	Rectangle = 'Rectangle'
	FillRect = 'FillRect'
	Obround = 'Obround'
	FillObround = 'FillObround'
	Polyline = 'Polyline'
	Polygon = 'Polygon'
	Text = 'Text'


class Style(DipTraceEnum):
	Free = 0
	TwoSides = 1
	ChipTwoSides = 2
	ChipFourSides = 3
