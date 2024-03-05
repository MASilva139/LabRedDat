import numpy as np
import math
from matplotlib import pyplot as plt

t = [0.0,0.5,1.0,1.5,2.0]
v = [214,134,101,61,54]
fv = []
for i in range(5):
    #0 1 2 3 4
    fv.append((200)*math.pow(math.e, -(0.693)*i))
print(fv)

vm = np.mean(v)

dv = [math.sqrt(214), math.sqrt(134), math.sqrt(101), math.sqrt(61), math.sqrt(54)]
print(dv)

fig, axis = plt.subplots()
axis.errorbar(t, v, dv, marker = "o", ecolor = "LightCoral", capsize = 3)
axis.plot(t, fv, color='Black')
plt.xlabel('Time elapsed, t [hours]')
plt.ylabel('Number counted, '+r"$\nu$"+', in 1 [min]')
plt.savefig('Tareas/T03/T03_p3,4b.png')