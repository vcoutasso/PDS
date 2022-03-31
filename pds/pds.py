import scipy.signal
import numpy as np

def delta(n):
    return 1. * (n == 0)

def u(n):
    return 1. * (n >= 0)

def conv (x, h):
    N = len(x)
    K = len(h)
    y = np.zeros(N)
    
    for n in range(N):
        for k in range(K):
            if 0 <= n-k:
                y[n] += h[k]*x[n-k]
    return y

def lfilter(b, a, x, axis=0, zi=None):
    return scipy.signal.lfilter(b, a, x, axis=axis, zi=zi)

def slow_filter(b, a, x):
    N = len(x)
    M = len(b)
    K = len(a)
    y = np.zeros(N)
    
    a /= a[0]
    b /= a[0]

    for n in range(N):
        for k in range(M):
            if 0 <= n-k:
                y[n] += b[k]*x[n-k]
        for k in range(1, K):
            if 0 <= n-k:
                y[n] -= a[k]*y[n-k]
            
    return y

def mse(x, y):
    return np.mean(np.abs(x-y)**2)

def sinc(n, wc):
    x = np.zeros(n.shape)
    idx = n != 0
    x[idx] = np.sin(wc*n[idx])/(np.pi*n[idx])
    x[n==0] = wc/np.pi

    return x

def dtft(x, n, w=np.linspace(-np.pi, np.pi, num=1024)):
    X = np.zeros(w.size, dtype=np.complex)

    for i in range(w.size):
        X[i] = np.sum(x * np.exp(-1j * w[i] * n))

    return X, w
