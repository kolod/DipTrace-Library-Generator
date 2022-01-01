#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!

import os
import subprocess
import webbrowser


def main():
    subprocess.call(['coverage', 'erase'])
    subprocess.call(['coverage', 'run', '--module', 'unittest', 'discover'])
    subprocess.call(['coverage', 'report'])
    subprocess.call(['coverage', 'html'])
    webbrowser.open(f"file://{os.getcwd()}/htmlcov/index.html", new=2)


if __name__ == '__main__':
    main()
