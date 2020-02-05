import numpy as np
from numpy import pi
from numpy.fft import fft
from numpy.fft import ifft
from numpy.fft import fftshift
from numpy.fft import ifftshift
import matplotlib.pyplot as plt

from skimage.data import shepp_logan_phantom
from skimage.transform import resize

from scipy.signal import convolve

FFT = lambda x: fftshift(fft(ifftshift(x)))
IFFT = lambda x: fftshift(ifft(ifftshift(x)))

EPS = 1e-18

## 4) Sptial 1D Convolution vs. Fourier Multiplication
N = 100
M = 36

X = np.random.randn(N, 1)
Y = np.random.randn(M, 1)

if (N > M):
    K = int(max(64, 2**int(np.log2(2*N))))
else:
    K = int(max(64, 2**int(np.log2(2*M))))

X_ = np.zeros(K)
X_[0:N] = X.squeeze()

Y_ = np.zeros(K)
Y_[0:M] = Y.squeeze()

# Z = np.convolve(X.squeeze(), Y.squeeze(), 'same')
Z = convolve(X.squeeze(), Y.squeeze(), 'same')
Z_ = ifft(fft(X_)*fft(Y_))
Z_ = np.real(Z_[int(M/2) - 1:N + int(M/2) - 1])

## Display
plt.subplot(221); plt.plot(X); plt.title('%d x %d' % (N, 1) + ' Source line');
plt.subplot(222); plt.plot(Y); plt.title('%d x %d' % (M, 1) + ' Kernel line');
plt.subplot(223); plt.plot(Z, 'g-'); plt.plot(Z_, 'r--');
plt.legend(['1D Convolution in spatial domain', 'Multiplication in Fourier domain'])
plt.title('Spatial 1D Convolution vs. Fourier Multiplication');

plt.subplot(224); plt.plot(Z - Z_); plt.title('Difference ( <= 1e-14 )');

plt.show()