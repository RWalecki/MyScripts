import numpy as np
import MyScripts.plots.table as table
import matplotlib.pyplot as plt
import random
import string

import matplotlib.gridspec as gridspec

pwd = '/tmp/'+''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(16))+'.pdf'

class testcase:

    def test_basic(self):

        fig, ax = plt.subplots()
        dat = np.random.rand(9,12)
        im = table(ax,dat,c_range=[dat.min(),dat.max()])
        plt.colorbar(im)
        plt.savefig(pwd,bbox_inches='tight')

    def test_edit_colorbar(self):

        fig, ax = plt.subplots()
        dat = np.random.rand(9,12)
        im = table(ax,dat,c_range=[dat.min(),dat.max()])
        plt.colorbar(im)
        ax.set_title('jojo')
        ax.set_xlabel('blabal_x')
        ax.set_ylabel('blabal_y')
        plt.savefig(pwd,bbox_inches='tight')


    def test_grid(self):

        dat = np.random.rand(9,12)
        gs = gridspec.GridSpec(2, 2)

        ax = plt.subplot(gs[0, 0])
        im = table(ax,dat,c_range=[dat.min(),dat.max()],fontsize=5)
        plt.colorbar(im)
        ax.set_xlabel('blabal_x')
        ax.set_ylabel('blabal_y')

        ax = plt.subplot(gs[0, 1])
        im = table(ax,dat,c_range=[dat.min(),dat.max()],fontsize=0)
        plt.colorbar(im)
        ax.set_xlabel('blabal_x')
        ax.set_ylabel('blabal_y')

        ax = plt.subplot(gs[1, 0])
        im = table(ax,dat,c_range=[dat.min(),dat.max()],fontsize=10)
        plt.colorbar(im)
        ax.set_xlabel('blabal_x')
        ax.set_ylabel('blabal_y')

        ax = plt.subplot(gs[1, 1])
        im = table(ax,dat,c_range=[dat.min(),dat.max()],fontsize=10)
        plt.colorbar(im)
        ax.set_xlabel('blabal_x')
        ax.set_ylabel('blabal_y')

        plt.savefig('/tmp/tmp.pdf',bbox_inches='tight')



if __name__ == "__main__":
    import nose
    nose.run(defaultTest=__file__, env={'NOSE_NOCAPTURE' : 1})
