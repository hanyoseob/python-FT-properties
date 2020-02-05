# transpose-operator

## Reference
1) Inner product
    - https://en.wikipedia.org/wiki/Inner_product_space

2) Transpose
    - http://en.wikipedia.org/wiki/Transpose

3) Complex conjugate
    - https://en.wikipedia.org/wiki/Complex_conjugate

### 1) Inner Product definition
        < X, Y >  = < [x1; x2; ...; xn], [y1; y2; ...; yn] >,  

                  = [x1; x2; ...; xn]' * [y1; y2; ...; yn],  

                  = SUM_(i=1)^(n) xi * yi,   

                  = (x1 * y1) + (x2 * y2) + ... + (xn * yn).

### 2) Transpose definition
If `A` satisfies the following relation,   

        < A * X, Y > = < X, AT * Y >,  

then,

        AT is transpose of A.

### 3) Complex conjugate definition
        (a + ib)' = (a - ib).

## Transpose for Matrix ver.
If `A` is defined as follow,

        A in R ^ (M, N),

then,

        AT in R ^ (N, M).

## Transpose for Function ver.
### 1) [differential function](https://en.wikipedia.org/wiki/Differential_operator)

If `A(x)` is  defined as follow,

        A(x) = x(i+1) - x(i),
        
then `AT(y)` is that,

        AT(y) = y(i) - y(i+1).

### 2) [Fourier transform](https://en.wikipedia.org/wiki/Fourier_transform)

If `A(x)` is Fourier transform,

        A(x) = fftn(x)/numel(x),

then `AT(y)` is Inverse Fourier transform,
          
        AT(y) = ifftn(y).

### 3) [Radon transform](https://en.wikipedia.org/wiki/Radon_transform) 

If `A(x)` is Radon transform called by `'Projection'`,

        A(x) = radon(x, THETA)
        
        where, THETA is degrees vector.
        
then `AT(y)` is Inverse Radon transform without Filtration called by `'Backprojection'`, 

        AT(y) = iradon(y, THETA, 'none', N).
        
        where, 'none' is filtration option and N is image size. 
        
