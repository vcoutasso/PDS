import scipy.signal
import numpy as np

def classification(a, b, tol=1e-6):
    poles, roots = _poles_and_roots(a, b, tol)

    is_fir = _is_fir(poles)
    is_stable = _is_stable(poles)
    is_recursive = _is_recursive(a, b)
    is_causal = _is_causal(poles, roots)

    return {
        'Polos': poles,
        'Zeros': roots,
        'FIR/IIR?': 'FIR' if is_fir else 'IIR',
        'Recursivo?': 'Sim' if is_recursive else 'Não',
        'Causal?': 'Sim' if not is_causal else 'Não',
        'Estável?': 'Sim' if is_stable else 'Não',
    }

def _is_fir(poles):
    return np.nonzero(poles)[0].size == 0

def _is_stable(poles):
    for pole in poles:
        if pole.real >= 0:
            return False

    return True

def _is_recursive(a, b):
    return np.sum(a != 0) > 1

def _is_causal(poles, roots):
    return poles.size < roots.size

def _poles_and_roots(a, b, tol):
    poles = np.roots(a)
    roots = np.roots(b)

    xx, yy = np.meshgrid(poles, roots)

    close_idx = np.argwhere(np.isclose(xx - yy, 0, atol=tol) == True)

    poles = np.delete(poles, close_idx[:, 1])
    roots = np.delete(roots, close_idx[:, 0])

    return poles, roots
