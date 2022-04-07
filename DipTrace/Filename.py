#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!

import DipTrace


class Filename(DipTrace.Base):
	tag = 'Filename'
	defaults = {
		'path': '',
		'var': '',
	}

	@property
	def path(self) -> str:
		return self._get_first_text_or_default('Path')

	@path.setter
	def path(self, path: str):
		self._set_first_text('Path', path)

	@property
	def var(self) -> str:
		return self._get_first_text_or_default('Var')

	@var.setter
	def var(self, var: str):
		self._set_first_text('Var', var)
