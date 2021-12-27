#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!

from lxml import etree
import DipTrace


class Origin(DipTrace.CommonCoordinates):
	def __init__(self, x: float = 0.0, y: float = 0.0):
		super().__init__('Origin', x, y)

	def load(self, xml: etree):
		if xml is not None:
			self.root = xml
		return self


if __name__ == "__main__":
	pass
