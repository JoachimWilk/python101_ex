#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pylab

a = int(raw_input("Podaj współczynnik a: "))

x1 = pylab.arange(-10, 0.5, 0.5)
x1 = [] #TODO: zrobić tutaj list
x2 = pylab.arange(0, 10.5, 0.5)

y1 = [i / -3 + a for i in x1 if i <= 0]
y2 = [i**2 / 3 for i in x2 if i >= 0]

pylab.plot(x1, y1, x2, y2)
pylab.title('Wykres f(x)')
pylab.grid(True)
pylab.show()
