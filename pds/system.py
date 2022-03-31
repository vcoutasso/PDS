import scipy.signal
import numpy as np

def properties(a, b, tol=1e-8):
    poles, roots = _poles_and_roots(a, b, tol)

    is_fir = _is_fir(poles)
    is_stable = _is_stable(poles)
    is_causal = _is_causal(a, b)

    return {
        'Polos': poles,
        'Zeros': roots,
        'FIR/IIR?': 'FIR' if is_fir else 'IIR',
        'Recursivo?': '-' if is_fir else '-', # TODO Implement
        'Causal?': 'Não' if is_causal else 'Sim',
        'Estável?': 'Sim' if is_stable else 'Não',
    }

def _is_fir(poles):
    return np.nonzero(poles)[0].size == 0

def _poles_and_roots(a, b, tol):
    poles = np.roots(a)
    roots = np.roots(b)

    xx, yy = np.meshgrid(poles, roots)

    close_idx = np.argwhere(np.isclose(xx - yy, 0, atol=tol) == True)

    poles = np.delete(poles, close_idx[:, 1])
    roots = np.delete(roots, close_idx[:, 0])

    return poles, roots

def _is_stable(poles):
    for pole in poles:
        if pole.real >= 0:
            return False

    return True

#FIXME: Does not work
def _is_causal(a, b):
    lti = scipy.signal.lti(a, b)

    _, response = scipy.signal.impulse2(lti, T=[-10])

    return response == 0
