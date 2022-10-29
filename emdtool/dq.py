# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/02_dq.ipynb.

# %% auto 0
__all__ = ['transform', 'inv_transform']

# %% ../nbs/02_dq.ipynb 7
def transform(theta, x):
    k = (2/3)*np.matrix([[np.cos(theta), np.cos(theta - 2*np.pi/3), np.cos(theta + 2*np.pi/3)],
    [np.sin(theta), np.sin(theta - 2*np.pi/3), np.sin(theta + 2*np.pi/3)],
    [0.5, 0.5, 0.5]])
    print('tranformation matrix (shape:{}): \n{}\n'.format(np.shape(k), k))

    x = np.matrix(x)
    print('abc matrix (shape:{}): \n{}\n'.format(np.shape(x), x))

    try:
        #np.shape(k)[1] == np.shape(x)[0]
        dq = np.matmul(k, x)
        print('tranformed matrix: \n', dq)
        return dq

    except:
        print('incompatible input shapes')

# %% ../nbs/02_dq.ipynb 11
def inv_transform(theta, x):
    k1 = np.matrix(((np.cos(theta), np.sin(theta), 1),
        (np.cos(theta - 2*np.pi/3), np.sin(theta - 2*np.pi/3), 1),
        (np.cos(theta + 2*np.pi/3), np.sin(theta + 2*np.pi/3), 1)))
    print('tranformation matrix (shape:{}): \n{}\n'.format(np.shape(k1), k1))

    x = np.matrix(x)
    print('dq matrix (shape:{}): \n{}\n'.format(np.shape(x), x))

    try:
        #np.shape(k)[1] == np.shape(x)[0]
        abc = np.matmul(x, k1)
        print('tranformed matrix: \n', abc)
        return abc

    except:
        print('incompatible input shapes')
