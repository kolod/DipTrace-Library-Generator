#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!

import DipTrace


class Point(DipTrace.CommonCoordinates):

	def __init__(self, x: float = 0.0, y: float = 0.0):
		super().__init__('Item', x, y)


if __name__ == "__main__":
	pass
