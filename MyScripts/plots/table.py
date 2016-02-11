import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.cm as cm

def table(
    ax,
    dat,
    c_range=None,
    fontsize=10,
    colorbar=True,
    highlight = [],
    cmap = cm.Reds,
):

    if c_range==None:
        vmax = np.max(np.abs(dat))
        vmin = -vmax
    else:
        vmin, vmax = c_range


    im = ax.imshow(dat.T,
               interpolation='nearest',
               cmap=cmap,
               vmin=vmin,
               vmax=vmax,
               )


    for i,j in highlight:
        rect = matplotlib.patches.Rectangle(
                (i-0.5,j-0.5), 1, 1, 
                color='red',
                fill=None, 
                #alpha=1,
                linewidth=2
                )
        ax.add_patch(rect)

    ax.set_xticks(np.arange(0, dat.shape[0], 1))
    ax.set_yticks(np.arange(0, dat.shape[1], 1))


    if fontsize==0:
        return im

    for (x,y),v in np.ndenumerate(dat):

        if v==0:continue

        val = np.int32(v*100)/100.

        if v<=(vmax-vmin)*0.5:
            color = 'black'
        else:
            color = 'white'

        ax.text(x, y, val, va='center', ha='center',color=color,fontsize=fontsize)

    return im
