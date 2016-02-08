import numpy as np
import pandas as pd
import MyScripts.latex.numpy_to_latex as numpy_to_latex
import random
import string

pwd = '/tmp/'+''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(16))+'.tex'

class testcase:

    def _test_basic(self):
        dat = np.random.rand(3,6)
        numpy_to_latex(dat,path = pwd)

        columns = [1, 2, 4, 6, 8, 12]
        numpy_to_latex(dat,columns=columns,path = pwd)

        index = ['m1','m2','m3']
        numpy_to_latex(dat,index=index,path = pwd)

        numpy_to_latex(
            dat,
            index=index,
            columns=columns,
            verbose=1,
            path = '/tmp/np.tex'
        )

    def _test_small(self):
        dat = np.random.rand(2,5)
        columns = ['1', '2', 'O', '6', 'avg.']
        index = ['m1','m2']
        numpy_to_latex(
            dat,
            index=index,
            columns=columns,
            path = pwd
        )

    def _test_large(self):
        dat = np.random.rand(40,10)
        columns = np.arange(10)+10
        index = np.arange(40)-10
        numpy_to_latex(
            dat,
            index=index,
            columns=columns,
            path = pwd
        )

    def _test_style(self):
        dat = np.random.rand(3,6)
        columns = [1, 2, 4, 6, 8, 12]
        index = ['m1','m2','m3']
        numpy_to_latex(
            dat,
            index=index,
            columns=columns,
            path = pwd
        )

        numpy_to_latex(
            dat,
            index=index,
            columns=columns,
            path = pwd,
            bold = [None,'h']
        )

        numpy_to_latex(
            dat,
            index=index,
            columns=columns,
            path = pwd,
            bold = ['min','v']
        )

        numpy_to_latex(
            dat,
            index=index,
            columns=columns,
            path = pwd,
            bold = ['max','h']
        )

    def _test_bold(self):
        dat = np.random.randint(0,9,[20,3])
        numpy_to_latex(
            dat,
            path = pwd,
            bold=['max','h']
        )
        dat = np.random.randint(0,9,[20,3])
        numpy_to_latex(
            dat,
            path = pwd,
            bold=['min','v']
        )

    def test_precision(self):
        dat = np.random.randint(0,90,[20,3])/100.
        numpy_to_latex(
            dat,
            path = pwd,
            bold=['max','h'],
            verbose=1
        )

if __name__ == "__main__":
    import nose
    nose.run(defaultTest=__file__, env={'NOSE_NOCAPTURE' : 1})
