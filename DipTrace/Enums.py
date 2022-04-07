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
			if v.value == value:
				return v
		raise ValueError(f'"{cls.__name__}" enum not found for "{value}"')


class Units(DipTraceEnum):
	mm = 'mm'
	mil = 'mil'
	inch = 'inch'


class Units3D(DipTraceEnum):
	mm = 'mm'
	mil = 'mil'
	inch = 'inch'
	wings = 'Wings'


class DimensionUnits(DipTraceEnum):
	common = 'Common'
	mm = 'mm'
	mil = 'mil'
	inch = 'inch'


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
	Resistor = 'Resistor'
	Capacitor = 'Capacitor'
	Inductor = 'Inductor'
	Diode = 'Diode'
	BJT = 'BJT'
	JFET = 'JFET'
	MOSFET = 'MOSFET'
	GaAsTransistor = 'Ga As Transistor'
	CurrentSource = 'Current Source'
	VoltageSource = 'Voltage Source'
	VoltageDependentCurrentSource = 'Voltage Dependent Current Source'
	VoltageDependentVoltageSource = 'Voltage Dependent Voltage Source'
	CurrentDependentCurrentSource = 'Current Dependent Current Source'
	CurrentDependentVoltageSource = 'Current Dependent Voltage Source'
	ArbitraryBehavioralSource = 'Arbitrary Behavioral Source'
	MutualInductance = 'Mutual Inductance'
	TransmissionLine = 'Transmission Line'


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


class LayerType(DipTraceEnum):
	Top = 'Top'
	TopDimension = 'Top Dimension'
	TopAssembly = 'Top Assy'
	TopSilk = 'Top Silk'
	TopOutline = 'Top Outline'
	TopCourtyard = 'Top Courtyard'
	TopKeepout = 'Top Keepout'
	TopMask = 'Top Mask'
	TopPaste = 'Top Paste'
	Bottom = 'Bottom'
	BottomAssembly = 'Bottom Assy'
	BottomSilk = 'Bottom Silk'
	BottomOutline = 'Bottom Outline'
	BottomCourtyard = 'Bottom Courtyard'
	BottomKeepout = 'Bottom Keepout'
	BottomMask = 'Bottom Mask'
	BottomPaste = 'Bottom Paste'
	BottomDimension = 'Bottom Dimension'
	BoardCutout = 'Board Cutout'


class TerminalShape(DipTraceEnum):
	Rectangle = 'Rectangle'
	Obround = 'Obround'
	Polygon = 'Polygon'
	DShape = 'D-shape'


class HoleType(DipTraceEnum):
	Round = 'Round'
	Obround = 'Obround'


class PadShape(DipTraceEnum):
	Ellipse = 'Ellipse'
	Obround = 'Obround'
	Rectangle = 'Rectangle'
	Polygon = 'Polygon'
	DShape = 'D-shape'


class MountType(DipTraceEnum):
	SurfaceMount = 'Surface'
	ThroughHole = 'Through'


class Visible(DipTraceEnum):
	Hide = 'Hide'
	Show = 'Show'


class ModelType(DipTraceEnum):
	Outline = 'Outline'
	File = 'File'
	IPC = 'IPC-7351'


class DimensionType(DipTraceEnum):
	Horizontal = 'Horizontal'
	Vertical = 'Vertical'
	Free = 'Free'
	Radius = 'Radius'
	Pointer = 'Pointer'


class MaskType(DipTraceEnum):
	Common = None
	Open = 'Open'
	Tented = 'Tented'
	ByPaste = 'By Paste'


class PasteType(DipTraceEnum):
	Common = None
	Solder = 'Solder'
	NoSolder = 'No Solder'
	Segments = 'Segments'


class PatternType(DipTraceEnum):
	Free = 'Free'
	IPC = 'IPC-7351'
	Circle = 'Circle'
	Lines = 'Lines'
	Square = 'Square'
	Matrix = 'Matrix'
	Rectangle = 'Rectangle'
	ZigZag = 'Zig-Zag'


class VisibleType(DipTraceEnum):
	Common = 0
	Show = 1
	Hide = 2
