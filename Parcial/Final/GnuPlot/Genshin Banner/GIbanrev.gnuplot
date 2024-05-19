# file: fit_csv.gnuplot
# set terminal pdfcairo
# set output 'plot.pdf'

set datafile separator ';'

d=0
#----------------------------------Función gaussiana
f(x) = Ag*exp(-((x-ug)/rg)**2/2)
Ag=100
ug=-1
rg=10
fit f(x) 'C:\Users\mario\Documents\F503\Parcial\Final\csv\Genshin Banner\Genshin Revenue Banner.csv' using 1:6 every :::0::d via Ag,ug,rg
#----------------------------------Función Logarítimica
g(x) = Al*log(((x+ul)/rl)**2/2)
#g(x) = Al*log(ul*x+rl)
Al=10000000
ul=1
rl=1
fit g(x) 'C:\Users\mario\Documents\F503\Parcial\Final\csv\Genshin Banner\Genshin Revenue Banner.csv' using 1:6 every :::0::d via Al,ul,rl
#----------------------------------Función Cúbica
i(x) = A3*x**3+B3*x**2+C3*x+D3
A3 = 500
B3 = 150
C3 = 1
D3 = 100
fit i(x) 'C:\Users\mario\Documents\F503\Parcial\Final\csv\Genshin Banner\Genshin Revenue Banner.csv' using 1:6 every :::0::d via A3,B3,C3,D3
#----------------------------------Función Cuartica
#j(x) = A4*x**4+B4*x**3+C4*x**2+D4*x+E4
A4 = 10
B4 = 1
C4 = 1
D4 = 1
E4 = -100
#fit j(x) 'C:\Users\mario\Documents\F503\Parcial\Final\csv\Genshin Banner\Genshin Revenue Banner.csv' using 1:6 every :::0::d via A4,B4,C4,D4,E4

#set timefmt "\"%Y-%m-%d\""
#set xrange ['"2022-11-23"':'"2024-05-23"']

set xrange [0:60]
set yrange [0:50000000]

# plot 'C:\Users\mario\Documents\F503\Parcial\Final\csv\Genshin Banner\Genshin Revenue Banner.csv' using 1:6, f(x)

plot 'C:\Users\mario\Documents\F503\Parcial\Final\csv\Genshin Banner\Genshin Revenue Banner.csv' using 1:6, 'C:\Users\mario\Documents\F503\Parcial\Final\csv\Genshin Banner\Genshin Revenue Banner.csv' every :::0::d using 1:6, f(x),\
 g(x),\
 i(x)

#plot 'C:\Users\mario\Documents\F503\Parcial\Final\csv\Gatcha Revenue\Gatcha Revenue.csv' every :::0::d using 1:5, f(x)
# plot f(x)