import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import sys

# rc('text', usetex=True)
font = {'size': 16}
plt.rc('font', **font)
plt.rc('axes', linewidth=2)
legend_properties = {'weight': 'bold'}

OU_g1 = np.load('/home/liuwei/Cluster/OU/id2016_p10_win55_0/iter0_gg_ng.npy')
OU_h1 = np.load('/home/liuwei/Cluster/OU/id2016_p10_win55_0/iter0_hh_ng.npy')
OU_g2 = np.load('/home/liuwei/Cluster/OU/id2016_p10_win55_0/iter202_gg_ng.npy')
OU_h2 = np.load('/home/liuwei/Cluster/OU/id2016_p10_win55_0/iter202_hh_ng.npy')
# OU_g2 = np.load('/home/liuwei/Cluster/OU/id1_p10_win1313_3/iter136_gg_ng.npy')
# OU_h2 = np.load('/home/liuwei/Cluster/OU/id1_p10_win1313_3/iter136_hh_ng.npy')
# B_g1 = np.load('/home/liuwei/Cluster/Bessel/id2016_p10_win1717_0/iter0_gg_ng.npy')
# B_h1 = np.load('/home/liuwei/Cluster/Bessel/id2016_p10_win1717_0/iter0_hh_ng.npy')
# B_g2 = np.load('/home/liuwei/Cluster/Bessel/id2016_p10_win1717_0/iter68_gg_ng.npy')
# B_h2 = np.load('/home/liuwei/Cluster/Bessel/id2016_p10_win1717_0/iter68_hh_ng.npy')
# '/home/liuwei/GitHub/Result/{}/id{}_p{}_win{}{}_{}'.format(process, run_id, p_patience, recur_win_gh,
#                                                                        recur_win_p, run_)
B_g1 = np.load('/home/liuwei/Cluster/Bessel/id10_p10_win1313_2/iter0_gg_ng.npy')
B_h1 = np.load('/home/liuwei/Cluster/Bessel/id10_p10_win1313_2/iter0_hh_ng.npy')
# B_g2 = np.load('/home/liuwei/GitHub/Result/Bessel/id12_p10_win1717_2/iter149_gg_ng.npy')
# B_h2 = np.load('/home/liuwei/GitHub/Result/Bessel/id12_p10_win1717_2/iter149_hh_ng.npy')
B_g2 = np.load('/home/liuwei/Cluster/Bessel/id10_p10_win1313_2/iter73_gg_ng.npy')
B_h2 = np.load('/home/liuwei/Cluster/Bessel/id10_p10_win1313_2/iter73_hh_ng.npy')
Boltz_g1 = np.load('/home/liuwei/Cluster/Boltz/id1_p10_win99_0/iter1_gg_ng.npy')
Boltz_h1 = np.load('/home/liuwei/Cluster/Boltz/id1_p10_win99_0/iter1_hh_ng.npy')
Boltz_g2 = np.load('/home/liuwei/Cluster/Boltz/id1_p10_win99_0/iter279_gg_ng.npy')
Boltz_h2 = np.load('/home/liuwei/Cluster/Boltz/id1_p10_win99_0/iter279_hh_ng.npy')

x1 = np.linspace(-0.01, 0.1, num=110, endpoint=False)
OU_real_g = 2.86 * x1
OU_real_h = 0.0013 * np.ones(x1.shape)
x2 = np.linspace(0.1, 1.1, num=100, endpoint=False)
B_real_g = 1 / x2 - 0.2
B_real_h = 0.5 * np.ones(x2.shape)
x3 = np.linspace(0., 1., num=100, endpoint=False)
Boltz_real_g = x3 - 1
Boltz_real_h = 0.2 * x3 ** 2

print((np.sum((B_real_g[6:81] - B_g2[6:81])**2) / np.sum(B_real_g[6:81]**2)))
print((np.sum((B_real_h[6:81] - B_h2[6:81])**2) / np.sum(B_real_h[6:81]**2)))
plt.figure(figsize=[24, 18])
plt.subplots_adjust(top=0.95, bottom=0.1, left=0.075, right=0.95, wspace=0.25, hspace=0.2)
ax = plt.subplot(2, 3, 1)
plt.text(-0.15, 1.10, 'a', fontsize=20, transform=ax.transAxes, fontweight='bold', va='top')
plt.plot(x1, OU_real_g, 'k-', linewidth=3, label='True $\mathbf{g}$')
plt.scatter(x1, OU_g1, c='b', marker='+', s=50, label='$\mathbf{\hat{g}_1}$')
plt.scatter(x1, OU_g2, c='r', marker='d', s=50, label='Final $\mathbf{\hat{g}}$')
# plt.scatter(b_x, b_lsq_g, c='r', marker='d', s=100, label='LLS')
plt.axvline(x=x1[19], ls='--', c='blue', linewidth=3)
plt.axvline(x=x1[101], ls='--', c='blue', linewidth=3)
plt.tick_params(direction='in', width=3, length=6)
plt.xticks(fontweight='bold')
plt.yticks(fontweight='bold')
plt.ylim(-0.05, 0.4)
plt.yticks(fontweight='bold')
plt.legend(loc='upper left', bbox_to_anchor=[0.2, 0.85], ncol=1)
ax.text(.5, .9, 'Heat Flux', horizontalalignment='center', transform=ax.transAxes, fontweight='bold')
plt.ylabel('g',  fontweight='bold')
plt.xlabel('x',  fontweight='bold')

ax = plt.subplot(2, 3, 4)
plt.text(-0.15, 1.10, 'd', fontsize=20, transform=ax.transAxes, fontweight='bold', va='top')
plt.plot(x1, OU_real_h * 1000, 'k-', linewidth=3, label='True $\mathbf{h}$')
plt.scatter(x1, OU_h1 * 1000, c='b', marker='+', s=50, label='$\mathbf{\hat{h}_1}$')
plt.scatter(x1, OU_h2 * 1000, c='r', marker='d', s=50, label='Final $\mathbf{\hat{h}}$')
# plt.scatter(b_x, b_lsq_g, c='r', marker='d', s=100, label='LLS')
plt.axvline(x=x1[19], ls='--', c='blue', linewidth=3)
plt.axvline(x=x1[101], ls='--', c='blue', linewidth=3)
plt.tick_params(direction='in', width=3, length=6)
plt.xticks(fontweight='bold')
plt.yticks(fontweight='bold')
plt.ylim(-0.3, 4)
plt.yticks(np.arange(0, 4, 1), fontweight='bold')
plt.legend(loc='upper left', bbox_to_anchor=[0.50, 0.90], ncol=1)
ax.text(.5, .9, 'Heat Flux', horizontalalignment='center', transform=ax.transAxes, fontweight='bold')
plt.ylabel('h($\mathbf{10^{-4}}$)',  fontweight='bold')
plt.xlabel('x',  fontweight='bold')
#
ax = plt.subplot(2, 3, 2)
plt.text(-0.15, 1.10, 'b', fontsize=20, transform=ax.transAxes, fontweight='bold', va='top')
plt.plot(x2, B_real_g, 'k-', linewidth=3, label='True $\mathbf{g}$')
plt.scatter(x2, B_g1, c='b', marker='+', s=50, label='$\mathbf{\hat{g}_1}$')
plt.scatter(x2, B_g2, c='r', marker='d', s=50, label='Final $\mathbf{\hat{g}}$')
plt.axvline(x=x2[14], ls='--', c='blue', linewidth=3)
plt.axvline(x=x2[87], ls='--', c='blue', linewidth=3)
plt.tick_params(direction='in', width=3, length=6)
plt.xticks(fontweight='bold')
plt.yticks(fontweight='bold')
plt.legend(loc='upper left', bbox_to_anchor=[0.45, 0.85], ncol=1)
ax.text(.5, .9, 'DNA Bubble', horizontalalignment='center', transform=ax.transAxes, fontweight='bold')
plt.ylabel('g',  fontweight='bold')
plt.xlabel('x',  fontweight='bold')

ax = plt.subplot(2, 3, 5)
plt.text(-0.15, 1.10, 'e', fontsize=20, transform=ax.transAxes, fontweight='bold', va='top')
plt.plot(x2, B_real_h, 'k-', linewidth=3, label='True $\mathbf{h}$')
plt.scatter(x2, B_h1, c='b', marker='+', s=50, label='$\mathbf{\hat{h}_1}$')
plt.scatter(x2, B_h2, c='r', marker='d', s=50, label='Final $\mathbf{\hat{h}}$')
plt.axvline(x=x2[14], ls='--', c='blue', linewidth=3)
plt.axvline(x=x2[87], ls='--', c='blue', linewidth=3)
plt.tick_params(direction='in', width=3, length=6)
plt.xticks(fontweight='bold')
plt.yticks(fontweight='bold')
# plt.ylim(4.995, 5.011)
# plt.yticks(np.arange(5.00, 5.02, 0.01), fontweight='bold')
plt.legend(loc='upper left', bbox_to_anchor=[0.45, 0.85], ncol=1)
ax.text(.5, .9, 'DNA Bubble', horizontalalignment='center', transform=ax.transAxes, fontweight='bold')
plt.ylabel('h',  fontweight='bold')
plt.xlabel('x',  fontweight='bold')

ax = plt.subplot(2, 3, 3)
plt.text(-0.15, 1.10, 'c', fontsize=20, transform=ax.transAxes, fontweight='bold', va='top')
plt.plot(x3, Boltz_real_g, 'k-', linewidth=3, label='True $\mathbf{g}$')
plt.scatter(x3, Boltz_g1, c='b', marker='+', s=100, label='$\mathbf{\hat{g}_1}$')
plt.scatter(x3, Boltz_g2, c='r', marker='d', s=50, label='Final $\mathbf{\hat{g}}$')
plt.axvline(x=x3[12], ls='--', c='blue', linewidth=3)
plt.axvline(x=x3[84], ls='--', c='blue', linewidth=3)
plt.tick_params(direction='in', width=3, length=6)
plt.xticks(fontweight='bold')
plt.ylim(-2.2, 0.3)
plt.yticks(np.arange(-2.00, 0.1, 0.5), fontweight='bold')
plt.legend(loc='upper left', bbox_to_anchor=[0.2, 0.45], ncol=1)
ax.text(.5, .9, 'Agent\'s Wealth', horizontalalignment='center', transform=ax.transAxes, fontweight='bold')
plt.ylabel('g',  fontweight='bold')
plt.xlabel('x',  fontweight='bold')
#
ax = plt.subplot(2, 3, 6)
plt.text(-0.15, 1.10, 'f', fontsize=20, transform=ax.transAxes, fontweight='bold', va='top')
plt.plot(x3, Boltz_real_h * 10, 'k-', linewidth=3, label='True $\mathbf{h}$')
plt.scatter(x3, Boltz_h1 * 10, c='b', marker='+', s=50, label='$\mathbf{\hat{h}_1}$')
plt.scatter(x3, Boltz_h2 * 10, c='r', marker='d', s=50, label='Final $\mathbf{\hat{h}}$')
plt.axvline(x=x3[12], ls='--', c='blue', linewidth=3)
plt.axvline(x=x3[84], ls='--', c='blue', linewidth=3)
plt.tick_params(direction='in', width=3, length=6)
plt.xticks(fontweight='bold')
plt.yticks(fontweight='bold')
plt.ylim(-0.2, 1.8)
plt.yticks(np.arange(0.00, 1.9, 0.5), fontweight='bold')
plt.legend(loc='upper left', bbox_to_anchor=[0.17, 0.85], ncol=1)
ax.text(.5, .9, 'Agent\'s Wealth', horizontalalignment='center', transform=ax.transAxes, fontweight='bold')
plt.ylabel('h ($\mathbf{10^{-1}}$)',  fontweight='bold')
plt.xlabel('x',  fontweight='bold')
plt.show()
# plt.savefig('/home/liuwei/erer')

# print(np.sum((OU_g - OU_real_g)**2)/np.sum(OU_real_g**2))
# print(np.sum((OU_h - OU_real_h)**2)/np.sum(OU_real_h**2))
# print(np.sum((B_g - B_real_g)**2)/np.sum(B_real_g**2))
# print(np.sum((B_h - B_real_h)**2)/np.sum(B_real_h**2))
# print(np.sum((Boltz_g - Boltz_real_g)**2)/np.sum(Boltz_real_g**2))
# print(np.sum((Boltz_h - Boltz_real_h)**2)/np.sum(Boltz_real_h**2))
# print(B_h)
