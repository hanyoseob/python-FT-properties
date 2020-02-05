import numpy as np
from numpy import pi
from numpy.fft import fft2
from numpy.fft import ifft2
from numpy.fft import fftshift
from numpy.fft import ifftshift
import matplotlib.pyplot as plt

from scipy.signal import convolve2d

from skimage.data import shepp_logan_phantom
from skimage.transform import resize

FFT = lambda x: fftshift(fft2(ifftshift(x)))
IFFT = lambda x: fftshift(ifft2(ifftshift(x)))

EPS = 1e-18

##
def gaussian_filter(sz, sgm):
    m, n = [(sz_ - 1.) / 2. for sz_ in sz]

    nx = np.linspace(-sz[0]/2, sz[0]/2, sz[0])
    ny = np.linspace(-sz[1]/2, sz[1]/2, sz[1])
    [mx, my] = np.meshgrid(nx, ny)

    h = np.exp(-(mx*mx + my*my) / (2*sgm*sgm))
    h = h / h.sum()

    return h

## 5) 2D Convolution vs. Multiplication
N = 256
M = 36

X = shepp_logan_phantom()
X = resize(X, (N, N), order=0)
Y = gaussian_filter((M, M), 3)

if (N > M):
    K = int(max(64, 2**int(np.log2(2*N))))
else:
    K = int(max(64, 2**int(np.log2(2*M))))

X_ = np.zeros((K, K))
X_[0:N, 0:N] = X

Y_ = np.zeros((K, K))
Y_[0:M, 0:M] = Y

Z = convolve2d(X, Y, 'same')
Z_ = np.real(ifft2(fft2(X_)*fft2(Y_)))
Z_ = Z_[int(M/2)-1:N + int(M/2)-1, int(M/2)-1:N + int(M/2)-1]

##
wndImg = [0, 1]
plt.subplot(231); plt.imshow(X, cmap='gray', vmin=wndImg[0], vmax=wndImg[1]); plt.axis('image'); plt.axis('off'); plt.title('%d x %d' % (N, N) + ' Source image');
plt.subplot(232); plt.imshow(Y, cmap='gray'); plt.axis('image'); plt.axis('off'); plt.title('%d x %d' % (M, M) + ' Kernel image');

plt.subplot(234); plt.imshow(Z, cmap='gray', vmin=wndImg[0], vmax=wndImg[1]); plt.axis('image'); plt.axis('off'); plt.title('Spatial 2D Convolution');
plt.subplot(235); plt.imshow(Z_, cmap='gray', vmin=wndImg[0], vmax=wndImg[1]); plt.axis('image'); plt.axis('off'); plt.title('Fourier 2D Multiplication');
plt.subplot(236); plt.imshow(Z - Z_, cmap='gray'); plt.axis('image'); plt.axis('off'); plt.title('Difference ( <= 1e-14 )');

plt.show()