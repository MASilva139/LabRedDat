# file: fit_csv.gnuplot
# set terminal pdfcairo
# set output 'plot.pdf'

set datafile separator ';'

d=1

f(x) = A*exp(-((x-u)/r)**2/2)

A=400
u=200
r=100

fit f(x) 'C:\Users\mario\Documents\F503\Parcial\Final\csv\Gatcha Revenue.csv' using 2:5 every :::0::d via A,u,r

#set timefmt "\"%Y-%m-%d\""
set xrange ['"2022-11-23"':'"2024-05-23"']

#set xrange [0:400]
set yrange [0:70000000]

# plot 'C:\Users\mario\Documents\F503\Parcial\Final\csv\Gatcha Revenue.csv' using 2:5, f(x)

plot 'C:\Users\mario\Documents\F503\Parcial\Final\csv\Gatcha Revenue.csv' using 2:5, 'C:\Users\mario\Documents\F503\Parcial\Final\csv\Gatcha Revenue.csv' every :::0::d using 2:5, f(x)

#plot 'C:\Users\mario\Documents\F503\Parcial\Final\csv\Gatcha Revenue.csv' every :::0::d using 2:5, f(x)
# plot f(x)

