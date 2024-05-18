 1/1: %history -o -g -f ipython_history.py
 1/3: %history -o -g -f ipython_history.py
17/14: clear
 2/1: 3!
 2/2: clear
 2/3: import math
 2/4: math.comb(3)
 2/5: math.comb(3,3)
 2/6: math.comb(3,2)
 2/7: math.comb(4,2)
 2/8: clear
 2/9: math.comb(1000,33)
2/10: clear
 3/1: clear
 3/2: import streamlit as st
 4/1: clear
 4/2: import pandas as pd
 5/1: clear
 5/2: import numpy as np
 5/3: import random as rnd
 5/4: rnd.gauss(15,10)
 5/5: rnd.gauss(15,1)
 5/6: rnd.gauss(15,5)
 5/7: rnd.gauss(15,5)
 5/8: rnd.gauss(15,5)
 5/9: rnd.gauss(15,5)
5/10: rnd.gauss(15,5)
5/11: rnd.gauss(15,5)
5/12: rnd.gauss(15,2)
5/13: rnd.gauss(15,2)
5/14: rnd.gauss(15,2)
5/15: rnd.gauss(15,2)
5/16: clear
5/17: for i in range(5)
5/18:
for i in range(5):
    l.append(rnd.gauss(15,2))
5/19: l = []
5/20:
for i in range(5):
    l.append(rnd.gauss(15,2))
5/21: l
 6/1: clear
 6/2: f = lambda x,y: x+y
 6/3: f(1,2)
 7/1: import scipy as sp
 7/2: sp.optimize.curve_fit()
 7/3: a = [1,2,3,4,5]
 7/4: b = a
 7/5:
def f(x,a,b):
    return ax+b
 7/6: la = a
 7/7: lb = b
 7/8: sp.optimize.curve_fit(f,la,lb)
 7/9:
def f(x,a,b):
    return a*x+b
7/10: sp.optimize.curve_fit(f,la,lb)
7/11: sa = [1,0.9,1.1,0.9]
7/12: sp.optimize.curve_fit(f,la,lb,sigma=sa)
7/13: a
7/14: sa = [1,0.9,1.1,0.9,0.8]
7/15: sp.optimize.curve_fit(f,la,lb,sigma=sa)
7/16: sp.optimize.curve_fit(f,la,lb)
7/17: sp.optimize.curve_fit(f,la,lb,sigma=sa)
 8/1: clear
 8/2: import pandas as pd
 8/3: import numpy as np
 8/4: np.empty((4,20))
 8/5: np.empty((20,4))
 8/6: np.empty((20,3))
 8/7: a = np.empty((20,3))
 8/8: a
 8/9: clear
8/10: np.empty((20,3))
8/11: a
8/12: clear
8/13: a = np.zeros((20,3))
8/14: a
8/15: a = np.empty((20,3))
8/16: a
8/17: clear
8/18: a = np.random((20,3))
8/19: a = np.random.rand((20,3))
8/20: a = np.random.random((20,3))
8/21: clear
8/22: a
8/23: a_pandas = pd.DataFrame(a)
8/24: a_pandas
8/25: a_pandas.columns = ['a','b','c']
8/26: a_pandas
8/27: a_pandas['a']
8/28: a_pandas['a'][3:7]
8/29: a_pandas['a'][7]
8/30: a_pandas['a'][:7]
8/31: a_pandas['a'][:]
8/32: a_pandas[:][:7]
8/33: a_pandas[['b','a']][:7]
8/34: %history -o -g -f ipython_history.py
8/35: %history -o -g -f ./history.py
8/36: a_pandas['a']
8/37: list(a_pandas['a'])
8/38: a_pandas['a'].to_list()
8/39: np.array(a_pandas['a'])
8/40: a_pandas['a'].to_numpy()
8/41: clear
8/42: tup = (1,2,3)
8/43: a,b,c = tup
8/44: a
8/45: b
8/46: c
8/47: (a,b,c) = tup
8/48: a
8/49: [1,2,5,3,9,0,-1]
8/50: a = [1,2,5,3,9,0,-1]
8/51: a.sort()
8/52: a
8/53: a = [1,2,5,3,9,0,-1,2,5,2,9,0,9,2,0,9,2,2,9]
8/54: np.array(a)
8/55: a_np = np.array(a)
8/56: a_np
8/57: a_pd = pd.DataFrame(a)
8/58: a_pd
8/59: a_pd.count
8/60: a_pd.count(2)
8/61: a_pd.count()
8/62: a_pd.count(axis=1)
8/63: a_pd.groupby(axis=1)
8/64: a_pd.value_counts()
8/65: a_pd.value_counts()[2]
8/66: a_pd.value_counts()[-1]
8/67: %history -o -g -f ./history.py
8/68: clear
10/1: import math
10/2: math.comb(1000,33)
10/3: math.comb(10,3)
10/4: math.comb([1,2],3)
10/5: import numpy as np
10/6: np.array([1,2,3])
10/7: a = np.array([1,2,3])
10/8: math.comb(a,1)
10/9: np.vectorize(math.comb)
10/10: np.vectorize(math.comb)([1,2],1)
10/11: np.vectorize(math.comb)([5,6],2)
10/12: math.comb(5,2)
10/13: math.comb(6,2)
10/14: np.vectorize(math.comb)(5,2)
10/15: 6**8
10/16: 6**np.array([1,2])
10/17: 6**(5-np.array([1,2]))
10/18:
def binom(x,n,p,A):
    print('binom(',x,n,p,A,')')
    comb = np.vectorize(math.comb)(n,x)
    p_x = p**x
    q_nx = (1-p)**(n-x)

    return comb*p_x*q_nx
10/19: binom(5,10,0.5,0)
10/20: binom([1,2],10,0.5,0)
10/21: binom(np.array([1,2]),10,0.5,0)
10/22: binom(1,10,0.5,0)
10/23: int(np.array([1,2]))
10/24: np.array([1,2]).astype(int)
10/25: a = 5
10/26: a.astype(float)
10/27: a = 1.3
10/28: math.comb(6,2)
10/29: math.comb(1,2)
10/30: math.comb(1,4)
11/1: clear
11/2: from scipy import special as ssp
11/3: ss.comb(5,4)
11/4: ssp.comb(5,4)
11/5: ssp.comb(5,3)
11/6: ssp.comb(5.2,3)
11/7: ssp.comb(5.3,3)
12/1: import pytest
12/2: import unittest
12/3: import sys
12/4: sys.getpath()
12/5: impor os
12/6: os.getcwd()
12/7: sys.getcwd()
12/8: import sys
12/9: getcwd()
12/10: sys.getpath()
12/11: os.getcwd()
12/12: import os
12/13: os.getcwd()
12/14: a = [5,4,3,2,1]
12/15: a.pop(1)
12/16: a.pop(1)
12/17: a.pop(1)
12/18: a.pop(1)
12/19: a.pop(1)
12/20: a = [5,4,3,2,1]
12/21: a.pop(1)
12/22: a
12/23: a
12/24: del a[1]
12/25: a
12/26: del a[1:2]
12/27: a
12/28: a = [5,4,3,2,1]
12/29: del a[1:3]
12/30: a
12/31: import asyncio
12/32:
def hello():
    print('h')
12/33:
async def bye():
    print('b')
12/34:
async def m():
    await hello()
    bye()
12/35: m()
12/36: asyncio.run(main())
12/37: asyncio.run(m())
13/1: clear
13/2: eval('1+2')
13/3: eval('1+2*5')
13/4: eval('1+2/5')
13/5: eval('1+10/5')
13/6: eval('1/0')
13/7: eval('1/0')
13/8: eval('1+10/5')
13/9: eval('1 + 10/5')
13/10: eval('1 + 10 / 5')
12/38: [1]+[2]
12/39: l1 = [0,0,0]
12/40: l1 == 0
12/41: l1.all == 0
12/42: import numpy as np
12/43: l1 = np.array(l1)
12/44: l1 == True
12/45: l1 == False
12/46: (l1 == False).all
12/47: (l1 == False).all()
12/48: l1
12/49: l2 = np.array([1,2,3])
12/50: np.concatenate(l1,l2)
12/51: l1
12/52: l2
12/53: np.concatenate((l1,l2))
12/54: s = '1 2
12/55: s = '1 2
12/56:

            """\
            6 6
            1 2
            1 3
            2 4
            2 5
            3 4
            4 6
            """
12/57:

            """\
            6 6
            1 2
            1 3
            2 4
            2 5
            3 4
            4 6
            """
12/58:
s = """\
6 6
1 2
1 3
2 4
2 5
3 4
4 6
"""
12/59: s
12/60: s.splitlines()
12/61: s.splitlines()[1:]
12/62: ss.split() for ss in s.splitlines()[1:]
12/63: [ss.split() for ss in s.splitlines()[1:]]
12/64: s[s.split() for ss in s.splitlines()[1:]]
12/65: np.concatenate((l1,l2))
12/66: np.concatenate((l1,l2,1))
12/67: np.concatenate(l1,2)
12/68: np.concatenate((l1,2))
12/69: np.concatenate((l1,[2]))
12/70:
class h:
    __init__(self,i):
        self.i = i
12/71:
class h:
    __init__(self,i):
        self.i = i
12/72:
class h:
    def __init__(self,i):
        self.i = i
12/73: h(3)
12/74: a = h(3)
12/75: l1 = [h(1),h(2),h(3)]
12/76: l1
12/77: l1 = np.array(l1)
12/78: l1
12/79: l1.i
12/80: l1[:].i
12/81: i.i for i in l1
12/82: [i.i for i in l1]
12/83: a = {1:2,2:3}
12/84: a
12/85: a.keys()
12/86: a.items()
12/87: a.values()
12/88: ss.split() for ss in s.splitlines()[1:]
12/89: ss.split() for ss in s.splitlines()[1:]
14/1: import q14
14/2:
q14.solve("""\
            6 6
            1 2
            1 3
            2 4
            2 5
            3 4
            4 6
            """)
14/3:
q14.solve("""\
            6 6
            1 2
            1 3
            2 4
            2 5
            3 4
            4 6
            """)
15/1: import q14
15/2:
q14.solve("""\
            6 6
            1 2
            1 3
            2 4
            2 5
            3 4
            4 6
            """)
16/1: import q14
16/2: clear
16/3:
q14.solve("""\
            6 6
            1 2
            1 3
            2 4
            2 5
            3 4
            4 6
            """)
17/1: import q14
17/2:
q14.solve("""\
            6 6
            1 2
            1 3
            2 4
            2 5
            3 4
            4 6
            """)
17/3: clear
18/1: import importlib
18/2: import q14
18/3: importlib.reload(q14)
18/4:
q14.solve("""\
            6 6
            1 2
            1 3
            2 4
            2 5
            3 4
            4 6
            """)
18/5:
q14.solve("""\
            6 6
            1 2
            1 3
            2 4
            2 5
            3 4
            4 6
            """)
18/6: importlib.reload(q14)
18/7:
q14.solve("""\
            6 6
            1 2
            1 3
            2 4
            2 5
            3 4
            4 6
            """)
18/8: importlib.reload(q14)
18/9:
q14.solve("""\
            6 6
            1 2
            1 3
            2 4
            2 5
            3 4
            4 6
            """)
18/10: importlib.reload(q14)
18/11:
q14.solve("""\
            6 6
            1 2
            1 3
            2 4
            2 5
            3 4
            4 6
            """)
18/12: importlib.reload(q14)
18/13:
q14.solve("""\
            6 6
            1 2
            1 3
            2 4
            2 5
            3 4
            4 6
            """)
18/14: importlib.reload(q14)
18/15:
q14.solve("""\
            6 6
            1 2
            1 3
            2 4
            2 5
            3 4
            4 6
            """)
18/16: importlib.reload(q14)
18/17:
q14.solve("""\
            6 6
            1 2
            1 3
            2 4
            2 5
            3 4
            4 6
            """)
18/18: importlib.reload(q14)
18/19:
q14.solve("""\
            6 6
            1 2
            1 3
            2 4
            2 5
            3 4
            4 6
            """)
18/20: importlib.reload(q14)
18/21:
q14.solve("""\
            6 6
            1 2
            1 3
            2 4
            2 5
            3 4
            4 6
            """)
18/22: importlib.reload(q14)
18/23:
q14.solve("""\
            6 6
            1 2
            1 3
            2 4
            2 5
            3 4
            4 6
            """)
18/24:
q14.solve("""\
            6 6
            1 2
            1 3
            2 4
            2 5
            3 4
            4 6
            """)
18/25:
q14.solve("""\
            6 6
            1 2
            1 3
            2 4
            2 5
            3 4
            4 6
            """)
18/26: importlib.reload(q14)
18/27:
q14.solve("""\
            6 6
            1 2
            1 3
            2 4
            2 5
            3 4
            4 6
            """)
18/28: importlib.reload(q14)
18/29: importlib.reload(q14)
18/30:
q14.solve("""\
            6 6
            1 2
            1 3
            2 4
            2 5
            3 4
            4 6
            """)
12/90: (True) and (True)0
12/91: (True) and (True)
12/92: (True) and (False)
18/31:
q14.solve("""\
            6 6
            1 2
            1 3
            2 4
            2 5
            3 4
            4 6
            """)
18/32: importlib.reload(q14)
18/33:
q14.solve("""\
            6 6
            1 2
            1 3
            2 4
            2 5
            3 4
            4 6
            """)
18/34: importlib.reload(q14)
18/35:
q14.solve("""\
            6 6
            1 2
            1 3
            2 4
            2 5
            3 4
            4 6
            """)
18/36:
q14.solve("""\
            6 6
            1 2
            1 3
            2 4
            2 5
            3 4
            4 6
            """)
18/37: importlib.reload(q14)
18/38:
q14.solve("""\
            6 6
            1 2
            1 3
            2 4
            2 5
            3 4
            4 6
            """)
18/39: importlib.reload(q14)
18/40:
q14.solve("""\
            6 6
            1 2
            1 3
            2 4
            2 5
            3 4
            4 6
            """)
18/41: importlib.reload(q14)
18/42:
q14.solve("""\
            6 6
            1 2
            1 3
            2 4
            2 5
            3 4
            4 6
            """)
18/43: importlib.reload(q14)
18/44:
q14.solve("""\
            6 6
            1 2
            1 3
            2 4
            2 5
            3 4
            4 6
            """)
18/45: importlib.reload(q14)
18/46:
q14.solve("""\
            6 6
            1 2
            1 3
            2 4
            2 5
            3 4
            4 6
            """)
18/47: importlib.reload(q14)
18/48:
q14.solve("""\
            6 6
            1 2
            1 3
            2 4
            2 5
            3 4
            4 6
            """)
18/49:
q14.solve(
            """\
            3 2
            1 2
            2 3
            """)
18/50: importlib.reload(q14)
18/51:
q14.solve(
            """\
            3 2
            1 2
            2 3
            """)
18/52: importlib.reload(q14)
18/53:
q14.solve(
            """\
            3 2
            1 2
            2 3
            """)
18/54: importlib.reload(q14)
18/55:
q14.solve(
            """\
            3 2
            1 2
            2 3
            """)
18/56:
q14.solve(
            """\
            3 2
            1 2
            2 3
            """)
18/57: importlib.reload(q14)
18/58:
q14.solve(
            """\
            3 2
            1 2
            2 3
            """)
18/59: importlib.reload(q14)
18/60:
q14.solve(
            """\
            3 2
            1 2
            2 3
            """)
18/61: importlib.reload(q14)
18/62:
q14.solve(
            """\
            3 2
            1 2
            2 3
            """)
18/63: importlib.reload(q14)
18/64:
q14.solve(
            """\
            3 2
            1 2
            2 3
            """)
19/1: import numpy as np
19/2: np.inf
19/3: np.inf + 5
19/4: clear
20/1: import datetime as dt
20/2: dt.datetime.strptime('2020-01-01','Y-m-d')
20/3: dt.datetime.strptime('2020-01-01','%Y-%m-%d')
   1: clear
   2: import numpy as np
   3: a = np.array([1,2,3])
   4: b = np.array([1,1,1])
   5: np.dot(a,b)
   6: import classification as cls
   7: cls.loss_hinge([1,2],[1,1],1)
   8: cls.loss_hinge([1,2],[1,4],1)
   9: cls.loss_hinge([1,2],[1,-4],1)
  10: import importlib as imp
  11: imp.reload(cls)
  12: cls.loss_hinge([1,2],[1,-4],1)
  13: cls.loss_hinge([1,2],[1,-4],1)
  14: imp.reload(cls)
  15: cls.loss_hinge([1,2],[1,-4],1)
  16: imp.reload(cls)
  17: cls.loss_hinge([1,2],[1,-4],1)
  18: a = cls.loss_hinge([1,2],[1,-4],1)
  19: a
  20: cls.loss_hinge([1,2],[1,-4],1) + 2
  21: imp.reload(cls)
  22: cls.loss_hinge([1,2],[1,-4],1) + 2
  23: a = cls.loss_hinge([1,2],[1,-4],1)
  24: a
  25: a
  26: a
  27: a
  28: clear
  29: import pandas as pd
  30: import plotly.express as px
  31: df_points = np.random((2,5))
  32: df_points = np.random.random((2,5))
  33: df_points
  34: df_points = df_points.tolist
  35: df_points
  36: df_points = np.random.random((2,5))
  37: df_points = df_points.tolist()
  38: df_points
  39: px.scatter(df_points)
  40: px.scatter(df_points)
  41: df_points
  42: df_points.append(['a','a','b','b','a'])
  43: df_points
  44: points = df_points
  45: points
  46: df_points = pd.DataFrame(points,columns=['x','y','correct'])
  47: points
  48: np.transpose(points)
  49: df_points = pd.DataFrame(np.transpose(points),columns=['x','y','correct'])
  50: df_points
  51: px.scatter(df_points,'x','y')
  52: px.scatter(df_points,'x','y')
  53: px.scatter(df_points,'x','y',color='correct')
  54: df_points['correct'] = ['correct','incorrect','correct','correct','incorrect']
  55: px.scatter(df_points,'x','y',color='correct')
  56: px['x'] = np.random.random(5)
  57: df_points['x'] = np.random.random(5)
  58: px.scatter(df_points,'x','y',color='correct')
  59: px.scatter(df_points,'x','y',color='correct')
  60: %history -o -g -f ./history.py
