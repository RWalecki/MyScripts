import pandas as pd
import numpy as np

def numpy_to_latex(dat,
                   columns = [],
                   index = [],
                   precision = 2,
                   path = '/tmp/test.tex',
                   verbose = 0,
                   bold = 'max'
                   ):
    '''
    how to use in latex:

        \documentclass{article}
        \usepackage{booktabs}
        \begin{document}
            \input{./table.tex}
        \end{document}

    '''
    if len(columns)==0:columns=np.arange(dat.shape[1])
    if len(index)==0:index=np.arange(dat.shape[0])
    dat = pd.DataFrame(dat,index=index ,columns=columns)
    if verbose>0:print dat

    if bold=='max':
        max_idx = dat.values.argmax(0)
        max_idy = np.arange(dat.shape[1])
    if bold=='min':
        max_idx = dat.values.argmin(0)
        max_idy = np.arange(dat.shape[1])
    if bold==None:
        max_idx = []
        max_idy = []

    #highlight same values

    tmp = np.int32(dat*10**precision)/float(10**precision)
    tmp = tmp.astype(str)

    for x,y in zip(max_idx,max_idy):

        #also highlight same values in this row
        for x_ in np.argwhere(tmp[:,y]==tmp[x,y])[:,0]:
            tmp[x_,y]='\textbf{'+tmp[x_,y]+'}'

    index = dat.axes[0]
    columns = dat.axes[1]

    tab = pd.DataFrame(tmp,index=index ,columns=columns)
    if verbose>0:print tab
    tab.to_latex(buf=path,escape=False)
