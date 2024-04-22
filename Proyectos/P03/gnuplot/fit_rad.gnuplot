set datafile separator ','

# Fit Cesio
f(x) = A*exp(-((x-u)/r)**2/2)

A = 100
u = 400
r = 100
# A=700
# u=500
# r=19.5838

fit f(x) 'C:\Users\mario\Documents\F503_LRD\Proyectos\P03\csv\Cesio.csv' using 2:3 via A,u,r

set yrange [0:10]
set xrange [330:510]

plot 'C:\Users\mario\Documents\F503_LRD\Proyectos\P03\csv\Cesio.csv' using 2:3, f(x)

# # Fit aire
# f(x) = A*exp(-((x-u)/r)**2/2)

# A=100
# u=50
# r=25

# fit f(x) 'C:\Users\mario\Documents\F503_LRD\Proyectos\P03\csv\Aire.csv' using 2:3 via A,u,r

# set yrange [0:60]
# set xrange [0:25]

# plot 'Aire.csv' using 2:3, f(x)
