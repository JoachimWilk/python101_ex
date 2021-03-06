#! /usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import random
import matplotlib.pyplot as plt


a = 1
b = -3
c = 1

x = np.arange(-10, 11, 1)

y = [a*i**2 + b*i + c for i in x]

plt.plot(x, y)
plt.title('Wykres f(x)=a*x^2+b*x+c')
plt.grid(True)
plt.show()
