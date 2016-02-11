import numpy as np
import random
import string
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

import MyScripts.plots.bars as bars

pwd = '/tmp/'+''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(16))+'.pdf'

class testcase:

    def test_basic(self):

        fig, ax = plt.subplots()
        dat = np.random.rand(2,5,8)
        print dat
        labels = ['a',
                'b',
                'c',
                'd',
                'e',
                'f',
                'g',
                'h',
                ]
        im = bars(ax,dat,width=0.15,xticks=labels)
        #plt.colorbar(im)
        plt.savefig('/tmp/tmp.pdf',bbox_inches='tight')

if __name__ == "__main__":
    import nose
    nose.run(defaultTest=__file__, env={'NOSE_NOCAPTURE' : 1})
