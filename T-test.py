import numpy as np

from scipy import stats


# data = np.load('./Pxt/Boltz_id{}_{}_sigma{}.npz'.format(2016, 19822012, 0.015))
data = np.load('./Pxt/Bessel_id{}_{}_sigma{}.npz'.format(10, 19822012, 0.018))
# data = np.load('./Pxt/OU_id{}_sigma{}.npz'.format(2015, 0.5))
x = data['x']
true_pxt = data['true_pxt']
noisy_pxt = data['noisy_pxt']

# data = np.load('/home/liuwei/GitHub/IFPE-Net/Pxt/Bessel/B_f_10_pxt_19822012_sigma0.05.npy')
# data = np.load('/home/liuwei/GitHub/IFPE-Net/Pxt/Bessel/B_f_10_noisy_19822012_sigma0.05.npy')
# x = data[0, 0, :]
# noisy_pxt = data[:, 1:, :]
# print(data.shape)
# print(x.shape, noisy_pxt.shape)

bar = np.max(noisy_pxt) * 0.01
for pos in range(x.shape[0]):
    p = noisy_pxt[:, :, pos].reshape(-1, 1)
    print(pos, stats.ttest_1samp(p, bar))

# print(t_list)
print(np.max(noisy_pxt))

