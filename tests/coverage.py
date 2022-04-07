#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!

import os
import subprocess
import webbrowser
import lxml.etree
import requests


def coverage_color(rate: float) -> str:
	if rate < 50.0:
		return 'red'
	elif rate < 75.0:
		return 'orange'
	elif rate < 90.0:
		return 'yellow'
	else:
		return 'green'


def make_coverage_badge(xml: str = 'coverage.xml', badge: str = 'coverage-badge.svg'):
	rate = float(lxml.etree.parse(xml).getroot().get('line-rate')) * 100.0
	color = coverage_color(rate)
	url = f'https://img.shields.io/badge/coverage-{rate}%25-{color}?style=flat-square'
	with open(badge, 'wb') as badge_output:
		r = requests.get(url, allow_redirects=True)
		badge_output.write(r.content)


def main():
	subprocess.call(['coverage', 'erase'])
	subprocess.call(['coverage', 'run', '--module', 'unittest', 'discover'])
	subprocess.call(['coverage', 'report'])
	subprocess.call(['coverage', 'html'])
	subprocess.call(['coverage', 'xml'])
	webbrowser.open(f"file://{os.getcwd()}/htmlcov/index.html", new=2)
	make_coverage_badge(badge='../images/coverage-badge.svg')


if __name__ == '__main__':
	main()
