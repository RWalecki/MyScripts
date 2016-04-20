import pandas as pd
import numpy as np

def numpy_to_latex(dat,
                   columns = [],
                   index = [],
                   precision = 2,
                   path = '/tmp/test.tex',
                   verbose = 0,
                   add_average = None,
                   bold = [None,None]
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
    columns = [str(c) for c in columns]
    if len(index)==0:index=np.arange(dat.shape[0])
    index = [str(c) for c in index]

    if add_average!=None:
        if add_average=='v':
            av = np.mean(dat,1)[None,:]
            columns.append('avr.')
            dat = np.vstack((dat.T,av)).T

        if add_average=='h':
            av = np.mean(dat,0)[:,None]
            dat = np.vstack((dat,av.T))
            index.append('avr.')


    if bold[1]=='h':dat=dat.T

    if bold[0]=='max':
        max_idx = dat.argmax(0)
        max_idy = np.arange(dat.shape[1])
    if bold[0]=='min':
        max_idx = dat.argmin(0)
        max_idy = np.arange(dat.shape[1])
    if bold[0]==None:
        max_idx = []
        max_idy = []

    if bold[1]=='h':
        tmp=max_idx
        max_idx=max_idy
        max_idy=tmp
        dat=dat.T

    #highlight same values



    tmp = np.int32(dat*10**precision)/float(10**precision)
    tmp = tmp.astype(str)



    for x,y in zip(max_idx,max_idy):

        ##also highlight same values in this row
        if bold[1]=='h':
            for y_ in np.argwhere(tmp[x,:]==tmp[x,y])[:,0]:
                tmp[x,y_]='\textbf{'+tmp[x,y_]+'}'
        else:
            for x_ in np.argwhere(tmp[:,y]==tmp[x,y])[:,0]:
                tmp[x_,y]='\textbf{'+tmp[x_,y]+'}'

    tab = pd.DataFrame(tmp,index=index ,columns=columns)
    if verbose>0:print tab
    tab.to_latex(buf=path,escape=False)
