import numpy as np
from numpy_to_latex import *
import os
pwd = os.path.dirname(os.path.abspath(__file__))


dat = np.random.rand(3,6)
ylabel = [1, 2, 4, 6, 8, 12]
xlabel = ['m1','m2','m3']
numpy_to_latex(dat,xlabel,ylabel,2,pwd+'/build/table_normal.tex')

dat = np.random.rand(2,5)
ylabel = ['1', '2', 'O', '6', 'avg.']
xlabel = ['m1','m2']
numpy_to_latex(dat,xlabel,ylabel,2,pwd+'/build/table_small.tex')

dat = np.random.rand(40,10)
ylabel = np.arange(10)+10
xlabel = np.arange(40)-10
numpy_to_latex(dat,xlabel,ylabel,2,pwd+'/build/table_big.tex')
