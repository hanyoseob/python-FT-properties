# FT-properties

### Reference
- https://en.wikipedia.org/wiki/Fourier_transform

### Execution
        >> demo_fourier_properties_0_all_examples.m

---

## 1) Linearity
### Reference
- https://en.wikipedia.org/wiki/Fourier_transform#Linearity

### Definition
For any complex numbers $a \in \mathbb{C}$ and $b \in \mathbb{C}$,

> $h(x) = a*f(x) + b*g(x)$ 
> $\xleftrightarrow{\mathcal{F}~(\textrm{Fourier transform})}$
> $\hat{h}(\xi) = a \cdot \hat{f}(\xi) + b \cdot \hat{g}(\xi)$

### Execution
        >> demo_fourier_properties_1_linearity.m

### Results
![alt text](img/linearity.png "FT properties: (1) Linearity")

## 2) Shift in Spatial domain
### Reference
- https://en.wikipedia.org/wiki/Fourier_transform#Translation_/_time_shifting

### Definition
For any real number $x_0 \in \mathbb{R}$,

> $h(x) = f(x-x_0)$ 
> $\xleftrightarrow{\mathcal{F}~(\textrm{Fourier transform})}$
> $\hat{h}(\xi) = e^{-2 \pi i x_0 \xi}\hat{f}(\xi)$

### Execution
        >> demo_fourier_properties_2_shift_in_spatial_domain.m
        
### Results
![alt text](img/shift_spational_domain.png "FT properties: (2) Shift in spatial domain")

## 3) Shift in Fourier domain
### Reference
- https://en.wikipedia.org/wiki/Fourier_transform#Modulation_/_frequency_shifting

### Definition
For any real number $\xi_0 \in \mathbb{R}$,

> $h(x) = e^{2 \pi i x \xi_0}f(x)$ 
> $\xleftrightarrow{\mathcal{F}~(\textrm{Fourier transform})}$
> $\hat{h}(\xi) = \hat{f}(\xi - \xi_0)$

### Execution
        >> demo_fourier_properties_3_shift_in_Fourier_domain.m
        
### Results
![alt text](img/shift_Fourier_domain.png "FT properties: (3) Shift in Fourier domain")

## 4) Convolution theorem
### Reference
- https://en.wikipedia.org/wiki/Fourier_transform#Convolution_theorem

### Definition

> $h(x) = (f*g)(x) = \int_{-\infty}^{\infty}{f(y)g(x-y)dy}$ 
> $\xleftrightarrow{\mathcal{F}~(\textrm{Fourier transform})}$
> $\hat{h}(\xi) = \hat{f}(\xi) \cdot \hat{g}(\xi)$

where, * is convolution operator and $\cdot$ is element-wise multiplication.

### Execution for 1D example
        >> demo_fourier_properties_4_1d_convolution_vs_multiplication.m

### Execution for 2D example
        >> demo_fourier_properties_5_2d_convolution_vs_multiplication.m

### Results
![alt text](img/conv_theoem_1d.png "FT properties: (4) Convolution theorem for 1D") (a) 1D example
![alt text](img/conv_theoem_2d.png "FT properties: (4) Convolution theorem for 2D") (b) 2D example