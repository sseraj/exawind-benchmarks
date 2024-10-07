
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import glob, pathlib
import math


size=13
params = {'legend.fontsize': 'large',
          'axes.labelsize': size,
          'axes.titlesize': size,
          'xtick.labelsize': size,
          'ytick.labelsize': size}
plt.rcParams.update(params)

nalu1 = pd.read_csv('tu_const_aoa_5.dat')
nalu3 = pd.read_csv('tu_sust_aoa_5.dat')

fun3d    = pd.read_csv('fun3d_t_aoa_5.dat')
overf    = pd.read_csv('overflow_aoa_5.dat')

exp      = pd.read_csv('exp.csv')
exp_cl   = exp['cl'][0]
exp_cd   = exp['cd'][0]

fig = plt.figure(1)
plt.plot(fun3d['h'],fun3d['cl'],'-o')
plt.plot(overf['h'],overf['cl'],'-o')
plt.plot(nalu3['h'],nalu3['cl'],'-o')
plt.plot(nalu1['h'],nalu1['cl'],'-o')
#plt.axhline(y = exp_cl, color = 'k', linestyle = '--')
plt.xlim([0, 0.01])
plt.ylim([0.96, 1.08])
plt.xlabel('h')
plt.ylabel('Lift coefficient, $C_{l}$')
plt.legend(['SST-$\gamma$: FUN3D','SST-$\gamma$: OVERFLOW','SST-$\gamma$: Nalu-Wind','SST-$\gamma$: Nalu-Wind w/ Const Tu'])
plt.tight_layout()
plt.savefig("nlf0416_aoa5_cl.png",dpi=300)

fig = plt.figure(2)
plt.plot(fun3d['h'],fun3d['cd'],'-o')
plt.plot(overf['h'],overf['cd'],'-o')
plt.plot(nalu3['h'],nalu3['cd'],'-o')
plt.plot(nalu1['h'],nalu1['cd'],'-o')
#plt.axhline(y = exp_cd, color = 'k', linestyle = '--')
plt.xlim([0, 0.01])
plt.ylim([0.006, 0.02])
plt.xlabel('h')
plt.ylabel('Drag coefficient, $C_{d}$')
plt.legend(['SST-$\gamma$: FUN3D','SST-$\gamma$: OVERFLOW','SST-$\gamma$: Nalu-Wind','SST-$\gamma$: Nalu-Wind w/ Const Tu'])
plt.tight_layout()
plt.savefig("nlf0416_aoa5_cd.png",dpi=300)

print("=======Nalu: Sust ==========")
nmesh=len(nalu3)
cl_t = nalu3['cl'][nmesh-1]
cd_t = nalu3['cd'][nmesh-1]
for i in range (nmesh):
    cl = nalu3['cl'][i]
    cd = nalu3['cd'][i]

    cl_err = (cl-cl_t)/cl_t*100
    cd_err = (cd-cd_t)/cd_t*100

    print("%d %3.2f %3.2f"%(i+1,cl_err,cd_err))

print("=======Nalu: Const Tu==========")
nmesh=len(nalu1)
cl_t = nalu1['cl'][nmesh-1]
cd_t = nalu1['cd'][nmesh-1]
for i in range (nmesh):
    cl = nalu1['cl'][i]
    cd = nalu1['cd'][i]

    cl_err = (cl-cl_t)/cl_t*100
    cd_err = (cd-cd_t)/cd_t*100

    print("%d %3.2f %3.2f"%(i+1,cl_err,cd_err))

plt.show()

