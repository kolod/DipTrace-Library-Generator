#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!

import DipTrace
import math
from typing import List

data = [
	{'uni': 'SMAJ5.0A', 'bi': 'SMAJ5.0CA', 'voltage': 5.0},
	{'uni': 'SMAJ6.0A', 'bi': 'SMAJ6.0CA', 'voltage': 6.0},
	{'uni': 'SMAJ6.5A', 'bi': 'SMAJ6.5CA', 'voltage': 6.5},
	{'uni': 'SMAJ7.0A', 'bi': 'SMAJ7.0CA', 'voltage': 7.0},
	{'uni': 'SMAJ7.5A', 'bi': 'SMAJ7.5CA', 'voltage': 7.5},
	{'uni': 'SMAJ8.0A', 'bi': 'SMAJ8.0CA', 'voltage': 8.0},
	{'uni': 'SMAJ8.5A', 'bi': 'SMAJ8.5CA', 'voltage': 8.5},
	{'uni': 'SMAJ9.0A', 'bi': 'SMAJ9.0CA', 'voltage': 9.0},
	{'uni': 'SMAJ10A', 'bi': 'SMAJ10CA', 'voltage': 10.0},
	{'uni': 'SMAJ11A', 'bi': 'SMAJ11CA', 'voltage': 11.0},
	{'uni': 'SMAJ12A', 'bi': 'SMAJ12CA', 'voltage': 12.0},
	{'uni': 'SMAJ13A', 'bi': 'SMAJ13CA', 'voltage': 13.0},
	{'uni': 'SMAJ14A', 'bi': 'SMAJ14CA', 'voltage': 14.0},
	{'uni': 'SMAJ15A', 'bi': 'SMAJ15CA', 'voltage': 15.0},
	{'uni': 'SMAJ16A', 'bi': 'SMAJ16CA', 'voltage': 16.0},
	{'uni': 'SMAJ17A', 'bi': 'SMAJ17CA', 'voltage': 17.0},
	{'uni': 'SMAJ18A', 'bi': 'SMAJ18CA', 'voltage': 18.0},
	{'uni': 'SMAJ20A', 'bi': 'SMAJ20CA', 'voltage': 20.0},
	{'uni': 'SMAJ22A', 'bi': 'SMAJ22CA', 'voltage': 22.0},
	{'uni': 'SMAJ24A', 'bi': 'SMAJ24CA', 'voltage': 24.0},
	{'uni': 'SMAJ26A', 'bi': 'SMAJ26CA', 'voltage': 26.0},
	{'uni': 'SMAJ28A', 'bi': 'SMAJ28CA', 'voltage': 28.0},
	{'uni': 'SMAJ30A', 'bi': 'SMAJ30CA', 'voltage': 30.0},
	{'uni': 'SMAJ33A', 'bi': 'SMAJ33CA', 'voltage': 33.0},
	{'uni': 'SMAJ36A', 'bi': 'SMAJ36CA', 'voltage': 36.0},
	{'uni': 'SMAJ40A', 'bi': 'SMAJ40CA', 'voltage': 40.0},
	{'uni': 'SMAJ43A', 'bi': 'SMAJ43CA', 'voltage': 43.0},
	{'uni': 'SMAJ45A', 'bi': 'SMAJ45CA', 'voltage': 45.0},
	{'uni': 'SMAJ48A', 'bi': 'SMAJ48CA', 'voltage': 48.0},
	{'uni': 'SMAJ51A', 'bi': 'SMAJ51CA', 'voltage': 51.0},
	{'uni': 'SMAJ54A', 'bi': 'SMAJ54CA', 'voltage': 54.0},
	{'uni': 'SMAJ58A', 'bi': 'SMAJ58CA', 'voltage': 58.0},
	{'uni': 'SMAJ60A', 'bi': 'SMAJ60CA', 'voltage': 60.0},
	{'uni': 'SMAJ64A', 'bi': 'SMAJ64CA', 'voltage': 64.0},
	{'uni': 'SMAJ70A', 'bi': 'SMAJ70CA', 'voltage': 70.0},
	{'uni': 'SMAJ75A', 'bi': 'SMAJ75CA', 'voltage': 75.0},
	{'uni': 'SMAJ78A', 'bi': 'SMAJ78CA', 'voltage': 78.0},
	{'uni': 'SMAJ85A', 'bi': 'SMAJ85CA', 'voltage': 85.0},
	{'uni': 'SMAJ90A', 'bi': 'SMAJ90CA', 'voltage': 90.0},
	{'uni': 'SMAJ100A', 'bi': 'SMAJ100CA', 'voltage': 100.0},
	{'uni': 'SMAJ110A', 'bi': 'SMAJ110CA', 'voltage': 110.0},
	{'uni': 'SMAJ120A', 'bi': 'SMAJ120CA', 'voltage': 120.0},
	{'uni': 'SMAJ130A', 'bi': 'SMAJ130CA', 'voltage': 130.0},
	{'uni': 'SMAJ150A', 'bi': 'SMAJ150CA', 'voltage': 150.0},
	{'uni': 'SMAJ160A', 'bi': 'SMAJ160CA', 'voltage': 160.0},
	{'uni': 'SMAJ170A', 'bi': 'SMAJ170CA', 'voltage': 170.0},
	{'uni': 'SMAJ180A', 'bi': 'SMAJ180CA', 'voltage': 180.0},
	{'uni': 'SMAJ200A', 'bi': 'SMAJ200CA', 'voltage': 200.0},
	{'uni': 'SMAJ220A', 'bi': 'SMAJ220CA', 'voltage': 220.0},
	{'uni': 'SMAJ250A', 'bi': 'SMAJ250CA', 'voltage': 250.0},
	{'uni': 'SMAJ300A', 'bi': 'SMAJ300CA', 'voltage': 300.0},
	{'uni': 'SMAJ350A', 'bi': 'SMAJ350CA', 'voltage': 350.0},
	{'uni': 'SMAJ400A', 'bi': 'SMAJ400CA', 'voltage': 400.0},
	{'uni': 'SMAJ440A', 'bi': 'SMAJ440CA', 'voltage': 440.0}
]


def pins() -> List[DipTrace.Pin]:
	return [
		DipTrace.Pin(
			name='1',
			number='1',
			group=0,
			x=2.54,
			y=0,
			orientation=180.0,
			length=2.54,
			font=DipTrace.NameFont()
		),
		DipTrace.Pin(
			name='2',
			number='2',
			group=0,
			x=-2.54,
			y=0,
			orientation=0.0,
			length=2.54,
			pad_index=2,
			font=DipTrace.NameFont()
		),
	]


def pin_shape_uni() -> List[DipTrace.Shape]:
	x = 1.27 * math.sin(math.radians(60.0))

	return [
		DipTrace.Shape(
			width=0.25,
			enabled=True,
			group=0,
			points=[
				DipTrace.Point(x=-2.54, y=0.0),
				DipTrace.Point(x=2.54, y=0.0),
			]
		),
		DipTrace.Shape(
			type=DipTrace.ShapeType.Polyline,
			width=0.25,
			enabled=True,
			group=0,
			points=[
				DipTrace.Point(x=-x, y=1.27),
				DipTrace.Point(x=x, y=0.00),
				DipTrace.Point(x=-x, y=-1.27),
				DipTrace.Point(x=-x, y=1.27)
			]
		),
		DipTrace.Shape(
			type=DipTrace.ShapeType.Polyline,
			width=0.25,
			enabled=True,
			group=0,
			points=[
				DipTrace.Point(x=x + 1.27 / 2, y=1.27),
				DipTrace.Point(x=x, y=1.27),
				DipTrace.Point(x=x, y=-1.27),
				DipTrace.Point(x=x - 1.27 / 2, y=-1.27)
			]
		)
	]


def pin_shape_bi() -> List[DipTrace.Shape]:
	x = 2.54 * math.sin(math.radians(60.0))

	return [
		DipTrace.Shape(
			width=0.25,
			enabled=True,
			group=0,
			points=[
				DipTrace.Point(x=-2.54, y=0.0),
				DipTrace.Point(x=2.54, y=0.0),
			]
		),
		DipTrace.Shape(
			width=0.25,
			enabled=True,
			group=0,
			type=DipTrace.ShapeType.Polyline,
			points=[
				DipTrace.Point(x=0.0, y=0.0),
				DipTrace.Point(x=-x, y=1.27),
				DipTrace.Point(x=-x, y=-1.27),
				DipTrace.Point(x=0.0, y=0.0),
				DipTrace.Point(x=x, y=1.27),
				DipTrace.Point(x=x, y=-1.27),
				DipTrace.Point(x=0.0, y=0.0)
			]
		),
		DipTrace.Shape(
			width=0.25,
			enabled=True,
			group=0,
			type=DipTrace.ShapeType.Polyline,
			points=[
				DipTrace.Point(x=1.27 / 2, y=1.27),
				DipTrace.Point(x=0, y=1.27),
				DipTrace.Point(x=0, y=-1.27),
				DipTrace.Point(x=-1.27 / 2, y=-1.27)
			]
		)
	]


def component_tvs_uni() -> List[DipTrace.Component]:
	return [
		DipTrace.Component(
			parts=[DipTrace.Part(
				name=d['uni'],
				reference='D',
				value=f'{d["voltage"]:.5g} V',
				category=DipTrace.Category(
					index=None,
					name='Diodes'
				),
				shapes=pin_shape_uni(),
				pins=pins(),
				pattern='PatType0',
				origin=DipTrace.Origin(),
				spice_model=DipTrace.SpiceModel(),
				show_numbers=DipTrace.VisibleType.Hide
			)]
		) for d in data]


def component_tvs_bi() -> List[DipTrace.Component]:
	return [
		DipTrace.Component(
			parts=[DipTrace.Part(
				name=d['bi'],
				reference='D',
				value=f'{d["voltage"]:.5g} V',
				category=DipTrace.Category(
					index=None,
					name='Diodes'
				),
				shapes=pin_shape_bi(),
				pins=pins(),
				pattern='PatType1',
				origin=DipTrace.Origin(),
				spice_model=DipTrace.SpiceModel(),
				show_numbers=DipTrace.VisibleType.Hide
			)]
		) for d in data]


if __name__ == "__main__":
	name = 'Diodes TVS'
	source_patterns_path = f'source/{name}.{DipTrace.PatternLibrary.extensions[0]}'
	expected_patterns_path = f'expected/{name}.{DipTrace.PatternLibrary.extensions[0]}'
	actual_patterns_path = f'actual/{name}.{DipTrace.PatternLibrary.extensions[0]}'
	expected_components_path = f'expected/{name}.{DipTrace.ComponentLibrary.extensions[0]}'
	actual_components_path = f'actual/{name}.{DipTrace.ComponentLibrary.extensions[0]}'

	DipTrace.ComponentLibrary(
		name='Diodes TVS',
		pattern_library=DipTrace.PatternLibrary().load(source_patterns_path),
		components=[
			*component_tvs_uni(),
			*component_tvs_bi()
		]
	).save(actual_components_path).pattern_library.save(actual_patterns_path)

	DipTrace.format_xml(actual_patterns_path)
	DipTrace.format_xml(actual_components_path)
	DipTrace.format_xml(expected_patterns_path)
	DipTrace.format_xml(expected_components_path)
	DipTrace.compare(expected_patterns_path, actual_patterns_path)
	DipTrace.compare(expected_components_path, actual_components_path)
