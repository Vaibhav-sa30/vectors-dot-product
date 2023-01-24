import numpy as np
def predict(w, x):
    w_t = np.transpose(w)
    dotp = w_t @ x
    if dotp >= 0:
        return 1
    else:
        return -1
