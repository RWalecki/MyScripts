import pandas as pd
import numpy as np

def numpy_to_latex(dat, xlabel = None, ylabel = None, precision = 2, path = '/tmp/test.tex' ):
    '''
    how to use in latex:

        \documentclass{article}
        \usepackage{booktabs}
        \begin{document}
            \input{./table.tex}
        \end{document}

    '''

    # define precision
    max_idx = dat.argmax(0)
    max_idy = np.arange(dat.shape[1])
    tmp = np.int32(dat*10**precision)/float(10**precision)
    tmp = tmp.astype(str)
    for x,y in zip(max_idx,max_idy):
        tmp[x,y]='\textbf{'+tmp[x,y]+'}'



    tab = pd.DataFrame(tmp,index=xlabel,columns=ylabel)
    tab.to_latex(buf=path,escape=False)
