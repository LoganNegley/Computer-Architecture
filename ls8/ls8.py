#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *

directory = "/examples"

cpu = CPU()

cpu.load(mult.ls8)
cpu.run()