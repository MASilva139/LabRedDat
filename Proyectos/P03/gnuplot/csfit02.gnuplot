set datafile separator ','

## Fit Cesio
# f(x) = A*exp(-((x-u)/r)**2/2)

# A = 5.08918
# u = 442.814
# r = 19.6161

# fit f(x) 'C:\Users\mario\Documents\F503_LRD\Proyectos\P03\csv\Cesio(t2).csv' using 2:3 via A,u,r

# set yrange [0:10]
# set xrange [390:510]

# plot 'C:\Users\mario\Documents\F503_LRD\Proyectos\P03\csv\Cesio(t2).csv' using 2:3, f(x)

# Fit Cesio 5/5
f(x) = A*exp(-((x-u)/r)**2/2)

A = 25.3682
u = 439.831
r = 19.6769

fit f(x) 'C:\Users\mario\Documents\F503_LRD\Proyectos\P03\csv\Cesio01(t2).csv' using 2:3 via A,u,r

set yrange [0:10]
set xrange [390:510]

plot 'C:\Users\mario\Documents\F503_LRD\Proyectos\P03\csv\Cesio01(t2).csv' using 2:3, f(x)


# # Fit aire
# f(x) = A*exp(-((x-u)/r)**2/2)

# A=100
# u=50
# r=25

# fit f(x) 'C:\Users\mario\Documents\F503_LRD\Proyectos\P03\csv\Aire.csv' using 2:3 via A,u,r

# set yrange [0:60]
# set xrange [0:25]

# plot 'Aire.csv' using 2:3, f(x)
