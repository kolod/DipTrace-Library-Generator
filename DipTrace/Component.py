#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!

import DipTrace


class Component(DipTrace.Common):
	def __init__(self):
		super().__init__('Component')

	def add_parts(self, parts):
		if type(parts) is list:
			for part in parts:
				self.add_parts(part)
		elif type(parts) is DipTrace.Part:
			self.root.append(parts.root)


if __name__ == "__main__":
	pass
