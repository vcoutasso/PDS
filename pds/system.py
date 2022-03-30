import numpy as np

def properties(a, b, tol=1e-8):
    poles = np.roots(a)
    roots = np.roots(b)

    xx, yy = np.meshgrid(poles, roots)
    is_fir = _is_fir(poles, roots, tol)

    return {
        'Polos': poles,
        'Zeros': roots,
        'FIR/IIR?': 'FIR' if is_fir else 'IIR',
        'Recursivo': '-' if is_fir else '-', # FIXME
        'Causal?': 'Não' if is_fir else 'Sim', # FIXME
        'Estável?': 'Sim' if is_fir else 'Não', # REVIEW
    }

def _is_fir(poles, roots, tol):
    xx, yy = np.meshgrid(poles, roots)

    close_idx = np.argwhere(np.isclose(xx - yy, 0, atol=tol) == True)

    poles = np.delete(poles, close_idx[:, 1])
    roots = np.delete(roots, close_idx[:, 0])

    return np.nonzero(poles)[0].size == 0
