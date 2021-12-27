#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!

import DipTrace


def run(colors):
	patternLib = DipTrace.PatternLibrary(
		name='LEDs',
		hint='LEDs'
	)
	componentLib = DipTraceComponentLibrary(
		name='LEDs',
		hint='LEDs'
	)

	for color in colors:
		p = pattern_3mm(color)
		c = component_3mm(color, p)
		patternLib.patterns.append(p)
		componentLib.components.append(c)

	for color in colors:
		p = pattern_5mm(color)
		c = component_5mm(color, p)
		patternLib.patterns.append(p)
		componentLib.components.append(c)

	# hack :)
	patternLib.patterns[0].recovery_code_int = -1000

	patternLib.save('LEDs.pattern.asc')
	componentLib.save('LEDs.component.asc')


if __name__ == "__main__":
	run([
		'green',
		'red',
		'orange',
		'clear'
	])
