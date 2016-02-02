import numpy as np
import pandas as pd
import MyScripts.latex.numpy_to_latex as numpy_to_latex


class testcase:

    def test_basic(self):
        dat = np.random.rand(3,6)
        columns = [1, 2, 4, 6, 8, 12]
        index = ['m1','m2','m3']
        dat = pd.DataFrame(dat,index=index ,columns=columns)
        numpy_to_latex(dat,2,'/tmp/np.tex')
        with open("/tmp/np.tex", "r") as out:
            for line in out:print line

    def test_small(self):
        dat = np.random.rand(2,5)
        columns = ['1', '2', 'O', '6', 'avg.']
        index = ['m1','m2']
        dat = pd.DataFrame(dat,index=index ,columns=columns)
        numpy_to_latex(dat,2,'/tmp/np.tex')
        with open("/tmp/np.tex", "r") as out:
            for line in out:print line

    def test_large(self):
        dat = np.random.rand(40,10)
        columns = np.arange(10)+10
        index = np.arange(40)-10
        dat = pd.DataFrame(dat,index=index ,columns=columns)
        numpy_to_latex(dat,2,'/tmp/np.tex')
        with open("/tmp/np.tex", "r") as out:
            for line in out:print line

    def test_style(self):
        dat = np.random.rand(3,6)
        columns = [1, 2, 4, 6, 8, 12]
        index = ['m1','m2','m3']
        dat = pd.DataFrame(dat,index=index ,columns=columns)

        numpy_to_latex(dat,2,'/tmp/np.tex')
        with open("/tmp/np.tex", "r") as out:
            for line in out:print line

        numpy_to_latex(dat,2,'/tmp/np.tex',bold=None,verbose=1)
        with open("/tmp/np.tex", "r") as out:
            for line in out:print line

        numpy_to_latex(dat,1,'/tmp/np.tex',bold='max',verbose=1)
        with open("/tmp/np.tex", "r") as out:
            for line in out:print line

        numpy_to_latex(dat,2,'/tmp/np.tex',bold='min',verbose=1)
        with open("/tmp/np.tex", "r") as out:
            for line in out:print line

if __name__ == "__main__":
    import nose
    nose.run(defaultTest=__file__, env={'NOSE_NOCAPTURE' : 1})
