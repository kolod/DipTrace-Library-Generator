#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!


class BaseClass(object):
	def __init__(self, *args, **kwargs):
		self.root = kwargs['root'] or 'root'
		print(" base ")

	def __str__(self):
		return self.root


class FirstMixin(BaseClass):
	def __init__(self, x: float = 0.0, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.root += ' ' + str(x)
		print(" first ")


class SecondMixin(BaseClass):
	def __init__(self, y: float = 0.0, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.root += ' ' + str(y)
		print(" second ")


class SuperClass(FirstMixin, SecondMixin):
	def __init__(self, *args, **kwargs):
		super().__init__(root='super', *args, **kwargs)
		print(" super ")


if __name__ == "__main__":
	base = SuperClass(x=1.0, y=2.0)
	print(base)
