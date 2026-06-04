import numpy as np

def vector_dot(x: np.ndarray, y: np.ndarray) -> float:
    x = np.asarray(x)
    y = np.asarray(y)
    if x.ndim != 1 or y.ndim != 1:
        raise ValueError("Must be 1D")
    if x.shape[0] != y.shape[0]:
        raise ValueError("Must be same size")
    res = 0
    for i in range(len(x)):
        res += x[i]*y[i]
    return res

def norm(x: np.ndarray, order=2) -> float:
    x = np.asarray(x)
    if x.ndim != 1:
        raise ValueError("Must be 1D")
    if order==2:
        return np.sqrt(vector_dot(x,x))
    if order==1:
        return np.sum(np.abs(x))
    elif order == np.inf:
        max = 0
        for val in x:
            if abs(val) > max:
                max = abs(val)
        return max
    raise ValueError("Order must be 1,2 or inf")
