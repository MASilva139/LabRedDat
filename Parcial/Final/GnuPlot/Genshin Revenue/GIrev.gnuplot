# file: fit_csv.gnuplot
# set terminal pdfcairo
# set output 'plot.pdf'

set datafile separator ';'

d=0
#----------------------------------Función gaussiana
f(x) = Ag*exp(-((x-ug)/rg)**2/2)
Ag = 18.5557
ug = 17.9711
rg = 76.2984
fit f(x) 'C:\Users\mario\Documents\F503\Parcial\Final\csv\App Revenue\AppRev001.csv' using 1:5 every :::0::d via Ag,ug,rg
#----------------------------------Función Logarítimica
g(x) = Al*log(((x+ul)/rl)**2/2)
#g(x) = Al*log(ul*x+rl)
Al = 0.0896234
ul = 2.66007
rl = -4.27267e-44
fit g(x) 'C:\Users\mario\Documents\F503\Parcial\Final\csv\App Revenue\AppRev001.csv' using 1:5 every :::0::d via Al,ul,rl
#----------------------------------Función Cúbica
i(x) = A3*x**3+B3*x**2+C3*x+D3
A3 = 5.07324e-05
B3 = -0.00446483
C3 = 0.0999895
D3 = 17.9175
fit i(x) 'C:\Users\mario\Documents\F503\Parcial\Final\csv\App Revenue\AppRev001.csv' using 1:5 every :::0::d via A3,B3,C3,D3
#----------------------------------Función Cuartica
#j(x) = -A4*x**4+B4*x**3+C4*x**2+D4*x+E4
A4 = 10
B4 = 1
C4 = 1
D4 = 1
E4 = 1
#fit j(x) 'C:\Users\mario\Documents\F503\Parcial\Final\csv\App Revenue\AppRev001.csv' using 1:5 every :::0::d via A4,B4,C4,D4,E4

# Establece que los datos del eje x son fechas
#set xdata time

# Especifica el formato de las fechas en tus datos (En este caso, las fechas están en el formato "YYYY-MM-DD")
#set timefmt "%Y-%m-%d"
#set xrange ['"2020-08-30"':'"2024-07-31"']

# Establece el formato de las fechas en el eje x (En este caso, las fechas se mostrarán en el formato "MM/DD/YY")
#set format x "%m/%d/%y"

set xrange [-3:55]
#set yrange [0:200000000]
set yrange [16:20]

# plot 'C:\Users\mario\Documents\F503\Parcial\Final\csv\App Revenue\AppRev001.csv' using 1:5, f(x)

plot 'C:\Users\mario\Documents\F503\Parcial\Final\csv\App Revenue\AppRev001.csv' using 1:5 notitle lt rgb "grey30", 'C:\Users\mario\Documents\F503\Parcial\Final\csv\App Revenue\AppRev001.csv' every :::0::d using 1:5 notitle lt rgb "black", f(x) title "Gauss fit" lt rgb "dark-red",\
 g(x) title "Logaritmic fit" lt rgb "steelblue",\
 i(x) title "Cubic fit" lt rgb "dark-violet"
 set ylabel "Ventas (en millones de $)/log"
 set xlabel "#Mes "
