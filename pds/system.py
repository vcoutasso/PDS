import pandas as pd
import numpy as np

def properties(a, b, tol=1e-8):
    poles = np.roots(a)
    roots = np.roots(b)

    print(np.meshgrid(poles, roots))

    return 0
