#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pylab

a = int(raw_input("Podaj współczynnik a: "))
b = int(raw_input("Podaj współczynnik b: "))
x = range(-10, 11)

y = [a * i + b for i in x]

pylab.plot(x, y)
pylab.title('Wykres f(x)= a*x + b')
pylab.grid(True)
pylab.show()
