import numpy as np
from numpy_to_latex import *
import os
pwd = os.path.dirname(os.path.abspath(__file__))
np.random.seed(1)


dat = np.random.rand(3,6)
columns = [1, 2, 4, 6, 8, 12]
index = ['m1','m2','m3']
dat = pd.DataFrame(dat,index=index ,columns=columns)
numpy_to_latex(dat,2,pwd+'/build/table_normal.tex')

dat = np.random.rand(2,5)
columns = ['1', '2', 'O', '6', 'avg.']
index = ['m1','m2']
dat = pd.DataFrame(dat,index=index ,columns=columns)
numpy_to_latex(dat,2,pwd+'/build/table_small.tex')

dat = np.random.rand(40,10)
columns = np.arange(10)+10
index = np.arange(40)-10
dat = pd.DataFrame(dat,index=index ,columns=columns)
numpy_to_latex(dat,2,pwd+'/build/table_large.tex')

dat = np.random.rand(3,6)
columns = [1, 2, 4, 6, 8, 12]
index = ['m1','m2','m3']
dat = pd.DataFrame(dat,index=index ,columns=columns)
numpy_to_latex(dat,2,pwd+'/build/table_normal.tex',bold=None,verbose=1)
numpy_to_latex(dat,1,pwd+'/build/table_normal.tex',bold='max',verbose=1)
numpy_to_latex(dat,2,pwd+'/build/table_normal.tex',bold='min',verbose=1)
