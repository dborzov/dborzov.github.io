import numpy as np
import matplotlib.pyplot as pyplot

print 'Plotting the soft threshold softly'
xx = [np.float((i-50)/5.) for i in range(100)]
yy = [np.exp(x)/(1 + np.exp(x)) for x in xx]

pyplot.figure(figsize=(6,6))
pyplot.plot(xx, yy, 'r-')
pyplot.xlim(-10.,10.)
pyplot.xlabel('$x$ ranges in $(-\infty,\infty)$')
pyplot.ylabel('y, limited to $(0,1)$')
pyplot.ylim(-0.5,1.5)
pyplot.hlines(0.,-10.,10.,linestyle='--')
pyplot.hlines(1.,-10.,10.,linestyle='--')
pyplot.vlines(0.,-1.,2.)
pyplot.savefig('softThreshold.png')
