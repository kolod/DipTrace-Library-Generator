#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!

import math
import DipTrace
from typing import List, Callable


def shapes_3mm() -> List[DipTrace.Shape]:
	r = 1.5
	x1 = r * math.cos(math.radians(45))
	y1 = r * math.sin(math.radians(45))
	x2 = r * math.cos(math.radians(45))
	y2 = r * math.sin(math.radians(45))

	r3 = 3.85 / 2
	x3 = 1.6
	y3 = math.sqrt(math.pow(r3, 2) - math.pow(x3, 2))

	return [
		DipTrace.Shape(
			points=[
				DipTrace.Point(x=-x1, y=-y1),
				DipTrace.Point(x=0.0, y=-r),
				DipTrace.Point(x=x2, y=-y2),
			],
			all_layers=False,
			locked=True,
			type=DipTrace.ShapeType.Arc,
			layer=DipTrace.LayerType.TopSilk,
		),
		DipTrace.Shape(
			points=[
				DipTrace.Point(x=-x1, y=y1),
				DipTrace.Point(x=0, y=r),
				DipTrace.Point(x=x2, y=y2),
			],
			all_layers=False,
			locked=True,
			type=DipTrace.ShapeType.Arc,
			layer=DipTrace.LayerType.TopSilk,
		),
		DipTrace.Shape(
			points=[
				DipTrace.Point(x=-x3, y=-y3),
				DipTrace.Point(x=0.0, y=-r3),
				DipTrace.Point(x=-x3, y=y3),
			],
			all_layers=False,
			locked=True,
			type=DipTrace.ShapeType.Arc,
			layer=DipTrace.LayerType.TopCourtyard,
		),
		DipTrace.Shape(
			points=[
				DipTrace.Point(x=-x3, y=-y3),
				DipTrace.Point(x=-x3, y=y3),
			],
			all_layers=False,
			locked=True,
			type=DipTrace.ShapeType.Line,
			layer=DipTrace.LayerType.TopCourtyard,
		),
		DipTrace.Shape(
			points=[
				DipTrace.Point(x=-x3, y=-y3),
				DipTrace.Point(x=0.0, y=-r3),
				DipTrace.Point(x=-x3, y=y3),
			],
			all_layers=False,
			locked=True,
			type=DipTrace.ShapeType.Arc,
			layer=DipTrace.LayerType.TopAssembly,
		),
		DipTrace.Shape(
			points=[
				DipTrace.Point(x=-x3, y=-y3),
				DipTrace.Point(x=-x3, y=y3),
			],
			all_layers=False,
			locked=True,
			type=DipTrace.ShapeType.Line,
			layer=DipTrace.LayerType.TopAssembly,
		)
	]


def shapes_5mm() -> List[DipTrace.Shape]:
	r = 2.95
	x = 2.6
	xo = -0.175
	y = math.sqrt(math.pow(r, 2) - math.pow(x, 2))

	return [
		DipTrace.Shape(
			points=[
				DipTrace.Point(x=xo - x, y=-y),
				DipTrace.Point(x=xo, y=-r),
				DipTrace.Point(x=xo - x, y=y),
			],
			all_layers=False,
			locked=True,
			type=DipTrace.ShapeType.Arc,
			layer=DipTrace.LayerType.TopSilk,
		),
		DipTrace.Shape(
			points=[
				DipTrace.Point(x=xo - x, y=-y),
				DipTrace.Point(x=xo - x, y=y),
			],
			all_layers=False,
			locked=True,
			type=DipTrace.ShapeType.Line,
			layer=DipTrace.LayerType.TopSilk,
		),
		DipTrace.Shape(
			locked=True,
			points=[
				DipTrace.Point(x=xo - x, y=-y),
				DipTrace.Point(x=xo, y=-r),
				DipTrace.Point(x=xo - x, y=y),
			],
			all_layers=False,
			type=DipTrace.ShapeType.Arc,
			layer=DipTrace.LayerType.TopCourtyard,
		),
		DipTrace.Shape(
			points=[
				DipTrace.Point(x=xo - x, y=-y),
				DipTrace.Point(x=xo - x, y=y),
			],
			all_layers=False,
			locked=True,
			type=DipTrace.ShapeType.Line,
			layer=DipTrace.LayerType.TopCourtyard,
		),
		DipTrace.Shape(
			points=[
				DipTrace.Point(x=xo - x, y=-y),
				DipTrace.Point(x=xo, y=-r),
				DipTrace.Point(x=xo - x, y=y),
			],
			all_layers=False,
			locked=True,
			type=DipTrace.ShapeType.Arc,
			layer=DipTrace.LayerType.TopAssembly,
		),
		DipTrace.Shape(
			points=[
				DipTrace.Point(x=xo - x, y=-y),
				DipTrace.Point(x=xo - x, y=y),
			],
			all_layers=False,
			locked=True,
			type=DipTrace.ShapeType.Line,
			layer=DipTrace.LayerType.TopAssembly,
		)
	]


def pad_types() -> List[DipTrace.PadType]:
	return [
		DipTrace.PadType(
			name='PadT0',
			type=DipTrace.MountType.ThroughHole,
			hole_type=DipTrace.HoleType.Round,
			hole=0.9,
			main_stack=DipTrace.MainStack(
				shape=DipTrace.PadShape.Obround,
				width=1.5,
				height=1.5
			),
			terminals=[DipTrace.Terminal(
				shape=DipTrace.TerminalShape.Rectangle,
				width=0.45,
				height=0.45,
				corner=10
			)]
		),
		DipTrace.PadType(
			name='PadT1',
			type=DipTrace.MountType.ThroughHole,
			hole_type=DipTrace.HoleType.Round,
			hole=0.9,
			main_stack=DipTrace.MainStack(
				shape=DipTrace.PadShape.Rectangle,
				width=1.5,
				height=1.5,
				corner=10
			),
			terminals=[DipTrace.Terminal(
				shape=DipTrace.TerminalShape.Rectangle,
				width=0.45,
				height=0.45,
				corner=10
			)]
		),
	]


def pads_3mm() -> List[DipTrace.Pad]:
	return [
		DipTrace.Pad(
			type='PadT1',
			number='1',
			x=-1.27,
			y=0,
			locked=True
		),
		DipTrace.Pad(
			type='PadT0',
			number='2',
			x=1.27,
			y=0,
			locked=True
		)
	]


def pads_5mm() -> List[DipTrace.Pad]:
	return [
		DipTrace.Pad(
			type='PadT1',
			number='1',
			x=-1.445,
			y=0.0,
			locked=True
		),
		DipTrace.Pad(
			type='PadT0',
			number='2',
			x=1.095,
			y=0.0,
			locked=True
		)
	]


def pattern_3mm(color: str) -> DipTrace.Pattern:
	return DipTrace.Pattern(
		name=f'LED-3mm-{color}',
		value=f'LED-3mm-{color}',
		reference='D',
		default_pad='PadT0',
		origin=DipTrace.Origin(
			cross=True,
			circle=True,
			common=DipTrace.Visible.Hide,
			courtyard=DipTrace.Visible.Show
		),
		pads=pads_3mm(),
		shapes=shapes_3mm(),
		model=DipTrace.Model3D(
			units=DipTrace.Units3D.mm,
			rotate=DipTrace.Rotate(x=90.0),
			offset=DipTrace.Offset(),
			zoom=DipTrace.Zoom(),
			filename=DipTrace.Filename(
				path=f'LED-3mm-{color}.step',
				var=f'LED-3mm-{color}.step'
			)
		)
	)


def pattern_5mm(color: str) -> DipTrace.Pattern:
	return DipTrace.Pattern(
		name=f'LED-5mm-{color}',
		value=f'LED-5mm-{color}',
		reference='D',
		default_pad='PadT0',
		origin=DipTrace.Origin(
			x=-0.175,
			cross=True,
			circle=True,
			common=DipTrace.Visible.Hide,
			courtyard=DipTrace.Visible.Show
		),
		pads=pads_5mm(),
		shapes=shapes_5mm(),
		model=DipTrace.Model3D(
			units=DipTrace.Units3D.mm,
			rotate=DipTrace.Rotate(x=90.0),
			offset=DipTrace.Offset(),
			zoom=DipTrace.Zoom(),
			ipc_x_offset=-0.175,
			filename=DipTrace.Filename(
				path=f'LED-5mm-{color}.step',
				var=f'LED-5mm-{color}.step'
			)
		)
	)


def pins() -> List[DipTrace.Pin]:
	return [
		DipTrace.Pin(
			number=1,
			name='P1',
			locked=True,
			orientation=180.0,
			x=2.54,
			y=0.0,
			length=2.54
		),
		DipTrace.Pin(
			number=2,
			name='P2',
			locked=True,
			orientation=0.0,
			x=-2.54,
			y=0.0,
			length=2.54
		)
	]


def shape() -> List[DipTrace.Shape]:
	x = 1.27 * math.sin(math.radians(60.0))

	return [
		DipTrace.Shape(
			width=0.25,
			enabled=True,
			points=[
				DipTrace.Point(x=-2.54, y=0.0),
				DipTrace.Point(x=2.54, y=0.0)
			],
			type=DipTrace.ShapeType.Line,
			locked=True,
		),
		DipTrace.Shape(
			width=0.25,
			enabled=True,
			points=[
				DipTrace.Point(x=-x, y=1.27),
				DipTrace.Point(x=x, y=0.00),
				DipTrace.Point(x=-x, y=-1.27),
				DipTrace.Point(x=-x, y=1.27)
			],
			type=DipTrace.ShapeType.Polyline,
			locked=True,
		),
		DipTrace.Shape(
			width=0.25,
			enabled=True,
			points=[
				DipTrace.Point(x=x, y=1.27),
				DipTrace.Point(x=x, y=-1.27)
			],
			type=DipTrace.ShapeType.Line,
			locked=True,
		),
		DipTrace.Shape(
			width=0.25,
			enabled=True,
			points=[
				DipTrace.Point(x=0.343, y=1.613),
				DipTrace.Point(x=1.587, y=3.492)
			],
			type=DipTrace.ShapeType.Arrow,
			locked=True,
		),
		DipTrace.Shape(
			width=0.25,
			enabled=True,
			points=[
				DipTrace.Point(x=-0.61, y=2.248),
				DipTrace.Point(x=0.635, y=4.127)
			],
			type=DipTrace.ShapeType.Arrow,
			locked=True,
		)
	]


def component_3mm(color: str, pattern: str) -> DipTrace.Component:
	return DipTrace.Component(
		parts=[
			DipTrace.Part(
				pattern=pattern,
				name=f'LED-3mm-{color}',
				value=f'LED-3mm-{color}',
				show_numbers=DipTrace.VisibleType.Hide,
				reference='D',
				part_name='Part 1',
				shapes=shape(),
				pins=pins(),
				spice_model=DipTrace.SpiceModel(
					model_type=DipTrace.SpiceModelType.SubCkt
				),
				category=DipTrace.Category()
			)
		]
	)


def component_5mm(color: str, pattern: str) -> DipTrace.Component:
	return DipTrace.Component(
		parts=[
			DipTrace.Part(
				pattern=pattern,
				name=f'LED-5mm-{color}',
				value=f'LED-5mm-{color}',
				show_numbers=DipTrace.VisibleType.Hide,
				reference='D',
				part_name='Part 1',
				shapes=shape(),
				pins=pins(),
				spice_model=DipTrace.SpiceModel(
					model_type=DipTrace.SpiceModelType.SubCkt
				),
				category=DipTrace.Category()
			)
		]
	)


def components(colors: List[str]):
	result = []
	index = 0

	for color in colors:
		result.append(component_3mm(color, f'PatType{index}'))
		index += 1

	for color in colors:
		result.append(component_5mm(color, f'PatType{index}'))
		index += 1

	return result


def make_patterns(colors: List[str], patterns: List[Callable[[str], DipTrace.Pattern]]) -> List[DipTrace.Pattern]:
	result = []
	for pattern in patterns:
		for color in colors:
			result.append(pattern(color))
	return result


if __name__ == "__main__":
	name                     = 'LEDs'
	led_colors               = ['green', 'red', 'orange', 'clear']
	source_patterns_path     = f'source/{name}.{DipTrace.PatternLibrary.extensions[0]}'
	expected_patterns_path   = f'expected/{name}.{DipTrace.PatternLibrary.extensions[0]}'
	actual_patterns_path     = f'actual/{name}.{DipTrace.PatternLibrary.extensions[0]}'
	expected_components_path = f'expected/{name}.{DipTrace.ComponentLibrary.extensions[0]}'
	actual_components_path   = f'actual/{name}.{DipTrace.ComponentLibrary.extensions[0]}'

	pattern_library = DipTrace.PatternLibrary(
		name='LEDs',
		hint='LEDs',
		pad_types=pad_types(),
		patterns=make_patterns(led_colors, [pattern_3mm, pattern_5mm])
	).save(actual_patterns_path)

	DipTrace.ComponentLibrary(
		name='LEDs',
		hint='LEDs',
		pattern_library=pattern_library,
		components=components(led_colors)
	).save(actual_components_path)

	DipTrace.format_xml(actual_patterns_path)
	DipTrace.format_xml(actual_components_path)
	DipTrace.format_xml(expected_patterns_path)
	DipTrace.format_xml(expected_components_path)
	DipTrace.compare(expected_patterns_path, actual_patterns_path)
	DipTrace.compare(expected_components_path, actual_components_path)
