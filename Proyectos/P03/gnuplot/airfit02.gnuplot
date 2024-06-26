set datafile separator ','

## Fit Cesio
# f(x) = A*exp(-((x-u)/r)**2/2)

# A=5.09287
# u=442.826
# r=19.5836
# A=700
# u=500
# r=19.5838

# fit f(x) 'C:\Users\mario\Documents\F503_LRD\Proyectos\P03\csv\Cesio.csv' using 2:3 via A,u,r

# set yrange [0:10]
# set xrange [300:500]

# plot 'C:\Users\mario\Documents\F503_LRD\Proyectos\P03\csv\Cesio.csv' using 2:3, f(x)

## Fit aire
f(x) = A*exp(-((x-u)/r)**2/2)

A = 63.5727
u = 2.1887
r = 1.59887

fit f(x) 'C:\Users\mario\Documents\F503_LRD\Proyectos\P03\csv\Aire(t2).csv' using 2:3 via A,u,r

set yrange [0:65]
set xrange [0:11]

plot 'C:\Users\mario\Documents\F503_LRD\Proyectos\P03\csv\Aire(t2).csv' using 2:3, f(x)
