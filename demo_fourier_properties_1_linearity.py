import numpy as np
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

## 1) Linearity
# a*f(x) + b*g(x) <== Fourier Transform ==> a*FFT(f(x)) + b*FFT(g(x))
N = 512

X = shepp_logan_phantom()
X = resize(X, (N, N), order=0)
X_fft = FFT(X)

X1 = X*(X > 0.95)*(X < 1.05)
X2 = X*(X > 0.35)*(X < 0.45)
X3 = X*(X > 0.25)*(X < 0.35)
X4 = X*(X > 0.15)*(X < 0.25)
X5 = X*(X > 0.05)*(X < 0.15)

X0 = X1 + X2 + X3 + X4 + X5

X1_fft = FFT(X1)
X2_fft = FFT(X2)
X3_fft = FFT(X3)
X4_fft = FFT(X4)
X5_fft = FFT(X5)

# X0_fft  = FFT(X0)
X0_fft = X1_fft + X2_fft + X3_fft + X4_fft + X5_fft

## Display
wndImg = [0, 1]
wndFFT = [0, 10]

plt.subplot(3,7,1); plt.imshow(X, cmap='gray', vmin=wndImg[0], vmax=wndImg[1]); plt.axis('image'); plt.axis('off'); plt.title('Ground truth : X');
plt.subplot(3,7,2); plt.imshow(X0, cmap='gray', vmin=wndImg[0], vmax=wndImg[1]); plt.axis('image'); plt.axis('off'); plt.title('X0');
plt.subplot(3,7,3); plt.imshow(X1, cmap='gray', vmin=wndImg[0], vmax=wndImg[1]); plt.axis('image'); plt.axis('off'); plt.title('X1');
plt.subplot(3,7,4); plt.imshow(X2, cmap='gray', vmin=wndImg[0], vmax=wndImg[1]); plt.axis('image'); plt.axis('off'); plt.title('X2');
plt.subplot(3,7,5); plt.imshow(X3, cmap='gray', vmin=wndImg[0], vmax=wndImg[1]); plt.axis('image'); plt.axis('off'); plt.title('X3');
plt.subplot(3,7,6); plt.imshow(X4, cmap='gray', vmin=wndImg[0], vmax=wndImg[1]); plt.axis('image'); plt.axis('off'); plt.title('X4');
plt.subplot(3,7,7); plt.imshow(X5, cmap='gray', vmin=wndImg[0], vmax=wndImg[1]); plt.axis('image'); plt.axis('off'); plt.title('X5');

plt.subplot(3,7,8); plt.imshow(np.log(abs(X_fft) + EPS), cmap='gray', vmin=wndFFT[0], vmax=wndFFT[1]); plt.axis('image'); plt.axis('off'); plt.title('Ground truth : FFT(X)');
plt.subplot(3,7,9); plt.imshow(np.log(abs(X0_fft) + EPS), cmap='gray', vmin=wndFFT[0], vmax=wndFFT[1]); plt.axis('image'); plt.axis('off'); plt.title('FFT(X0)');
plt.subplot(3,7,10); plt.imshow(np.log(abs(X1_fft) + EPS), cmap='gray', vmin=wndFFT[0], vmax=wndFFT[1]); plt.axis('image'); plt.axis('off'); plt.title('FFT(X1)');
plt.subplot(3,7,11); plt.imshow(np.log(abs(X2_fft) + EPS), cmap='gray', vmin=wndFFT[0], vmax=wndFFT[1]); plt.axis('image'); plt.axis('off'); plt.title('FFT(X2)');
plt.subplot(3,7,12); plt.imshow(np.log(abs(X3_fft) + EPS), cmap='gray', vmin=wndFFT[0], vmax=wndFFT[1]); plt.axis('image'); plt.axis('off'); plt.title('FFT(X3)');
plt.subplot(3,7,13); plt.imshow(np.log(abs(X4_fft) + EPS), cmap='gray', vmin=wndFFT[0], vmax=wndFFT[1]); plt.axis('image'); plt.axis('off'); plt.title('FFT(X4)');
plt.subplot(3,7,14); plt.imshow(np.log(abs(X5_fft) + EPS), cmap='gray', vmin=wndFFT[0], vmax=wndFFT[1]); plt.axis('image'); plt.axis('off'); plt.title('FFT(X5)');

plt.subplot(3,7,16); plt.imshow(np.log(abs(X_fft - X0_fft) + EPS), cmap='gray', vmin=wndFFT[0], vmax=wndFFT[1]); plt.axis('image'); plt.axis('off'); plt.title('FFT(X) - FFT(X0)');
plt.subplot(3,7,17); plt.imshow(np.log(abs(X_fft - X1_fft) + EPS), cmap='gray', vmin=wndFFT[0], vmax=wndFFT[1]); plt.axis('image'); plt.axis('off'); plt.title('FFT(X) - FFT(X1)');
plt.subplot(3,7,18); plt.imshow(np.log(abs(X_fft - X2_fft) + EPS), cmap='gray', vmin=wndFFT[0], vmax=wndFFT[1]); plt.axis('image'); plt.axis('off'); plt.title('FFT(X) - FFT(X2)');
plt.subplot(3,7,19); plt.imshow(np.log(abs(X_fft - X3_fft) + EPS), cmap='gray', vmin=wndFFT[0], vmax=wndFFT[1]); plt.axis('image'); plt.axis('off'); plt.title('FFT(X) - FFT(X3)');
plt.subplot(3,7,20); plt.imshow(np.log(abs(X_fft - X4_fft) + EPS), cmap='gray', vmin=wndFFT[0], vmax=wndFFT[1]); plt.axis('image'); plt.axis('off'); plt.title('FFT(X) - FFT(X4)');
plt.subplot(3,7,21); plt.imshow(np.log(abs(X_fft - X5_fft) + EPS), cmap='gray', vmin=wndFFT[0], vmax=wndFFT[1]); plt.axis('image'); plt.axis('off'); plt.title('FFT(X) - FFT(X5)');

plt.show()