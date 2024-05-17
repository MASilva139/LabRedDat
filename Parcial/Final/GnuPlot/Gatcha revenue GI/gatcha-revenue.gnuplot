# file: fit_csv.gnuplot
# set terminal pdfcairo
# set output 'plot.pdf'

set datafile separator ';'

d=1
#----------------------------------Función gaussiana
#f(x) = A*exp(-((x-u)/r)**2/2)
#A=1.05966e+09
#u=-1
#r=10
#fit f(x) 'C:\Users\mario\Documents\F503\Parcial\Final\csv\Gatcha Revenue\Gatcha Revenue.csv' using 1:5 every :::0::d via A,u,r
#----------------------------------Función Logarítimica
#f(x) = A*log(-((x-u)/r)**2/2)
#A=2
#u=0
#r=10
#fit f(x) 'C:\Users\mario\Documents\F503\Parcial\Final\csv\Gatcha Revenue\Gatcha Revenue.csv' using 1:5 every :::0::d via #A,u,r
#----------------------------------Función Cuadrática
f(x) = A2*x**2+B2*x+C2
A2 = 1
B2 = 1
C2 = 1
fit f(x) 'C:\Users\mario\Documents\F503\Parcial\Final\csv\Gatcha Revenue\Gatcha Revenue.csv' using 1:5 every :::0::d via A2,B2,C2
#----------------------------------Función Cúbica
#f(x) = A3*x**3+B3*x**2+C3*x+D3
A3 = 1
B3 = 1
C3 = 1
D3 = 1
#fit f(x) 'C:\Users\mario\Documents\F503\Parcial\Final\csv\Gatcha Revenue\Gatcha Revenue.csv' using 1:5 every :::0::d via A3,B3,C3,D3
#----------------------------------Función Cuartica
#f(x) = A4*x**4+B4*x**3+C4*x**1+D4*x+E4
A4 = 1
B4 = 1
C4 = 1
D4 = 1
E4 = 1
#fit f(x) 'C:\Users\mario\Documents\F503\Parcial\Final\csv\Gatcha Revenue\Gatcha Revenue.csv' using 1:5 every :::0::d via A4,B4,C4,D4,E4

#set timefmt "\"%Y-%m-%d\""
#set xrange ['"2022-11-23"':'"2024-05-23"']

set xrange [0:30]
set yrange [0:70000000]

# plot 'C:\Users\mario\Documents\F503\Parcial\Final\csv\Gatcha Revenue\Gatcha Revenue.csv' using 1:5, f(x)

plot 'C:\Users\mario\Documents\F503\Parcial\Final\csv\Gatcha Revenue\Gatcha Revenue.csv' using 1:5, 'C:\Users\mario\Documents\F503\Parcial\Final\csv\Gatcha Revenue\Gatcha Revenue.csv' every :::0::d using 1:5, f(x)

#plot 'C:\Users\mario\Documents\F503\Parcial\Final\csv\Gatcha Revenue\Gatcha Revenue.csv' every :::0::d using 1:5, f(x)
# plot f(x)

