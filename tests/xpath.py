#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!

from lxml import etree


def run():
	with open('../samples/part_test.sample.xml', 'r') as part_file:
		root = etree.fromstring(part_file.read())
		for tag in root.findall('.//Shapes/Shape'):
			print(etree.tostring(tag).decode("utf-8"))
			for sub_teg in tag.findall('.//Points/Item'):
				print(etree.tostring(sub_teg).decode("utf-8"))


if __name__ == "__main__":
	run()
