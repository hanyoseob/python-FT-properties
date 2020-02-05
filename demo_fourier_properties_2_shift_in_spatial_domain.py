import numpy as np
from numpy import pi
from numpy.fft import fft2
from numpy.fft import ifft2
from numpy.fft import fftshift
from numpy.fft import ifftshift
import matplotlib.pyplot as plt

from skimage.data import shepp_logan_phantom
from skimage.transform import resize

FFT = lambda x: fftshift(fft2(ifftshift(x)))
IFFT = lambda x: fftshift(ifft2(ifftshift(x)))

EPS = 1e-18

## 2) Shift in spatial domain
# f(x - a) <== Fourier Transform ==> exp(-j*2pi*a*kx) * FFT(f(x))
N = 512

X = shepp_logan_phantom()
X = resize(X, (N, N), order=0)
X_fft = FFT(X)

nx = np.linspace(1, N, N)
ny = np.linspace(1, N, N)
[mx, my] = np.meshgrid(nx, ny)

dx = 100
dy = 100

sht = np.exp(-1j*2*pi*(dx/N*mx + dy/N*my))

Y_fft = sht*X_fft
Y = IFFT(Y_fft)

wndImg = [0, 1]
wndAng = [-pi, pi]
wndFFT = [0, 10]

## Display
plt.subplot(2, 3, 1); plt.imshow(np.abs(X), cmap='gray', vmin=wndImg[0], vmax=wndImg[1]); plt.axis('image'); plt.axis('off'); plt.title('Ground truth : Magitude');
plt.subplot(2, 3, 2); plt.imshow(np.angle(X), cmap='gray', vmin=wndAng[0], vmax=wndAng[1]); plt.axis('image'); plt.axis('off'); plt.title('Ground truth : Phase');
plt.subplot(2, 3, 3); plt.imshow(np.log(np.abs(X_fft) + EPS), cmap='gray', vmin=wndFFT[0], vmax=wndFFT[1]); plt.axis('image'); plt.axis('off'); plt.title('Ground truth : Fourier domain');

plt.subplot(2, 3, 4); plt.imshow(np.abs(Y), cmap='gray', vmin=wndImg[0], vmax=wndImg[1]); plt.axis('image'); plt.axis('off'); plt.title('Spatial Shift_(dx=%d, dy=%d)' % (dx, dy) +  ' : Magitude');
plt.subplot(2, 3, 5); plt.imshow(np.angle(Y) % pi, cmap='gray', vmin=wndAng[0], vmax=wndAng[1]); plt.axis('image'); plt.axis('off'); plt.title('Spatial Shift_(dx=%d, dy=%d)' % (dx, dy) +  ' : Phase');
plt.subplot(2, 3, 6); plt.imshow(np.log(np.abs(Y_fft) + EPS), cmap='gray', vmin=wndFFT[0], vmax=wndFFT[1]); plt.axis('image'); plt.axis('off'); plt.title('Spatial Shift_(dx=%d, dy=%d)' % (dx, dy) +  ' : Fourier domain');

plt.show()