# Python script for plotting curves for gm/Id method design
# MIT license. https://opensource.org/licenses/MIT
import sys
import os
sys.path.append(os.path.expanduser('~/src'))
import numpy as np
import rawread
import matplotlib as mpl
import matplotlib.pyplot as plt
arrs, plots = rawread.rawread(os.path.expanduser('~/ckt/gmid/gmid.raw'))

n = 0
for mos in ['mn', 'mp']:
    gm = np.asarray([elt['@%s[gm]' % mos] for elt in arrs])
    id = np.abs(np.asarray([elt['i(@%s[id])' % mos] for elt in arrs]))
    gds = np.asarray([elt['@%s[gds]' % mos] for elt in arrs])
    cgs = np.asarray([elt['@%s[cgs]' % mos] for elt in arrs])
    cgg = np.asarray([elt['@%s[cgg]' % mos] for elt in arrs])
    w = np.asarray([elt['@%s[w]' % mos] for elt in arrs])
    l = np.asarray([elt['@%s[l]' % mos] for elt in arrs])
    gm_id = gm/id
    gds_w = gds/w
    gm_gds = gm/gds
    gm_cgg = gm/cgg
    fteff = gm_cgg*gm_id
    gaineff = gm_gds*gm_id
    id_w = id/w
    label = ['%g' % elt for elt in l[:,0]]
    
    curves = (
        (gds_w,   'gds/w %s' % mos,             plt.semilogy),
        (gm_gds,  'gm/gds %s' % mos,            plt.plot),
        (gm_cgg,  '\omega_t = gm/cgg %s' % mos, plt.semilogy),
        (fteff,   '\omega_t*gm/id %s' % mos,    plt.semilogy),
        (gaineff, 'gm/gds*gm/id %s' % mos,      plt.plot),
        (id_w,   'id/w %s' % mos,               plt.semilogy))

    
    for curve in curves:
        fig = plt.figure(n)
        ax = plt.subplot(111)
        curve[2](gm_id.T, curve[0].T)
        # Shrink current axis by 20%
        box = ax.get_position()
        ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
        # Put a legend to the right of the current axis
        ax.legend(label, loc='center left', bbox_to_anchor=(1, 0.5))
        # ax.legend(label, loc='best', ncol=3, fancybox=True) #
        plt.title(curve[1])
        fig.savefig(('%d_%s_%s.pdf' % (n, mos, curve[1])).replace('/','_'), format='pdf')
        n = n+1